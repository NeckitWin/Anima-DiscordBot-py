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
                money INTEGER,
                gems INTEGER
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
                query = '''INSERT INTO users VALUES (?, ?, ?)'''
                await cursor.execute(query, (user.id, 0, 0))
                await db.commit()

    async def update_money(self, user_id, money: int, gems: int):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''UPDATE users SET money = money + ?, gems = gems + ? WHERE id = ?'''
            await cursor.execute(query, (money, gems, user_id))
            await db.commit()