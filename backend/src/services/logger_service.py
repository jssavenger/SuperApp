import logging
from pathlib import Path

_CURRENT_PATH= Path(__file__).parent.parent
_LOG_FOLDER_PATH= _CURRENT_PATH / "log" / "app.log"

# formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger= logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# console handler
console_handler= logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# file handler
file_handler= logging.FileHandler(_LOG_FOLDER_PATH, mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# add handler
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("test info")
logger.debug("test debug")
logger.error("test error")