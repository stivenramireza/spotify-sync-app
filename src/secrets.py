from src.logger import logger

import os

PYTHON_ENV = os.environ.get('PYTHON_ENV')
if PYTHON_ENV == 'production':
    logger.info('Using production environment variables')
else:
    logger.info('Using development environment variables')
