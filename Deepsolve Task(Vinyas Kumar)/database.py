# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# 🔁 Change these to your real MySQL username/password
DATABASE_URL = "mysql+pymysql://root:password@localhost/shopify_insights"

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Create tables in MySQL
Base.metadata.create_all(bind=engine)
