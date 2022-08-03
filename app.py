
from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

import os


app = Flask(__name__)
 


# Settings for migrations

# adding configuration for using a sqlite database
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'database.db')

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)


# Models
class Profile(db.Model):
	# Id : Field which stores unique id for every row in
	# database table.
	# first_name: Used to store the first name if the user
	# last_name: Used to store last name of the user
	# Age: Used to store the age of the user
	id = db.Column(db.Integer, primary_key=True)
	tanggal = db.Column(db.String(20), unique=False, nullable=False)
	keterangan = db.Column(db.String(20), unique=False, nullable=False)
	debit = db.Column(db.Integer, nullable=False)
	kredit = db.Column(db.Integer, nullable=False)



@app.route('/')
def index():
    profiles = Profile.query.all()
    return render_template('index.html', profiles=profiles)

@app.route('/form')
def faiz():
    return render_template('form.html')

@app.route('/upload', methods=["POST"])
def profile():
     if request.method == 'POST':
        tanggal = request.form['tanggal']
        keterangan = request.form['keterangan']
        kredit = request.form['kredit'] 
        debit = request.form['debit']
        if tanggal != '' and keterangan != '' and debit != '' and kredit !='':
            p = Profile(tanggal=tanggal, kredit=kredit, debit=debit, keterangan=keterangan)
            db.session.add(p)
            db.session.commit()
            return redirect('/')
        else:
            return redirect('/')
    
@app.route('/delete/<int:id>')
def erase(id):
    data = Profile.query.get(id)
    db.session.delete(data)
    db.session.commit() 
    return redirect('/')

@app.route('/<int:id>/edit')
def edit(id):
    profiles = Profile.query.get(id)
    return render_template('editprofile.html', profiles=profiles,id=id)

@app.route('/<int:id>/update/', methods=['POST'])
def update_profile(id):
     if request.method == 'POST':
         profile = Profile.query.get(id)
         profile.tanggal = request.form["tanggal"]
         profile.keterangan = request.form['keterangan'] 
         profile.debit = request.form['debit']
         profile.kredit = request.form['kredit']
         db.session.add(profile)
         db.session.commit()
         return redirect('/')




