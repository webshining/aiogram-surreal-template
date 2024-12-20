from typing import Callable, Dict, Awaitable, Any

from aiogram import BaseMiddleware
from aiogram.types import Update, Message, CallbackQuery, InlineQuery

from database.models import User


class UserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ):
        if event.message:
            await self.handle_message(event.message, data)
        elif event.callback_query:
            await self.handle_callback_query(event.callback_query, data)
        elif event.inline_query:
            await self.handle_inline_query(event.inline_query, data)
        return await handler(event, data)

    @staticmethod
    async def handle_message(message: Message, data: Dict[str, Any]):
        from_user = message.from_user
        data['user'] = await User.update_or_create(id=from_user.id, name=from_user.full_name,
                                                   username=from_user.username,
                                                   lang=from_user.language_code)

    @staticmethod
    async def handle_callback_query(call: CallbackQuery, data: Dict[str, Any]):
        await call.answer()
        from_user = call.from_user
        data['user'] = await User.update_or_create(id=from_user.id, name=from_user.full_name,
                                                   username=from_user.username,
                                                   lang=from_user.language_code)

    @staticmethod
    async def handle_inline_query(query: InlineQuery, data: Dict[str, Any]):
        from_user = query.from_user
        data['user'] = await User.update_or_create(id=from_user.id, name=from_user.full_name,
                                                   username=from_user.username,
                                                   lang=from_user.language_code)
