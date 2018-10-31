from flask import Flask, render_template, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

def verify_email(email):
    if email != '':
        at_sign = 0
        period = 0
        for char in email:
            if char == '@':
                atsign += 1
            elif char == '.':
                period += 1
        if ((len(email) < 3 or len(email) > 20) or (at_sign != 1) or (period != 1) or (" " in email)):
            return False
        else:
            return True
    else:
        return True

@app.route('/index', methods=['POST'])
def sign_up():
    username = request.form['username']
    password = request.form['password']
    verify_pass = request.form['ver_pass']
    email = request.form['email']
    Error = False
    error = {
        'user' : "",
        'pass':"",
        'match':"",
        'email':""
    }

    if (username == "" or " " in username or len(username) < 3 or len(username) > 20):
        error['user'] = "That is not a valid username."
        Error = True
        pass
    else:
        pass

    if (password == "" or " " in password or len(password) < 3 or len(password) > 20):
        error['pass'] = "That is not a valid password."
        Error = True
        pass
    else:
        pass

    if (verify_pass != password or verify_pass == ""):
        error['match'] = "Passwords do not match."
        Error = True
        pass
    else:
        pass 

    if (verify_email(email) != True):
        error['email'] = "That is not a valid email."
        Error = True
        pass
    else:
        pass

    if (Error):
        return render_template('/index.html', username = username, error = error)
    else:
        return render_template('/welcome.html', username = username, email = email)

@app.route('/')

def index():
    compound_error = request.args.get('error')
    return render_template('index.html', error=compound_error and cgi.escape(compound_error, quote=True))

app.run()