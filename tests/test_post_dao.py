import pytest

from app.posts.dao.posts_dao import PostsDAO


class TestPostsDAO:

    @pytest.fixture
    def posts_dao(self):
        return PostsDAO('data/data.json')

    @pytest.fixture
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    @pytest.fixture
    def posts(self, posts_dao):
        return posts_dao.get_posts_all()

    # Все посты
    def test_get_posts_all_check_type(self, posts):
        assert type(posts) == list, 'Все посты должны быть списком'
        for post in posts:
            assert type(post) == dict, 'Каждый пост должен быть словарём'

    def test_get_posts_all_has_keys(self, keys_expected, posts):
        for i in range(len(posts)):
            post = posts[i]
            post_keys = set(post.keys())
            assert post_keys == keys_expected, 'Полученные ключи не верны'

    # Посты по id
    def test_post_by_id_chek_type(self, posts_dao, posts):
        for i in range(len(posts)):
            post = posts_dao.post_by_id(i + 1)
            assert type(post) == dict, 'Каждый пост должен быть словарём'

    def test_post_by_id_has_keys(self, posts_dao, keys_expected, posts):
        for i in range(len(posts)):
            post = posts_dao.post_by_id(i + 1)
            post_keys = set(post.keys())
            assert post_keys == keys_expected, 'Полученные ключи не верны'

    parameters_to_get_by_id = range(1, 9)

    @pytest.mark.parametrize("post_id", parameters_to_get_by_id)
    def test_post_by_id_chek_type_correct_pk(self, posts_dao, post_id):
        post = posts_dao.post_by_id(post_id)
        assert post["pk"] == post_id, 'Номер поста не соответствует загруженному.'

    # Посты по пользователю

    def test_post_by_username_chek_type(self, posts_dao):
        username = 'Leo'
        posts = posts_dao.post_by_username(username)
        assert type(posts) == list, 'Посты должны быть списком'
        assert type(posts[0]) == dict, 'Пост должен быть словарем'

    def test_post_by_username_has_keys(self, posts_dao, keys_expected):
        username = 'leo'
        post = posts_dao.post_by_username(username)[0]
        post_keys = set(post.keys())
        assert post_keys == keys_expected, 'Полученные ключи не верны'

    parameters_to_get_by_user = [
        ('leo', [1, 5]),
        ('johnny', [2, 6]),
        ('zzzzz', [])
    ]

    @pytest.mark.parametrize("username, correct_post_pk", parameters_to_get_by_user)
    def test_post_by_username_chek_correct_postername(self, posts_dao, username, correct_post_pk):
        posts = posts_dao.post_by_username(username)

        post_pk = []
        for post in posts:
            post_pk.append(post['pk'])

        assert post_pk == correct_post_pk, f'Имя постера не соответствует {username}.'

    # Поиск

    def test_search_posts_check_type(self, posts_dao):
        posts = posts_dao.search_posts('a')
        assert type(posts) == list, 'Все посты должны быть списком'
        for post in posts:
            assert type(post) == dict, 'Каждый пост должен быть словарём'

    def test_search_posts_has_keys(self, keys_expected, posts_dao):
        posts = posts_dao.search_posts('a')
        for i in range(len(posts)):
            post = posts[i]
            post_keys = set(post.keys())
            assert post_keys == keys_expected, 'Полученные ключи не верны'

    queryes_posts = [
        ('Ага', [1]),
        ('катер', [8]),
        ('вышел', [2]),
        ('sssss', []),
        ('да', [1, 2, 3, 4, 5, 8])

    ]

    @pytest.mark.parametrize("query, correct_posts", queryes_posts)
    def test_search_posts_chek_correct_answer(self, posts_dao, query, correct_posts):
        posts = posts_dao.search_posts(query)
        posts_filtered = []
        for post in posts:
            posts_filtered.append(post['pk'])

        assert posts_filtered == correct_posts, f'Найденные посты не соответствует {query}.'
