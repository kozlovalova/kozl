from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["post","get"])
def integer():
    massage = ""
    if request.method == 'POST' :
        user =  request.form.get('user')
        password = request.form.get('password')
        massage = massage + user + '' + password  
        return render_template("proba.html", massage == massage)
    
    return render_template ('proba.html', massage = 'Форма готова для принятия данных')

if __name__ == "__main__":
    print("run server")
    app.run()
    