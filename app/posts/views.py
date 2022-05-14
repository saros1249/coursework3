from flask import Blueprint, render_template, request

from config.config import POST_PATH
from .dao.posts_dao import PostsDAO

posts_dao = PostsDAO(POST_PATH)
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")


@posts_blueprint.route('/')
def page_posts_all():
    posts_all = posts_dao.get_posts_all()
    return render_template('index.html', posts=posts_all)


@posts_blueprint.route('/search/')
def page_searh_posts():
    s = request.args.get('s')
    posts_filtered = posts_dao.search_posts(s)
    counter = len(posts_filtered)
    return render_template('search.html', s=s, posts=posts_filtered, counter=counter)


@posts_blueprint.route('/posts/<int:post_id>/')
def page_one_post(post_id):
    return posts_dao.post_by_id(post_id)


@posts_blueprint.route('/users/<username>/')
def page_username_post(username):
    return posts_dao.post_by_username(username)
