from sqlalchemy.ext.asyncio import create_async_engine
from app.settings import settings


engine = create_async_engine(
    settings.database_url,
    echo=False,          # SQL логирование (True только для dev)
    pool_pre_ping=True,  # проверка соединения
    future=True,
)

