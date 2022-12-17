import sqlite3 as sql
import os



class BaseWorker:
    def set_base_path(self, base_path: str):
        self.base_path = base_path

    def check_base(self):
        return os.path.exists(self.base_path)

    def create_base(self, sql_file: str):
        connection = sql.connect(self.base_path)
        cur = connection.cursor()
        with open(sql_file, "r") as file:
            scripts = file.read()
            try:
                cur.executescript(scripts)
                connection.commit()
            except sql.Error as error:
                print(error)
            finally:
                connection.close()