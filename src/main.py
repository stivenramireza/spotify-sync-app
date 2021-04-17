import uvicorn

from src.secrets import PYTHON_ENV
from src.logger import logger
from src.api import app


def main() -> None:
    logger.info(f'Images resizer app running at port 8000 in {PYTHON_ENV} mode')
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
