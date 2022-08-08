from flask import Blueprint, flash, jsonify, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import User, Note
from . import db
import json 
from .static.scripts.time import current_time

views = Blueprint('views', __name__)


@views.route('/notes/', methods=['GET', 'POST'])
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

@views.route('/about/')
@login_required
def about():   
    return render_template("about.html", user=current_user)


@views.route('/help/', methods = ['GET', 'POST'])
def help(): 
    return render_template("help.html", user=current_user)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home(): 
    return render_template("home.html", user = current_user, time = current_time())

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

@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin(): 
    if current_user.get_id() == "1": 
        users = User.query.all()
        return render_template("admin.html", user = current_user, list_users = users)
    else: 
        return """
        <h1 style="text-align: center"> Nu puteti accesa daca nu sunteti admin! </h1>
        """ 
