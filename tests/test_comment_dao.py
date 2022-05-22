import pytest

from app.posts.dao.comments_dao import CommentsDAO


class TestCommentsDAO:

    @pytest.fixture
    def comments_dao(self):
        return CommentsDAO('data/comments.json')

    @pytest.fixture
    def keys_expected(self):
        return {"post_id", "commenter_name", "comment", "pk"}

    @pytest.fixture
    def comments(self, comments_dao):
        return comments_dao.load_data()

    # Комментарии по id пользователя
    def get_comments_by_post_id_chek_type(self, comments_dao, comments):
        for i in range(len(comments)):
            comment = comments_dao.get_comments_by_post_id(i + 1)
            assert type(comment) == dict, 'Каждый комментарий должен быть словарём'

    def test_get_comments_by_post_id_has_keys(self, comments_dao, keys_expected):
        comments = comments_dao.get_comments_by_post_id(4)
        for comment in comments:
            comment_keys = set(comment.keys())
            assert comment_keys == keys_expected, 'Полученные ключи не верны'

    parameters_to_get_comments_by_id = range(1, 9)

    @pytest.mark.parametrize("post_id", parameters_to_get_comments_by_id)
    def test_get_comments_by_post_id_chek_type_correct_post_id(self, comments_dao, post_id):
        comments = comments_dao.get_comments_by_post_id(post_id)
        for comment in comments:
            assert comment["post_id"] == post_id, 'Номер поста не соответствует загруженному.'
