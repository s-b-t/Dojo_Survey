from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'dr1nkfr0mthefla$k'

@app.route('/')
def displayform():
    return render_template('form.html')

@app.route('/processform', methods = ['POST'])
def processform():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def displayresult():
    return render_template('show.html')

if __name__=="__main__":
    app.run(debug=True)