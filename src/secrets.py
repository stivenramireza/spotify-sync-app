import os

from src.logger import logger

PYTHON_ENV = os.environ.get('PYTHON_ENV')
if PYTHON_ENV == 'production':
    logger.info('Using production environment variables')
else:
    logger.info('Using development environment variables')

PORT = os.environ.get('PORT')
