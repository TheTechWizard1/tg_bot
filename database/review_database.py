import sqlite3
from .queries import ReviewQueries

class ReviewDatabase:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        # Контекстный менеджер
        with sqlite3.connect(self.path) as connect:
            connect.execute(ReviewQueries.CREATE_REVIEW_TABLE)

    def execute(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as connect:
            connect.execute(query, params)