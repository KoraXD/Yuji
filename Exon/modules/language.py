import itertools
from collections.abc import Iterable
from typing import Generator, List, Union

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

import Exon.modules.sql.language_sql as sql
from Exon.langs import get_language, get_languages, get_string
from Exon.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from Exon.modules.helper_funcs.decorators import Exoncallback, Exoncmd


def paginate(iterable: Iterable, page_size: int) -> Generator[List, None, None]:
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (
            itertools.islice(i1, page_size, None),
            list(itertools.islice(i2, page_size)),
        )
        if len(page) == 0:
            break
        yield page


def gs(chat_id: Union[int, str], string: str) -> str:
    try:
        lang = sql.get_chat_lang(chat_id)
        return get_string(lang, string)
    except:
        return "ᴍᴇ ɴᴏᴡ ʙᴜsʏ ᴡʜᴇɴ ғʀᴇᴇ ᴀᴅᴅ ᴛʜɪs "
