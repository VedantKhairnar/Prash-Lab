from flask import Flask, render_template, redirect, request


app = Flask(__name__)



@app.route('/')
def redirection():
    return redirect('/Home')

@app.route('/Home')
def HomePage():
    return render_template('Home.html')
    

@app.route('/Research')
def Research():
	return render_template('Research.html')

@app.route('/Labmembers')
def Labmembers():
	return render_template('labmembers.html')
	
@app.route('/Publication')
def Publication():
	return render_template('Publication.html')
	
@app.route('/contect')
def contect():
	return render_template('contect.html')

if __name__ == '__main__':
	app.debug = True
	app.run()
