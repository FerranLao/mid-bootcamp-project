import json
from flask import request
from app import app
from configs.postgres import pgdb

@app.route("/")
def helloWordl():
    query = pgdb.execute("SELECT * FROM penguins;")
    print(next(query))
    return 'Hello world'
