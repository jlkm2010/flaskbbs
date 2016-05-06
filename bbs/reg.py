from bbs import app
from flask import render_template, flash, redirect, session, url_for, request, g


@app.route('/register', methods=['POST'])
def register():
    print(request.form['username'])
    print(request.form['email'])
    print(request.form['password'])

    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)