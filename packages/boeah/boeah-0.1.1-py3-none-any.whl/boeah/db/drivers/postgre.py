import psycopg2


class Postgre:
    def connect(self):
        psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="Abcd1234"
        )
