
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cria o URL do database para o SQLAlchemy
DATABASE_URL = "mysql+mysqlconnector://megadados:megadados123@localhost:3306/shopcart"

# Cria o engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Cria uma classenSessionLocal
# Cada instancia de Session é uma sessão do database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a classe Base
# Usada para criar os modelos ou classe do database (modelos ORM)
Base = declarative_base()

