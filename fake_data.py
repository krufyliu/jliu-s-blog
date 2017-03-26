import random
from hashlib import md5
from datetime import datetime
from faker import Factory
from models import db, User, Post, Tag

fake = Factory.create('zh_CN')

hash = md5()
hash.update('abcd1234')
user = User(fake.user_name(), fake.email())
user.password = hash.hexdigest()
db.session.add(user)
db.session.commit()

tag_one = Tag('Python')
tag_two = Tag('Flask')
tag_three = Tag('SQLAlchemy')
tag_four = Tag('JmilkFan')
tag_list = [tag_one, tag_two, tag_three, tag_four]

for i in xrange(100):
    new_post = Post(fake.name(), fake.text())
    new_post.user = user
    new_post.publish_at = datetime.now()
    new_post.tags = random.sample(tag_list, random.randint(1, 3))
    db.session.add(new_post)
db.session.commit()

