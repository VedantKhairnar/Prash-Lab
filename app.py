from flask import Flask, render_template, redirect, request


app = Flask(__name__,static_url_path="/templates/static/css/style.css",static_folder= "templates/static/css/style.css")






@app.route('/Home')
def HomePage():
    return render_template('Home.html')
    

@app.route('/Research')
def Research():
	return render template('Research.html')

@app.route('/labmembers')
def Labmembers():
	return render_template('labmembers.html')
	
@app.route('/Publicatin')
def Publication():
	return render_template('Publication.html')
	
@app.route('/contect')
def contect():
	return render_template('contect.html')

if __name__ == '__main__':
	app.debub = True
