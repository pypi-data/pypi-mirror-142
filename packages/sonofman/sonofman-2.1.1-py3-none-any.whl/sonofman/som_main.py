#!/usr/bin/env python3

# noinspection SpellCheckingInspection
"""
==========
Install
==========

=> 1) ok when installing all UTF8, iso88591 of en_US, fr_FR, it_IT, es_ES, terminal in UTF8:
sudo dpkg-reconfigure locales
locale

My locales
-------------
LANG=en_US.utf8
LANGUAGE=en_US.utf8
LC_CTYPE="en_US.utf8"
LC_NUMERIC="en_US.utf8"
LC_TIME="en_US.utf8"
LC_COLLATE="en_US.utf8"
LC_MONETARY="en_US.utf8"
LC_MESSAGES="en_US.utf8"
LC_PAPER="en_US.utf8"
LC_NAME="en_US.utf8"
LC_ADDRESS="en_US.utf8"
LC_TELEPHONE="en_US.utf8"
LC_MEASUREMENT="en_US.utf8"
LC_IDENTIFICATION="en_US.utf8"
LC_ALL=en_US.utf8

=> 2) no need to install unicurses, the library is in the project :)


==========================
Last minute before release
==========================
- msg when no result?
- clear tab caches


=============
Next releases
=============
- [Theme ready]
x Check Windows


=============
Other
=============
- bug: echo in PyCharm Terminal!
- resizing => dimensions changes


=============
Coding
=============
- wclear => werase ?
- wgetch => getch  ?
- nodelay(false), linked to getch
"""

import os
import pkg_resources
import re
import sys
import traceback
import xml.etree.ElementTree
import sonofman.som_config as som_config
import sonofman.som_dal as som_dal
import sonofman.som_unicurses as u
import sonofman.som_version as som_version
import sonofman.som_winutil as som_winutil
import sonofman.som_util as som_util
import sonofman.som_cachetab as som_cachetab

_DEBUG = False

somconfig = som_config.SomConfig()
somdal = som_dal.SomDal(path_to_data=somconfig.path)
somversion = som_version.SomVersion
somsignal = None
somutil = som_util.SomUtil

# if _DEBUG:
#     import sonofman.som_signal as som_signal
#     # noinspection PyRedeclaration
#     somsignal = som_signal.SomSignal("{0}".format(pkg_resources.resource_filename('sonofman.data', 'log.txt')))

_locale = None
_alt_locale = None
_tabId = -1
_bbName = _tbbName = "k"
_bNumber = 1
_cNumber = 1
_history = []
_action_type = None
_action_bbname = None
_action_query = None
_delimiterVerse = "§§"
_attrFirst = u.A_REVERSE
_maxY = 0
_maxX = 0
_searchStringLimit = 3
_useColors = False
_colorTheme = None
_colorThemeDialog = None
_colorThemeErr = None
_colorThemeFunc1 = None
_colorThemeFunc2 = None
_colorBible = {"k": "", "v": "", "l": "", "d": "", "a": "", "o": "", "s": "", "2": ""}
_themeNr = None
_reset_status_before_key = True
_resource = {}
_title = ""
_sub_title = ""
_xml = None
_win_row = None
_panel_row = None
_win_status = None
_win_title = None
_wm_util = None
_cy = -1


def set_locale(local):
    """
    Set locale resources
    :param local: "en" (default), "es", "fr", "it", "pt", "de"
    :return: set locale resource
    """

    global _resource, _locale, _alt_locale, _bbName, _tbbName

    if local == "en":
        _resource = {
            "ABOUT": "About/Contact",
            "ALL": "All",
            "ALT_LANGUAGE": "ALT_LANGUAGE",
            "ARTICLES": "Articles",
            "BIBLE_PREFERED": "Bible preferred",
            "BIBLE_MULTI": "Bibles to display",
            "BOOK": "Book",
            "BOOKS": "Books",
            "CLEAR": "Clear",
            "COLOR_MODE": "Color (mode)",
            "COLORS": "Colors",
            "CONFIRM": "Confirm (<ENTER>, <ESC>)",
            "ERR": "Error",
            "ERR_EMPTY": "No result!",
            "ERR_INVALID": "Invalid!",
            "ERR_OPERATION_CANCELLED": "Operation cancelled!",
            "FILTER": "Filter",
            "FOUND": "Found",
            "HELP": "Help",
            "KEYS": "Keys",
            "MENU": "Menu",
            "PARABLES": "Parables",
            "OPEN": "Open",
            "SAVE": "Save",
            "SEARCH": "Search",
            "SEARCH_LANGUAGE": "Bibles",
            "SETTINGS": "Settings",
            "SYSTEM": "System",
            "QUIT": "Quit",
            "CONTEXT_MENU": "Context menu",
            "OPEN_CHAPTER": "Open chapter",
            "CROSS_REFERENCES": "Cross references",
            "HISTORY": "History"
        }
    elif local == "es":
        _resource = {
            "ABOUT": "A propósito/Contacto",
            "ALL": "Todo",
            "ALT_LANGUAGE": "ALT_LANGUAGE",
            "ARTICLES": "Artículos",
            "BIBLE_PREFERED": "Biblia preferida",
            "BIBLE_MULTI": "Biblias a mostrar",
            "BOOK": "Libro",
            "BOOKS": "Libros",
            "COLOR_MODE": "Color (modo)",
            "COLORS": "Colores",
            "CLEAR": "Eliminar",
            "CONFIRM": "Confirma (<ENTER>, <ESC>)",
            "ERR": "Errore",
            "ERR_EMPTY": "Ningún resultado!",
            "ERR_INVALID": "Inválido!",
            "ERR_OPERATION_CANCELLED": "Operación cancelada!",
            "FILTER": "Filtro",
            "FOUND": "Encontrado",
            "HELP": "Ayuda",
            "KEYS": "Teclas",
            "MENU": "Menú",
            "PARABLES": "Parábolas",
            "OPEN": "Abrir",
            "SAVE": "Salvar",
            "SEARCH": "Buscar",
            "SEARCH_LANGUAGE": "Biblias",
            "SETTINGS": "Parámetros",
            "SYSTEM": "System",
            "QUIT": "Cerrar",
            "CONTEXT_MENU": "Menú contextual",
            "OPEN_CHAPTER": "Abrir capítulo",
            "CROSS_REFERENCES": "Referencias cruzadas",
            "HISTORY": "Historial"
        }
    elif local == "fr":
        _resource = {
            "ABOUT": "A propos/Contact",
            "ALL": "Tout",
            "ALT_LANGUAGE": "ALT_LANGUAGE",
            "ARTICLES": "Articles",
            "BIBLE_PREFERED": "Bible préférée",
            "BIBLE_MULTI": "Bibles à afficher",
            "BOOK": "Livre",
            "BOOKS": "Livres",
            "CLEAR": "Effacer",
            "COLOR_MODE": "Couleur (mode)",
            "COLORS": "Couleurs",
            "CONFIRM": "Confirmez (<ENTER>, <ESC>)",
            "ERR": "Erreur",
            "ERR_EMPTY": "Pas de résultat!",
            "ERR_INVALID": "Invalide!",
            "ERR_OPERATION_CANCELLED": "Opération annulée!",
            "FILTER": "Filtre",
            "FOUND": "Trouvé",
            "HELP": "Aide",
            "KEYS": "Touches",
            "MENU": "Menu",
            "OPEN": "Ouvrir",
            "PARABLES": "Paraboles",
            "SAVE": "Sauver",
            "SEARCH": "Chercher",
            "SEARCH_LANGUAGE": "Bibles",
            "SETTINGS": "Params",
            "SYSTEM": "System",
            "QUIT": "Quitter",
            "CONTEXT_MENU": "Menu contextuel",
            "OPEN_CHAPTER": "Ouvrir chapitre",
            "CROSS_REFERENCES": "Références croisées",
            "HISTORY": "Historique"
        }
    elif local == "it":
        _resource = {
            "ABOUT": "A proposito/Contatto",
            "ALL": "Tutto",
            "ALT_LANGUAGE": "ALT_LANGUAGE",
            "ARTICLES": "Articoli",
            "BIBLE_PREFERED": "Bibbia preferita",
            "BIBLE_MULTI": "Bibbie ad affiggere",
            "BOOK": "Libro",
            "BOOKS": "Libri",
            "CLEAR": "Eliminare",
            "COLOR_MODE": "Colore (modalità)",
            "COLORS": "Colori",
            "CONFIRM": "Conferma (<ENTER>, <ESC>)",
            "ERR": "Errore",
            "ERR_EMPTY": "Alcun risultato!",
            "ERR_INVALID": "Invalido!",
            "ERR_OPERATION_CANCELLED": "Operazione cancellata!",
            "FILTER": "Filtro",
            "FOUND": "Trovato",
            "HELP": "Aiuto",
            "KEYS": "Tasti",
            "MENU": "Menu",
            "PARABLES": "Parabole",
            "OPEN": "Aprire",
            "SAVE": "Salvare",
            "SEARCH": "Cercare",
            "SEARCH_LANGUAGE": "Bibbie",
            "SETTINGS": "Parametri",
            "SYSTEM": "System",
            "QUIT": "Chiudere",
            "CONTEXT_MENU": "Menu contestuale",
            "OPEN_CHAPTER": "Aprire capitolo",
            "CROSS_REFERENCES": "Riferimenti incrociati",
            "HISTORY": "Cronologia"
        }
    elif local == "pt":
        _resource = {
            "ABOUT": "Sobre/Contato",
            "ALL": "Tudo",
            "ALT_LANGUAGE": "ALT_LANGUAGE",
            "ARTICLES": "Artigos",
            "BIBLE_PREFERED": "Bíblia favorita",
            "BIBLE_MULTI": "Bíblias para mostrar",
            "BOOK": "Livro",
            "BOOKS": "Livros",
            "COLOR_MODE": "Cor (modo)",
            "COLORS": "Cores",
            "CLEAR": "Eliminar",
            "CONFIRM": "Confirma (<ENTER>, <ESC>)",
            "ERR": "Errore",
            "ERR_EMPTY": "Nenhum resultado!",
            "ERR_INVALID": "Inválido!",
            "ERR_OPERATION_CANCELLED": "Operação cancelada!",
            "FILTER": "Filtro",
            "FOUND": "Encontrado",
            "HELP": "Ajuda",
            "KEYS": "Teclas",
            "MENU": "Menu",
            "PARABLES": "Parábolas",
            "OPEN": "Abrir",
            "SAVE": "Salvar",
            "SEARCH": "Buscar",
            "SEARCH_LANGUAGE": "Bíblias",
            "SETTINGS": "Parâmetros",
            "SYSTEM": "Sistema",
            "QUIT": "Fechar",
            "CONTEXT_MENU": "Menu de contexto",
            "OPEN_CHAPTER": "Abrir capítulo",
            "CROSS_REFERENCES": "Referências cruzadas",
            "HISTORY": "Histórico"
        }
    elif local == "de":
        _resource = {
            "ABOUT": "Über/Kontakt",
            "ALL": "Alle",
            "ALT_LANGUAGE": "Alternative Sprache (Artikeln)",
            "ARTICLES": "Artikeln",
            "BIBLE_PREFERED": "Lieblingsbibel",
            "BIBLE_MULTI": "Zu zeigende Bibeln",
            "BOOK": "Buch",
            "BOOKS": "Bücher",
            "CLEAR": "Zu löschen",
            "COLOR_MODE": "Farbe (Modus)",
            "COLORS": "Farben",
            "CONFIRM": "Bestätigen (<ENTER>, <ESC>)",
            "ERR": "Fehler",
            "ERR_EMPTY": "Kein Ergebnis!",
            "ERR_INVALID": "Ungültig!",
            "ERR_OPERATION_CANCELLED": "Vorgang abgebrochen!",
            "FILTER": "Filter",
            "FOUND": "Gefunden",
            "HELP": "Hilfe",
            "KEYS": "Tasten",
            "MENU": "Menü",
            "PARABLES": "Parabeln",
            "OPEN": "Öffnen",
            "SAVE": "Speichern",
            "SEARCH": "Suchen",
            "SEARCH_LANGUAGE": "Bibeln",
            "SETTINGS": "Einstellungen",
            "SYSTEM": "System",
            "QUIT": "Beenden",
            "CONTEXT_MENU": "Kontextmenü",
            "OPEN_CHAPTER": "Kapitel öffnen",
            "CROSS_REFERENCES": "Querverweisen",
            "HISTORY": "Geschichte"
        }
    else:
        _locale = "en"
        _alt_locale = _locale
        _bbName = _tbbName = "k"
        somutil.print("! Unsupported locale ('{0}'), locale set to 'en'.".format(local))
        set_locale(_locale)


# noinspection PyBroadException
def res(k):
    try:
        return _resource[k]
    except Exception:
        if _DEBUG:
            somutil.print("! Unknown key: '{0}'".format(k))
        return "KEY"


def res_ponct(k):
    """Add ponctuation for presentation"""
    return "{0}: ".format(res(k))


def print_ex(ex):
    msg = "{0} > {1}\n\n".format(res("ERR"), ex)
    stack = stack_trace()
    sys.stderr.write(msg)
    sys.stderr.write(stack)

    height = _maxY
    width = _maxX

    win_ex = u.newwin(height, width, 2, 0)
    u.mvwaddstr(win_ex, 1, 1, msg, _colorTheme)
    u.waddstr(win_ex, stack, _colorTheme)
    u.wgetch(win_ex)
    finish(1)


def stack_trace():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lst = ["*** "]
    lst_trace = traceback.format_exception(exc_type, exc_value, exc_traceback)
    lst.append("".join(str(i) for i in lst_trace))
    return "".join(str(i) for i in lst)


def show_search(is_search):
    """
    Search in the bible or open a book
    :param is_search: True = search, False = open a book only
    :return: 1) bbname
             2) query
    """

    dict_menu = get_bible_dict_verbose()
    width = _maxX

    msg = res_ponct("SEARCH") if is_search else res_ponct("OPEN")
    menu_title = res("SEARCH_LANGUAGE")

    # Bible
    # noinspection PyTypeChecker
    selected_bible_menu_index = get_bible_menu_index(_bbName)
    menu_selected, movement, char_key = show_menu(0, menu_title, dict_menu, False, False, selected_bible_menu_index)

    if menu_selected < 0:
        return None, None

    bbnames = get_bible_dict_short()
    bbname_selected = bbnames[menu_selected]

    # To return
    book_nr = ""

    # Book (1 line)
    language_selected = "({0}) ".format(dict_menu[menu_selected])
    book_name_selected = show_books(0, res("BOOKS"), bbname_selected, res("ALL") if is_search else None)

    if book_name_selected is None:
        return None, None
    elif book_name_selected == res("ALL"):
        upd_book_name = ""
    else:
        book_nr = book_name_selected.split(")")[0].replace("(", "").lstrip()
        book_nr = "{0:} ".format(book_nr)
        book_name_start = book_name_selected.find(")") + 1
        upd_book_name = "{0} ".format(book_name_selected[book_name_start:].rstrip())

    win_q = u.newwin(3, width, 2, 0)     # len(language_selected) + len(upd_book_name)
    u.wbkgd(win_q, " ", _colorTheme)
    u.mvwhline(win_q, 2, 0, u.ACS_HLINE + _colorTheme, width)
    u.mvwaddstr(win_q, 0, 0, language_selected)
    u.waddstr(win_q, upd_book_name)
    u.update_panels()
    u.doupdate()

    if is_search:
        u.echo()
        search_string = u.wgetstr(win_q)
        u.noecho()

        search_string = search_string.decode("utf-8") if len(search_string) > 0 else ""
        u.wclear(win_q)
        u.wrefresh(win_q)
    else:
        chapter_count = somdal.get_bible_chapter_count_by_book(book_nr)[0]

        while True:
            u.echo()
            search_string = u.wgetstr(win_q)    # TODO: get escape and quit
            u.noecho()

            search_string = search_string.strip().decode("utf-8") if len(search_string) > 0 else "1"
            is_number = re.match(r"^[\d]*$", search_string)
            cnumber = -1

            if is_number:
                cnumber = int(search_string)
            if not is_number or cnumber <= 0 or cnumber > chapter_count:
                msg = "{0} [1..{1}]".format(res("ERR_INVALID"), chapter_count)
                show_status(msg, _colorTheme, False)
                u.wclear(win_q)
                u.mvwhline(win_q, 2, 0, u.ACS_HLINE + _colorTheme, width)
                u.mvwaddstr(win_q, 0, 0, language_selected)
                u.waddstr(win_q, upd_book_name)
                u.wrefresh(win_q)
                continue
            else:
                break

    u.delwin(win_q)

    # Finally
    u.noecho()
    # if win_b is not None:
    #    u.delwin(win_b)

    return bbname_selected, "{0}{1}".format(book_nr, search_string)


def show_menu(menu_x, menu_title, dict_menu, allow_scrolling_menu=False, allow_filter_menu=False, selected_menu_index=0):
    """
    Create, show menu and returns the selected item index
    :param menu_x: position x; 0 as default
    :param menu_title: title msg
    :param dict_menu: menu. Dictionary of text => no colors: { 0: "text"... }, \
    Dictionary of list items => colors: { 0: ["text", "attributes"]... }
    :param allow_scrolling_menu: scrolling menu
    :param allow_filter_menu: use filter (press TAB key to change filter)
    :param selected_menu_index: start value selected
    :return: 1) index of item selected or position (-1 if not selected)
             2) -1|0|1 has movement (-1 = up, 0 = selected or ESC, 1 = down, 3 = filter)
             3) char of key pressed when allow_filter_menu is True else None
    """

    win_b = win_lb = panel = None
    try:
        if len(dict_menu) == 0:
            return 0, -1, None    # Reload up

        allow_color_menu = True if type(dict_menu[0]) is list else False
        max_height = len(dict_menu) + 2
        max_width = len(menu_title)

        for i in dict_menu.keys():
            menu_item_width = len(dict_menu.get(i))
            if menu_item_width > max_width:
                max_width = menu_item_width

        max_width += 4
        if max_height > _maxY:
            raise Exception("Terminal height should be bigger!")

        size = len(dict_menu)

        win_lb = u.newwin(max_height + 1, _maxX, 2, menu_x)     # TODO: here to remove hline, use max_width instead
        u.wbkgd(win_lb, " ", _colorTheme)
        u.mvwhline(win_lb, max_height, 0, u.ACS_HLINE + _colorTheme, _maxX)
        u.wrefresh(win_lb)

        win_b = u.newwin(max_height, max_width, 2, menu_x)
        u.wbkgd(win_b, " ", _colorTheme)
        panel = u.new_panel(win_lb)
        u.panel_above(panel)
        u.update_panels()
        u.doupdate()

        u.noecho()
        u.keypad(win_b, True)

        highlight = selected_menu_index
        # TODO: reverse the selected
        while True:
            u.wattron(win_b, _colorThemeDialog)
            u.box(win_b)
            u.mvwaddstr(win_b, 0, 2, menu_title)
            u.wattroff(win_b, _colorTheme)

            for i in range(0, size):
                attr = _colorTheme if i != highlight else u.A_REVERSE
                if not allow_color_menu:
                    u.mvwaddstr(win_b, 1 + i, 2, dict_menu[i], attr)
                else:
                    u.mvwaddstr(win_b, 1 + i, 2, dict_menu[i][0], eval(dict_menu[i][1]) if i != highlight else eval(dict_menu[i][1]) + u.A_REVERSE)

            key = u.wgetch(win_b)
            if key == 27:
                return -1, 0, None
            elif key in (32, 10):   # space, enter
                return highlight, 0, None
            elif key == u.KEY_DOWN:
                if highlight + 1 >= size:
                    if not allow_scrolling_menu:
                        highlight = 0
                    else:
                        return 0, 1, None
                else:
                    highlight += 1
            elif key == u.KEY_UP:
                if highlight - 1 < 0:
                    if not allow_scrolling_menu:
                        highlight = size - 1
                    else:
                        return size - 1, -1, None
                else:
                    highlight -= 1
            elif key == u.KEY_END:
                highlight = size - 1
            elif key == u.KEY_HOME:
                highlight = 0
            elif key == u.KEY_RIGHT:
                if not allow_scrolling_menu:
                    pass
                else:
                    return highlight + size, 1, None
            elif key == u.KEY_LEFT:
                if not allow_scrolling_menu:
                    pass
                else:
                    return highlight - size, -1, None
            else:
                if re.match("^[a-zA-Z]*$", chr(key)):
                    if allow_filter_menu:
                        return highlight, 3, chr(key)
    except Exception as ex:
        print_ex(ex)
    finally:
        if win_b is not None:
            u.delwin(win_b)
        if win_lb is not None:
            u.delwin(win_lb)
        if panel is not None:
            u.del_panel(panel)
        u.update_panels()
        u.doupdate()


def clear_status():
    """
    Clear status bar
    """
    if _reset_status_before_key:
        u.wclear(_win_status)
        u.wrefresh(_win_status)


# noinspection PyBroadException
def show_status(msg, attr, reset_status_before_key=False):
    """
    Show message in status bar some seconds
    :param msg: message
    :param attr: attribute
    :param reset_status_before_key: if True, wclear will clear the status before user input in main loop
    """

    global _reset_status_before_key
    _reset_status_before_key = reset_status_before_key

    try:
        if len(msg) == 0:
            return
        msg = msg.replace("\n", " ")

        x = y = 0
        u.wclear(_win_status)
        u.mvwaddstr(_win_status, y, x, msg, attr)
        u.wrefresh(_win_status)

        # TODO: show the msg for specific time
    except Exception:
        pass
        # TODO: print_ex(ex) ?


def save_action(action_type, action_bbname, action_query, should_add=True):
    """
    Save action type
    :param action_type: "A": article, "P": parable, "S": search, "B" book, other: none
    :param action_bbname: bible name
    :param action_query: query
    :param should_add: True:add, False:update
    """
    global _action_type, _action_bbname, _action_query, _history, _tabId

    _action_type = action_type
    _action_bbname = action_bbname
    _action_query = action_query
    _history = [action_bbname, action_query]

    tabtype = "S" if _action_type == "B" else _action_type
    fullquery = _action_query
    bbname = _action_bbname

    if should_add:
        # Add
        tabid = somdal.get_first_cache_tab_id_by_query(tabtype, fullquery)
        if tabid >= 0:
            if tabid != _tabId or _tabId < 0:
                _tabId = tabid
                show_title_and_subtitle()
            return

        tabid = somdal.get_cache_tab_id_max() + 1
        ct = som_cachetab.SomCacheTab(
            rq=True,
            tabid=tabid,
            tabtype=tabtype,
            tabtitle=_action_query,
            fullquery=fullquery,
            scrollposy=0,
            bbname=bbname,
            isbook=0,
            ischapter=0,
            isverse=0,
            bnumber=0,
            cnumber=0,
            vnumber=0,
            trad=_tbbName,
            orderby=0,
            favfilter=0
        )
        somdal.add_cache_tab(ct)
        _tabId = tabid
        show_title_and_subtitle()
    else:
        # Update
        tabid = _tabId
        ct = som_cachetab.SomCacheTab(
            rq=True,
            tabid=tabid,
            tabtype=tabtype,
            tabtitle=_action_query,
            fullquery=fullquery,
            scrollposy=0,
            bbname=bbname,
            isbook=0,
            ischapter=0,
            isverse=0,
            bnumber=0,
            cnumber=0,
            vnumber=0,
            trad=_tbbName,
            orderby=0,
            favfilter=0
        )
        somdal.update_cache_tab(ct)
        # _tabId OK

    # Manage limit
    if tabtype in ("A", "P"):
        count = somdal.get_cache_tab_count_by_type(tabtype)
        if count > som_util.SomUtil.history_limit:
            tabid_del = somdal.get_first_cache_tab_id_by_type(tabtype)
            if tabid_del >= 0:
                somdal.delete_cache_tab_by_id(tabid_del)


def save_title(title):
    global _title
    _title = title.replace("\n", "")


def save_sub_title(sub_title):
    global _sub_title
    _sub_title = sub_title.replace("\n", "")


# noinspection PyBroadException
def show_title_and_subtitle():
    """Show full title bar"""
    global _tabId

    try:
        title = _title
        sub_title = _sub_title

        if len(_title) == 0:
            title = somversion.app_name
            sub_title = ""
            full_title = title
        elif len(sub_title) == 0:
            full_title = title
        else:
            words = sub_title.split(" ")
            if len(words) == 4:
                if words[1].isdigit() and words[2].isdigit() and words[3].upper() == "CR:":
                    sub_title = "{0} {1}.{2}".format(words[0], words[1], words[2])
            full_title = "[{2}] {0} > {1}".format(title, sub_title, _tabId)

        size = _maxX
        if len(full_title) >= size:
            full_title = "{0}.".format(full_title[0: size - 1])

        y = 0
        x = _maxX - len(full_title) - 1
        if x < 0:
            x = 0

        u.wclear(_win_title)
        u.mvwaddstr(_win_title, y, x, full_title, u.A_NORMAL)
        u.wrefresh(_win_title)
    except Exception:
        pass
        # TODO: print_ex(ex) ?


def merge_words(from_word_pos, words):
    to_word_pos = len(words)
    merged_string = ""
    for i in range(from_word_pos, to_word_pos):
        fmt = "{0} {1}" if i != from_word_pos else "{0}{1}"
        merged_string = fmt.format(merged_string, words[i])
    return merged_string


# noinspection PyUnusedLocal
def prepare_bible_search_string(bbname, query):
    """
    Prepare search bible parameters (called only by get_bible_search)
    :param bbname: bible name
    :param query: complete query
    :return: search_type, book_number, chapter_number, verse_number, verse_number_to, search_string, book name verbose
            search_type: 0:no search, 1:search string, 2:verses from to, 3:book, 4:cr
    """

    book_number = chapter_number = verse_number = verse_number_to = -1
    book_name_verbose = book_short_name = ""
    search_string = ""
    search_type = 0   # 0:no search, 1:search string, 2:verses from to, 3:book, 4:cr

    words = query.split(" ")
    word_count = len(words)
    if word_count == 0:
        pass
    else:
        if search_type == 0:
            if words[0].isdigit():
                book_number = int(words[0])

        if search_type == 0:
            if word_count == 4:
                if words[0].isdigit() and words[1].isdigit() and words[2].isdigit() and words[3].isdigit():
                    search_type = 2
                    if book_number <= 0:
                        book_number = int(words[0])
                    chapter_number = int(words[1])
                    verse_number = int(words[2])
                    verse_number_to = int(words[3])
                    # call
                elif words[1].isdigit() and words[2].isdigit() and words[3].upper() == "CR:":
                    search_type = 4
                    if book_number <= 0:
                        book_number = int(words[0])
                    chapter_number = int(words[1])
                    verse_number = int(words[2])
                    verse_number_to = -1
                    # call

        if search_type == 0:
            if word_count == 3:
                # <bNumber> <cNumber> <vNumber>
                if (words[0].isdigit() and words[1].isdigit() and words[2].isdigit()) or (
                        book_number > 0 and words[1].isdigit() and words[2].isdigit()):
                    search_type = 1
                    if book_number <= 0:
                        book_number = int(words[0])
                    chapter_number = int(words[1])
                    verse_number = int(words[2])
                    # call

        if search_type == 0:
            if word_count >= 3:
                # <bNumber> <cNumber> <expr> ...
                if (words[0].isdigit() and words[1].isdigit()) or (book_number > 0 and words[1].isdigit()):
                    search_type = 1
                    if book_number <= 0:
                        book_number = int(words[0])
                    chapter_number = int(words[1])
                    verse_number = 0
                    search_string = merge_words(2, words)
                    # call

        if search_type == 0:
            if word_count == 2:
                # <bNumber> <cNumber>
                if (words[0].isdigit() and words[1].isdigit()) or (book_number > 0 and words[1].isdigit()):
                    search_type = 3
                    if book_number <= 0:
                        book_number = int(words[0])
                    chapter_number = int(words[1])
                    verse_number = 0
                    # call

        if search_type == 0:
            if word_count >= 2:
                # <bNumber> <expr> ...
                if words[0].isdigit() or book_number > 0:
                    search_type = 1
                    if book_number <= 0:
                        book_number = int(words[0])
                    chapter_number = 0
                    verse_number = 0
                    search_string = merge_words(1, words)
                    # call

        if search_type == 0:
            if word_count == 1:
                # <bNumber>
                if words[0].isdigit():
                    search_type = 3
                    if book_number <= 0:
                        book_number = int(words[0])
                    chapter_number = 1
                    verse_number = 0
                    # call

        if search_type == 0:
            if len(query) >= _searchStringLimit:
                # Finally <expr> ...
                search_type = 1
                book_number = 0
                chapter_number = 0
                verse_number = 0
                search_string = merge_words(0, words)
                # call

        if book_number > 0:
            book_name_verbose, book_short_name = somdal.get_book_ref(bbname, book_number)

    # Finally
    return search_type, book_number, chapter_number, verse_number, verse_number_to, search_string, book_name_verbose


def get_bible_search(bbname, query, should_add=True):
    """
    Get bible search result (called after show_search)
    :param bbname: bible name
    :param query: query
    :param should_add: True:add, False:update
    :return: strings
    """

    global _bNumber, _cNumber

    # TODO: change here the regex. Actually it's impossible to quit a search, a book search
    # TODO: don't change history if we quit or there is no result
    # TODO: if there is no result, tell it and ask to retry or quit

    s = ""
    search_type = 0
    if len(query) > 0:
        search_type, book_number, chapter_number, verse_number, verse_number_to, search_string, book_name_verbose = prepare_bible_search_string(bbname, query)

        if search_type > 0:
            vcount = 0
            _bNumber = book_number
            _cNumber = chapter_number

            if search_type == 1:
                save_title(res("SEARCH"))
                s, vcount = somdal.search_bible_string(_delimiterVerse, _tbbName, bbname, book_number,
                                                       chapter_number, search_string)
            elif search_type == 2:
                save_title(res("SEARCH"))
                s = somdal.get_verses(_delimiterVerse, _tbbName, book_number, chapter_number,
                                      verse_number, verse_number_to)
            elif search_type == 3:
                save_title(res("BOOKS"))
                s = somdal.search_bible(_delimiterVerse, _tbbName, book_number, chapter_number)

            elif search_type == 4:
                save_title(res("CROSS_REFERENCES"))
                s = somdal.get_cross_references(_delimiterVerse, _tbbName, book_number, chapter_number, verse_number)

            if len(s) > 0:
                _wm_util.move(0)
                if len(book_name_verbose) > 0:
                    words = query.split(" ")
                    words[0] = book_name_verbose
                    sub_title = " ".join(words)
                else:
                    sub_title = query

                save_sub_title(sub_title)
                show_title_and_subtitle()

                if search_type == 1:
                    msg = "{0}: {1}".format(res("FOUND"), vcount)
                    show_status(msg, _colorTheme, False)       # was: + u.A_BOLD
            else:
                save_sub_title(query)
                show_title_and_subtitle()
                show_status(res("ERR_EMPTY"), _colorTheme, False)
                return ""
    else:
        save_title(res("SEARCH"))
        save_sub_title(query)
        show_title_and_subtitle()
        show_status(res("ERR_OPERATION_CANCELLED"), _colorTheme, False)
        return ""

    # Save history
    if search_type == 0:
        action_type = ""
    elif search_type == 3:
        action_type = "B"
    else:
        action_type = "S"

    save_action(action_type, bbname, query, should_add=should_add)
    return s


def menu():
    """
    Menu of preferences
    :return: False: ESC, True: used
    """
    global _useColors

    menu_k = "MENU"
    menu_title = res(menu_k)

    show_menu_title = res(menu_k)
    save_title(show_menu_title)

    if _locale == "de":
        dict_menu = {
            0: res("BIBLE_PREFERED"),
            1: res("ALT_LANGUAGE"),
            2: res("BIBLE_MULTI"),
            3: res("COLOR_MODE"),
            4: res("COLORS"),
            5: res("ABOUT")
        }
    else:
        dict_menu = {
            0: res("BIBLE_PREFERED"),
            1: res("BIBLE_MULTI"),
            2: res("COLOR_MODE"),
            3: res("COLORS"),
            4: res("ABOUT")
        }

    menu_selected, movement, char_key = show_menu(0, menu_title, dict_menu, False, False)
    menu_is_used = False

    if _locale == "de":
        if menu_selected < 0:
            menu_is_used = False
        elif menu_selected == 0:
            menu_is_used = False if show_bible_prefered() is None else True
        elif menu_selected == 1:
            show_alt_language()
            menu_is_used = True
        elif menu_selected == 2:
            show_bible_multi()
            menu_is_used = True
        elif menu_selected == 3:
            menu_is_used = show_themes()
        elif menu_selected == 4:
            show_bible_colors()
            menu_is_used = True
        elif menu_selected == 5:
            show_about()
            menu_is_used = True
        return menu_is_used
    else:
        if menu_selected < 0:
            menu_is_used = False
        elif menu_selected == 0:
            menu_is_used = False if show_bible_prefered() is None else True
        elif menu_selected == 1:
            show_bible_multi()
            menu_is_used = True
        elif menu_selected == 2:
            menu_is_used = show_themes()
        elif menu_selected == 3:
            show_bible_colors()
            menu_is_used = True
        elif menu_selected == 4:
            show_about()
            menu_is_used = True
        return menu_is_used


def show_bible_prefered():
    """
    Menu of bible prefered
    :return: item selected or None
    """
    global _bbName, _tbbName, _locale, _alt_locale

    # panel_below(panel_search)
    dict_menu = get_bible_dict_verbose()
    menu_title_upd = "{0}: {1} ".format(res("BIBLE_PREFERED"), _bbName)
    menu_item_selected, movement, char_key = show_menu(0, menu_title_upd, dict_menu, False)

    if menu_item_selected < 0:
        return None
    elif menu_item_selected == 0:
        _bbName = "k"
        _locale = "en"
        _alt_locale = _locale
    elif menu_item_selected == 1:
        _bbName = "2"
        _locale = "en"
        _alt_locale = _locale
    elif menu_item_selected == 2:
        _bbName = "v"
        _locale = "es"
        _alt_locale = _locale
    elif menu_item_selected == 3:
        _bbName = "l"
        _locale = "fr"
        _alt_locale = _locale
    elif menu_item_selected == 4:
        _bbName = "o"
        _locale = "fr"
        _alt_locale = _locale
    elif menu_item_selected == 5:
        _bbName = "d"
        _locale = "it"
        _alt_locale = _locale
    elif menu_item_selected == 6:
        _bbName = "a"
        _locale = "pt"
        _alt_locale = _locale
    elif menu_item_selected == 7:
        _bbName = "s"
        _locale = "de"
        _alt_locale = "en"

    if _tbbName.find(_bbName) < 0:
        _tbbName = "{0}{1}".format(_bbName, _tbbName)

    restart(True)
    return menu_item_selected


def show_alt_language():
    """
    Menu of alt language
    :return: item selected or None
    """
    global _alt_locale

    dict_menu = {
        0: "English",
        1: "Español",
        2: "Français",
        3: "Italiano",
        4: "Português"
    }

    if _alt_locale == "es":
        alt_language_verbose = dict_menu[1]
    elif _alt_locale == "fr":
        alt_language_verbose = dict_menu[2]
    elif _alt_locale == "it":
        alt_language_verbose = dict_menu[3]
    elif _alt_locale == "pt":
        alt_language_verbose = dict_menu[4]
    else:
        alt_language_verbose = dict_menu[0]

    menu_title_upd = "{0}: {1} ".format(res("ALT_LANGUAGE"), alt_language_verbose)
    menu_item_selected, movement, char_key = show_menu(0, menu_title_upd, dict_menu, False)

    if menu_item_selected < 0:
        return None
    elif menu_item_selected == 0:
        _alt_locale = "en"
    elif menu_item_selected == 1:
        _alt_locale = "es"
    elif menu_item_selected == 2:
        _alt_locale = "fr"
    elif menu_item_selected == 3:
        _alt_locale = "it"
    elif menu_item_selected == 4:
        _alt_locale = "pt"

    restart(True)
    return menu_item_selected


def show_bible_multi():
    """
    Menu to select bibles to display
    """
    global _tbbName, _bbName

    dict_menu = {
        0: res("CLEAR"),
        1: "(EN) King James 1611 (K)",
        2: "(EN) King James 2000 (2)",
        3: "(ES) Reina Valera (V)",
        4: "(FR) Louis Segond (L)",
        5: "(FR) Ostervald (O)",
        6: "(IT) G. Diodati (D)",
        7: "(PT) Almeida (A)",
        8: "(DE) Schlachter (S)"
    }

    # TODO: use get_bible_dict and change CLEAR option
    menu_title = res("BIBLE_MULTI")
    tbbname = _tbbName

    # TODO: if to simplify
    while True:
        menu_title_upd = "{0}: {1} ".format(menu_title, tbbname)
        menu_item_selected, movement, char_key = show_menu(0, menu_title_upd, dict_menu, False, False)

        if menu_item_selected < 0:
            if len(tbbname) == 0:
                _tbbName = tbbname = _bbName
            else:
                if tbbname.find(_bbName) < 0:
                    tbbname = "{0}{1}".format(_bbName, tbbname)
                _tbbName = tbbname
            break

        elif menu_item_selected == 0:
            tbbname = ""

        elif menu_item_selected == 1:
            bbname = "k"
            if tbbname.find(bbname) < 0:
                tbbname = "{0}{1}".format(tbbname, bbname)
            else:
                tbbname = tbbname.replace(bbname, "")

        elif menu_item_selected == 2:
            bbname = "2"
            if tbbname.find(bbname) < 0:
                tbbname = "{0}{1}".format(tbbname, bbname)
            else:
                tbbname = tbbname.replace(bbname, "")

        elif menu_item_selected == 3:
            bbname = "v"
            if tbbname.find(bbname) < 0:
                tbbname = "{0}{1}".format(tbbname, bbname)
            else:
                tbbname = tbbname.replace(bbname, "")

        elif menu_item_selected == 4:
            bbname = "l"
            if tbbname.find(bbname) < 0:
                tbbname = "{0}{1}".format(tbbname, bbname)
            else:
                tbbname = tbbname.replace(bbname, "")

        elif menu_item_selected == 5:
            bbname = "o"
            if tbbname.find(bbname) < 0:
                tbbname = "{0}{1}".format(tbbname, bbname)
            else:
                tbbname = tbbname.replace(bbname, "")

        elif menu_item_selected == 6:
            bbname = "d"
            if tbbname.find(bbname) < 0:
                tbbname = "{0}{1}".format(tbbname, bbname)
            else:
                tbbname = tbbname.replace(bbname, "")

        elif menu_item_selected == 7:
            bbname = "a"
            if tbbname.find(bbname) < 0:
                tbbname = "{0}{1}".format(tbbname, bbname)
            else:
                tbbname = tbbname.replace(bbname, "")

        elif menu_item_selected == 8:
            bbname = "s"
            if tbbname.find(bbname) < 0:
                tbbname = "{0}{1}".format(tbbname, bbname)
            else:
                tbbname = tbbname.replace(bbname, "")

    restart(False)


def show_bible_colors():
    """
    Menu to select bible colors
    """
    global _colorBible

    menu_title = res("COLORS")
    dict_menu = get_bible_dict_verbose()
    if not _useColors:
        dict_menu_colors = {
            0: ["Normal", "u.A_NORMAL"],
            1: ["Dim", "u.A_DIM"],
            2: ["Bold", "u.A_BOLD"],
            3: ["Underline", "u.A_UNDERLINE"],
            4: ["Reverse", "u.A_REVERSE"]
        }
        replace_colors()
    else:
        # TODO: add more colors and make pagination
        dict_menu_colors = {
            0: ["Normal", "u.A_NORMAL"],
            1: ["Dim", "u.A_DIM"],
            2: ["Bold", "u.A_BOLD"],
            3: ["Underline", "u.A_UNDERLINE"],
            4: ["Reverse", "u.A_REVERSE"],
            5: ["COLOR1", "u.color_pair(1)"],
            6: ["COLOR2", "u.color_pair(2)"],
            7: ["COLOR3", "u.color_pair(3)"],
            8: ["COLOR4", "u.color_pair(4)"],
            9: ["COLOR5", "u.color_pair(5)"],
            10: ["COLOR6", "u.color_pair(6)"],
            11: ["COLOR11", "u.color_pair(11)"],
            12: ["COLOR12", "u.color_pair(12)"],
            13: ["COLOR13", "u.color_pair(13)"],
            14: ["COLOR21", "u.color_pair(21)"],
            15: ["COLOR22", "u.color_pair(22)"]
        }

    while True:
        menu_item_selected, movement, char_key = show_menu(0, menu_title, dict_menu, False, False)

        color_key = ""
        color = []
        if menu_item_selected == -1:
            break
        elif menu_item_selected == 0:
            color_key = "k"
        elif menu_item_selected == 1:
            color_key = "2"
        elif menu_item_selected == 2:
            color_key = "v"
        elif menu_item_selected == 3:
            color_key = "l"
        elif menu_item_selected == 4:
            color_key = "o"
        elif menu_item_selected == 5:
            color_key = "d"
        elif menu_item_selected == 6:
            color_key = "a"
        elif menu_item_selected == 7:
            color_key = "s"

        color_item = _colorBible[color_key].split("#")
        if len(color_item) >= 2:
            str_color = color_item[0]
            code_color = color_item[1]
        else:
            str_color = color_item[0]
            code_color = ""
        arr_attr = str_color.split("+")
        for item_color in arr_attr:
            color.append(item_color)

        str_color = ""
        for c in color:
            str_color = "{0}+{1}".format(str_color, c)

        if len(color) > 0 and str_color[0] == "+":
            str_color = str_color[1:]

        while True:
            menu_title_color = "{0}: {1} -> ({2}) {3}".format(menu_title, dict_menu[menu_item_selected], str_color, code_color)
            menu_item_selected_color, movement_color, char_key_color = show_menu(0, menu_title_color, dict_menu_colors, False, False)

            if menu_item_selected_color == -1:
                _colorBible[color_key] = "{0}#{1}".format(str_color, code_color)
                color.clear()
                break
            elif menu_item_selected_color < 5:
                item_color = "A_{0}".format(dict_menu_colors[menu_item_selected_color][0].upper())
                # noinspection PyBroadException
                if item_color in color:
                    color.remove(item_color)
                else:
                    color.append(item_color)

                str_color = ""
                for c in color:
                    str_color = "{0}+{1}".format(str_color, c)

                if len(color) > 0 and str_color[0] == "+":
                    str_color = str_color[1:]
            else:
                item_color = dict_menu_colors[menu_item_selected_color][0].upper()
                if item_color == code_color:
                    code_color = ""
                else:
                    code_color = item_color

    restart(False)


def show_themes():
    """
    Menu to select themes
    :return: False: ESC, True: used
    """
    global _useColors, _themeNr

    dict_menu_themes = {
        0: "No color",
        1: "Classic Blue  (with white)",
        2: "Classic Black (with green)",
        3: "Classic White (with black)"
    }

    menu_title = res("COLOR_MODE")
    menu_item_selected, movement, char_key = show_menu(0, menu_title, dict_menu_themes, False, False)

    if menu_item_selected == -1:
        return False

    _themeNr = menu_item_selected
    _useColors = False if menu_item_selected == 0 else True
    load_colors()
    restart(False)


def test():
    win_b = u.newwin(5, 40, 0, 0)
    u.box(win_b)
    u.wbkgd(win_b, " ", _colorThemeFunc2)
    u.mvwaddstr(win_b, 1, 1, "My string", u.A_BOLD)
    u.mvwaddstr(win_b, 3, 1, "Test...", u.A_REVERSE)
    panel = u.new_panel(win_b)
    u.panel_above(panel)
    u.update_panels()
    u.doupdate()
    u.getch()
    u.del_panel(panel)
    u.delwin(win_b)


def focus_row_init():
    global _cy
    _cy = _wm_util.win_top_border_lines - 1     # Tip: -1 to find first
    focus_row(1)


def focus_row(step):
    """
    param step: +1, -1
    """
    global _win_row, _panel_row, _cy

    new_cy = _cy
    pos_from = _wm_util.win_top_border_lines
    pos_to = _wm_util.win_top_border_lines + _wm_util.win_lines

    # Find row
    while True:
        # Move
        if step == -1:
            new_cy = pos_from if new_cy < pos_from else new_cy - 1
        elif step == 1:
            new_cy = pos_to if new_cy > pos_to else new_cy + 1
        else:
            return

        # Possible range but not sure something is written
        if new_cy < pos_from or new_cy > pos_to or new_cy < 0:
            return  # TODO: add cond. for last in page

        # Check the line
        pos = _wm_util.position_in_list_by_cy(new_cy)
        if pos > _wm_util.s_lines_max:
            return
        if len(_wm_util.s_lst) == 0:
            return

        row = _wm_util.s_lst[pos][0]
        lst_content = row.split("|")

        if len(lst_content) == 2:
            if lst_content[0] != _bbName:
                continue
            if lst_content[1].find(":") < 0:
                continue
            break   # if pos > _wm_util.win_lines - _wm_util.win_top_border_lines - _wm_util.win_bottom_border_lines

    # Display row
    _cy = new_cy

    if _win_row is not None:
        u.delwin(_win_row)

    if _panel_row is not None:
        u.del_panel(_panel_row)

    _win_row = u.newwin(1, _maxX, _cy, 0)
    _panel_row = u.new_panel(_win_row)

    u.wbkgd(_win_row, " ", _colorThemeFunc2 if _useColors else _colorThemeFunc2 + u.A_REVERSE)
    u.mvwaddstr(_win_row, 0, 0, lst_content[1], _colorThemeFunc2 if _useColors else _colorThemeFunc2 + u.A_REVERSE)

    u.panel_above(_panel_row)
    u.update_panels()
    u.doupdate()


def show_context_menu(panel_ref, win_ref):
    global _bNumber, _cNumber

    if _cy < 0:
        return

    if len(_wm_util.s_lst) == 0:
        return

    # Row with ID
    pos_in_list = _wm_util.position_in_list_by_cy(_cy)
    if pos_in_list < 0 or pos_in_list >= len(_wm_util.s_lst):
        return
    row = _wm_util.s_lst[pos_in_list][0]
    bible_id = _wm_util.s_lst[pos_in_list][1][0]

    if bible_id != '':
        ref_book_short, ref_book_name, bnumber, cnumber, vnumber = somdal.get_verse(bible_id)
        if ref_book_short is None:
            return
    else:
        # Row without ID
        row_content = row.split("|")

        if len(row_content) != 2:
            return

        pos_column = row_content[1].find(":")
        if pos_column < 0:
            return

        ref_full = row_content[1][0: pos_column]  # Exod 22.2
        ref_split_part0 = ref_full.split(" ")
        ref_book_short = ref_split_part0[0].strip()
        ref_split_part1 = ref_split_part0[1].split(".")
        cnumber = int(ref_split_part1[0])
        vnumber = int(ref_split_part1[1])
        bnumber = somdal.get_book_number_by_bsname(_bbName, ref_book_short)
        if bnumber <= 0:
            return
        ref_book_name, dummy = somdal.get_book_ref(_bbName, bnumber)

    # Menu
    has_cr = True if row.find("[") >= 0 else False
    if has_cr:
        dict_context_menu = {
            0: f"{res('OPEN_CHAPTER')}",
            1: f"{res('CROSS_REFERENCES')}"
        }
    else:
        dict_context_menu = {
            0: f"{res('OPEN_CHAPTER')}"
        }

    u.panel_below(panel_ref)

    menu_title = res("CONTEXT_MENU")
    menu_item_selected, movement, char_key = show_menu(0, menu_title, dict_context_menu, False, False)

    if menu_item_selected == -1:
        return

    elif menu_item_selected == 0:
        _bNumber = bnumber
        _cNumber = cnumber
        action_type = "B"
        action_query = f"{bnumber} {cnumber}"
        title = res("BOOK")
        sub_title = f"{ref_book_name} {cnumber}"
        s = somdal.get_verses(_delimiterVerse, _tbbName, bnumber, cnumber, 1, None)

    elif menu_item_selected == 1:
        action_type = "S"
        action_query = f"{bnumber} {cnumber} {vnumber} CR:"
        title = res("CROSS_REFERENCES")
        sub_title = f"{ref_book_name} {cnumber}.{vnumber}"
        s = somdal.get_cross_references(_delimiterVerse, _tbbName, bnumber, cnumber, vnumber)

    save_action(action_type, _bbName, action_query)
    save_title(title)
    save_sub_title(sub_title)
    show_title_and_subtitle()

    reset_window(panel_ref, win_ref)
    _wm_util.fill_window(s, 0)
    focus_row_init()


# noinspection PyUnusedLocal
def show_about():
    dict_menu = {
        0: "- {0}{1} -".format(somversion.app_name[0].upper(), somversion.app_name[1:]),
        1: "{0} ({1}) - {2}".format(somversion.app_version,
                                 somversion.db_version,
                                 somversion.app_version_date),
        2: "Email    : {0}".format(somversion.author_email),
        3: "Gitlab   : {0}".format(somversion.url),
        4: "Telegram : {0}".format(somversion.telegram)
    }

    menu_title = res("ABOUT")
    menu_item_selected, movement, char_key = show_menu(0, menu_title, dict_menu, False, False)


def show_art_prbl(is_article, art_name_filter):
    """
    Show menu with articles or parables
    :param is_article: is article
    :param art_name_filter: article name
    :return: 1) item name selected
             2) prbl digits
             3) item verbose name
    """

    if is_article:
        menu_k = "ARTICLES"
        menu_title = res(menu_k)
        array_name = "ART_ARRAY"
    else:
        menu_k = "PARABLES"
        menu_title = res(menu_k)
        array_name = "PRBL_ARRAY"

    show_menu_title = res(menu_k)
    save_title(show_menu_title)

    dict_menu = {}
    xml_lst = _xml.find(array_name).findall("item")

    # Simple filter
    if art_name_filter is not None:
        f = 0
        xml_lst_filtered = []
        for item in xml_lst:
            if item.text.find(art_name_filter) >= 0:
                xml_lst_filtered.append(xml_lst[f])
            f += 1
        xml_lst = xml_lst_filtered

    # Create menu
    i = 0
    for item in xml_lst:
        if is_article:
            xml_item = _xml.find(item.text)
            dict_menu[i] = xml_item.text
        else:
            prbl_fields = item.text.split("|")
            prbl_name = prbl_fields[0]
            xml_prbl_name = _xml.find(prbl_name)
            dict_menu[i] = xml_prbl_name.text
        i += 1

    pos_start = 0
    pos_block = 0
    size_menu_mini = 10
    size_menu = len(dict_menu)

    while True:
        j = 0
        dict_menu_mini = {}
        for i in range(pos_start, pos_start + size_menu_mini):
            if i >= size_menu:
                break
            dict_menu_mini[j] = dict_menu[i]
            j += 1

        highlight_menu_index = 0
        menu_item_selected, movement, char_key = show_menu(0, menu_title, dict_menu_mini, True, False, highlight_menu_index)

        if movement == 0:
            break
        elif movement in (-1, 1):
            pos_block += movement
            if pos_block < 0:
                pos_block = 0
            pos_start = pos_block * size_menu_mini

    # Finally
    if menu_item_selected < 0:
        return None, None, None

    xml_item_selected = xml_lst[pos_block * size_menu_mini + menu_item_selected]
    item_verbose_name = dict_menu[pos_block * size_menu_mini + menu_item_selected]

    if is_article:
        item_name = _xml.find(xml_item_selected.text).tag
    else:
        item_name = xml_item_selected.text

    if is_article:
        return item_name, None, item_verbose_name
    else:
        prbl_arr = item_name.split("|")
        item_name = prbl_arr[0]
        prbl_digits = prbl_arr[1]
        return item_name, prbl_digits, item_verbose_name


def show_books(menu_x, menu_title_book, bbname, res_all_item):
    """
    Show books
    :param menu_x: x pos
    :param menu_title_book: title
    :param bbname: language
    :param res_all_item: resource
    :return: book name selected
    """

    is_order_by_name = True
    lst = somdal.get_list_book_by_name(25, bbname, is_order_by_name, res_all_item, "")
    i = 0
    dict_menu = {}
    for item in lst:
        dict_menu[i] = item
        i += 1

    menu_title_filter = " {0} ({1}): ".format(res("FILTER"), res("BOOKS"))
    size_menu = len(dict_menu)
    size_menu_mini = 10
    pos_start = 0
    pos_block = 0

    while True:
        j = 0
        dict_menu_mini = {}
        for i in range(pos_start, pos_start + size_menu_mini):
            if i >= size_menu:
                break
            dict_menu_mini[j] = dict_menu[i]
            j += 1

        highlight_menu_index = 1 if len(dict_menu_mini) == 2 and dict_menu_mini[0] == res("ALL") else 0
        menu_item_selected, movement, char_key = show_menu(menu_x, menu_title_book, dict_menu_mini, True, True,
                                                           highlight_menu_index)
        if movement == 0:
            break
        elif movement in (-1, 1):
            pos_block += movement
            if pos_block < 0:
                pos_block = 0
            pos_start = pos_block * size_menu_mini
        elif movement == 3:
            win_filter = u.newwin(3, _maxX, 2, 0)
            u.wbkgd(win_filter, " ", _colorTheme)
            u.mvwhline(win_filter, 2, 0, u.ACS_HLINE + _colorTheme, _maxX)
            u.mvwaddstr(win_filter, 0, 0, menu_title_filter)  # + char_key
            u.update_panels()
            u.doupdate()

            u.echo()
            filter_string = u.wgetstr(win_filter)
            u.noecho()
            filter_string = filter_string.strip().decode("utf-8") if len(filter_string) > 0 else ""

            u.delwin(win_filter)
            u.update_panels()
            u.doupdate()

            lst = somdal.get_list_book_by_name(25, bbname, is_order_by_name, res_all_item, filter_string)
            if len(lst) == 0:
                continue

            i = 0
            dict_menu = {}
            for item in lst:
                dict_menu[i] = item
                i += 1

            pos_block = 0
            pos_start = 0
            size_menu = len(dict_menu)

    # Finally
    if menu_item_selected < 0:
        return None

    item_selected = dict_menu_mini[menu_item_selected]
    return item_selected


def get_history_dict_menu():
    """
    Get history_dict_menu
    :return: dict_menu
    """
    lst = somdal.get_list_all_cache_tab_for_history()
    if len(lst) == 0:
        return None

    i = 0
    dict_menu = {}
    tabtitle = ""
    for item in lst:
        tabid, tabtype, bbname, fullquery = item[0], item[1], item[2], item[3]
        if tabtype in ("A", "P"):
            verbose_name = _xml.find(fullquery).text
            tabtitle = "{0} {1}".format(tabid, verbose_name)
        elif tabtype == "S":
            words = fullquery.split(" ")
            words_count = len(words)

            """
            if (words_count == 4 and words[0].isdigit() and words[1].isdigit() and words[2].isdigit() and words[3].isdigit()) \
                    or (words_count == 4 and words[0].isdigit() and words[1].isdigit() and words[2].isdigit() and words[3].upper() == "CR:") \
                    or (words_count == 3 and words[0].isdigit() and words[1].isdigit() and words[2].isdigit()) \
                    or (words_count == 2 and words[0].isdigit() and words[1].isdigit()):
                bbname_ref = _bbName
            else:
                bbname_ref = bbname
            """
            bbname_ref = bbname

            if words_count >= 2 and words[0].isdigit():
                bnumber = int(words[0])
                book_name_verbose, dummy = somdal.get_book_ref(bbname_ref, bnumber)
                if book_name_verbose is None:
                    tabtitle = "{0} {1}".format(tabid, fullquery)
                else:
                    words[0] = book_name_verbose
                    words_str = ""
                    for part in words:
                        words_str = "{0} {1}".format(words_str, part)
                    tabtitle = "{0}{1}".format(tabid, words_str)
            else:
                tabtitle = "{0} {1}".format(tabid, fullquery)

        dict_menu[i] = tabtitle     # item
        i += 1

    return dict_menu


def show_history_menu(menu_x, menu_title_cache_tab):
    """
    Show cache tabs
    :param menu_x: x pos
    :param menu_title_cache_tab: title
    :param res_all_item: resource
    :return: item selected or None if esc
    """

    dict_menu = get_history_dict_menu()
    if dict_menu is None or len(dict_menu) == 0:
        return None
    size_menu = len(dict_menu)
    size_menu_mini = 10
    pos_start = 0
    pos_block = 0
    highlight_menu_index = 0

    while True:
        j = 0
        dict_menu_mini = {}
        for i in range(pos_start, pos_start + size_menu_mini):
            if i >= size_menu:
                break
            dict_menu_mini[j] = dict_menu[i]
            j += 1

        menu_item_selected, movement, char_key = show_menu(menu_x, menu_title_cache_tab, dict_menu_mini, True, True,
                                                           highlight_menu_index)
        if movement == 0:
            break
        elif movement in (-1, 1):
            pos_block += movement
            if pos_block < 0:
                pos_block = 0
            pos_start = pos_block * size_menu_mini
            highlight_menu_index = 0
        elif movement == 3:
            if char_key not in ("x", "X"):
                continue
            if dict_menu_mini is None or len(dict_menu_mini) == 0:
                continue

            try:
                item_to_delete = dict_menu_mini[menu_item_selected]
            except KeyError:
                continue

            tabid_to_delete = int(item_to_delete.split(" ")[0])
            somdal.delete_cache_tab_by_id(tabid_to_delete)

            # Rebuild menu
            dict_menu = get_history_dict_menu()
            if dict_menu is None or len(dict_menu) == 0:
                return None
            size_menu = len(dict_menu)
            highlight_menu_index = menu_item_selected

    # Finally
    if menu_item_selected < 0 or menu_item_selected >= len(dict_menu_mini):
        return None

    item_selected = dict_menu_mini[menu_item_selected]
    return item_selected


def get_bible_dict_verbose():
    return {
        0: "(EN) King James 1611 (K)",
        1: "(EN) King James 2000 (2)",
        2: "(ES) Reina Valera (V)",
        3: "(FR) Louis Segond (L)",
        4: "(FR) Ostervald (O)",
        5: "(IT) G. Diodati (D)",
        6: "(PT) Almeida (A)",
        7: "(DE) Schlachter (S)"
    }


def get_bible_dict_short():
    return {
        0: "k",
        1: "2",
        2: "v",
        3: "l",
        4: "o",
        5: "d",
        6: "a",
        7: "s"
    }


def get_bible_menu_index(bbname):
    if bbname == "k":
        return 0
    elif bbname == "2":
        return 1
    elif bbname == "v":
        return 2
    elif bbname == "l":
        return 3
    elif bbname == "o":
        return 4
    elif bbname == "d":
        return 5
    elif bbname == "a":
        return 6
    elif bbname == "s":
        return 7
    return 0


# noinspection PyBroadException
def get_article(art_name):
    """
    Get article
    :param art_name: article name
    :return: article content as list, art_name_verbose
    """

    sep_block = "__ <br>"  # Space needed at the end
    art_name_verbose = _xml.find(art_name).text
    xml_art_content = _xml.find("{0}_CONTENT".format(art_name))
    if xml_art_content is not None:
        art_content = xml_art_content.text
    else:
        xml_en = xml.etree.ElementTree.parse(
            "{0}".format(pkg_resources.resource_filename('sonofman.data', 'strings-en.xml')),
            xml.etree.ElementTree.XMLParser()).getroot()
        xml_art_content = xml_en.find("{0}_CONTENT".format(art_name))
        art_content = xml_art_content.text

    tag = "R"
    tag_start = "<{0}>".format(tag)
    tag_end = "</{0}>".format(tag)
    while True:
        rtag_start = art_content.find(tag_start)
        if rtag_start < 0:
            break
        rtag_end = art_content.find(tag_end, rtag_start)
        if rtag_end < 0:
            continue
        rdigits = art_content[rtag_start:rtag_end].replace(tag_start, "").split(" ")
        if len(rdigits) == 4:
            bbname = _bbName
            bnumber, cnumber, verse_number, verse_number_to = int(rdigits[0]), int(rdigits[1]), int(rdigits[2]), int(rdigits[3])
        else:
            bbname, bnumber, cnumber, verse_number, verse_number_to = rdigits[0], int(rdigits[1]), int(rdigits[2]), int(rdigits[3]), int(rdigits[4])
        s = somdal.get_verses(_delimiterVerse, _tbbName, bnumber, cnumber, verse_number, verse_number_to)   # bbName??
        s_string = somdal.get_verses_string(s)
        art_content = "{0}{1}{2}<br><br>{3}".format(art_content[0:rtag_start], sep_block, s_string,
                                                    art_content[rtag_end + len(tag_end):])

    tag = "HB"
    tag_start = "<{0}>".format(tag)
    tag_end = "</{0}>".format(tag)
    while True:
        rtag_start = art_content.find(tag_start)
        if rtag_start < 0:
            break

        rtag_end = art_content.find(tag_end, rtag_start)
        if rtag_end < 0:
            continue

        bnumber = art_content[rtag_start:rtag_end].replace(tag_start, "")
        bbname = _bbName
        bname, bsname = somdal.get_book_ref(bbname, bnumber)
        s = "<br><br>_HB_{0}<br><br>".format(bname)
        art_content = "{0}{1}{2}".format(art_content[0:rtag_start], s, art_content[rtag_end + len(tag_end):])

    art_content = art_content.replace("\n", "")  # At the beginning
    art_content = art_content.replace("<b>", "")
    art_content = art_content.replace("</b>", "")
    art_content = art_content.replace("<blockquote>", "\n{0}".format(sep_block))
    art_content = art_content.replace("</blockquote>", "\n")
    art_content = art_content.replace("<i>", "")
    art_content = art_content.replace("</i>", "")
    art_content = art_content.replace("<u>", "")
    art_content = art_content.replace("</u>", "")
    art_content = art_content.replace("<center>", "")
    art_content = art_content.replace("</center>", "")
    art_content = art_content.replace("<H>", "\n\n#")
    art_content = art_content.replace("</H>", "\n\n")
    art_content = art_content.replace("<HA/>", "#{0}<br><br>".format(art_name_verbose))
    art_content = art_content.replace("<HS>", "<br>• ")
    art_content = art_content.replace("</HS>", "<br><br>")
    art_content = art_content.replace("\\'", "'")
    art_content = art_content.replace('\\"', '"')
    art_content = art_content.replace("&#8230;", "...")
    art_content = art_content.replace("&nbsp;", " ")
    art_content = art_content.replace("&lt;", "<")
    art_content = art_content.replace("&gt;", ">")
    art_content = art_content.replace("<br>", "\n")  # At the end

    lst = []
    art_content_arr = art_content.splitlines(True)
    ref = ["", ""]
    for itm in art_content_arr:
        item = [itm, ref]
        lst.append(item)

    return lst, art_name_verbose


def move_art_prbl(is_article, step):
    """
    Move LEFT/RIGHT within ART/PRBL
    param is_article: is article
    param step: +1, -1
    No return value
    """

    array_name = "ART_ARRAY" if is_article else "PRBL_ARRAY"
    xml_lst = _xml.find(array_name).findall("item")

    # Search
    pos = 0
    if is_article:
        for item in xml_lst:
            if item.text == _action_query:
                break
            pos += 1
    else:
        for item in xml_lst:
            if item.text.split("|")[0] == _action_query:
                break
            pos += 1

    # Move
    if (pos + step) >= len(xml_lst) or (pos + step < 0):
        return

    pos += step
    action_query = xml_lst[pos].text if is_article else xml_lst[pos].text.split("|")[0]
    save_action(_action_type, _action_bbname, action_query, should_add=False)
    show_history(_history, 0)


def show_history(history, from_line_nr):
    """
    Show history
    :param history: history parameter
    :param from_line_nr:
    """

    if len(history) != 2:
        return

    history_bbname, history_query = history

    if history_query.find("ART") == 0:
        s, art_name_verbose = get_article(history_query)
        _wm_util.fill_window(s, from_line_nr)
        focus_row_init()

        save_action("A", history_bbname, history_query)
        save_title(res("ARTICLES"))
        save_sub_title(art_name_verbose)
        show_title_and_subtitle()

    elif history_query.find("PRBL") == 0:
        xml_lst = _xml.find("PRBL_ARRAY").findall("item")
        prbl_digits = None
        prbl_name_verbose = ""
        for item in xml_lst:
            prbl_fields = item.text.split("|")
            prbl_name = prbl_fields[0]
            if prbl_name == history_query:
                prbl_digits = prbl_fields[1]
                prbl_name_verbose = _xml.find(prbl_name).text
                break

        if prbl_digits is None:
            raise Exception("Unable to find parable '{0}'!".format(history_query))

        digits = prbl_digits.split(" ")
        bnumber, cnumber, verse_number, verse_number_to = int(digits[0]), int(digits[1]), int(digits[2]), int(digits[3])

        s = somdal.get_verses(_delimiterVerse, _tbbName, bnumber, cnumber, verse_number, verse_number_to)
        _wm_util.fill_window(s, from_line_nr)
        focus_row_init()

        save_action("P", history_bbname, history_query)
        save_title(res("PARABLES"))
        save_sub_title(prbl_name_verbose)
        show_title_and_subtitle()
    else:
        s = get_bible_search(history_bbname, history_query)
        _wm_util.fill_window(s, from_line_nr)
        focus_row_init()

    return


def replace_colors():
    for k in _colorBible.keys():
        pos_color = _colorBible[k].find("COLOR")
        if pos_color >= 0:
            _colorBible[k] = _colorBible[k][0:pos_color]


def load_colors():
    global _colorBible

    color_k = somconfig.get_option("PREFERENCES", "COLOR_K" if _useColors else "NO_COLOR_K", None, "#")
    color_2 = somconfig.get_option("PREFERENCES", "COLOR_2" if _useColors else "NO_COLOR_2", None, "#")
    color_v = somconfig.get_option("PREFERENCES", "COLOR_V" if _useColors else "NO_COLOR_V", None, "#")
    color_l = somconfig.get_option("PREFERENCES", "COLOR_L" if _useColors else "NO_COLOR_L", None, "#")
    color_o = somconfig.get_option("PREFERENCES", "COLOR_O" if _useColors else "NO_COLOR_O", None, "#")
    color_d = somconfig.get_option("PREFERENCES", "COLOR_D" if _useColors else "NO_COLOR_D", None, "#")
    color_a = somconfig.get_option("PREFERENCES", "COLOR_A" if _useColors else "NO_COLOR_A", None, "#")
    color_s = somconfig.get_option("PREFERENCES", "COLOR_S" if _useColors else "NO_COLOR_S", None, "#")
    _colorBible = {"k": color_k, "v": color_v, "l": color_l, "d": color_d, "a": color_a, "o": color_o, "s": color_s, "2": color_2}


def load_config():
    global _locale, _alt_locale, _useColors, _bbName, _tbbName, _history, _colorBible, _themeNr

    _locale = somconfig.get_option("PREFERENCES", "LOCALE", ("en", "es", "fr", "it", "pt", "de"), "en")
    _alt_locale = somconfig.get_option("PREFERENCES", "ALT_LOCALE", ("en", "es", "fr", "it", "pt"), "en")
    _themeNr = somconfig.get_option("PREFERENCES", "USE_COLORS", ("0", "1", "2", "3"), "0")
    _useColors = False if _themeNr == "0" else True
    _bbName = somconfig.get_option("PREFERENCES", "BIBLE_PREFERED", ("k", "v", "l", "d", "a", "o", "s", "2"), "k")
    _tbbName = somconfig.get_option("PREFERENCES", "BIBLE_MULTI", None, _bbName)

    if _locale != "de":
        _alt_locale = _locale

    load_colors()

    if not _useColors:
        replace_colors()

    set_locale(_locale)

    try:
        history_current_key = somconfig.get_option("PREFERENCES", "HISTORY_CURRENT", None, "0")
        if somconfig.config.has_option("HISTORY", history_current_key):
            history_current_value = somconfig.get_option("HISTORY", history_current_key, None, "ART_APP_HELP")
            history_current_values = history_current_value.split("#")
            history_current_values_size = len(history_current_values)
            if history_current_values_size == 2:
                _history = [history_current_values[0], history_current_values[1]]
            elif history_current_values_size == 1:
                _history = [_bbName, history_current_values[0]]
            else:
                somutil.print("! (was) invalid history option: '{0}'".format(history_current_value))
                _history = [_bbName, "ART_APP_HELP"]
        else:
            somutil.print("! (was) invalid history_current: '{0}'".format(history_current_key))
            _history = [_bbName, "ART_APP_HELP"]
    except Exception as ex:
        somutil.print("! (was) unable to read history, please check: {0}".format(ex))
        _history = [_bbName, "ART_APP_HELP"]

    # somconfig.get_option("PREFERENCES", "BIBLE_TRAD")     # => tbbname
    # somconfig.get_option("UI", "COLOR_THEME_NR")
    # somconfig.get_option("UI", "COLOR_THEME_DIALOG_NR")
    # somconfig.get_option("UI", "COLOR_THEME_ERROR_NR")


def save_config():
    if not _useColors:
        replace_colors()

    somconfig.set_option("PREFERENCES", "LOCALE", _locale)
    somconfig.set_option("PREFERENCES", "ALT_LOCALE", _alt_locale)
    somconfig.set_option("PREFERENCES", "USE_COLORS", _themeNr)
    somconfig.set_option("PREFERENCES", "BIBLE_PREFERED", _bbName)
    somconfig.set_option("PREFERENCES", "BIBLE_MULTI", _tbbName)
    somconfig.set_option("PREFERENCES", "COLOR_K" if _useColors else "NO_COLOR_K", _colorBible["k"])
    somconfig.set_option("PREFERENCES", "COLOR_2" if _useColors else "NO_COLOR_2", _colorBible["2"])
    somconfig.set_option("PREFERENCES", "COLOR_V" if _useColors else "NO_COLOR_V", _colorBible["v"])
    somconfig.set_option("PREFERENCES", "COLOR_L" if _useColors else "NO_COLOR_L", _colorBible["l"])
    somconfig.set_option("PREFERENCES", "COLOR_O" if _useColors else "NO_COLOR_O", _colorBible["o"])
    somconfig.set_option("PREFERENCES", "COLOR_D" if _useColors else "NO_COLOR_D", _colorBible["d"])
    somconfig.set_option("PREFERENCES", "COLOR_A" if _useColors else "NO_COLOR_A", _colorBible["a"])
    somconfig.set_option("PREFERENCES", "COLOR_S" if _useColors else "NO_COLOR_S", _colorBible["s"])

    history_item = "{0}#{1}".format(_action_bbname, _action_query)
    somconfig.set_option("PREFERENCES", "HISTORY_CURRENT", "0")
    somconfig.set_option("HISTORY", "0", history_item)

    somconfig.save_config()


def restart(allow_to_load_another_article):
    """
    Restart
    :param allow_to_load_another_article: True/False
    """
    if allow_to_load_another_article:
        if _action_query == "ART_APP_HELP_BEGINNING":
            save_action("A", _bbName, "ART_APP_HELP")

    save_config()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def finish(return_code):
    global _wm_util

    del _wm_util
    u.endwin()
    u.reset_shell_mode()
    u.curs_set(1)

    somutil.print("* Tips: if you have problems in console, type reset or CTRL-D to restore it.")
    exit(return_code)


def reset_window(panel, win):
    u.panel_above(panel)
    u.update_panels()
    u.doupdate()

    u.wclear(win)


# noinspection PyTypeChecker
def main():
    global _maxY, _maxX, _bbName, _bNumber, _cNumber, _useColors, _colorTheme, _colorThemeDialog, \
            _colorThemeErr, _colorThemeFunc1, _colorThemeFunc2, _themeNr, _reset_status_before_key, _win_status, \
            _win_title, _xml, _wm_util, _cy, _tabId

    try:
        # Config
        load_config()

        # Resource
        _xml = xml.etree.ElementTree.parse(
            "{0}".format(pkg_resources.resource_filename('sonofman.data', 'strings-{0}.xml'.format(_alt_locale))),
            xml.etree.ElementTree.XMLParser()).getroot()

        # Settings before initialization of ncurses
        os.environ.setdefault('ESCDELAY', '25')

        # Screen
        stdscr = u.initscr()
        u.start_color()
        u.noecho()

        # Colors
        if _useColors:
            if u.has_colors():
                u.init_pair(0, -1, -1)
                u.init_pair(1, u.COLOR_WHITE, u.COLOR_BLACK)
                u.init_pair(2, u.COLOR_GREEN, u.COLOR_BLACK)
                u.init_pair(3, u.COLOR_CYAN, u.COLOR_BLACK)
                u.init_pair(4, u.COLOR_MAGENTA, u.COLOR_BLACK)
                u.init_pair(5, u.COLOR_YELLOW, u.COLOR_BLACK)
                u.init_pair(6, u.COLOR_RED, u.COLOR_BLACK)
                u.init_pair(11, u.COLOR_WHITE, u.COLOR_BLUE)
                u.init_pair(12, u.COLOR_BLACK, u.COLOR_CYAN)
                u.init_pair(13, u.COLOR_YELLOW, u.COLOR_BLUE)
                u.init_pair(21, u.COLOR_WHITE, u.COLOR_RED)
                u.init_pair(22, u.COLOR_BLACK, u.COLOR_WHITE)
            else:
                _useColors = False
                for i in (0, 1, 2, 3, 4, 5, 6, 11, 12, 13, 21, 22):
                    u.init_pair(i, -1, -1)
        else:
            for i in (0, 1, 2, 3, 4, 5, 6, 11, 12, 13, 21, 22):
                u.init_pair(i, -1, -1)

        color_theme_no_color_nr = 0
        color_theme_err_nr = 21
        color_theme_func_nr1 = 1
        color_theme_func_nr2 = 12

        if _themeNr == "1":
            color_theme_nr = 11
            color_theme_dialog_nr = 11
        elif _themeNr == "3":
            color_theme_nr = 22
            color_theme_dialog_nr = 22
        else:
            color_theme_nr = 2
            color_theme_dialog_nr = 1

        _colorTheme = u.color_pair(color_theme_nr if _useColors else color_theme_no_color_nr)
        _colorThemeDialog = u.color_pair(color_theme_dialog_nr if _useColors else color_theme_no_color_nr)
        _colorThemeErr = u.color_pair(color_theme_err_nr if _useColors else color_theme_no_color_nr)
        _colorThemeFunc1 = u.color_pair(color_theme_func_nr1 if _useColors else color_theme_no_color_nr)
        _colorThemeFunc2 = u.color_pair(color_theme_func_nr2 if _useColors else color_theme_no_color_nr)

        # Dims
        _maxY, _maxX = u.getmaxyx(stdscr)
        somutil.print("* Lines/Cols: {0}x{1}".format(_maxY, _maxX))

        win_main_top_border_lines = 2     # 2 lines
        win_main_bottom_border_lines = 3  # 3 lines
        win_main_lines = _maxY - win_main_top_border_lines - win_main_bottom_border_lines  # Border Y
        win_main_cols = _maxX      # Border X: 0
        win_title_cols = _maxX

        if _maxY < 20:
            somutil.print("! Terminal should have min. 20 lines")

        # Bar
        u.mvwhline(stdscr, _maxY - 3, 0, _colorTheme, _maxX)
        u.mvwaddstr(stdscr, _maxY - 2, 0, " " * _maxX, _colorTheme)
        function_keys_dict = {
            "1|M": res("MENU"),
            "2|{0}".format("B" if sys.platform == 'darwin' else "F2"): res("BOOKS"),
            "3|{0}".format("S" if sys.platform == 'darwin' else "F3"): res("SEARCH"),
            "4|{0}".format("A" if sys.platform == 'darwin' else "F4"): res("ARTICLES"),
            "5|{0}".format("P" if sys.platform == 'darwin' else "F5"): res("PARABLES"),
            "6|Q": res("QUIT")
        }
        func_pos = 0
        for k in sorted(function_keys_dict.keys()):
            v = function_keys_dict[k]
            kstr = k.split("|")[1]
            u.mvwaddstr(stdscr, _maxY - 2, func_pos, kstr, _colorThemeFunc1)
            func_pos += len(kstr)
            u.mvwaddstr(stdscr, _maxY - 2, func_pos, v, _colorThemeFunc2 if _useColors else _colorThemeFunc2 + u.A_REVERSE)
            func_pos += len(v)
            u.mvwaddstr(stdscr, _maxY - 2, func_pos, " ", _colorThemeFunc1)
            func_pos += 1
        if (func_pos - 1) > win_title_cols:
            u.mvwaddstr(stdscr, _maxY - 2, 0, " " * _maxX, _colorTheme)
            u.mvwaddstr(stdscr, _maxY - 2, 0, "H:", _colorThemeFunc1)
            u.mvwaddstr(stdscr, _maxY - 2, 2, res("HELP"), _colorThemeFunc2 if _useColors else _colorThemeFunc2 + u.A_REVERSE)
        del function_keys_dict

        # Title
        u.mvwhline(stdscr, 1, 0, _colorTheme, _maxX)

        _win_title = u.newwin(1, win_title_cols, 0, 0)
        u.wbkgd(_win_title, " ", _colorThemeFunc2)
        u.keypad(_win_title, False)
        panel_title = u.new_panel(_win_title)

        _win_status = u.newwin(1, win_title_cols, _maxY - 1, 0)
        u.wbkgd(_win_status, " ", _colorTheme)
        u.keypad(_win_status, False)
        panel_status = u.new_panel(_win_status)

        win_main = u.newwin(win_main_lines, win_main_cols, win_main_top_border_lines, 0)
        u.wbkgd(win_main, " ", _colorTheme)
        u.keypad(win_main, True)
        # u.notimeout(win_main, True)   # TODO: notimeout ?
        # u.nodelay(win_main, True)     # TODO: nodelay ?
        panel_main = u.new_panel(win_main)
        # wbkgd(win_main, " ", color_pair(2))

        u.panel_above(panel_main)
        u.update_panels()
        u.doupdate()

        # Settings after initialization of ncurses
        u.curs_set(1)

        # Search
        _wm_util = som_winutil.WinUtil(win_main, win_main_lines, win_main_cols, win_main_top_border_lines, win_main_bottom_border_lines, _colorBible)
        show_history(_history, 0)

        while True:
            key = u.wgetch(win_main)    # key = u.getch()

            if not _reset_status_before_key:        # TODO: to optimize
                _reset_status_before_key = True
                clear_status()

            if key in (118, 86):  # v V
                focus_row(1)

            elif key in (116, 84):  # t T, u.KEY_SR:Shift-Up, u.KEY_SF:Shift-Down
                focus_row(-1)

            elif key == 10:
                show_context_menu(panel_main, win_main)

            elif key == 9:  # TAB
                cache_tab_selected = show_history_menu(0, res("HISTORY"))
                if cache_tab_selected is None:
                    continue
                words = cache_tab_selected.split(" ")
                tabid = int(words[0])
                ct = somdal.get_cache_tab_by_id(tabid)
                if ct is None:
                    continue
                _tabId = tabid
                history = [ct.bbname, ct.fullquery]
                show_history(history, 0)

            elif key in (u.KEY_UP, u.KEY_PPAGE):
                mv = _wm_util.move(-1)
                if not mv:
                    continue
                _wm_util.fill_window(None, _wm_util.s_line_pos)
                focus_row_init()

            elif key in (u.KEY_DOWN, u.KEY_NPAGE):
                mv = _wm_util.move(1)
                if not mv:
                    continue
                _wm_util.fill_window(None, _wm_util.s_line_pos)
                focus_row_init()

            elif key == u.KEY_LEFT:
                if _action_type == 'B':
                    if _cNumber <= 1:
                        continue
                    _cNumber -= 1

                    query = "{0} {1}".format(_bNumber, _cNumber)
                    s = get_bible_search(_action_bbname, query, should_add=False)
                    _wm_util.fill_window(s, 0)
                    focus_row_init()

                elif _action_type == 'A':
                    move_art_prbl(True, -1)
                    focus_row_init()

                elif _action_type == 'P':
                    move_art_prbl(False, -1)
                    focus_row_init()

            elif key == u.KEY_RIGHT:
                if _action_type == 'B':
                    ci = somdal.get_bible_chapter_count_by_book(_bNumber)
                    if _cNumber >= ci[0]:
                        continue
                    _cNumber += 1

                    query = "{0} {1}".format(_bNumber, _cNumber)
                    s = get_bible_search(_action_bbname, query, should_add=False)
                    _wm_util.fill_window(s, 0)
                    focus_row_init()

                elif _action_type == 'A':
                    move_art_prbl(True, 1)
                    focus_row_init()

                elif _action_type == 'P':
                    move_art_prbl(False, 1)
                    focus_row_init()

            elif key in (u.KEY_F(2), u.KEY_F(3), 98, 66, 115, 83):   # b B, s S
                u.panel_below(panel_main)
                u.update_panels()
                u.doupdate()

                bbname, query = show_search(True if key in (u.KEY_F(3), 115, 83) else False)
                if bbname is None and query is None:
                    show_status(res("ERR_OPERATION_CANCELLED"), _colorTheme, False)
                    continue

                s = get_bible_search(bbname, query)
                if len(s) == 0:
                    reset_window(panel_main, win_main)
                    show_history(_history, _wm_util.s_line_pos)
                    continue

                reset_window(panel_main, win_main)
                _wm_util.fill_window(s, _wm_util.s_line_pos)
                focus_row_init()

            elif key in (u.KEY_F(4), 97, 65, 104, 72):  # a A, h H
                art_name_filter = "ART_APP_HELP" if key in (104, 72) else None
                u.panel_below(panel_main)

                art_name, art_ref, art_verbose_name = show_art_prbl(True, art_name_filter)
                if art_name is None:
                    show_status(res("ERR_OPERATION_CANCELLED"), _colorTheme, False)
                    continue

                save_action("A", _bbName, art_name)
                save_sub_title(art_verbose_name)
                show_title_and_subtitle()

                s, art_verbose_name = get_article(art_name)
                reset_window(panel_main, win_main)
                _wm_util.fill_window(s, 0)
                focus_row_init()

            elif key in (u.KEY_F(5), 112, 80):  # p P
                u.panel_below(panel_main)

                prbl_name, prbl_digits, prbl_verbose_name = show_art_prbl(False, None)
                if prbl_name is None:
                    show_status(res("ERR_OPERATION_CANCELLED"), _colorTheme, False)
                    continue

                digits = prbl_digits.split(" ")
                _bNumber, _cNumber, verse_number, verse_number_to = int(digits[0]), int(digits[1]), int(digits[2]), int(digits[3])

                save_action("P", _bbName, prbl_name)
                save_sub_title(prbl_verbose_name)
                show_title_and_subtitle()

                s = somdal.get_verses(_delimiterVerse, _tbbName, _bNumber, _cNumber, verse_number, verse_number_to)
                reset_window(panel_main, win_main)
                _wm_util.fill_window(s, 0)
                focus_row_init()

            elif key in (114, 82):  # r R
                restart(False)

            elif key in (u.KEY_F(10), 113, 81):  # q Q
                show_status("{0} - {1}".format(res("QUIT"), res("CONFIRM")), _colorTheme, True)

                key = u.getch()
                if key == 10:
                    save_config()
                    finish(0)
                else:
                    clear_status()

            elif key == u.KEY_HOME:
                _wm_util.fill_window(None, 0)
                focus_row_init()

            elif key in (109, 77):  # m M
                is_used = menu()
                if not is_used:
                    show_status(res("ERR_OPERATION_CANCELLED"), _colorTheme, False)

    except Exception as ex:
        print_ex(ex)


if __name__ == '__main__':
    main()


"""
Not used
--------

def f4():
    height = _maxY
    width = _maxX
    win = newwin(height, width, 2, 0)
    wbkgd(win, " ", _colorThemeDialog)

    row_pos = 3
    item_width = 25
    max_item_by_row = floor(width / item_width)
    books = libs.get_list_book_by_name(item_width, _bbName, True, "")
    mvwaddstr(win, row_pos, 0, "", _colorTheme)
    i = 1
    for b in books:
        waddstr(win, b, _colorTheme)
        if i >= max_item_by_row:
            i = 1
            row_pos += 1
            mvwaddstr(win, row_pos, 0, "", _colorTheme)
        else:
            i += 1

    panel = new_panel(win)
    panel_above(panel)
    update_panels()
    doupdate()

    mvwaddstr(win, 1, 1, _("BOOK"), _colorTheme)
    echo()
    wgetstr(win)
    noecho()
    delwin(win)
# -----------------------------------------------------------------------        
               
# debug
# region Description
# if len(sys.argv) != 4:
#     sys.argv.append("f")
#     sys.argv.append(1)
#     sys.argv.append(1)
#
# sys.argv.pop(0)
# lang = sys.argv.pop(0)
# if lang == "e":
#     _bbName = "k"
# elif lang == "f":
#     _bbName = "l"
# elif lang == "s":
#     _bbName = "v"
# elif lang == "i":
#     _bbName = "d"
# else:
#     sys.stderr.write("usage: som_main.py <lang> <bNumber> <cNumber>")
#     exit(1)
# _bNumber = int(sys.argv.pop(0))
# _cNumber = int(sys.argv.pop(0))
# endregion
#
# locale.setlocale(locale.LC_ALL, '')
# code = locale.getpreferredencoding()
#
# try:
# from unicurses import * was here
# except:
# pass
# -----------------------------------------------------------------------        
               
# elif key == KEY_F(4):
#     panel_below(panel_search)
#
#     f4()
#
#     panel_above(panel_search)
#     update_panels()
#     doupdate()
#     fill_window(win_main, win_search_lines, s_line_pos)
"""
