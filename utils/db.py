from arena.data import Postgres
from sql.queries import historicValues, dateSpecificValue

pg = Postgres({
    "host": "localhost", 
    "user": "username", 
    "password": "password",
    "port": 5432,
    "database": "database"})

def getHistoryValues(onSuccess, onError):
    pg.run_query(historicValues, 
                 onSuccess=onSuccess, 
                 onError=onError)

def getDateSpecificValue(date, onSuccess, onError):
    pg.run_query(dateSpecificValue, 
                 params={"date": date}, 
                 onSuccess=onSuccess, 
                 onError=onError)