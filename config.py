import os

CSRF_ENABLED = False
SECRET_KEY = 'you-will-never-guess'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'bbs.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
