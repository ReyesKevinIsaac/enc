from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')

def home ():
    
        
    return render_template('home.html')

@app.route('/enc', methods=['POST'])

def enc():
    from cryptography.fernet import Fernet

    dato=request.form['dato'] ## Dato
    key=Fernet.generate_key() 
    oCifrado = Fernet(key)
    d_encriptado=oCifrado.encrypt(str.encode(dato))  ## Encriptación
        
    # d_desencriptado_b = oCifrado.decrypt(d_encriptado) ## Desencriptación

    return  d_encriptado

if __name__ == '__main__':
    app.run(debug=True)
