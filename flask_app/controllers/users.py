
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def home():
    return render_template('home.html', users = User.get_all_users(), one_user=one_user)

@app.route('/add/user')
def add_user():
    return render_template("create.html")
    
@app.route('/new/user', methods=['POST'])
def new_user():
    User.save(request.form)
    print(request.form)
    return redirect('/')


@app.route('/edit/user/<int:user_id>')
def edit_user(user_id):
        return render_template('update.html', one_user = User.get_one(user_id))

@app.route('/update/user', methods=['POST'])
def update_user():
    User.update(request.form)
    print(request.form)
    return redirect('/')

@app.route('/show/<int:user_id>')
def one_user(user_id):
    return render_template('show.html', one_user=User.get_one(user_id))


@app.route('/delete/<int:user_id>')
def delete(user_id):
    User.delete(user_id)
    return redirect('/')



if __name__=='__main__':
    app.run(debug=True)