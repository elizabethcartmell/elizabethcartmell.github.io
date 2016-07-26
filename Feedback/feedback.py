from flask import Flask
from flask import render_template
from flask import request
import unicodecsv
import csv

app = Flask("myApp")


@app.route("/")
def enter():
	return render_template("index.html")

@app.route("/question.html",)
def question():
	return render_template('question.html')

@app.route("/question", methods=['POST'])
def save_data():

	form_data = request.form

	question1 = form_data['question1']
	question2 = form_data['question2']
	question3 = form_data['question3']
	question4 = form_data['question4']
	question5 = form_data['question5']
	question6 = form_data['question6']

	with open("results.csv", mode="a") as csvfile:
		fieldnames = ['question1', 'question2', 'question3', 'question4', 'question5', 'question6']
		writer = unicodecsv.DictWriter(csvfile,fieldnames=fieldnames)
		writer.writerow({'question1': question1, 'question2':question2, 'question3':question3, 'question4':question4, 'question5':question5, 'question6':question6, })

	return render_template('thankyou.html')
print "All Ok"


app.run(debug=True)