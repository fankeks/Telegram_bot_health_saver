import sqlite3 as sq


class DataBase:
    __obj = None
    __init = None

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = super().__new__(cls)
        return cls.__obj

    def __init__(self, path):
        if self.__init is None:
            self.__path = path
            self.__cur = None
            self.__con = None
            self.__keys = None

    def start(self):
        if self.__con is None:
            self.__con = sq.connect(self.__path)
            self.__cur = self.__con.cursor()
            self.__cur.execute('''CREATE TABLE IF NOT EXISTS users (
                user_id TEXT NOT NULL PRIMARY KEY,
                gender TEXT,
                age FLOAT,
                height FLOAT,
                weight FLOAT,
                activity FLOAT
                )''')
            self.__con.commit()
            self.__keys = ['user_id', 'gender', 'age', 'height', 'weight', 'activity']

    @property
    def keys(self):
        return self.__keys

    def get_value(self, name, user_id):
        try:
            value = self.__cur.execute(f"SELECT {name} FROM users WHERE user_id == '" + str(user_id) + "'").fetchall()[0][0]
            return value
        except:
            return None

    def add_user(self, user_id):
        try:
            self.__cur.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
            self.__con.commit()
            return True
        except:
            return False

    def set_value(self, name, user_id, value):
        try:
            self.__cur.execute(f'UPDATE users SET {name} = ? WHERE user_id = ?', (f"{value}", user_id))
            self.__con.commit()
            return True
        except:
            return False

    def close(self):
        self.__con.close()


data = DataBase("C://Users//Hp//Desktop//PyCharm//telegram_bots//Telegram_bot_health_saver//Data_base//bot_db.db")