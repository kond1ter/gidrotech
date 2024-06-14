from config import *
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session
from sqlalchemy import Column, Integer, String, JSON

engine = create_engine("{0}+{1}://{2}:{3}@{4}/{5}".format(
    DB_DIALECT, DB_DRIVER, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME
))
session = scoped_session(sessionmaker(autoflush=False, bind=engine, expire_on_commit=False))

class Base(DeclarativeBase):
    pass

