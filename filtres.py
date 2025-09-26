from db import *
async def is_wait_category_user(message):
    a = await db_users.find_one(filter={'id': message.from_user.id, "state":'wait new category'})
    if a != None:
        return True
    else:
        return False
    

async def is_delet_category_user(message):
    a = await db_users.find_one(filter={'id': message.from_user.id, "state":'wait delete category'})
    print(a)
    if a != None:
        return True
    else:
        return False