from flask import Flask, render_template
#Para crear nuestras rutas del servidor o url
app = Flask(__name__)
PORT = 5000

#Decolorador
#Metodo route recibe un nombre para poder crear una url
@app.route('/', methods = ['GET'])
def Login():
    return render_template('Login.html')

@app.route('/templates/index.html')
def home():
    return render_template('index.html')

@app.route('/templates/pages-profile.html')
def profile():
    return render_template('pages-profile.html')

@app.route('/templates/table-basic.html')
def table():
    return render_template('table-basic.html')

@app.route('/templates/footer.html')
def footer():
    return render_template('footer.html')
    

if __name__ == '__main__':
    #app.debug = True
    app.run(port = PORT)
