# ITP Week 3 Day 1 Exercise

# ENUMERATE!

# 1. Read all instructions first!
# 
# Prompt: given a list of names, create a list of dictionaries with the index as the user_id and name

users_list = ["Alex", "Bob", "Charlie", "Dexter", "Edgar", "Frank", "Gary"]

# example output    
# [{"user_id": 0, "name": "Alex"}, etc, etc]

# 1a. Create a function that takes a single string value and returns the desired dictionary

def create_user(index, name):
    return{
        "user_id": index,
        "name": name
    }
    
# 1b. Create a new empty list called users_dict_list

users_dict_list = []
    
for user_id, name in enumerate(users_list):
    result = create_user(user_id, name)  
    users_dict_list.append(result)
print(users_dict_list)   

# 1c. Loop through users_list that calls the function for each item and appends the return value to users_dict_list

# 2. Prompt: Given a series of dictionaries and desired output (mock_data.py), can you provide the correct commands?
from mock_data import mock_data
# 2a. retrieve the gender of Morty Smith
print(mock_data["results"][1]["gender"])
# 2b. retrieve the length of the Rick Sanchez episodes
print(len(mock_data["results"][0]["episode"]))

# 2c. retrieve the url of Summer Smith location

print(mock_data["results"][2]["location"]["url"])
