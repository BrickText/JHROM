import sqlite3

from settings.database_settings import DB_NAME


class DatabaseConnection:

    def __init__(self):
        self.db = sqlite3.connect(DB_NAME)
        self.db.row_factory = sqlite3.Row
        self.c = self.db.cursor()

    def get_cursor(self):
        return self.c
