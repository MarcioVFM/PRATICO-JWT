from sqlite3 import Connection

class OrdersRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def register_order(self, description: str, date: str, user_id: int) -> None:
        cursor = self.__conn
        cursor.execute(
            '''
            INSERT INTO pedidos
                (description, date, id_usuario)
            VALUES 
                (?, ?, ?)
            ''', (description, date, user_id)
        )
        cursor.commit()

    def list_user_orders(self, user_id: int) -> tuple[int, str, str, int]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT *
            FROM pedidos
            WHERE id_usuario = ?
            ''', (user_id,)
        )
        order = cursor.fetchall()
        return order
