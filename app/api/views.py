import logging

from flask import Blueprint, jsonify

from app.posts.dao.posts_dao import PostsDAO
from config.config import POST_PATH

posts_dao = PostsDAO(POST_PATH)

logger = logging.getLogger('basic')

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts/')
def page_api():
    logger.debug('Запрошены все посты через API.')
    posts = posts_dao.get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:posts_id>/')
def page_api_posts_id(posts_id):
    logger.debug(f'Запрошен пост по ID {post_id} через API.')
    one_post = posts_dao.post_by_id(posts_id)
    return jsonify(one_post)
