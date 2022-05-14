from flask import Blueprint, jsonify

api_blueprint = Blueprint('api_blueprint', __name__)

@api_blueprint.route('/api/')
def page_api():
    return 'All posts'

@api_blueprint.route('/api/posts/<int:posts_id>/')
def page_api_posts_id(posts_id):
    return jsonify({'content':'One post'})
