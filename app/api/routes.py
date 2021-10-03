from flask import Blueprint, json, jsonify, request
from app.models import Charactor, db, FavoriteCharactor, User
from .apiauthhelper import token_required

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/characters', methods=['GET'])
def characters():
    characters = {a.name: a.to_dict() for a in Charactor.query.all()}
    return jsonify(characters)

@api.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    try:
        character = Charactor.query.get(id).to_dict()
        return jsonify(character)
    except:
        return jsonify(f"Character ID: {id} does not exist in the database")

@api.route('/characters/<int:id>', methods=['DELETE'])
@token_required
def delete_character(id):
    try:
        character = Charactor.query.get(id)
        db.session.delete(character)
        db.session.commit()
        return jsonify({'Deleted': character.to_dict()})
    except:
        return jsonify(f"Character of id: {id} does not exist in the database")

@api.route('/addcharacters', methods=['POST'])
@token_required
def addcharacter():
    req = request.get_json()
    newcharacter = Charactor()
    newcharacter.from_dict(req)
    db.session.add(newcharacter)
    db.session.commit()

    return jsonify({'Created': Charactor.query.all()[-1].to_dict()})

@api.route('/characters/<int:id>', methods=['PUT'])
@token_required
def updatecharacter(id):
    resp = request.get_json()
    print(resp)
    character = Charactor.query.get(id)
    character.from_dict(resp)
    db.session.commit()
    return jsonify({'Updated': character.to_dict()})

@api.route('/favcharacter/<string:id>', methods=['GET'])
@token_required
def getfavcharacter(id):
    try:
        favlist = FavoriteCharactor.query.filter(FavoriteCharactor.user_id==id).all()
        herolist_dict={}
        for fav in favlist:
            character_id=fav.character_id
            hero = Charactor.query.get(character_id)
            print(hero)
            herolist_dict[hero.id]=hero.to_dict()
        return jsonify(herolist_dict)
    except:
        return jsonify(f"User ID: {id} does not have favorite character")

@api.route('/favcharacter/<string:userid>/<int:id>', methods=['POST'])
@token_required
def addfavcharacter(userid, id):
    req = request.get_json()
    try:
        user = User.query.get(userid)
    except:
        return jsonify(f"User id: {userid} does not exist in the database")
    try:
        hero = Charactor.query.filter_by(id=id).first()
        hero.user.append(user)
        db.session.commit()
        return jsonify(f"Character ID: {id} has been added to {user.name}'s favorite list")
    except:
        return jsonify(f"Character id: {id} does not exist in the database")

@api.route('/favcharacter/<string:userid>/<int:id>', methods=['DELETE'])
@token_required
def deletefavcharacter(userid, id):
    try:
        user = User.query.get(userid)
    except:
        return jsonify(f"User id: {userid} does not exist in the database")
    try:
        hero = Charactor.query.filter_by(id=id).first()
    except:
        return jsonify(f"Character id: {id} does not exist in the database")
    try:
        hero.user.remove(user)
        db.session.commit()
    except:
        return jsonify(f"The character ID:{id} is not in the {user.name}'s favorite list")
    return jsonify(f"Character ID: {id} has been removed from {user.name}'s favorite list")