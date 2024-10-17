from ..managers import posts_manager
from banedetta_db import DataSynchronizer
from main import db

async def synchronization():
	ds = DataSynchronizer(db, "tg")

	async for data in ds.synchronize_problems():
		match data["problem"]:
			case "no_post":
				c_post_id = await posts_manager.create_post(data)
				await db.update_c_post_id(c_post_id, data["id"])

			case "resolved":
				await posts_manager.edit_post(data)
				await db.update_post_id("tg", -1, data["id"])
				await db.update_c_post_id(-1, data["id"])
