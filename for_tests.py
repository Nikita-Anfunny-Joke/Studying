

# pip install psycopg2 если библиотека не установлена
import psycopg2

database="startml",
user="robot-startml-ro",
password="pheiph0hahj1Vaif",
host="postgres.lab.karpov.courses",
port=6432

import pandas as pd

df = pd.read_sql(
    """SELECT * FROM "feed_action" LIMIT 10 """,
    con="postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
        "postgres.lab.karpov.courses:6432/startml"
)

df.head(5)
