from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for
from . import main
from ..models import Comment,User,Pitch
from .. import db,photos
from .forms import UpdateProfile,NewPitch,CommentForm


@main.route('/')
def index():
    pitches =  Pitch.query.all()
    interview_pitch = Pitch.get_pitches_by_category('1')
    pickup_lines = Pitch.get_pitches_by_category('2')
    product_pitch = Pitch.get_pitches_by_category('3')
    promotion_pitch = Pitch.get_pitches_by_category('4')
    if pitches is None:
        return redirect(url_for('new_pitch.html'))
        title = "pitches"
    return render_template("index.html", pitches = pitches, interviews = interview_pitch, pickups = pickup_lines,products = product_pitch,promotions = promotion_pitch )

@main.route('/pitch', methods = ['GET','POST'])
@login_required
def pitch():
    form = NewPitch()
    if form.validate_on_submit():
        pitch = Pitch(category = form.category.data,title = form.title.data,pitch = form.pitch.data,user_id = current_user.id)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
        title = "pitches"
        
    return render_template('new_pitch.html',pitch_form = form)



@main.route('/details/<int:id>')
def details(id):
    pitch = Pitch.get_pitch(id)
    comments = Comment.get_comments(id)
    return render_template('details.html', pitch = pitch, comments = comments)



@main.route('/details/comments/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    title = 'post comment'
    pitch = Pitch.get_pitch(id)
    comments = Comment.get_comments(id)
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment( comment = comment, user_id = current_user.id, pitch_id = id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.details', id = id))

    return render_template('new_comment.html', comment_form=form, title=title,comments=comments , pitch = pitch)

@main.route('/details/<int:id>/upvote', methods=['POST'])
@login_required
def upvote(id):
    pitch = Pitch.get_pitch(id)
    pitch[0].upvotes = pitch[0].upvotes + 1 if pitch[0].upvotes is not None else 1
    db.session.add(pitch[0])
    db.session.commit()
    return redirect(url_for('main.details', id = id))

@main.route('/details/<int:id>/downvote', methods=['POST'])
@login_required
def downvote(id):
    pitch = Pitch.get_pitch(id)
    pitch[0].downvotes = pitch[0].downvotes + 1 if pitch[0].downvotes is not None else 1
    db.session.add(pitch[0])
    db.session.commit()
    return redirect(url_for('main.details', id = id))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))