from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
import os

DB_FILENAME = "sqlite:///" + os.path.join(os.path.dirname(__file__), "database.db")
if os.path.exists(DB_FILENAME):
        os.remove(DB_FILENAME)
engine      = create_engine(DB_FILENAME)
db_session  = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import web_world_builder.models.town
    import web_world_builder.models.geography
    Base.metadata.create_all(bind=engine)
