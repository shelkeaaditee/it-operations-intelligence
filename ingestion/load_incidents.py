
import csv
import psycopg
import os
from dotenv import load_dotenv

CSV_FILE = "data/incidents.csv"

try:
    with psycopg.connect(
           host=os.getenv("DB_HOST"),
           port=os.getenv("DB_PORT"),
           dbname=os.getenv("DB_NAME"),
           user=os.getenv("DB_USER"),
           password=os.getenv("DB_PASSWORD")
       )as connection:

        with connection.cursor() as cursor:
            with open(CSV_FILE, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    cursor.execute(
                        """
                        INSERT INTO incidents (
                            incident_id,
                            short_description,
                            priority,
                            category,
                            status,
                            support_group,
                            created_at,
                            resolved_at,
                            sla_due_at
                        )
                        VALUES (
                            %s, %s, %s, %s, %s, %s,
                            %s, %s, %s
                        )
                        """,
                        (
                            row["incident_id"],
                            row["short_description"],
                            row["priority"],
                            row["category"],
                            row["status"],
                            row["support_group"],
                            row["created_at"],
                            row["resolved_at"] or None,
                            row["sla_due_at"]
                        )
                    )

    print("Successfully loaded incidents into PostgreSQL!")

except Exception as error:
    print("Data loading failed.")
    print(error)
