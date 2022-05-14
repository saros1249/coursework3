import pytest

from app.posts.dao.posts_dao import PostsDAO

class TestPostsDAO:

    @pytest.fixture
    def posts_dao(self):
        return PostsDAO('data/data.json')


    def test_get_posts_all_check_type(self, posts_dao):
        posts = posts_dao.get_posts_all()
        assert type(posts) == list, 'Все посты должны быть списком'
        assert type(posts[0]) == dict, 'Каждый пост должен быть словарём'

    def test_get_posts_all_has_keys(self, posts_dao):
        posts = posts_dao.get_posts_all()
        for i in range(len(posts)):
            first_post = posts[i]
            keys_expected = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
            first_post_keys = set(first_post.keys())
            assert first_post_keys == keys_expected, 'Полученные ключи не верны'



