import pymongo
client = pymongo.MongoClient('localhost',port = 27017)
db = client['proekt1']
db_users = db['users']



# x = {
#     "id": "56734",
#     "name": "",
#     "state": "",
#     "temp_name": "",
#     "country": "",
#     "town": "",
#     "date": ""
#     }

# ДОБАВЛЕНИЕ ДАННЫХ
# db_users.insert_many([{"username": "gosha", 'age': 10}, {"username": "alex", 'age': 15}, {"username": "gosha", 'age': 7}])



# y = [
#     {"username": "gosha"}, 
#     {"username": "alex"}
# ]

# db_users.insert_many(y)



#УДАЛЕНИЕ ДАННЫХ

# b = db_users.delete_one(filter={"id": "12345"})
# print(b)

# b = db_users.delete_many(filter={"age": 7,"username": "gosha"})
# print(b)

# b = db_users.delete_many(filter={}) # удалить всех



# ОБНОВЛЕНИЕ ДАННЫХ
#если у пользователя вообще нет ключа age, то он создаться. Если не будет найдет пользователь по фильтру, то ничего не произойдет
# db_users.update_one(filter={'age': 10,'username': 'gosha'},update={'$set':{'age': '22'}})
# #удаление ключа полностью 
# db_users.update_one(filter={'age': 10,'username': 'gosha'},update={'$unset':{'age': ""}})



# ПОЛУЧЕНИЕ ДАННЫХ 
# Выдает словарь 
user = db_users.find_one(filter={'age': 10,'username': "gosha"})
#Выдает курсор. По нему можно писать цикл, он как список. Только цикл
users = db_users.find(filter={'age': 10,'username': "gosha"})
for i in users:
    print(i)

#Выдает список
users = db_users.find(filter={'age': 10,'username': "gosha"}).to_list()
print(users)