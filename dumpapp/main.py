from config.config import settings
from internal.application import createuser_handle
import time
def main():
    USERS = [
        {
            "userId": "9",
            "phone": "+84909999999",
            "name": "demo9"
        }
    ]
    print("The Inserting loop is running")
    createuser_handle.insert_loop(USERS,300)

if __name__ == "__main__":
    app=main()
