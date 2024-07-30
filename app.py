from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption and decryption
# You must use this key for both encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encrypt', methods=['POST'])
def encrypt():
    text_to_encrypt = request.form['text']
    encrypted_text = cipher_suite.encrypt(text_to_encrypt.encode()).decode()
    return render_template('index.html', encrypted_text=encrypted_text, decrypted_text='')


@app.route('/decrypt', methods=['POST'])
def decrypt():
    text_to_decrypt = request.form['text']
    decrypted_text = cipher_suite.decrypt(text_to_decrypt.encode()).decode()
    return render_template('index.html', encrypted_text='', decrypted_text=decrypted_text)


if __name__ == '__main__':
    app.run(debug=True)
