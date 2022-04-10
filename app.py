# from ast import Num
from random import randint, choice, sample
# import pdb
from surveys import satisfaction_survey
from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WhatATime'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

responses = []

count = 0

survey_length = len(satisfaction_survey.questions)

@app.route('/')
def show_survey():
    global count
    if count == 0:
        return render_template('start.html', survey=satisfaction_survey)
    else:
        return render_template('thanks.html', survey=satisfaction_survey, res=responses, zip=zip)

@app.route('/question/<num>')
def show_question(num):
    new_num = int(num)
    if new_num == count and survey_length > count:
        new_num = int(num)
        return render_template('questions.html', survey=satisfaction_survey, count=new_num)
    elif count > survey_length and count != 0:
        return f'<h1>Thank you for taking the Survey!</h1>'
    elif count < new_num and count < survey_length:
        return f'<h1>You do not have access to that question anymore<h1>'
    else:
        return redirect('/')
        

@app.route('/question_next')
def setup_next_question():
    answer = request.args['answer']
    global count
    count = count + 1
    responses.append(answer)
    return redirect(f'/question/{count}')