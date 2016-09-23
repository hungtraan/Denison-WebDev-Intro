from flask import Flask, request, render_template

app = Flask(__name__)

# Turn debug on to allow real-time content update on updating (saving) this file
app.config['DEBUG'] = True

@app.route('/')
def home():
	return "<h1>Hey</h1>"

@app.route('/<string>')
def dynamic(string):
	return "<h1>%s</h1>"%string

@app.route('/hi/<name>')
def hello(name):
	return "<p>Hi %s</p>"%name

@app.route('/hello')
def hello2():
	name = request.args.get('name')
	if name is None:
		return "Hello there!"
	
	return "<p>Hello %s</p>"%name

@app.route('/syllabus')
def syllabus():
	return render_template("syllabus.html")

if __name__ == '__main__':
	app.run()