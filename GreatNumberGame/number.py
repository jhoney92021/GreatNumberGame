from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'invisible poops'

def startValues():
    session['answer'] = random.randint(1 , 100)
    session['var'] = '' 
    session['color'] = 'yellow'
    print('-------ANSWER---'+ str(session['answer']) +'---ANSWER-----------')



@app.route('/')
def default():
    startValues()
    print('-------ANSWER---'+ str(session['answer']) +'---ANSWER-----------')
    return render_template('index.html', var=session['var'], color=session['color'], restart='')

@app.route('/results', methods=['POST'])
def results():
    print('-------ANSWER---'+ str(session['answer']) +'---ANSWER-----------')
    session['guess'] = request.form['guess']
    return redirect('/wrongAgainBob')

@app.route('/wrongAgainBob')
def bobBarker():
        print('-------ANSWER---'+ str(session['answer']) +'---ANSWER-----------')
        if int(session['guess']) == int(session['answer']):
            session['var'] = session['guess'] + ' Winner!'
            session['color'] = 'green'
            session['restart'] = 'Restart'
            
        if int(session['guess']) < int(session['answer']):
            session['var'] = 'Too Low!'
            session['color'] = 'red'
            session['restart'] = ''

        if int(session['guess']) > int(session['answer']):
            session['var'] = 'Too High!'   
            session['color'] = 'red'
            session['restart'] = ''         
        return render_template('index.html',var=session['var'], color=session['color'], restart=session['restart'])

if __name__=='__main__':
    app.run(debug=True)