# app/database.py
from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url='sqlite://ecommerce.db',
        modules={'models': ['app.models']}
    )
    await Tortoise.generate_schemas()
