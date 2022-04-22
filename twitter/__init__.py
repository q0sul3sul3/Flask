from flask import Flask
from twitter.route import index, login

def create_app():
	app = Flask(__name__)
	app.add_url_rule('/', 'index', index) # 訪問 / 網址，則index方法 # 預設 get方法
	app.add_url_rule('/login', 'login', login, methods=['GET', 'POST']) # 增加 post方法
	app.config["SECRET_KEY"] = '7797bacd231b4753b54ec929d2569695' # RuntimeError: A secret key is required to use CSRF.
	app.debug = True # 或是指令打 python3 manager.py runserver -d
	return app