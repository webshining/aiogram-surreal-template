from aiogram import Dispatcher

from .commands import set_default_commands
from .handlers import admin_router, user_router
from .middlewares import i18n_middleware, UserMiddleware, AdminMiddleware


def setup_routes(dp: Dispatcher):
    dp.update.middleware(i18n_middleware)
    dp.update.middleware(UserMiddleware())

    admin_router.message.middleware(AdminMiddleware())
    admin_router.callback_query.middleware(AdminMiddleware())

    dp.include_routers(user_router, admin_router)
