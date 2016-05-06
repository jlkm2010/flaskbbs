import time

from flask.ext.login import current_user

from bbs import app, models, db
from flask import render_template, flash, redirect, session, url_for, request, g


@app.route('/post/save', methods=['POST'])
def save_post():
    post = models.Post(title=request.form['title'], body=request.form['content'], user_id=current_user.id, timestamp=time.time())
    db.session.add(post)
    db.session.commit()
    flash('发布成功~')
    return redirect(url_for('index'))


@app.route('/detail', methods=['GET'])
def post_detail():
    post_id = request.args.get('post_id')
    post = models.Post.query.get(post_id)
    user = models.User.query.get(post.user_id)
    replys = models.Reply.query.filter_by(post_id=post_id).all()
    newReplys = []
    for r in replys:
        user = models.User.query.get(r.user_id)
        newReplys.append({'reply': r, 'user': user})
    return render_template("detail.html", post=post, user=user, replys=newReplys)


@app.route('/reply', methods=['POST'])
def reply():
    reply = models.Reply(content=request.form['content'], post_id=request.form['post_id'],
                         user_id=current_user.id, timestamp=time.time())
    db.session.add(reply)
    db.session.commit()
    flash('发表成功~')
    return redirect(url_for('post_detail', post_id=request.form['post_id']))


@app.route('/delete', methods=['GET'])
def delete():
    post_id = request.args.get('post_id')
    post = models.Post.query.get(post_id)
    replys = models.Reply.query.filter_by(post_id=post_id).all()
    for reply in replys:
        db.session.delete(reply)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('user_posts', user_id=current_user.id))