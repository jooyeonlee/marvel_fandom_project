from flask_login.utils import login_required
from app.forms import NewCharacterForm
from flask import Blueprint, render_template, request, url_for, flash, redirect
from app.models import db, Charactor, FavoriteCharactor
from flask_login import current_user, login_required

character = Blueprint('character', __name__, template_folder='marvel_templates')

@character.route('/addcharacter', methods=['GET', 'POST'])
@login_required
def addcharacter():
    form = NewCharacterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            newhero = Charactor(name=form.name.data, description=form.description.data, comics_appeared_in=form.comics.data, super_power=form.superpower.data)
            db.session.add(newhero)
            db.session.commit()
        else:
            print('fail')
        return redirect(url_for('home'))
    return render_template('addcharacter.html', form=form)

@character.route('/character', methods=['GET'])
def characterlist():
    herolist = [hero.to_dict() for hero in Charactor.query.all()]
    favlist = [fav.character_id for fav in FavoriteCharactor.query.filter(FavoriteCharactor.user_id==current_user.id).all()]
    return render_template('character.html', herolist=herolist, favlist=favlist)

@character.route('/character/add/<character_id>')
@login_required
def addfavorite(character_id):
    hero = Charactor.query.filter_by(id=character_id).first()
    hero.user.append(current_user)
    db.session.commit()
    return redirect(url_for('character.characterlist'))

@character.route('/character/delete/<character_id>')
@login_required
def deletefavorite(character_id):
    hero = Charactor.query.filter_by(id=character_id).first()
    hero.user.remove(current_user)
    db.session.commit()
    return redirect(url_for('character.mycharacters'))

@character.route('/mycharacters')
@login_required
def mycharacters():
    favlist = FavoriteCharactor.query.filter(FavoriteCharactor.user_id==current_user.id).all()
    herolist_dict = []
    for fav in favlist:
        herolist = Charactor.query.filter_by(id=fav.character_id).all()
        for hero in herolist:
            herolist_dict.append(hero.to_dict())
    return render_template('mycharacter.html', herolist=herolist_dict)
