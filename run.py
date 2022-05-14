from flask import Flask


from app.api.views import api_blueprint
from app.posts.views import posts_blueprint

app = Flask(__name__)

app.register_blueprint(api_blueprint)
app.register_blueprint(posts_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5005)