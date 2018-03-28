from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import decouple

engine = create_engine(decouple.config('SQLALCHEMY_DATABASE_URI'), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	import scripts.models
	Base.metadata.create_all(bind=engine)