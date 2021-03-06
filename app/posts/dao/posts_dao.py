# Основные функции.
import json

from config.exeption import DataJsonError


class PostsDAO:
    """ Класс позволяет работать со всеми постами"""

    def __init__(self, path):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path = path

    def load_data(self):
        """ Загружает данные из файла и возвращает список словарей"""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except(FileNotFoundError, json.JSONDecodeError):
            raise DataJsonError

    def get_posts_all(self):
        """ Возвращает список всех постов"""
        posts = self.load_data()
        return posts

    def search_posts(self, query):
        """ Поиск постов по ключевому слову, возврвщает список"""
        posts = self.get_posts_all()
        posts_filtered = []
        query_lower = query.lower()
        try:
            for post in posts:
                if query_lower in post['content'].lower():
                    posts_filtered.append(post)
            return posts_filtered
        except(FileNotFoundError, json.JSONDecodeError):
            raise DataJsonError

    def post_by_id(self, post_id):
        """ Возвращает пост по id"""
        posts = self.get_posts_all()
        try:
            for post in posts:
                if post['pk'] == post_id:
                    return post
        except(FileNotFoundError, json.JSONDecodeError):
            raise DataJsonError

    def post_by_username(self, username):
        """ Возвращает список постов по имени"""
        posts = self.get_posts_all()
        posts_username = []
        try:
            for post in posts:
                if username.lower() == post['poster_name'].lower():
                    posts_username.append(post)
            return posts_username
        except(FileNotFoundError, json.JSONDecodeError):
            raise DataJsonError

    def posts_by_tag(self, tagname):
        """ Возвращает список постов по тегу '#tagname'"""
        posts = self.get_posts_all()
        posts_by_tag = []
        tag = '#' + tagname
        try:
            for post in posts:
                if tag in post['content']:
                    posts_by_tag.append(post)
            return posts_by_tag
        except(FileNotFoundError, json.JSONDecodeError):
            raise DataJsonError

    def tag(self, username):
        """ Возвращает список тегов"""
        posts = self.get_posts_all()
        tag_list = []
        try:
            for post in posts:
                if username == post['poster_name']:
                    content_list = post['content'].split()
                    for i in range(len(content_list)):
                        if len(content_list[i]) > 1 and content_list[i][1] != ' ' and '#' in content_list[i]:
                            tag_list.append({post['pk']: content_list[i][1:]})
            return tag_list
        except(FileNotFoundError, json.JSONDecodeError):
            raise DataJsonError
