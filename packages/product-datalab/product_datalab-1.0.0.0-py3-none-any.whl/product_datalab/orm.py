from sqlalchemy import create_engine
import pandas as pd

class sql:
    def __init__(self,secret):
        self.username = secret['USERNAME']
        self.password = secret['PASSWORD']
        self.host = secret['HOST']
        self.port = secret['PORT']
        self.db_name = secret['DB_NAME']
        try:
            self.engine = create_engine(
                    f'redshift+psycopg2://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}'
                )
        except Exception as e:
            self.engine = None

    def __str__(self):
        return f'Conf <{self.db_name} : {self.type}> '
    
    def run(self,query):
        try:
            df = pd.read_sql(query,self.engine)
            return df
        
        except:
            return

    def insert(self,df,table,schema):
        try:
            df.to_sql(
                name = table,
                con = self.engine,
                schema = schema,
                index = False,
                if_exists = 'append'
            )
            return True
        
        except Exception as e:
            print(e)
            return False