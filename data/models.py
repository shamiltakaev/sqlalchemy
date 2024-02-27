import datetime
from sqlalchemy import orm, Column, String, DateTime, Integer, Boolean, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String, nullable=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    position = Column(String, nullable=True)
    speciality = Column(String, nullable=True)
    address = Column(String, nullable=True)
    email = Column(String, index=True, unique=True, nullable=True)
    modified_date = Column(DateTime, default=datetime.datetime.now)
    hashed_password = Column(String, nullable=True)


    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)




class Jobs(SqlAlchemyBase):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    job = Column(String, nullable=True)
    work_size = Column(Integer, default=0)
    collaborators = Column(String, nullable=True)
    start_date = Column(DateTime, default=datetime.datetime.now)
    end_date = Column(DateTime, default=datetime.datetime.now)
    is_finished = Column(Boolean, default=True)
    team_leader = Column(Integer, ForeignKey("users.id"))
    orm.relationship("User")

    def __repr__(self):
        return f"{self.id} {self.job}"
