from flask import Flask,render_template,request


app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def calculate():
       ones = ''
       twos = ''
       As   =' '
       if request.method == "POST":

         IA_1  = float(request.form.get('one'))
         ones  = (IA_1*30)/100
         IA_2  = float(request.form.get('two'))
         twos  = (IA_2*30)/100
         ASS_1 = float(request.form.get('ass'))
         As    = ASS_1
       return render_template("home.html",ones=ones,twos=twos,As=As)

if __name__=="__main__":
    app.run(debug=True)