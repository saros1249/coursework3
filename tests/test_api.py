import pytest
from app.posts.dao.posts_dao import PostsDAO

class TestApi:

    @pytest.fixture
    def posts_dao(self):
        return PostsDAO('data/data.json')

    @pytest.fixture
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    @pytest.fixture
    def posts(self, posts_dao):
        return posts_dao.get_posts_all()

    def test_page_api_check_type(self, posts):
        assert type(posts) == list, 'Все посты должны быть списком'
        for post in posts:
            assert type(post) == dict, 'Каждый пост должен быть словарём'

    def test_get_posts_all_has_keys(self, keys_expected, posts):
        for i in range(len(posts)):
            post = posts[i]
            post_keys = set(post.keys())
            assert post_keys == keys_expected, 'Полученные ключи не верны'

        def test_post_by_id_chek_type(self, posts_dao, posts):
            for i in range(len(posts)):
                post = posts_dao.post_by_id(i + 1)
                assert type(post) == dict, 'Каждый пост должен быть словарём'

        def test_post_by_id_has_keys(self, posts_dao, keys_expected, posts):
            for i in range(len(posts)):
                post = posts_dao.post_by_id(i + 1)
                post_keys = set(post.keys())
                assert post_keys == keys_expected, 'Полученные ключи не верны'