DEBUG = True

USERNAME = 'root'
PASSWORD = 'Tjfanautico6.'
SERVER = 'localhost'
DB = 'magpy'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True