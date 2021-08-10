import json
from app import app
from configs.postgres import json_query

@app.route("/")
def helloWordl():
    query = json_query("SELECT * FROM penguins;")
    return query
