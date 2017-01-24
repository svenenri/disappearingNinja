from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "Shh...Secret"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/ninja")
def ninja():
	check = False
	return render_template("ninja.html", check = check)

@app.route("/ninja/<color>")
def ninjaColor(color):
	check = True
	return render_template("ninja.html", color = color, check = check)

app.run(debug = True)
