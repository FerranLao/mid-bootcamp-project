import os
import sys
import datetime
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sklearn.impute import SimpleImputer

load_dotenv()
postgres_url = os.getenv('POSTGRES_URL')
engine = create_engine(postgres_url)


df = pd.read_csv('./penguins.csv')

#? this columns are all the same data Region=Anvers Stage="Adult, 1 Egg Stage and comments"
df = df.drop(["Region", "Stage", "Comments"],axis=1)

df.columns = [c.lower().replace(' ','_') for c in df.columns] 

#? clean up the species name -- Adelie Penguin (Pygoscelis adeliae) -> Adelie 
df['species']=[item.split(' ')[0] for item in df['species']]

#? turn clutch_completion into boolean for simplicity
df['clutch_completion']=[True if item == 'Yes' else False for item in df['clutch_completion']]

#? transform the dates from a string to a date object
def format_date(date:str)->str:
    splited = date.split('/')
    splited[2]= ('20' if splited[2] else '19') + splited[2]
    return '/'.join(splited)

df['date_egg']=[datetime.datetime.strptime(format_date(date_egg), '%m/%d/%Y') for date_egg in df['date_egg']]

#? fill the nulss with the most frequent value
filler = SimpleImputer(strategy="most_frequent")
df.iloc[:, :] = filler.fit_transform(df)

df["sex"] = ['MALE' if item == "." else item for item in df["sex"]]
try:
    df.to_sql('penguins',engine)
    pen = engine.execute("SELECT * FROM penguins")
    print('Done sample-->',next(pen))
except Exception as err:
    print(err)
    sys.exit(1)
