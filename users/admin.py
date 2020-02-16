from django.contrib import admin
from .models import UsersData
import json

#Register model
admin.site.register(UsersData)



#To store data into database
with open('users.json',encoding='utf-8') as data:
    json_data = json.load(data)
    
    for d in json_data:
        users = UsersData(**d)
        users.save()