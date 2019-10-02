import psycopg2
from db_connection import cursor

class QuoteModel:

    def __init__(self, _id, quote):
        self._id = _id
        self.quote = quote

    def json(self):
        return {'id': self._id, 'quote':, self.quote}

    @classmethod
    def find_by_id(cls, _id):
        query = "SELECT * FROM quotes WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = cursor.fetchone()

        if row:
            return cls(*row)