from sqlite3 import Connection

class UserRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_user(self, username: str, password: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
        INSERT INTO usuario
            (username, password)
        VALUES
            (?, ?) 
        ''', (username, password)
        )
        self.__conn.commit()
    
    def find_user_by_username(self, username: int) -> tuple[int, str, str]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT id, username, password
            FROM usuario
            WHERE username = ?
            ''', (username,)
        )
        user = cursor.fetchone()
        return user


