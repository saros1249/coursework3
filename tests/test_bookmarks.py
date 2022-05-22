import pytest

from app.posts.dao.bookmarks_dao import BookmarksDAO


class TestBookmarksDAO:

    @pytest.fixture
    def bookmarks_dao(self):
        return BookmarksDAO('data/bookmarks.json')

    @pytest.fixture
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    @pytest.fixture
    def post(self):
        return {
            "poster_name": "larry",
            "poster_avatar": "https://randus.org/avatars/m/81898dbdbdffdb18.png",
            "pic": "https://images.unsplash.com/photo-1494952200529-3ceb822a75e2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80",
            "content": "Утром отправились на катере #Путешествия обследовать ближайшие острова – острова в основном каменные, бесполезные и необитаемые. На обратном пути попали в бурю, и нас чуть не унесло в океан. В течение 10 минут наш катер несся к отмели, а потом мы стали дрейфовать между скал, держась за трос. Наконец погода наладилась и мы смогли совершить обратный путь. Когда уже прибыли домой, я попросил, чтобы на следующий день нам устроили на катере экскурсию по морю. Нас провели по морскому дну от одного острова к другому, показали различные интересные объекты, которые встречаются в этом районе.",
            "views_count": 141,
            "likes_count": 45,
            "pk": 8
        }

    # Все посты
    def test_get_bookmarks_all_check_type(self, bookmarks_dao):
        bookmarks = bookmarks_dao.get_bookmarks_all()
        assert type(bookmarks) == list, 'Все закладки должны быть списком'
        for bookmark in bookmarks:
            assert type(bookmark) == dict, 'Каждая закладка должен быть словарём'

    def test_get_bookmarks_all_keys(self, keys_expected, bookmarks_dao):
        bookmarks = bookmarks_dao.get_bookmarks_all()
        for i in range(len(bookmarks)):
            bookmark = bookmarks[i]
            bookmark_keys = set(bookmark.keys())
            assert bookmark_keys == keys_expected, 'Полученные ключи не верны'

    def test_post_add_to_bookmarks(self, bookmarks_dao, post):
        bookmarks = bookmarks_dao.get_bookmarks_all()
        bookmarks_dao.post_add_to_bookmarks(post)
        bookmarks_added = bookmarks_dao.get_bookmarks_all()
        assert len(bookmarks_added) > len(bookmarks), 'Пост не добавлен'

    def test_post_remove_bookmarks(self, bookmarks_dao, post):
        bookmarks = bookmarks_dao.get_bookmarks_all()
        bookmarks_dao.post_remove_bookmarks(post)
        bookmarks_deleted = bookmarks_dao.get_bookmarks_all()
        assert len(bookmarks_deleted) < len(bookmarks), 'Пост не удалён'
