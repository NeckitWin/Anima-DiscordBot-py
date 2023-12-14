import aiosqlite
import disnake


class UserDB:
    def __init__(self):
        self.name = "dbs/users.db"

    async def create_table(self):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name VARCHAR,
                xp INTEGER,
                lvl INTEGER,
                money INTEGER
            )'''
            await cursor.execute(query)
            await db.commit()

    async def get_user(self, user: disnake.Member):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''SELECT * FROM users WHERE id = ?'''
            await cursor.execute(query, (user.id,))
            return await cursor.fetchone()

    async def add_user(self, user: disnake.Member):
        async with aiosqlite.connect(self.name) as db:
            if not await self.get_user(user):
                cursor = await db.cursor()
                query = '''INSERT INTO users VALUES (?, ?, ?, ?, ?)'''
                await cursor.execute(query, (user.id, user.name, 0, 0, 1000))
                await db.commit()

    async def update_user(self, user: disnake.Member):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''UPDATE users SET xp = xp + ? WHERE id = ?'''
            await cursor.execute(query, (1, user.id))
            await db.commit()

    async def get_top(self):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''SELECT * FROM users ORDER BY xp DESC LIMIT 10'''
            await cursor.execute(query)
            return await cursor.fetchall()

    async def update_name(self, user: disnake.Member):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''UPDATE users SET name = ? WHERE id = ?'''
            await cursor.execute(query, (user.name, user.id))
            await db.commit()