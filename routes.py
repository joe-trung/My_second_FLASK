from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Task
import forms
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html',tasks=tasks)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('Task added to the database')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

#
# {{url_for('edit, task_id=task_id) }}
# {{url_for('delete, task_id=task_id) }}