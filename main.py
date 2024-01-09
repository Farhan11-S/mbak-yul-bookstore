'''
Anggota kelompok : 
1. 202351080 - Fattakhul Munir Wildan Syafian 
2. 202351086 - Farhan Sangaji 
3. 202351094 - Yunus Dwi Wibisono

'''

import json
from admin import main as admin
from shop import main as shop


def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data.get("users", [])
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    users = read_json_file("users.json")
    authorizedUser = dict()

    if users:
        isLoggedIn = False
        for user in users:
            isLoggedIn = user["username"] == username and user["password"] == password
            if isLoggedIn:
                authorizedUser = user
                break

        if isLoggedIn:
            print("Login successful!")
            if authorizedUser["role"] == 1:
                admin()
            elif authorizedUser["role"] == 2:
                shop()
            else:
                print("Invalid role. Please contact 911")

        else:
            print("Login failed. Invalid username or password.")
            login()
    else:
        print("Sorry there is something wrong with the database right now.")


if __name__ == "__main__":
    login()
