from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
#     "postgres",
#     "root",
#     "localhost",
#     30432,
#     "TodoApplicationDatabase",
# )
SQLALCHEMY_DATABASE_URL = (
    "postgresql://postgres:root@host.docker.internal:30432/TodoApplicationDb"
)

engine = create_engine(
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} ## For sqlite
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
