from aiogram.enums import ChatType
from aiogram.filters import BaseFilter
from aiogram.types import Message
from main import config, db

class IsCorrectChat(BaseFilter):

	async def __call__(self, message: Message):
		return (
			message.chat.id == config.chat_id or
			message.chat.username == config.chat_id[1:]
		) and message.chat.type == ChatType.SUPERGROUP

class IsPostFate(BaseFilter):
	async def __call__(self, message: Message):
		if not (
			message.from_user.id in config.users or
			message.from_user.username in config.users
		): return False

		statuses = {"+": "confirmed", "-": "denied"}

		if (
			(post_id := message.message_thread_id) and
			(data := await db.get_data_by_post_id("tg", post_id)) and
			(status := statuses.get(message.text))
		):
			data["status"] = status
			return {"data": data}

		return False