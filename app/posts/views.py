from flask import Blueprint, render_template, request, redirect

from config.config import *
from .dao.bookmarks_dao import BookmarksDAO
from .dao.comments_dao import CommentsDAO
from .dao.posts_dao import PostsDAO

posts_dao = PostsDAO(POST_PATH)
comments_dao = CommentsDAO(COMMENT_PATH)
bookmarks_dao = BookmarksDAO(BOOKMARK_PATH)

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")


@posts_blueprint.route('/')
def page_posts_all():
    counter_bookmarks = len(bookmarks_dao.get_bookmarks_all())
    posts_all = posts_dao.get_posts_all()
    try:
        return render_template('index.html', posts=posts_all, counter_bookmarks=counter_bookmarks)
    except:
        return "Не удaлось загрузить посты."


@posts_blueprint.route('/search/')
def page_searh_posts():
        s = request.args.get("s", "")
        if s != "":
            posts_filtered = posts_dao.search_posts(s)
            counter = len(posts_filtered)
        else:
            posts_filtered =[]
            counter = 0
        return render_template('search.html', query=s, posts=posts_filtered, counter=counter)


@posts_blueprint.route('/posts/<int:post_id>/')
def page_one_post(post_id):
    try:
        post = posts_dao.post_by_id(post_id)
        comments = comments_dao.get_comments_by_post_id(post_id)
        comments_counter = len(comments)
        return render_template('post.html', post=post, comments=comments, comments_counter=comments_counter)
    except:
        return "Не удалось загрузить пост."


@posts_blueprint.route('/bookmarks/')
def get_bookmarks_all():
    bookmarks = bookmarks_dao.get_bookmarks_all()
    try:
        return render_template("bookmarks.html", posts=bookmarks)
    except:
        return 'Данные не загружены'


@posts_blueprint.route('/bookmarks/add/<int:post_id>/')
def page_add_to_bookmarks(post_id):
    post = posts_dao.post_by_id(post_id)
    bookmarks_dao.post_add_to_bookmarks(post)
    return redirect("/", code=302)


@posts_blueprint.route('/bookmarks/remove/<int:post_id>/')
def page_remove_bookmarks(post_id):
    post = posts_dao.post_by_id(post_id)
    bookmarks_dao.post_remove_bookmarks(post)
    return redirect("/", code=302)


@posts_blueprint.route('/users/<username>/')
def page_username_post(username):
    posts_username = posts_dao.post_by_username(username)
    tagnames = posts_dao.tag(username)
    try:
        return render_template('user-feed.html', posts=posts_username, tagnames=tagnames)
    except:
        return "Не удлось загрузить посты."


@posts_blueprint.route('/tag/<tagname>')
def page_post_by_tag(tagname):
    post_by_tag = posts_dao.posts_by_tag(tagname)
    try:
        return render_template('tag.html', posts=post_by_tag, tagname=tagname)
    except:
        "Не удлось загрузить посты."
