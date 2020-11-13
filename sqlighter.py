import sqlite3

class SQLighter:
    sqlite3.connect(":memory:", check_same_thread = False)

    def __init__(self, base):

        """Подключаемся к БД и сохраняем курсор соединения"""
        sqlite3.connect(":memory:", check_same_thread = False)
        self.connection = sqlite3.connect('base.db', check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status = True):
        """"Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `people` WHERE `status` = ?", (status,)).fetchall()

    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `people` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, username, first_name, last_name, status=True):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `people` (`user_id`,`status`,`username`, `first_name`,`last_name`)"
                                       "VALUES(?,?,?,?,?)", (user_id, status, username, first_name, last_name))

    def update_subscription(self, user_id, last_name, first_name, username, status):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `people` SET status = ? and `username` = ? and `first_name` = ? and "
                                       "`last_name` = ? WHERE `user_id` = ? ",(status, user_id, username, first_name,
                                                                               last_name))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()