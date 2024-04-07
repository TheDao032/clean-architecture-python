from config.config import settings
from internal.application import createuser_handle
import time
if __name__ == "__main__":
    USERS = [
        {
            "userId": "9",
            "phone": "+84909999999",
            "name": "demo9"
        }
    ]

    print("The Inserting loop is running")
    app = createuser_handle.insert_loop(USERS)
