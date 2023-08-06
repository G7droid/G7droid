"""
Cyberspace bot core.

Functions are inside the `plugins` directory.
This file just initialize them all.
"""
import asyncio
import colorama
from pyrogram import Client, idle
from pyrogram.session import Session

from config import API_HASH, API_ID, BOT_TOKEN, WORKERS
from database import db, save

# Inicializa o colorama
colorama.init()

# Inicializa o cliente.

client = Client(
    "bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=WORKERS,
    plugins={"root": "plugins"},
)

# Desativa a mensagem do Pyrogram no início.
# Restaura a configuração original das cores
colorama.deinit()
# Exemplo de uso de cores
Session.notice_displayed = True


async def main():
    await client.start()
    print(colorama.Fore.RED + "bot iniciado by: @Lzccs")
    client.me = await client.get_me()

    await idle()

    await client.stop()
    save()
    db.close()


loop = asyncio.get_event_loop()

if __name__ == "__main__":
    loop.run_until_complete(main())
