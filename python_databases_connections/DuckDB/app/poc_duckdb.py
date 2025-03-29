import duckdb

def create_table():
    with duckdb.connect("example.db") as con:
        con.sql("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                email TEXT
            )
        """)
        print("Table 'users' created successfully.")


def create_user(user_id, name, age, email):
    with duckdb.connect("example.db") as con:
        con.sql(f"""
            INSERT INTO users VALUES ({user_id}, '{name}', {age}, '{email}')
        """)
        print("User created successfully.")


def read_users():
    with duckdb.connect("example.db") as con:
        result = con.sql("SELECT * FROM users").fetchall()
        for row in result:
            print(row)


def update_user(user_id, name=None, age=None, email=None):
    with duckdb.connect("example.db") as con:
        if name:
            con.sql(f"UPDATE users SET name = '{name}' WHERE id = {user_id}")
        if age:
            con.sql(f"UPDATE users SET age = {age} WHERE id = {user_id}")
        if email:
            con.sql(f"UPDATE users SET email = '{email}' WHERE id = {user_id}")
        print(f"User with ID {user_id} updated successfully.")


def delete_user(user_id):
    with duckdb.connect("example.db") as con:
        con.sql(f"DELETE FROM users WHERE id = {user_id}")
        print(f"User with ID {user_id} deleted successfully.")


if __name__ == "__main__":
    create_table()
    create_user(1, "Alice", 30, "alice@example.com")
    create_user(2, "Bob", 25, "bob@example.com")

    print("\nAll users:")
    read_users()

    print("\nUpdating user with ID 1:")
    update_user(1, age=31, email="alice_new@example.com")

    print("\nAll users after update:")
    read_users()

    print("\nDeleting user with ID 2:")
    delete_user(2)

    print("\nAll users after deletion:")
    read_users()
