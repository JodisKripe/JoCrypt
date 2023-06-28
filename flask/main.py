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
    data = {"result": JoCryptL.Hash(text)}
    return render_template("result.html", data=data)

@app.route("/RevSubs",methods=['POST','GET'])
def RevSubs():
  if(request.method=='POST'):
    text=request.form['text']
    data = {"result": JoCryptL.ReverseSubstitution(text)}
    return render_template("result.html", data=data)

@app.route("/Subs",methods=['POST','GET'])
def Subs():
  if(request.method=='POST'):
    text=request.form['text']
    data = {"result": JoCryptL.SubstitutionCipher(text)}
    return render_template("result.html", data=data)

@app.route("/railfence",methods=['POST','GET'])
def RailFence():
  if(request.method=='POST'):
    text=request.form['text']
    key=int(request.form['key'])
    data = {"result": JoCryptL.encryptRailFence(text,key)}
    return render_template("result.html", data=data)

@app.route("/railfencedecry",methods=['POST','GET'])
def decryptRailFence():
  if(request.method=='POST'):
    text=request.form['text']
    key=int(request.form['key'])
    data = {"result": JoCryptL.decryptRailFence(text,key)}
    return render_template("result.html", data=data)

@app.route("/caesar",methods=['POST','GET'])
def CaesarEncrypt():
  if(request.method=='POST'):
    text=request.form['text']
    key=int(request.form['key'])
    data = {"result": JoCryptL.CaesarEncrypt(text,key)}
    return render_template("result.html", data=data)

@app.route("/caesardecry",methods=['POST','GET'])
def CaesarDecrypt():
  if(request.method=='POST'):
    text=request.form['text']
    key=int(request.form['key'])
    data = {"result": JoCryptL.CaesarDecrypt(text,key)}
    return render_template("result.html", data=data)    

@app.route("/rev",methods=['POST','GET'])
def ReverseString():
  if(request.method=='POST'):
    text=request.form['text']
    data = {"result": JoCryptL.ReverseString(text)}
    return render_template("result.html", data=data)

@app.route("/box",methods=['POST','GET'])
def BoxCipher():
  if(request.method=='POST'):
    text=request.form['text']
    data = {"result": JoCryptL.BoxCipher(text)}
    return render_template("result.html", data=data)

@app.route("/boxdecry",methods=['POST','GET'])
def BoxCipherDecryption():
  if(request.method=='POST'):
    text=request.form['text']
    data = {"result": JoCryptL.BoxCipherDecryption(text)}
    return render_template("result.html", data=data)

@app.route("/hashcli",methods=['POST','GET'])
def hashcli():
  if(request.method=='POST'):
    text=request.form['text']
    return JoCryptL.Hash(text)

@app.route("/RevSubscli",methods=['POST','GET'])
def RevSubscli():
  if(request.method=='POST'):
    text=request.form['text']
    return JoCryptL.ReverseSubstitution(text)

@app.route("/Subscli",methods=['POST','GET'])
def Subscli():
  if(request.method=='POST'):
    text=request.form['text']
    return JoCryptL.Substitution(text)

@app.route("/railfencecli",methods=['POST','GET'])
def RailFencecli():
  if(request.method=='POST'):
    text=request.form['text']
    key=int(request.form['key'])
    return JoCryptL.encryptRailFence(text,key)

@app.route("/railfencedecrycli",methods=['POST','GET'])
def decryptRailFencecli():
  if(request.method=='POST'):
    text=request.form['text']
    key=int(request.form['key'])
    return JoCryptL.decryptRailFence(text,key)

@app.route("/caesarcli",methods=['POST','GET'])
def CaesarEncryptcli():
  if(request.method=='POST'):
    text=request.form['text']
    key=int(request.form['key'])
    return JoCryptL.CaesarEncrypt(text,key)

@app.route("/caesardecrycli",methods=['POST','GET'])
def CaesarDecryptcli():
  if(request.method=='POST'):
    text=request.form['text']
    key=int(request.form['key'])
    return JoCryptL.CaesarDecrypt(text,key)    

@app.route("/revcli",methods=['POST','GET'])
def ReverseStringcli():
  if(request.method=='POST'):
    text=request.form['text']
    return JoCryptL.ReverseString(text)

@app.route("/boxcli",methods=['POST','GET'])
def BoxCiphercli():
  if(request.method=='POST'):
    text=request.form['text']
    return JoCryptL.BoxCipher(text)

@app.route("/boxdecrycli",methods=['POST','GET'])
def BoxCipherDecryptioncli():
  if(request.method=='POST'):
    text=request.form['text']
    return JoCryptL.BoxCipherDecryption(text)


if __name__ == "__main__":
  app.run(host='0.0.0.0')
