from sqlmodel import Field, SQLModel, create_engine


class Hero(SQLModel, table=True):
 #table=true tells sqlmodel this is a table model
 # without which it would be a data model
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

# If you have a server database (for example PostgreSQL or MySQL),
# the engine will hold the network connections to that database.
# more about SQLAlchemy: https://docs.sqlalchemy.org/en/14/core/engines.html

sqlite_file_name = "learn_sqlmodel.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True) #echo prints all statements

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()