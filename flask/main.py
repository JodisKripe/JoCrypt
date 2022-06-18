import JoCryptL
from flask import Flask,redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("hash.html")

@app.route("/hash",methods=['POST','GET'])
def hash():
  if(request.method=='POST'):
    text=request.form['text']
    return JoCryptL.Hash(text)

@app.route("/RevSubs",methods=['POST','GET'])
def RevSubs():
  if(request.method=='POST'):
    text=request.form['text']
    return JoCryptL.ReverseSubstitution(text)

@app.route("/Subs",methods=['POST','GET'])
def Subs():
  if(request.method=='POST'):
    text=request.form['text']
    return JoCryptL.Substitution(text)

@app.route("/railfence",methods=['POST','GET'])
def RailFence():
  if(request.method=='POST'):
    text=request.form['text']
    key=int(request.form['key'])
    return JoCryptL.encryptRailFence(text,key)

@app.route("/railfencedecry",methods=['POST','GET'])
def decryptRailFence():
  if(request.method=='POST'):
    text=request.form['text']
    key=int(request.form['key'])
    return JoCryptL.decryptRailFence(text,key)

@app.route("/caesar",methods=['POST','GET'])
def CaesarEncrypt():
  if(request.method=='POST'):
    text=request.form['text']
    key=int(request.form['key'])
    return JoCryptL.CaesarEncrypt(text,key)

@app.route("/caesardecry",methods=['POST','GET'])
def CaesarDecrypt():
  if(request.method=='POST'):
    text=request.form['text']
    key=int(request.form['key'])
    return JoCryptL.CaesarDecrypt(text,key)    

@app.route("/rev",methods=['POST','GET'])
def ReverseString():
  if(request.method=='POST'):
    text=request.form['text']
    return JoCryptL.ReverseString(text)
  
@app.route("/boxdecry",methods=['POST','GET'])
def BoxCipherDecryption():
  if(request.method=='POST'):
    text=request.form['text']
    return JoCryptL.BoxCipherDecryption(text)

if __name__ == "__main__":
  app.run(port=5000)
