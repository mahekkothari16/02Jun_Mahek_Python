def login(username, password, user_dict):
    return user_dict.get(username) == password
