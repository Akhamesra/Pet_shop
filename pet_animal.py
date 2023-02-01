from flask import render_template, Flask,redirect,url_for,request
from form import owner
from db import Pet, DBconnection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey' #CSRF token

db = DBconnection()
try:
    db.create_table('pet_shop3','pet_name','pet_breed','owner')
except Exception as e:
    pass # As Database already exist 


@app.route('/')
def index():
    try:
        pet_shop3 = db.select_result('pet_shop3')
        return render_template('index.html',pet_shop3 = pet_shop3)
    except Exception as e:
        error = "An error has occured while showing result! : " + str(e)
        return render_template('error.html',msg = error)
        

@app.route('/create',methods = ['GET','POST'])
def create():
    try:
        form = owner()
        if request.method == 'POST' and form.validate_on_submit():
            name = form.name.data.capitalize()
            pet_name = form.pet_name.data.capitalize()
            pet_breed = form.pet_breed.data
            db.insert_db('pet_shop3',pet_name,pet_breed,name)
            return  redirect(url_for('index'))
        return render_template('create.html',form = form)
    except Exception as e:
        error = "An error has occured while adding the data! : "+ str(e)
        return render_template('error.html',msg=error)

@app.route('/delete/<int:ids>')
def delete(ids):
    try:
        db.delete_row('pet_shop3',ids)
        return redirect(url_for('index'))
    except Exception as e:
        error = "An error has occured while Deleting the data! : "+ str(e)
        return render_template('error.html',msg=error)

@app.route('/edit/<int:ids>',methods = ['GET', 'POST'])
def edit(ids):
    try : 
        pet_shop_row = db.select_row('pet_shop3',ids)
        form = owner()
        if request.method == 'POST' and form.   validate_on_submit():
            name = form.name.data
            pet_name = form.pet_name.data
            pet_breed = form.pet_breed.data

            db.edit('pet_shop3',pet_name,pet_breed,name,ids)
            return redirect(url_for('index'))   
        return render_template('edit.html',form = form)
    except Exception as e:
        error = "An error has occured while Editing the data! : "+ str(e)
        return render_template('error.html',msg=error)

@app.route('/error/msg')
def error(msg):
    return render_template('error.html', error=msg)

if __name__ == '__main__':
    app.run(debug=True, port = 5500)

