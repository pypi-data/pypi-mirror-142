#!/usr/bin/env python3

import pkg_resources
import sqlite3
from sonofman import som_cachetab, som_util


class SomDal:
    def __init__(self, path_to_data=""):
        som_path_db = pkg_resources.resource_filename('sonofman.data', 'bible.db') if path_to_data == "" else "{0}/bible.db".format(path_to_data)
        self.somutil = som_util.SomUtil
        self.somutil.print("* System Db: {0}".format(som_path_db))
        self.conn = sqlite3.connect(som_path_db)

    def search_bible(self, delimiter_verse, tbbname, bnumber, cnumber):
        """
        Search bible
        :param delimiter_verse:
        :param tbbname:
        :param bnumber:
        :param cnumber:
        :return: list of verses
        """
        try:
            c = self.conn.cursor()
            c.execute("SELECT b.id, b.vNumber, b.vText, r.bName, r.bsName, n.mark, b.bbName, t.tot, {0} "
                      "FROM bible b "
                      "INNER JOIN bibleRef r ON r.bbName=b.bbName AND r.bNumber=b.bNumber "
                      "LEFT OUTER JOIN bibleNote n ON n.bNumber=b.bNumber AND n.cNumber=b.cNumber AND n.vNumber=b.vNumber "
                      "LEFT OUTER JOIN bibleCrossRefi t ON t.bNumber=b.bNumber AND t.cNumber=b.cNumber AND t.vNumber=b.vNumber "
                      "WHERE b.bbName IN {1} "
                      "AND b.bNumber={2} "
                      "AND b.cNumber={3} "
                      "ORDER BY b.vNumber ASC, bbNameOrder ASC".format(
                        self.case_bible("b.bbName", tbbname),
                        self.in_bible(tbbname),
                        bnumber,
                        cnumber))

            t_size = len(tbbname) - 1
            i = 0
            lst = []
            if len(tbbname) > 1:
                should_extra_delimiter = True
                delimiter_verse = "§"
            else:
                should_extra_delimiter = False
            for c in c.fetchall():
                if i >= t_size:
                    i = 0
                    if should_extra_delimiter:
                        extra_delimiter = "§§"
                    else:
                        extra_delimiter = ""
                else:
                    i += 1
                    extra_delimiter = ""

                before_delimiter = "{0}|".format(c[6])
                cr_tot = "" if c[7] is None or c[7] == 0 else " [{0}]".format(c[7])
                text = "{6}{0:s} {1}.{2}{7}: {3}{4}{5}".format(c[4], cnumber, c[1], c[2], delimiter_verse, extra_delimiter, before_delimiter, cr_tot)
                ref = [c[0], c[6]]
                item = [text, ref]
                lst.append(item)

            return lst
        except Exception as ex:
            raise ex

    def search_bible_string(self, delimiter_verse, tbbname, bbname, bnumber, cnumber, search_string):
        """
        Search text in Bible
        :return 1) list of verses
                2) number of verses found
        """

        try:
            where_book = where_chapter = where_search_string = ""
            search_string = "%{0}%".format(search_string.replace("'", "_"))
            if bnumber > 0:
                where_book = "AND b.bNumber={0} ".format(bnumber)
            if cnumber > 0:
                where_chapter = "AND b.cNumber={0} ".format(cnumber)
            if len(search_string) > 0:
                where_search_string = "AND b.vText like '{0}' ".format(search_string)
            c = self.conn.cursor()

            query = (
                "SELECT a.id, a.vNumber, a.vText, r.bName, r.bsName, n.mark, a.bbName, a.cNumber, t.tot, {4} "
                "FROM bible a, "
                "(SELECT b.bNumber, b.cNumber, b.vNumber "
                "FROM bible b "
                "WHERE b.bbName='{0}' "
                "{1}"
                "{2}"
                "{3}"
                "ORDER BY b.bNumber ASC, b.cNumber ASC, b.vNumber ASC) o "
                "LEFT OUTER JOIN bibleNote n ON n.bNumber=a.bNumber AND n.cNumber=a.cNumber AND n.vNumber=a.vNumber "
                "LEFT OUTER JOIN bibleCrossRefi t ON t.bNumber=a.bNumber AND t.cNumber=a.cNumber AND t.vNumber=a.vNumber "
                "INNER JOIN bibleRef r ON r.bbName=a.bbName AND r.bNumber=a.bNumber "
                "WHERE a.bNumber=o.bNumber AND a.cNumber=o.cNumber AND a.vNumber=o.vNumber AND a.bbName IN {5} "
                "ORDER BY a.bNumber ASC, a.cNumber ASC, a.vNumber ASC, bbNameOrder ASC".format(
                    bbname,
                    where_book,
                    where_chapter,
                    where_search_string,
                    self.case_bible("a.bbName", tbbname),
                    self.in_bible(tbbname)))

            c.execute(query)

            t_size = len(tbbname) - 1
            i = 0
            lst = []
            if len(tbbname) > 1:
                should_extra_delimiter = True
                delimiter_verse = "§"
            else:
                should_extra_delimiter = False
            for c in c.fetchall():
                if i >= t_size:
                    i = 0
                    if should_extra_delimiter:
                        extra_delimiter = "§§"
                    else:
                        extra_delimiter = ""
                else:
                    i += 1
                    extra_delimiter = ""

                before_delimiter = "{0}|".format(c[6])
                cr_tot = "" if c[8] is None or c[8] == 0 else " [{0}]".format(c[8])
                text = "{6}{0:s} {1}.{2}{7}: {3}{4}{5}".format(c[4], c[7], c[1], c[2], delimiter_verse, extra_delimiter, before_delimiter, cr_tot)
                ref = [c[0], c[6]]
                item = [text, ref]
                lst.append(item)

            return lst, int(len(lst) / len(tbbname))
        except Exception as ex:
            raise ex

    def get_bible_chapter_count_by_book(self, bnumber):
        """
        Get bible chapter count by book
        :param bnumber: book number
        :return: 1) chapter count
                 2) verse count
        """
        ci = [0, 0]  # cCount, vCount
        try:
            c = self.conn.cursor()
            c.execute("SELECT COUNT(b.cNumber), SUM(b.vCount) "
                      "from bibleCi b WHERE b.bNumber={0} "
                      "GROUP BY b.bNumber".format(bnumber))

            for c in c.fetchall():
                ci[0] = c[0]
                ci[1] = c[1]
            return ci
        except Exception as ex:
            raise ex

    def get_book_number_by_bsname(self, bbname, bsname):
        """
        Get book number by bsname or -1 if not found
        """
        try:
            cu = self.conn.cursor()
            cu.execute(f"SELECT bNumber FROM bibleRef where bbName='{bbname}' AND bsName like '{bsname}'")
            c = cu.fetchone()
            if c is None:
                return -1
            return c[0]
        except Exception as ex:
            raise ex

    def get_book_ref(self, bbname, bnumber):
        """
        Get book reference
        :param bbname: bible name
        :param bnumber: book number
        :return: 1) book name verbose or None if not found
                 2) book name short or None if not found
        """
        try:
            cu = self.conn.cursor()
            cu.execute("SELECT bName, bsName "
                      "from bibleRef "
                      "WHERE bbName='{0}' "
                      "AND bNumber={1}".format(
                        bbname,
                        bnumber))
            c = cu.fetchone()
            if c is None:
                return None, None

            return c[0], c[1]
        except Exception as ex:
            raise ex

    def get_list_book_by_name(self, item_width, bbname, is_order_by_name, res_all_item, search_string):
        """
        Get list book filtered by name and ordered by name or by book nr
        :param item_width: width for long name
        :param bbname: book language
        :param is_order_by_name: to order by name
        :param res_all_item: "ALL" item. Set None for not include it
        :param search_string: book to search
        :return: list of books filtered
        """

        try:
            where_book = ""
            if len(search_string) > 0:
                search_string = "%{0}%".format(search_string.replace("'", "_"))
                if len(search_string) > 0:
                    where_book = "AND bName like '{0}' ".format(search_string)

            c = self.conn.cursor()
            c.execute("SELECT bNumber, bName, bsName "
                      "from bibleRef "
                      "WHERE "
                      "bbName = '{0}' "
                      "{1}"
                      "ORDER BY {2} ASC ".format(
                        bbname,
                        where_book,
                        "bName" if is_order_by_name else "bNumber"))

            lst = []
            item_width = item_width - 5  # (99)...<space> at the end
            for c in c.fetchall():
                bname = c[1][0:item_width]
                item = "({1:2d}) {2:{0}s}".format(item_width, c[0], bname)
                lst.append(item)
            if res_all_item is not None:
                lst.insert(0, res_all_item)
            return lst
        except Exception as ex:
            raise ex

    def get_verse(self, bible_id):
        """
        Get verse references
        :param bible_id: ID
        :return: bsname, bname, bnumber, cnumber, vnumber or bsname=None if not found
        """

        try:
            cu = self.conn.cursor()
            cu.execute(f'''SELECT r.bsName, r.bName, b.bNumber, b.cNumber, b.vNumber FROM bible b 
                    INNER JOIN bibleRef r ON r.bbName=b.bbName AND r.bNumber=b.bNumber 
                    LEFT OUTER JOIN bibleNote n ON n.bNumber=b.bNumber AND n.cNumber=b.cNumber AND n.vNumber=b.vNumber 
                    LEFT OUTER JOIN bibleCrossRefi t ON t.bNumber=b.bNumber AND t.cNumber=b.cNumber AND t.vNumber=b.vNumber 
                    WHERE b.id={bible_id}''')

            c = cu.fetchone()
            if c is None:
                return None, None, -1, -1, -1
            return c[0], c[1], c[2], c[3], c[4]
        except Exception as ex:
            raise ex

    def get_verses(self, delimiter_verse, tbbname, bnumber, cnumber, vnumber_from, vnumber_to=None):
        """
        Get list of verses
        :param self
        :param delimiter_verse:
        :param tbbname:
        :param bnumber:
        :param cnumber:
        :param vnumber_from:
        :param vnumber_to: None if not used
        :return: list of verses
        """

        try:
            vnumber_to_clause = "AND b.vNumber <= {0} ".format(vnumber_to) if vnumber_to is not None else ""

            c = self.conn.cursor()
            c.execute("SELECT b.id, b.vNumber, b.vText, r.bName, r.bsName, n.mark, b.bbName, b.cNumber, t.tot, {0} "
                      "FROM bible b "
                      "INNER JOIN bibleRef r ON r.bbName=b.bbName AND r.bNumber=b.bNumber "
                      "LEFT OUTER JOIN bibleNote n ON n.bNumber=b.bNumber AND n.cNumber=b.cNumber AND n.vNumber=b.vNumber "
                      "LEFT OUTER JOIN bibleCrossRefi t ON t.bNumber=b.bNumber AND t.cNumber=b.cNumber AND t.vNumber=b.vNumber "
                      "WHERE b.bbName IN {1} "
                      "AND b.bNumber={2} "
                      "AND b.cNumber={3} "
                      "AND b.vNumber >= {4} "
                      "{5}"
                      "ORDER BY b.vNumber ASC, bbNameOrder ASC".format(
                        self.case_bible("b.bbName", tbbname),
                        self.in_bible(tbbname),
                        bnumber,
                        cnumber,
                        vnumber_from,
                        vnumber_to_clause))

            t_size = len(tbbname) - 1
            i = 0
            lst = []
            if len(tbbname) > 1:
                should_extra_delimiter = True
                delimiter_verse = "§"
            else:
                should_extra_delimiter = False

            for c in c.fetchall():
                if i >= t_size:
                    i = 0
                    if should_extra_delimiter:
                        extra_delimiter = "§§"
                    else:
                        extra_delimiter = ""
                else:
                    i += 1
                    extra_delimiter = ""

                before_delimiter = "{0}|".format(c[6])
                cr_tot = "" if c[8] is None or c[8] == 0 else " [{0}]".format(c[8])
                text = "{6}{0:s} {1}.{2}{7}: {3}{4}{5}".format(c[4], c[7], c[1], c[2], delimiter_verse, extra_delimiter, before_delimiter, cr_tot)
                ref = [c[0], c[6]]
                item = [text, ref]
                lst.append(item)

            return lst
        except Exception as ex:
            raise ex

    @staticmethod
    def get_verses_string(lst_verses):
        """
        Get verses as string
        :param lst_verses: list to convert in string
        :return: list of verses as string
        """
        res = "".join(str(item[0]) for item in lst_verses)
        return res

    def get_cross_references(self, delimiter_verse, tbbname, bnumber, cnumber, vnumber):
        try:
            cu = self.conn.cursor()

            if len(tbbname) > 1:
                should_extra_delimiter = True
                delimiter_verse = "§"
            else:
                should_extra_delimiter = False

            t_size = len(tbbname) - 1
            lst = []

            i = 0
            while i <= 1:
                if i == 0:
                    query = f'''SELECT b.id, b.bbName, b.bNumber, b.cNumber, b.vNumber, b.vText, r.bName, r.bsName, n.mark, b.bbName, t.tot, {self.case_bible("b.bbName", tbbname)} 
FROM bible b 
INNER JOIN bibleRef r ON r.bbName=b.bbName AND r.bNumber=b.bNumber 
LEFT OUTER JOIN bibleNote n ON n.bNumber=b.bNumber AND n.cNumber=b.cNumber AND n.vNumber=b.vNumber 
LEFT OUTER JOIN bibleCrossRefi t ON t.bNumber=b.bNumber AND t.cNumber=b.cNumber AND t.vNumber=b.vNumber 
WHERE b.bbName IN {self.in_bible(tbbname)} 
AND b.bNumber={bnumber} 
AND b.cNumber={cnumber} 
AND b.vNumber={vnumber} 
ORDER BY b.vNumber ASC, bbNameOrder ASC'''

                else:
                    query = f'''SELECT b.id, b.bbName, b.bNumber, b.cNumber, b.vNumber, b.vText, r.bName, r.bsName, n.mark, b.bbName, t.tot, {self.case_bible("b.bbName", tbbname)} 
FROM bibleCrossRef c 
INNER JOIN bible b ON b.bNumber=c.bNumberTo AND b.cNumber=c.cNumberTo AND b.vNumber=c.vNumberTo 
INNER JOIN bibleRef r ON r.bbName=b.bbName AND r.bNumber=b.bNumber 
LEFT OUTER JOIN bibleNote n ON n.bNumber=b.bNumber AND n.cNumber=b.cNumber AND n.vNumber=b.vNumber 
LEFT OUTER JOIN bibleCrossRefi t ON t.bNumber=b.bNumber AND t.cNumber=b.cNumber AND t.vNumber=b.vNumber 
WHERE b.bbName IN {self.in_bible(tbbname)} 
AND c.bNumberFrom={bnumber} 
AND c.cNumberFrom={cnumber} 
AND c.vNumberfrom={vnumber} 
ORDER BY c.crId ASC, bbNameOrder ASC'''

                i += 1
                j = 0

                cu.execute(query)
                for c in cu.fetchall():
                    if j >= t_size:
                        j = 0
                        if should_extra_delimiter:
                            extra_delimiter = "§§"
                        else:
                            extra_delimiter = ""
                    else:
                        j += 1
                        extra_delimiter = ""

                    before_delimiter = "{0}|".format(c[1])
                    cr_tot = "" if c[10] is None or c[10] == 0 else " [{0}]".format(c[10])
                    text = "{6}{0:s} {1}.{2}{7}: {3}{4}{5}".format(c[7], c[3], c[4], c[5], delimiter_verse,
                                                                   extra_delimiter, before_delimiter, cr_tot)
                    ref = [c[0], c[1]]
                    item = [text, ref]
                    lst.append(item)

            return lst
        except Exception as ex:
            raise ex

    @staticmethod
    def case_bible(fld, string):
        """
        Construct CASE clause Bible
        EX: CASE b.bbName WHEN 'f' THEN 1 WHEN 'k' THEN 2 END bbNameOrder
        :param fld: Table field to case (ex: b.bbName)
        :param string: TRAD
        :return: string with CASE clause for bbNameOrder
        """

        try:
            size = len(string)
            sb = ["CASE {0}".format(fld)]
            for i in range(0, size):
                sb.append(" WHEN '{0}' THEN ".format(string[i]))
                sb.append(i + 1)
            sb.append(" END bbNameOrder")
            res = "".join(str(item) for item in sb)
            return res
        except Exception as ex:
            raise ex

    @staticmethod
    def in_bible(trad):
        """
        Construct IN clause Bible with ( ).
        Rem: there is no check of the content, quote, double quotes. Works only for chars
        :param trad: traduction
        :return: string for IN clause
        """

        try:
            size = len(trad)
            if size <= 1:
                return "('{0}')".format(trad)

            sb = []
            for i in range(0, size):
                if len(sb) > 0:
                    sb.append(",")
                sb.append("'{0}'".format(trad[i]))
            sb.insert(0, "(")
            sb.append(")")
            res = "".join(str(item) for item in sb)
            return res
        except Exception as ex:
            raise ex

    def add_cache_tab(self, ct):
        try:
            cu = self.conn.cursor()
            query = f'''INSERT OR REPLACE INTO cacheTab (tabId, tabType, tabTitle, fullQuery, scrollPosY, bbName, isBook, isChapter, isVerse, bNumber, cNumber, vNumber, trad, orderBy, favFilter)
                VALUES ({ct.tabid}, '{ct.tabtype}', '{ct.tabtitle}', '{ct.fullquery}', {ct.scrollposy}, '{ct.bbname}', {ct.isbook}, {ct.ischapter}, {ct.isverse}, {ct.bnumber}, {ct.cnumber}, {ct.vnumber}, '{ct.trad}', {ct.orderby}, {ct.favfilter}) '''
            cu.execute(query)
            self.conn.commit()
        except Exception as ex:
            raise ex

    def update_cache_tab(self, ct):
        try:
            cu = self.conn.cursor()
            query = f'''UPDATE cacheTab SET 
                tabType='{ct.tabtype}', 
                tabTitle='{ct.tabtitle}',  
                fullQuery='{ct.fullquery}',  
                scrollPosY={ct.scrollposy},  
                bbName='{ct.bbname}', 
                isBook={ct.isbook}, 
                isChapter={ct.ischapter},  
                isVerse={ct.isverse}, 
                bNumber={ct.bnumber}, 
                cNumber={ct.cnumber},  
                vNumber={ct.vnumber},  
                trad='{ct.trad}', 
                orderBy={ct.orderby},
                favFilter={ct.favfilter}  
              WHERE tabId={ct.tabid}'''
            cu.execute(query)
            self.conn.commit()
        except Exception as ex:
            raise ex

    def delete_cache_tab_by_id(self, tabid):
        try:
            cu = self.conn.cursor()
            cu.execute(f"DELETE FROM cacheTab WHERE tabId={tabid}")
            self.conn.commit()
        except Exception as ex:
            raise ex

    def get_cache_tab_by_id(self, tabid):
        try:
            cu = self.conn.cursor()
            cu.execute(f'''SELECT tabId, tabType, tabTitle, fullQuery, scrollPosY, bbName, isBook, isChapter, isVerse, bNumber, cNumber, vNumber, trad, orderBy, favFilter 
                FROM cacheTab WHERE tabId={tabid}''')

            c = cu.fetchone()
            if c is None:
                return None

            ct = som_cachetab.SomCacheTab(
                rq=False,
                tabid=c[0],
                tabtype=c[1],
                tabtitle=c[2],
                fullquery=c[3],
                scrollposy=c[4],
                bbname=c[5],
                isbook=c[6],
                ischapter=c[7],
                isverse=c[8],
                bnumber=c[9],
                cnumber=c[10],
                vnumber=c[11],
                trad=c[12],
                orderby=c[13],
                favfilter=c[14]
            )
            return ct
        except Exception as ex:
            raise ex

    def get_cache_tab_id_max(self):
        """
        Get max tab ID (starts at 0)
        :return: cache tab ID max (-1 in case of error of not found)
        """
        try:
            cu = self.conn.cursor()
            cu.execute('''SELECT MAX(tabId) max FROM cacheTab WHERE tabId >= 0''')

            c = cu.fetchone()
            if c is None or c[0] is None:
                return -1

            return c[0]
        except Exception as ex:
            return -1

    def get_cache_tab_count_by_type(self, tabtype):
        """
        Get cache tab count by type
        :return: count of cache tabs or -1 if not found
        """
        try:
            cu = self.conn.cursor()
            cu.execute(f'''SELECT COUNT(*) tot FROM cacheTab WHERE tabType='{tabtype}' ''')

            c = cu.fetchone()
            if c is None or c[0] is None:
                return -1

            return c[0]
        except Exception as ex:
            return -1

    def get_first_cache_tab_id_by_type(self, tabtype):
        """
        Get first cache tab ID by type
        :return: cache tab ID or -1 if not found
        """
        try:
            cu = self.conn.cursor()
            cu.execute(f'''SELECT tabId FROM cacheTab WHERE tabType='{tabtype}' ORDER BY tabId ASC LIMIT 1''')

            c = cu.fetchone()
            if c is None or c[0] is None:
                return -1

            return c[0]
        except Exception as ex:
            return -1

    def get_first_cache_tab_id_by_query(self, tabtype, fullquery):
        """
        Get first cache tab ID by query
        :return: cache tab ID or -1 if not found
        """
        try:
            fullquery = som_util.SomUtil.rq(fullquery)
            where_condition = f"tabType='{tabtype}' AND fullQuery='{fullquery}'" if tabtype != "F" else "tabType='{tabtype}' AND favFilter={favfilter} AND fullQuery='{fullquery}'"

            cu = self.conn.cursor()
            query = f'''SELECT tabId, tabType, tabTitle, fullQuery, scrollPosY, bbName, isBook, isChapter, isVerse, bNumber, cNumber, vNumber, trad, orderBy, favFilter 
                FROM cacheTab WHERE {where_condition} ORDER BY tabId ASC LIMIT 1'''
            cu.execute(query)

            c = cu.fetchone()
            if c is None:
                return -1

            return c[0]
        except Exception as ex:
            return -1

    def get_list_all_cache_tab_for_history(self):
        """
        Get list all cache tabs ordered by tabid desc
        Rem: old version as there is no favs and filters
        """
        try:
            cu = self.conn.cursor()
            cu.execute('''SELECT tabId, tabType, tabTitle, fullQuery, bbName, bNumber, cNumber, vNumber FROM cacheTab ORDER BY tabId DESC''')

            lst = []
            for c in cu.fetchall():
                if c is None:
                    continue
                # item = [c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7]]
                item_lst = [c[0], c[1], c[4], c[3]]
                lst.append(item_lst)

            return lst
        except Exception as ex:
            raise ex
