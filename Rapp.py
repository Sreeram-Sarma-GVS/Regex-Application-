from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("teststring")
        regex = request.form.get("Regex")

        try:
            result = re.findall(regex, text)  # Use findall for multiple matches
        except re.error as e:
            result = f"Invalid regex: {e}"

        return render_template("finalresult.html", result=result)
    return render_template("Rhome.html")

@app.route("/validation_email",methods=["GET", "POST"])
def email_validation():
    msg=''
    if request.method == "POST":
        email=request.form.get("email_check")
        regex_code = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
        if email:
            if re.match(regex_code, email):
                msg='Valid email address!'
            else:
                msg='Invalid email address!'
        else:
            msg='Email address nor provided'
    return render_template('validation.html',msg=msg)

if __name__ == '__main__':
    app.run(debug=True)