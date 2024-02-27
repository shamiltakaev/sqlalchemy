import datetime
import sqlalchemy
from sqlalchemy import orm, Column, String, DateTime, Integer, Boolean, ForeignKey
from .db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    content = Column(String, nullable=True)
    created_date = Column(DateTime, default=datetime.datetime.now)
    is_private = Column(Boolean, default=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = orm.relationship('User')
