
# Import necessary module
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine


def query(db):
  def decorator(fn):
  	def replacement():
  		engine = create_engine(f'sqlite:///{db}')
  		with engine.connect() as con:
  			rs = fn(con)
  			df = pd.DataFrame(rs.fetchall())
  			df.columns = rs.keys()
  			print(df)
  	return replacement
  return decorator


@query('sqlite_db_pythonsqlite.db')
def Q1(con):
	return con.execute(...)





if __name__ == '__main__':
  Q1()