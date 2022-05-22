import logging
import random

from flask import Blueprint, render_template, request, redirect

from config.config import *
from config.exeption import DataJsonError
from .dao.bookmarks_dao import BookmarksDAO
from .dao.comments_dao import CommentsDAO
from .dao.posts_dao import PostsDAO

logger = logging.getLogger('basic')
posts_dao = PostsDAO(POST_PATH)
comments_dao = CommentsDAO(COMMENT_PATH)
bookmarks_dao = BookmarksDAO(BOOKMARK_PATH)

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")


@posts_blueprint.route('/')
def page_posts_all():
    try:
        logger.debug('Запрошены все посты.')
        counter_bookmarks = len(bookmarks_dao.get_bookmarks_all())
        posts_all = posts_dao.get_posts_all()
        if len(posts_all) > 10:
            posts = random.sample(posts_all, 10)
        else:
            posts = posts_all
            logger.debug('Получены все посты.')
        return render_template('index.html', posts=posts, counter_bookmarks=counter_bookmarks)
    except DataJsonError:
        logger.debug('Не удaлось загрузить посты.')
        return 'Не удaлось загрузить посты.'


@posts_blueprint.route('/search/')
def page_searh_posts():
    s = request.args.get("s", "")
    logger.debug(f'Идёт поиск слова {s}.')
    if s != "":
        posts_filtered = posts_dao.search_posts(s)
        counter = len(posts_filtered)
        tagnames = []
        for post in posts_filtered:
            tagnames.extend(posts_dao.tag(post['poster_name']))
    else:
        posts_filtered = []
        counter = 0
    return render_template('search.html', query=s, posts=posts_filtered, counter=counter, tagnames=tagnames)


@posts_blueprint.route('/posts/<int:post_id>/')
def page_one_post(post_id):
    logger.debug(f'Запрошен пост по ID {post_id}.')
    try:
        post = posts_dao.post_by_id(post_id)
        comments = comments_dao.get_comments_by_post_id(post_id)
        comments_counter = len(comments)
        logger.debug(f'Получен пост по ID {post_id}.')
        return render_template('post.html', post=post, comments=comments, comments_counter=comments_counter)
    except DataJsonError:
        logger.debug('Не удалось загрузить пост.')
        return "Не удалось загрузить пост."


@posts_blueprint.route('/bookmarks/')
def get_bookmarks_all():
    logger.debug('Запрошены все закладки.')
    bookmarks = bookmarks_dao.get_bookmarks_all()
    try:
        logger.debug(f'Получены все закладки.')
        return render_template("bookmarks.html", posts=bookmarks)
    except DataJsonError:
        logger.debug('Не удaлось загрузить закладки.')
        return 'Не удaлось загрузить закладки.'


@posts_blueprint.route('/bookmarks/add/<int:post_id>/')
def page_add_to_bookmarks(post_id):
    logger.debug('Добавлна закладка.')
    post = posts_dao.post_by_id(post_id)
    bookmarks_dao.post_add_to_bookmarks(post)
    return redirect("/", code=302)


@posts_blueprint.route('/bookmarks/remove/<int:post_id>/')
def page_remove_bookmarks(post_id):
    logger.debug('Удалена закладка.')
    post = posts_dao.post_by_id(post_id)
    bookmarks_dao.post_remove_bookmarks(post)
    return redirect("/", code=302)


@posts_blueprint.route('/users/<username>/')
def page_username_post(username):
    logger.debug(f'Запрошен пост по имени {username}.')
    posts_username = posts_dao.post_by_username(username)
    tagnames = posts_dao.tag(username)
    try:
        logger.debug(f'Получен пост по имени {username}.')
        return render_template('user-feed.html', posts=posts_username, tagnames=tagnames)
    except DataJsonError:
        logger.debug('Не удaлось загрузить пост.')
        return "Не удлось загрузить пост."


@posts_blueprint.route('/tag/<tagname>')
def page_post_by_tag(tagname):
    logger.debug(f'Запрошены все посты по тэгу {tagname}.')
    post_by_tag = posts_dao.posts_by_tag(tagname)
    try:
        logger.debug(f'Получены все посты по тэгу {tagname}.')
        return render_template('tag.html', posts=post_by_tag, tagname=tagname)
    except DataJsonError:
        logger.debug('Не удaлось загрузить посты.')
        "Не удалось загрузить посты."
