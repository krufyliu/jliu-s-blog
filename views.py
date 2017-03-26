from flask import render_template, request
from sqlalchemy import func
from main import app
from models import db, Post, Comment, Tag, posts_tags
from forms import CommentForm

def sidebar_data():
    recent_posts = db.session.query(Post).order_by(Post.publish_at.desc()).limit(5).all()
    top_tags = db.session.query(
            Tag, func.count(posts_tags.c.post_id).label('total')
        ).join(
            posts_tags
        ).group_by(Tag).order_by('total desc').limit(5).all()
    return recent_posts, top_tags

@app.route('/')
def home():
    page = int(request.args.get('page', 1))
    posts = Post.query.order_by(
        Post.publish_at.desc()
    ).paginate(page, 10)
    recent_posts, top_tags = sidebar_data()
    return render_template('home.html',
                           posts=posts,
                           recent_posts=recent_posts,
                           top_tags=top_tags)

@app.route('/posts/<int:post_id>', endpoint='posts.show')
def show(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    recent_posts, top_tags = sidebar_data()
    return render_template('posts/show.html', **locals())

@app.route('/posts/<int:post_id>/comments', methods=['POST'], endpoint='comments.create')
def create(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(form.email.data, form.text.data)
        new_comment.post = post
        db.session.add(new_comment)
        db.session.commit()
    recent_posts, top_tags = sidebar_data()
    return render_template('posts/show.html', **locals())