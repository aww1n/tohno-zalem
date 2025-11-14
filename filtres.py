from db import *
async def is_wait_new_category_user(message):
    a = await db_users.find_one(filter={'id': message.from_user.id, "state":'wait new category'})
    if a != None:
        return True
    else:
        return False
    

async def is_delete_category_user(message):
    a = await db_users.find_one(filter={'id': message.from_user.id, "state":'wait delete category'})
    if a != None:
        return True
    else:
        return False
    
#//////////////////////////////////////////////////////////////////////////////

async def is_wait_category_for_new_subcategory_user(message):
    a = await db_users.find_one(filter={'id': message.from_user.id, "state":'wait category for new subcategory'})
    if a != None:
        return True
    else:
        return False
    

async def is_wait_new_subcategory_user(message):
    a = await db_users.find_one(filter={'id': message.from_user.id, "state":'wait new subcategory'})
    if a != None:
        return True
    else:
        return False
    



async def is_wait_category_for_delete_subcategory_user(message):
    a = await db_users.find_one(filter={'id': message.from_user.id, "state":'wait category for delete subcategory'})
    if a != None:
        return True
    else:
        return False
    




async def is_wait_subcategory_for_delete_subcategory_user(message):
    a = await db_users.find_one(filter={'id': message.from_user.id, "state":'wait delete subcategory'})
    if a != None:
        return True
    else:
        return False
    

