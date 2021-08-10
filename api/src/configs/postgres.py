
from sqlalchemy import create_engine
from config import POSTGRES_URL
from flask import jsonify


engine = create_engine(POSTGRES_URL)

pgdb = engine.connect()

def json_query(query:str)-> str:
    data = pgdb.execute(query).fetchall()
    return jsonify([dict(row) for row in data])