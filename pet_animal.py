from flask import render_template, Flask,redirect,url_for,request
from form import owner
from db import Pet, DBconnection
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey' #CSRF token
logging.basicConfig(filename="log.log",level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s : %(message)s')

db = DBconnection()
try:
    db.create_table('pet_shop3','pet_name','pet_breed','owner')
    app.logger.info('DataBase Created')
except Exception as e:
    app.logger.info('Database Already created')
    pass # As Database already exist 

#app.logger.info('')
@app.route('/')
def index():
    try:    
        pet_shop3 = db.select_result('pet_shop3')
        #app.logger.info('Showing the table at index page')
        return render_template('index.html',pet_shop3 = pet_shop3)    
    except Exception as e:
        error = "An error has occured while showing result! : " + str(e)
        app.logger.warning(error)
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
            app.logger.info('Details inserted into the table.')
            return  redirect(url_for('index'))
        app.logger.info('Form not validated')
        return render_template('create.html',form = form)
    except Exception as e:
        error = "An error has occured while adding the data! : "+ str(e)
        app.logger.exception(error)
        return render_template('error.html',msg=error)

@app.route('/delete/<int:ids>')
def delete(ids):
    try:
        db.delete_row('pet_shop3',ids)
        app.logger.info(f'Row Deleted with id = {ids}')
        return redirect(url_for('index'))
    except Exception as e:
        error = "An error has occured while Deleting the data! : "+ str(e)
        app.logger.exception(error)
        return render_template('error.html',msg=error)

@app.route('/edit/<int:ids>',methods = ['GET', 'POST'])
def edit(ids):
    try : 
        pet_shop_row = db.select_row('pet_shop3',ids)
        form = owner()
        if request.method == 'POST' and form.validate_on_submit():
            name = form.name.data
            pet_name = form.pet_name.data
            pet_breed = form.pet_breed.data
            db.edit('pet_shop3',pet_name,pet_breed,name,ids)
            app.logger.info('Data edited')
            return redirect(url_for('index'))  
        app.logger.info('Edit form not validated')
        return render_template('edit.html',form = form)
    except Exception as e:
        error = "An error has occured while Editing the data! : "+ str(e)
        app.logger.exception(error)
        return render_template('error.html',msg=error)

@app.route('/error/msg')
def error(msg):
    return render_template('error.html', error=msg)

if __name__ == '__main__':
    app.run(debug=True, port = 5200)

