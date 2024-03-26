import aiosqlite


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
            self.__keys = ['user_id', 'gender', 'age', 'height', 'weight', 'activity']

    async def start(self):
        async with aiosqlite.connect(self.__path) as cur:
            await cur.execute('''CREATE TABLE IF NOT EXISTS users (
                user_id TEXT NOT NULL PRIMARY KEY,
                gender TEXT,
                age FLOAT,
                height FLOAT,
                weight FLOAT,
                activity FLOAT
                )''')
            await cur.commit()

    @property
    def keys(self):
        return self.__keys

    async def get_value(self, name, user_id):
        try:
            async with aiosqlite.connect(self.__path) as cur:
                value = await cur.execute(f"SELECT {name} FROM users WHERE user_id == '" + str(user_id) + "'")
                value = await value.fetchall()
                return value[0][0]
        except:
            return None

    async def add_user(self, user_id):
        try:
            async with aiosqlite.connect(self.__path) as cur:
                await cur.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
                await cur.commit()
            return True
        except:
            return False

    async def set_value(self, name, user_id, value):
        try:
            async with aiosqlite.connect(self.__path) as cur:
                await cur.execute(f'UPDATE users SET {name} = ? WHERE user_id = ?', (f"{value}", user_id))
                await cur.commit()
            return True
        except:
            return False


data = DataBase("Data_base//bot_db.db")