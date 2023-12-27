LEXICON_default: dict[str, str] = {
    "greeting": ("Приветствую,", """<b>Это бот группы "Волга"</b>:
            и книга, и чтец, и база выдержек, и словарь.
            \n\nИнтерактивное меню: /menu.
            \n\nСправка по текущей области команд: /help.
            <i>Внизу имеется кнопка меню, 
            для навигации в любой области команд.</i>"""),
    "help": """<b>Стартовая область команд:</b>
    /start - запуск бота
    /help - список команд текущей области
    /menu - интерактивное меню
    "/стр ###" - открыть станицу книги
    "/фраг ###" - открыть главу книги
    /cancel - отмена, выход из области команд""",
    "unknown": """Ошибка ввода:
            команда неизвестна 
            или недоступна в данной области команд.
            \n/cancel - возврат к начальной области команд""",
    "cancel-denied": "Это начальная область команд",
    "urls": """Полезные ссылки:
            Прямая аудио трансляция ББ, русская
            https://icecast.kab.tv/live1-rus-574bcfd5.mp3
            Прямая аудио трансляция ББ, english
            http://icecast.kab.tv/live1-eng-574bcfd5.mp3
            Словарь из игры:
            http://www.kabbalah.info/rus/content/view/full/59550
            """,
    "my_info": ('Ваш прогресс:',
                'Всего ответов:',
                'Верные ответы:',
                'Ошибочные ответы:'),
    "spam": "Анти-спам система. Блокировка сообщений 5 сек."
            "При ошибочном срабатывании сообщите администратору."
}


LEXICON_dict: dict[str, str] = {
    "add_term": 'Введите\n'
            '\tтермин, перевод и объяснение,'
            '\nразделяя их двумя заками $.'
            "\n\n<b>Шаблон:</b>"
            '\n{термин}$${перевод}$${о б ъ я с н е н и е}'
            '\n\nили без перевода:'
            '\n{термин}$$$${о б ъ я с н е н и е}'
            '\n\n<b>Пример:</b>'
            '\nОр$$свет$$всё получаемое в мирах "еш ми еш".'
            '\n\n"Меню" - отмена ввода',
    "cancel": 'Отмена области команд: Игра "Словарь"',
    "user_right_answer": "Верно",
    "user_wrong_answer": "Неверно",
    "system_right_answer": ("Верный ответ:",
                            "Перевод:",
                            "Определение:"),
    "add_cancel": "Ввод нового определения отменен.",
    "add_success": "Новый термин добавлен в словарь.",
    "report": "Определение отправлено на проверку.",
    "help": """<b>Область команд: Игра "Словарь":</b>
            Если в словаре достаточно терминов,
            то будет сформирован вопрос и 4 варианта ответа.
            Кнопки ответов регистрируют ответ пользователя.
            <i>Ведется подсчет верных и ошибочных ответов.</i>
            "REPORT" - сообщает администратору о
            неверно сформированном или 
            некорректном вопросе.
            "✖" - вернуться в меню
            /reset_stats - сброс своей игровой статистики""",
    "reset_stats": "Игровая статистика сброшена",
    "need_more_terms": """В базе данных недостаточно терминов
            для составления тестов.
            \nДобавьте новые термины
            в главном меню."""
}

LEXICON_reading_book: dict[str, str] = {
    "cancel": 'отмена области команд чтения "Молитвы и намерения"',
    "help": """<b>Область команд чтения книги:</b>
            /стр ### - открыть страницу (№ 1-251) сборника "Молитва и Намерение".
            /фраг ### - открыть страницу с фрагментом (№ 1-150).
            "🔊" - получить файл озвучки текста.
           "64/251" - сохранить страницу в закладки.
            "✖" - вернуться в меню."""
}


LEXICON_bookmarks: dict[str, str] = {
    "/bookmarks": "<b>Это список ваших закладок:</b>",
    "edit_bookmarks": "<b>Редактировать закладки</b>",
    "edit_bookmarks_button": "❌ Редактировать",
    "add_bookmark": "Страница добавлена в закладки!",
    "bookmark_limit": "Достигнут предел.",
    "del_button": "❌",
    "cancel_button": "ОТМЕНА",
    "menu": "МЕНЮ",
    "cancel_text": """Отмена области команд "Закладки".
        \n/continue - продолжить чтение книги""",
    "no_bookmarks": """У вас пока нет ни одной закладки.\n
        Чтобы добавить страницу в закладки - 
        во время чтения книги 
        нажмите на кнопку вида "64/251"
        с номером этой страницы.""",
    "help": """Область команд "Закладки":
    Закладки добавляются при чтении книги
    нажатием на кнопку вида "64/251"
    с номером текущей страницы.
    Нажатие на закладку перелистывает
    книгу на указанную страницу.
    "РЕДАКТИРОВАТЬ" - вход в режим
    удаления закладок.
    """
}

LEXICON_excerpts: dict[str: str] = {
    "exit_excerpts": "Отмена области команд работы с отрывками",
    "cancel_adding_excerpt": "Ввод нового отрывка отменен.",
    "added_by": "...добавил:",
    "no_excerpts": """Список отрывков пуст. 
                <i>Добавьте отрывок в главном меню.</i>""",
    "add_excerpt": """Введите целиком отрывок, которым хотите поделиться.\n
                <i>"МЕНЮ" - отмена ввода.</i>""",
    "adding_error": "Ошибка при добавлении отрывка",
    "adding_success": "Отрывок добавлен",
    "only_one_excerpt": "В базе данных только один отрывок",
    "excerpt_deleted": "Отрывок удален"
}

LEXICON_letters: dict[str: str] = {
    "menu_letters_button": "Узнику",
    "exit_letters": "Отмена области команд работы с письмами",
    "cancel_adding_letter": "Ввод нового письма отменен.",
    "added_by": "...добавил:",
    "no_letters": """Список писем пуст. 
                <i>Добавьте письмо в главном меню.</i>""",
    "add_letter": """Введите целиком письмо, которым хотите поделиться.\n
                <i>"МЕНЮ" - отмена ввода.</i>""",
    "adding_error": "Ошибка при добавлении письма",
    "adding_success": "Письмо добавлено",
    "only_one_letter": "В базе данных только одно письмо",
    "letter_deleted": "Письмо удалено",
    "edit_letter": """Введите целиком замену этому письму.\n
                <i>"МЕНЮ" - отмена ввода.</i>""",
    "edit_error": "Ошибка при изменении письма",
    "edit_success": "Письмо изменено",
}


LEXICON_menu: dict[str, str] = {
    "/read_book": '📖 читать "Молитва и Намерение"',
    "/bookmarks": '🔖 закладки "Молитва и Намерение"',
    "/random_excerpt": "🗂 отрывок",
    "/add_excerpt": "✉ добавить отрывок",
    "/read_letter": '📝 "Узнику"',
    "/add_letter": "✉ добавить письмо",
    "/play_dict": '⚖ игра "Словарь"',
    "/add_term": "✉ добавить термин",
    "/my_info": "🧮 Моя статистика",
    "/urls": "🔗 ссылки",
    "": ""
}

LEXICON_COMMANDS: dict[str, str] = {
    "/start": "запуск бота",
    "/menu": "меню",
    "/help": "список команд",
    "/cancel": "отмена, выход из области команд"
}