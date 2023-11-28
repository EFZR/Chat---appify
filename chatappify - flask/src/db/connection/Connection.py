import sqlite3
from flask import g, current_app


class Connection:
    @classmethod
    def dict_factory(cls, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    @classmethod
    def connection(cls):
        try:
            if "db" not in g:
                g.db = sqlite3.connect(
                    current_app.config["DATABASE"],
                    detect_types=sqlite3.PARSE_DECLTYPES,
                )
                g.db.row_factory = cls.dict_factory
                g.db.execute("PRAGMA foreign_keys = ON;")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
        return g.db

    @classmethod
    def close_connection(cls):
        db = g.pop("db", None)
        if db is not None:
            db.close()
