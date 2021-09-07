from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Table


engine = create_engine('sqlite:///./database.db')

Base = declarative_base(bind=engine)

metadata = MetaData(bind=engine)

Base.metadata.create_all()

class Test(Base):
    __table__ = Table('test', metadata, autoload=True)

session = Session(bind=engine)

users = session.query(Test).all()

for user in users:
    print(user.id, user.username)