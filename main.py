import logging
import sys
from collections import Counter
from typing import Optional

from models.document import Document


def init_logging():
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(log_format)

    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def rewrite_letter(
    letter: str, article: str, lowered: bool = True
) -> Optional[str]:
    logger = init_logging()
    letter = Document(letter, lowered)
    article = Document(article, lowered)

    if letter.is_writable(article):
        _, subtracted = article.remove_characters(
            letter.get_counter(), update_value=True
        )
        rewrited_letter = letter.rewrite_with_characters(subtracted)
        return rewrited_letter

    return None
