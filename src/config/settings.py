import databases
import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///pr.db")

metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///pr.db")


