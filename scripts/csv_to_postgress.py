import os
from dotenv import load_dotenv
import datetime

import pandas as pd
from sqlalchemy import create_engine

load_dotenv()
postgres_url = os.getenv('POSTGRES_URL')
engine = create_engine(postgres_url)


df = pd.read_csv('./penguins.csv')

#? this columns are all the same data Region=Anvers Stage="Adult, 1 Egg Stage"
df.drop(["Region", "Stage"],axis=1)

df.columns = [c.lower().replace(' ','_') for c in df.columns] 

#? clean up the species name -- Adelie Penguin (Pygoscelis adeliae) -> Adelie 
df['species']=[item.split(' ')[0] for item in df['species']]

#? transform the dates from a string to a date object
def format_date(date:str)->str:
    splited = date.split('/')
    splited[2]= ('20' if splited[2] else '19') + splited[2]
    return '/'.join(splited)

df['date_egg']=[datetime.datetime.strptime(format_date(date_egg), '%m/%d/%Y') for date_egg in df['date_egg']]

#? remove all rows with 2 or more nuls to avoid incomplete data
nullIndexes = []
for index, row in df.iterrows():
    if row.isna().sum()>2:
        print(index)
        nullIndexes.append(index)

df = df.drop(nullIndexes)

