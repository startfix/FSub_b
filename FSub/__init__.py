import os

from pyromod import Client
from pyrogram.types import BotCommand

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_DB,
    FORCE_SUB_,
    FORCE_SUB_TOTAL,
    LOGGER,
    ADMINS,
    BOT_TOKEN,
    PROTECT_CONTENT,
)


class FSub(Client):
    def __init__(self):
        super().__init__(
            name      = "Bot",
            api_id    = API_ID, 
            api_hash  = API_HASH,
            bot_token = BOT_TOKEN,
            in_memory = True,
            plugins   = dict(root="FSub/plugins"))

    async def start(self):
        try:
            await super().start()
            get_bot_profile = await self.get_me()
            self.bot_logger = LOGGER
            self.username   = get_bot_profile.username
            self.bot_logger.info(f"Memulai bot: @{self.username} (ID: {get_bot_profile.id})")
        except Exception as e:
            LOGGER.error(e)
            exit()
        
        try:
            self.bot_logger.info("Menyetel perintah bot...")
            await self.set_bot_commands([
                BotCommand("start", "Mulai bot"),
                BotCommand("ping", "Periksa latensi bot"),
                BotCommand("batch", "[Admin] Pesan massal"),
                BotCommand("broadcast", "[Admin] Kirim pesan siaran"),
                BotCommand("users", "[Admin] Periksa jumlah pengguna bot"),
                BotCommand("restart", "[Admin] Mulai ulang bot")])
            self.bot_logger.info("Perintah bot berhasil disetel.")
        except Exception as e:
            self.bot_logger.error(e)
            pass

        for key, chat_id in FORCE_SUB_.items():
            try:
                self.bot_logger.info(f"Memeriksa akses bot di FORCE_SUB_{key}...")
                get_chat    = await self.get_chat(chat_id)
                invite_link = get_chat.invite_link
                if not invite_link:
                    await self.export_chat_invite_link(chat_id)
                    invite_link = get_chat.invite_link
                setattr(self, f"FORCE_SUB_{key}", invite_link)
                self.bot_logger.info(f"FORCE_SUB_{key} terdeteksi: {get_chat.title} (ID: {get_chat.id})")
            except Exception as e:
                self.bot_logger.error(e)
                self.bot_logger.error(f"@{self.username} tidak memiliki akses mengundang pengguna dengan tautan di FORCE_SUB_{key}. Pastikan bot menjadi admin dan diberi akses mengundang pengguna dengan tautan.")
                exit()

        try:
            self.bot_logger.info("Memeriksa akses bot di CHANNEL_DB...")
            hello_world = await self.send_message(CHANNEL_DB, "Hello World!") ; await hello_world.delete()
            get_chat    = await self.get_chat(CHANNEL_DB)
            self.bot_logger.info(f"CHANNEL_DB terdeteksi: {get_chat.title} (ID: {get_chat.id})")
        except Exception as e:
            self.bot_logger.error(e)
            self.bot_logger.error(f"@{self.username} tidak memiliki akses/tidak berhasil mengirim pesan di CHANNEL_DB. Pastikan bot menjadi admin dan diberi akses mengirim pesan.")
            exit()
        
        if os.path.exists('restart.txt'):
            with open('restart.txt', 'r') as f:
                chat_id    = int(f.readline().strip())
                message_id = int(f.readline().strip())
                await self.edit_message_text(chat_id, message_id, "Bot dimulai ulang.")
            
            os.remove('restart.txt')

        self.bot_logger.info("Bot berhasil diaktifkan!")
    
    async def stop(self, *args):
        await super().stop()
        self.bot_logger.warning("Bot telah berhenti!")
    
FSub = FSub()
