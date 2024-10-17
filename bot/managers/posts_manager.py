from aiogram import types
from main import bot, config

inputs = {
	"animation": types.InputMediaAnimation,
	"audio": types.InputMediaAudio,
	"document": types.InputMediaDocument,
	"photo": types.InputMediaPhoto,
	"video": types.InputMediaVideo
}

def _get_post_text(post_config: dict, data: dict) -> str:
	return (
		post_config["post"].format(
			banned=data["banned"],
			by=data["by"],
			reason=data["reason"]
		) + "\nBAN ID: " + str(data["id"])
	)

async def create_post(data: dict) -> int:
	post_config = config.post_templates["waiting"]
	text = _get_post_text(post_config, data)

	if config.post_media_enable:
		media = post_config["media"]

		# method = bot.send_animation if media["type"] == "animation" else bot.send_media_group
		# response = (await method(config.channel_id, media["url"], caption = text)
		# 	if media["type"] == "animation" else await bot.send_media_group(config.channel_id,
		# 		[inputs.get(media["type"])(media = media["url"], caption = text)]))
		# return response[0].message_id if media["type"] != "animation" else response.message_id

		method = bot.send_animation if media["type"] == "animation" else bot.send_media_group

		if media["type"] == "animation":
			response = await method(config.channel_id, media["url"], caption = text, parse_mode = config.parse_mode)
		else:
			media_group = [inputs[media["type"]](media = media["url"], caption = text, parse_mode = config.parse_mode)]
			response = await method(config.channel_id, media_group)

		return response[0].message_id if media["type"] != "animation" else response.message_id

	return (await bot.send_message(config.channel_id, text)).message_id

async def edit_post(data: dict):
	post_config = config.post_templates[data["status"]]
	text = _get_post_text(post_config, data)

	if config.post_media_enable:
		media = post_config["media"]
		tmedia = inputs[media["type"]](media = media["url"], caption = text)
		await bot.edit_message_media(tmedia, chat_id = config.channel_id, message_id = data["tg_post_c"])
		return

	await bot.edit_message_text(text, chat_id = config.channel_id, message_id = data["tg_post_c"])
