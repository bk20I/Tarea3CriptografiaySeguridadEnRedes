from flask import Flask, render_template
from base64 import b64encode
import hashlib
from Crypto.Util.Padding import pad


'''
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                              protection="scryptAndAES128-CBC")
file_out = open("rsa_key.bin", "wb")
file_out.write(encrypted_key)
file_out.close()
print(key.publickey().export_key())
'''

data =  input('Ingrese Dato: ')
hashSha256 = hashlib.sha256()
hashSha256.update(data.encode('utf-8'))
print(hashSha256.hexdigest())
dataStringAscii = str(hashSha256.hexdigest())
print (dataStringAscii)


app = Flask(__name__)
@app.route('/',methods=['GET'])
def index():
    return render_template('main.html',resultado = dataStringAscii)

