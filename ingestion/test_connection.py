import psycopg
import os
from dotenv import load_dotenv

load_dotenv()
try:
    with psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    ) as connection:
        print("Successfully connected to PostgreSQL!")

except Exception as error:
    print("Database connection failed.")
    print(error)


# import os
# import psycopg
# from dotenv import load_dotenv

# from pathlib import Path

# load_dotenv(Path(__file__).resolve().parent.parent / ".env")
# print("DB_USER found:", bool(os.getenv("DB_USER")))
# print("DB_PASSWORD found:", bool(os.getenv("DB_PASSWORD")))
# # try:
# #     connection = psycopg.connect(
# #     host=os.getenv("DB_HOST"),
# #     port=os.getenv("DB_PORT"),
# #     dbname=os.getenv("DB_NAME"),
# #     user=os.getenv("DB_USER"),
# #     password=os.getenv("DB_PASSWORD")
# #     )

# #     print("PostgreSQL connection successful!")

# #     connection.close()

# # except Exception as error:
# #     print("Database connection failed:", error)