from app import app, db
from app.models import Chapter, Title
from flask import render_template, redirect, url_for,request
from app.forms import EditChapterForm, EditTitleForm, LoginForm
from flask_login import current_user, login_user, login_required,logout_user
from app.models import User

@app.route('/')
def index():
	chapters = Chapter.query.filter(True).order_by(Chapter.added_time.desc())
	return render_template('index.html',title='Home',chapters=chapters)

@app.route('/titles/<title_id>')
def title(title_id):
	title = Title.query.filter_by(id=title_id).first_or_404()
	chapters = Chapter.query.filter_by(title=title).order_by(Chapter.chapter_number)
	return render_template('title.html',title=title.title_name,chapters=chapters)

@app.route('/chapters/<chapter_id>')
def chapter(chapter_id):
	chapter = Chapter.query.filter_by(id=chapter_id).first_or_404()
	title_name = Title.query.filter_by(id = chapter.title_id)[0]
	return render_template('chapter.html', title=chapter.chapter_name, 
						chapter=chapter,title_name=title_name)

@app.route('/chapters/<chapter_id>/edit', methods=['GET','POST'])
@login_required
def edit_chapter(chapter_id):
	chapter = Chapter.query.filter_by(id=chapter_id).first_or_404()
	form = EditChapterForm()
	if form.validate_on_submit():
		chapter.chapter_name = form.chapter_name.data
		chapter.chapter_number = form.chapter_number.data
		chapter.poster_url = form.poster_url.data
		chapter.read_url = form.read_url.data
		db.session.commit()
		return redirect(url_for('chapter', chapter_id=chapter_id))
	elif request.method == 'GET':
		form.chapter_name.data = chapter.chapter_name
		form.chapter_number.data = chapter.chapter_number
		form.poster_url.data = chapter.poster_url
		form.read_url.data = chapter.read_url
	return render_template('edit_chapter.html', title='edit - '+chapter.chapter_name,
		form=form)

@app.route('/add_title', methods=['GET','POST'])
@login_required
def add_title():
	title=Title()
	form = EditTitleForm()
	if form.validate_on_submit():
		title.title_name = form.title_name.data
		title.description = form.description.data
		db.session.commit()
		return redirect(url_for('title', title_id=title.id))
	return render_template('edit_title.html', title="add title", form=form)

@app.route('/titles/<title_id>/add_chapter', methods=['GET','POST'])
@login_required
def add_chapter(title_id):
	title = Title.query.filter_by(id=title_id).first_or_404()
	chapter = Chapter(title_id=title.id)
	form = EditChapterForm()
	if form.validate_on_submit():
		chapter.chapter_name = form.chapter_name.data
		chapter.poster_url = form.poster_url.data
		chapter.read_url = form.read_url.data
		db.session.add(chapter)
		db.session.commit()
		return redirect(url_for('chapter', chapter_id=chapter.id))
	return render_template('edit_chapter.html', title='add chapter',
		form=form)

@app.route('/chapters/<chapter_id>/delete')
@login_required
def delete_chapter(chapter_id):
	chapter = Chapter.query.filter_by(id=chapter_id).first_or_404()
	db.session.delete(chapter)
	db.session.commit()
	return redirect(url_for('index'))
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			return redirect(url_for('login'))
		login_user(user, remember=False)
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign in', form=form)
