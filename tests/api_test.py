from run import app


class TestApi:

    def test_app_page_api_status_code(self):
        response = app.test_client().get('/api/posts/', follow_redirects=True)
        assert response.status_code == 200, 'Статус код всех постов неверен'
        assert response.mimetype == 'application/json', 'Получен не json'

    def test_app_page_api_posts_id_status_code(self):
        response = app.test_client().get('/api/posts/1/', follow_redirects=True)
        assert response.status_code == 200, 'Статус код всех постов неверен'
        assert response.mimetype == 'application/json', 'Получен не json'
