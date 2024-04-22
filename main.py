from pyrogram import Client, filters
from pyrogram.types import Message


client = Client(api_id=API_ID, api_hash=API_HASH, name='maxplus')


@client.on_message(filters.user('@carakaton') & filters.text)
async def my_handler(_: Client, message: Message):
    if 'L2' in message.text:
        await message.reply('+')


if __name__ == '__main__':
    client.run()
