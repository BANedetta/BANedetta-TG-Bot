# The ID or username of users who can decide the fate of bans
# (usernames without the "@" sign)
users = [1098773489, "taskov1ch"]

# TG Channel ID
channel_id = "@taskov1ch_group" # -1002391264384

# Channel Discussion chat ID
chat_id = "@taskov1ch_chat" # -1002237373576

# Since Telegram has a limit of 1024 characters if the message contains media,
# it's better to decide in advance whether to send the media along with the post.
# When this feature is disabled, media will not be attached to the post,
# and the limit will increase to 4096 characters.
post_media_enable = False

# Parse mode
from aiogram.enums import ParseMode
parse_mode = ParseMode.MARKDOWN

# At the end of the post there will be a text similar to "BAN ID: <id>"
# due to the difference in the IDs issued in the channel and the discussion chat.
# I will definitely correct this misunderstanding in the future, but for now it is so...
# Also, please, when creating a publication in the channel,
# do not use"BAN ID: <id>" at the end of the publication.
post_templates = {
	"waiting": {
		"media": {
			"type": "animation", # animation, audio, document, photo, video
			"url": "https://i.ibb.co/xHVZrK4/fsU8dbK.gif"
		},
		"post": """
Player *{banned}* was blocked by player *{by}*.
Reason: _{reason}_.
Evidence is expected within 6 hours, otherwise, your account will be blocked!
		"""
	},
	"confirmed": {
		"media": {
			"type": "animation",
			"url": "https://i.ibb.co/Chhmz7H/brooh-Chel.gif"
		},
		"post": """
Player *{banned}* was blocked by player *{by}*.
Reason: _{reason}_.
Confirmed!
		"""
	},
	"denied": {
		"media": {
			"type": "animation",
			"url": "https://i.ibb.co/gDyZY24/cvyvvqv-Ywvddw8.gif"
		},
		"post": """
Player *{banned}* was blocked by player *{by}*.
Reason: _{reason}_.
Not confirmed! *{banned}* has been unblocked, and *{by}* has been blocked.
		"""
	},
}
