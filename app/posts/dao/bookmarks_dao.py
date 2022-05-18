# Функции для работы с закладками постов.
import json

class BookmarksDAO:

    def __init__(self, path):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path = path

    def get_bookmarks_all(self):
        """ Загружает данные из файла и возвращает список словарей"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data



    def post_add_to_bookmarks(self, post):
        """Добавляет пост в закладки"""
        bookmarks_added = self.get_bookmarks_all()
        bookmarks_added.append(post)
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(bookmarks_added, file, ensure_ascii=False, indent=2)


    def post_remove_bookmarks(self, post):
        """Удаляет аост из закладок"""
        bookmarks_deleted = self.get_bookmarks_all()
        bookmarks_deleted.remove(post)
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(bookmarks_deleted, file, ensure_ascii=False, indent=2)

