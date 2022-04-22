from flask_script import Manager
from twitter import create_app
# must install flask_script --> pip install flask_script

app = create_app()
manager = Manager(app)

if __name__ == "__main__":
	manager.run()