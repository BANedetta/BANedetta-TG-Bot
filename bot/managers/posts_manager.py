from main import bot, config
from aiogram import types

# The fu***** Telegram API
methods = {
	"animation": bot.send_animation,
	"audio": bot.send_audio,
	"document": bot.send_document,
	"photo": bot.send_photo,
	"video": bot.send_video
}

async def __get_ready_post_params(post_config, data):
	ban_context = "\nBAN ID: " + str(data["id"])
	text = post_config["post"].format(banned = data["banned"],
		by = data["by"], reason = data["reason"]) + ban_context
	params = {"chat_id": config.channel_id, "text": text}

	if config.post_media_enable:
		attachments = post_config["attachments"]
		params.update({attachments["type"]: attachments["url"], "caption": text})
		params.pop("text")

	return params

async def create_post(data: dict) -> int:
	post_config = config.post_templates["waiting"]
	method = methods[post_config["attachments"]["type"]] if config.post_media_enable else bot.send_message
	params = await __get_ready_post_params(post_config, data)
	response = await method(**params)
	return response.message_id

async def edit_post(data: dict):
	post_config = config.post_templates[data["status"]]
	params = await __get_ready_post_params(post_config, data)
	params["message_id"] = data["tg_post_c"]

	if config.post_media_enable:
		media = post_config["attachments"]
		media_type = post_config["attachments"]["type"]
		if media_type in methods:
			media = types.InputMediaPhoto(media=media["url"], caption=params["caption"])  # Example for photo
			await bot.edit_message_media(media=media, chat_id=params["chat_id"], message_id=data["tg_post_c"])
		# Edit the caption
		# await bot.edit_message_caption(chat_id=params["chat_id"], message_id=data["tg_post_c"], caption=params["caption"])
	else:
		# Edit only the text if no media is enabled
		await bot.edit_message_text(chat_id=params["chat_id"], message_id=data["tg_post_c"], text=params["text"])
