import time

from flask import g

from bbs import models

# u = models.User(nickname='susan', email='susan@email.com', password='123', timestamp=time.time())
# db.session.add(u)
# db.session.commit()

# cur = connect_db().execute('select nickname, email, password from user order by id desc')
# user = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
# print(user)

users = models.User.query.all()
print(users)