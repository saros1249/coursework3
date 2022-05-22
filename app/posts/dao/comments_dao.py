# Функции для работы с комментариями
import json

from config.exeption import DataJsonError


class CommentsDAO:

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

    def get_comments_by_post_id(self, post_id):
        """ Возвращает список комментариев по id поста"""
        comments = self.load_data()
        comments_filtered = []
        try:
            for comment in comments:
                if comment["post_id"] == post_id:
                    comments_filtered.append(comment)
            return comments_filtered
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataJsonError
