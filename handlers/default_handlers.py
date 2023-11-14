from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery

from database.queries import AsyncQuery
from filters.filters import IsCloseButton
from keyboards.menu_kb import create_menu_keyboard
from lexicon.lexicon import LEXICON_default
from handlers.menu_handlers import process_menu_message


router = Router()


@router.message(Command(commands=["start"]))
async def process_start_message(message: Message, state: FSMContext) -> None:
    """Хендлер команды /start, сбрасывает состояние, отсылает информационные сообщения,
    аутентификация пользователя. Если пользователь отсутствует в БД, то создает
    строку в таблице users с начальным значениями для этого пользователя."""
    await state.clear()
    await message.answer(
        text=f"{LEXICON_default['greeting'][0]} {message.from_user.first_name}!"
    )
    await message.answer(text=LEXICON_default['greeting'][1])
    await process_menu_message(message, state)
    if await AsyncQuery.select_user(message.from_user.id) is None:
        await AsyncQuery.insert_user(message.from_user.id, message.from_user.first_name)


@router.message(Command(commands=["help"]), StateFilter(default_state))
async def process_help_dictionary(message: Message) -> None:
    """Хендлер команды /help. Присылает пользователю список команд."""
    await message.answer(LEXICON_default["help"])


@router.message(Command(commands=["cancel"]), StateFilter(default_state))
async def process_cancel_denied_message(message: Message) -> None:
    """Хендлер команды /cancel. Сообщает пользователю, что в данный момент действует
    начальная область команд, и нет области которую нужно отменять"""
    await message.answer(text=LEXICON_default["cancel-denied"] + ', ' + message.from_user.first_name + '.')


@router.message(Command(commands=["Cancel"]))
async def process_cancel_message_not_default_state(message: Message, state: FSMContext) -> None:
    """Хендлер сброса любых состояний к начальному"""
    await state.clear()
    await message.answer(text=LEXICON_default["Cancel"])


@router.callback_query(IsCloseButton())
async def process_any_close_button(callback: CallbackQuery, state: FSMContext):
    """Хендлер завершения игры по кнопке закрытия.
    Сброс состояния, удаление сообщения и клавиатуры."""
    user = await AsyncQuery.select_user(callback.from_user.id)
    await callback.message.edit_text(
        text=f"<b>{user.name}</b> (🍪{user.answers}):",
        reply_markup=create_menu_keyboard()
    )



@router.message(Command(commands=["my_info"]))
async def process_info_message(message: Message) -> None:
    """Хендлер команды /my_info. Присылает сообщение с данными статистики пользователя
    в игре 'Словарь'"""
    user = await AsyncQuery.select_user(message.from_user.id)
    tpl = LEXICON_default["my_info"]
    await message.answer(
        text=f"{tpl[0]}\n\n"
        f"{tpl[1]} {user.answers}\n"
        f"{tpl[2]} {user.right_answers}\n"
        f"{tpl[3]} {user.wrong_answers}\n\n"
        f"{tpl[4]}"
    )


@router.message(Command(commands=['urls']))
async def process_urls_command(message: Message) -> None:
    """Хендлер команды /urls. Присылает сообщение с указанием ссылок
    на полезные ресурсы по тематике бота"""
    await message.answer(text=LEXICON_default['urls'])
