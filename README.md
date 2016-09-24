# Intro to Web Development

Instructor: Hung Tran (tran_h3@denison.edu)

## 2016/09/24 (Saturday) class in folder `09-22`:
- Read HTML Basics: http://marksheet.io/html-basics.html
- Practice 10+ problems on basic HTML: https://www.codecademy.com/courses/web-beginner-en-HZA3b
- Offline practice material: [Google Drive link](https://drive.google.com/drive/folders/0B9Afgj6vrmnzUjFOcmdXM2JVUE0?usp=sharing) (learn by seeing how elements look like, see how it was built with Inspector tool in the browswer or look at the source HTML, then try to **reproduce it**)

## 2016/09/22 (Thursday) class in folder `09-22`:

You can download this whole folder:
- `test_server.py` is the demo server from class
	- Run it by opening up your terminal and run it with Python 
	```python test_server.py```
	- Open web browser and go to: `localhost:5000` or `127.0.0.1:5000`
	- You can visit different paths we've defined like `/your_name`, `hi/your_name`, `hello?name=your_name`, `/syllabus`

- the `templates` folders has a `syllabus.html` file, which is the html document that got render when we go to `localhost:5000/syllabus` 
	- Try changing some basic HTML on there and refresh the page

- If you want make your computer become a real "web server", use `ngrok`
	- In terminal: ```./ngrok http 5000```, this opens up port 5000 on your localhost and allows http connections into this port (which is current served by our server)
	- Copy the URL provided by `ngrok` and paste that into your browser to see
	![screenshot](https://camo.githubusercontent.com/98b1ce97a5ab810a555c09d56cf3a1b8d152bcf1/68747470733a2f2f6d6f6e6f736e61702e636f6d2f66696c652f484a636b4847536f724f756f45716d366b424e4662374d5157644e6548662e706e67)

- Deployment to Heroku:
	- Create your own Heroku.com account and follow [this tutorial](https://devcenter.heroku.com/articles/git)

##### Resources:
- Client & server: https://www.youtube.com/watch?v=gE5WUbmb6Cc
- IP: https://www.youtube.com/watch?v=loNXwtH5ckM
- DNS concept: https://www.youtube.com/watch?v=72snZctFFtA
- DNS hierarchy: https://www.youtube.com/watch?v=wFOiAJNGoMQ
- DNS visualized: https://www.youtube.com/watch?v=2ZUxoi7YNgs
-HTTP, GET and POST: https://www.youtube.com/watch?v=K7h1PzqNgOs
- CRUD: https://youtu.be/NEiyC6bt8_s?t=16s
- Review of creating a "Hello world" Flask app: https://www.youtube.com/watch?v=bzX_auqvePs
