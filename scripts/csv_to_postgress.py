import os
from dotenv import load_dotenv

import pandas as pd
from sqlalchemy import create_engine

load_dotenv()
postgres_url = os.getenv('POSTGRES_URL')
engine = create_engine(postgres_url)


df = pd.read_csv('./penguins.csv')
df.columns = [c.lower().replace(' ','_') for c in df.columns] 
print(df['island'].unique())
for column in df:
   if len(df[column].value_counts()) <=1:
       print(column)