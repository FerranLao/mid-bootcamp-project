import os
import dotenv
dotenv.load_dotenv()


POSTGRES_URL = os.getenv('POSTGRES_URL')
PORT = os.getenv("PORT")