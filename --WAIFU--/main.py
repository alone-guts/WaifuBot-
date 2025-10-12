from WAIFU import *
import importlib
import logging
from WAIFU.modules import ALL_MODULES


def main() -> None:
    for module_name in ALL_MODULES:
        imported_module = importlib.import_module("WAIFU.modules." + module_name)
    LOGGER("WAIFU.modules").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")

    WAIFU.start()
    application.run_polling(drop_pending_updates=True)
    LOGGER("WAIFU").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎MADE BY WAIFU☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    send_start_message()
    

if __name__ == "__main__":
    main()
    
    