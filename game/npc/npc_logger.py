import os
import logging

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),'logs')
os.makedirs(LOG_DIR,exist_ok=True)

logger = logging.getLogger('NPC')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(name)s] %(message)s')

debug_handler = logging.FileHandler(os.path.join(LOG_DIR,"NPC_debug.log"),encoding='utf-8')
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)

logger.addHandler(debug_handler)

