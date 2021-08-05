
from sqlalchemy import create_engine
from config import POSTGRES_URL


engine = create_engine(POSTGRES_URL)

pgdb = engine.connect()
