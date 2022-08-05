from flask import Blueprint, flash, jsonify, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json 


views = Blueprint('views', __name__)


@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():   
    if request.method == 'POST': 
        note = request.form.get('note')

        if(len(note) < 1): 
            flash('Notita este prea scurta!', category='error')
        else: 
            new_note = Note(data=note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Notita a fost adaugata!', category='success')
    return render_template("notes.html", user=current_user)

@views.route('/about')
@login_required
def about():   
    return render_template("about.html", user=current_user)


@views.route('/help/', methods = ['GET', 'POST'])
def help(): 
    return render_template("help.html", user=current_user)

@views.route('/')
@login_required
def home(): 
    return render_template("home.html", user = current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note(): 
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)

    if note: 
        if note.user_id == current_user.id: 
            db.session.delete(note) 
            db.session.commit()
    
    return jsonify({})

@views.route('/', methods = ['GET', 'POST'])
def default(): 
    return render_template("login.html", user = current_user)
 