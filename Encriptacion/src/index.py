from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def home ():
    from cryptography.fernet import Fernet

    dato=input()
    key=Fernet.generate_key()
    oCifrado = Fernet(key)
    d_encriptado=oCifrado.encrypt(str.encode(dato))


    return render_template('home.html',d_encriptado)

if __name__ == '__main__':
    app.run(debug=True)
