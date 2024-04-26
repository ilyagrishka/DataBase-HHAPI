import psycopg2


def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о компаниях и вакансиях."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE company (
                company_name SERIAL PRIMARY KEY,
                company_id int NOT NULL,
                company_address varchar,
                number of employees INTEGER
                
            )
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancy (
                name_vac SERIAL PRIMARY KEY,
                vac_id INT REFERENCES company(company_id),
                salary int NOT NULL
                )
        """)

    conn.commit()
    conn.close()


def save_data_to_database():
    pass


