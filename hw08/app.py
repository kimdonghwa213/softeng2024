from flask import Flask, render_template
import pandas as pd
App = Flask(__name__)

@App.route('/')
def index():
    return render_template('index.html',title='Home')

@App.route('/career')
def career():
    return render_template('career.html',title='Career')

@App.route('/about_me')
def about_me():
    return render_template('about_me.html',title='About Me')

@App.route('/blog')
def blog_list():
    df = pd.read_csv('blog.csv')
    post_list = []
    for i, row in df.iterrows():
        post_list.append({
            "title": row["title"],
            "content": row["content"]
        })
    print(post_list)
    return render_template('blog.html', title="blog post", posts=post_list)
App.run(debug=True)