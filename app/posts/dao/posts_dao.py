import json

class PostsDAO:

    """ Класс позволяет работать со всеми постами"""

    def __init__(self, path):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path = path

    def load_data(self):
        """ Загружает данные из файла и возвращает список словарей"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_posts_all(self):
        """ Возвращает список всех постов"""
        posts = self.load_data()
        return posts

    def search_posts(self, query):
        """ Поиск постов по ключевому слову, возврвщает список"""
        posts = self.get_posts_all()
        posts_filtered = []
        query_lower = query.lower()
        for post in posts:
            if query_lower in post["content"].lower():
                posts_filtered.append(post)
        return posts_filtered

    def post_by_id(self, post_id):
        """ Возвращает пост по id"""
        posts = self.get_posts_all()
        for post in posts:
            if post['pk'] == post_id:
                return post


    def post_by_username(self, username):
        """ Возвращает список постов по имени"""
        posts = self.get_posts_all()
        posts_username = []
        for post in posts:
            if post['poster_name'] == username:
                posts_username.append(post)
                return posts_username
