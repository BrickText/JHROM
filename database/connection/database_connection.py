import sqlite3

from settings.database_settings import DB_NAME
from database.queries.create_table_queries import *


class Database:

    def __init__(self, database_name=DB_NAME):
        self.db_name = DB_NAME
        self.create_connection()

    def create_connection(self):
        self.db = sqlite3.connect(self.db_name)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def drop_tables(self):
        self.cursor.execute(DROP_MOVIE_TABLE)
        self.cursor.execute(DROP_USER_TABLE)
        self.cursor.execute(DROP_RESETVATION_TABLE)
        self.cursor.execute(DROP_PROJECTION_TABLE)

    def create_tables(self):
        self.cursor.execute(CREATE_MOVIE_TABLE)
        self.cursor.execute(CREATE_USER_TABLE)
        self.cursor.execute(CREATE_PROJECTION_TABLE)
        self.cursor.execute(CREATE_RESERVATION_TABLE)
        self.db.commit()

    def get_cursor(self):
        return self.cursor

    def get_db(self):
        return self.db
