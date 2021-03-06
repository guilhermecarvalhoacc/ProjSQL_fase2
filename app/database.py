
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()  



USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")


# Cria o URL do database para o SQLAlchemy
DATABASE_URL = f"mysql+mysqlconnector://{USER}:{PASSWORD}@localhost:3306/shopcart"


print(f"url is {DATABASE_URL}")


# Cria o engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Cria uma classenSessionLocal
# Cada instancia de Session é uma sessão do database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a classe Base
# Usada para criar os modelos ou classe do database (modelos ORM)
Base = declarative_base()

