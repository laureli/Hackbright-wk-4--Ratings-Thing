from flask import Flask, render_template, redirect, g, url_for, request

import model

app = Flask(__name__)


# @app.route("/", methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['name'] != app.config['']

@app.route('/login', methods=['GET', 'POST'])
def login():
    model.connect_to_db()
    error = None
    if request.method == 'GET':
        name = request.args.get("name")
        password = request.args.get("password")
        user = model.login(name, password)
        print user
        if user == "NO":
            return render_template('login.html', error=error)
        if request.args.get('name') != user.name:
            error = 'Invalid username'
        elif request.args.get('password') != user.password:
            error = 'Invalid password'
        else:
            # session['logged in'] = True
            # flash('You are now logged in.')
            return redirect("/get_user?id="+str(user.idnum))
    return render_template('login.html', error=error)


@app.route("/get_user")
def show_user():
    model.connect_to_db()
    idnum = request.args.get("id")
    u = model.get_user(idnum)
    return render_template("show_user.html", user=u)


if __name__ == "__main__":
    app.run(debug=True)
