from flask import Flask, render_template
import requests
from post import Post

posts = requests.get("https://api.npoint.io/afe3235f562051ec8034").json()
blog_objects = []
for post in posts:
    blog_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    blog_objects.append(blog_obj)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", post_objects=blog_objects)


# mind the string to int conversion in the decorator routing
@app.route('/post/<int:index>')
def post_page(index):
    requested_blog = None
    for blog in blog_objects:
        if blog.id == index:
            requested_blog = blog
    return render_template('post.html', post=requested_blog)


if __name__ == "__main__":
    app.run(debug=True)
