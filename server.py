from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "kusrabak arse"

# home page with session counter
@app.route('/')
def index():
    if  "count" not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

# from with nuttons that increase count by 2 or reset session count
@app.route('/+2reset', methods=["POST"])
def plus2():
    if request.form["change"] == "add":
        session['count'] += 1
    elif request.form["change"] == "reset":
        session.clear()
    return redirect('/')

#reset session
@app.route("/destroy_session")
def dest_sess():
    session.clear()
    return redirect('/')


if __name__== "__main__":
    app.run(debug=True)