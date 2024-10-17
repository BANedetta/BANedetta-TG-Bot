from ..managers import posts_manager
from .tg_router_rules import IsCorrectChat, IsPostFate
from aiogram import Router
from aiogram.types import Message
from main import db, config

rt = Router()

@rt.message(IsCorrectChat(), IsPostFate())
async def update_post_fate(message: Message, data: dict):
	await (db.confirm if data["status"] == "confirmed" else db.deny)(data["id"])
	await db.update_post_id("tg", -1, data["id"])
	await db.update_c_post_id(-1, data["id"])
	await posts_manager.edit_post(data)

@rt.message(IsCorrectChat())
async def update_post_id(message: Message):
	if message.from_user.id != 777000:
		return

	if not (text := message.caption or message.text): return

	ban_id = text.splitlines()[-1].lstrip("BAN ID: ")

	if ban_id.isdigit() and await db.get_data(id := int(ban_id)):
		await db.update_post_id("tg", message.message_id, id)
		pass
