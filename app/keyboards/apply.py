from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ApplyCallback(CallbackData, prefix="apply"):
    data: str


def get_apply_markup(data: str, *args) -> InlineKeyboardMarkup:
    args = [str(i) for i in args]
    buttons = [InlineKeyboardButton(text="🆗", callback_data=ApplyCallback(data=data).pack())]

    builder = InlineKeyboardBuilder()
    builder.add(*buttons)
    return builder.as_markup()
