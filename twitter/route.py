from flask import render_template, redirect
from twitter.forms import LoginForm

def index():
	name = {'username': 'root'}
	posts = [
		{
			'author': {'username': 'root'}, 
			'body': "Hi, I'm root", 
		}, 
		{
			'author': {'username': 'root'}, 
			'body': "Hi, I'm root", 
		},
		{
			'author': {'username': 'root'}, 
			'body': "Hi, I'm root", 
		}
	]
	return render_template('index.html', name=name, posts=posts)

def login():
	form = LoginForm(csrf_enabled=False) # csrf_enabled=False
	if form.validate_on_submit(): # 點擊submit則跳轉到index.html
		msg = "username={}, password={},remember_me{}".format(
			form.username.data, form.password.data, form.remember_me.data
			)
		print(msg)
		return redirect('/') # redirect() 內建方法
	# if request.method == 'POST':
 #        return redirect('/')

	return render_template('login.html', title="Sign In", form=form) # title 網頁標題