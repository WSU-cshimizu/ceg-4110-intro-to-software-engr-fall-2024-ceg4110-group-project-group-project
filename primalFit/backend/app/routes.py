from flask import Blueprint, jsonify, request, session
from .models import User, Routine, Exercise
from . import db

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return "Hello, World!"


@bp.route("/login", methods =["POST"])
def login_user():
    email = request.json.get("email")
    password = request.json.get("password")

    user = User.query.filter(User.email == email).first_or_404()
    
    if(user.password == password):
        json_values = user.to_json()
        return(jsonify(json_values), 200)
    else:
        return(jsonify({"message": "Wrong Password"}), 401)


@bp.route("/register", methods =["POST"])
def create_user():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")
    birthdate = request.json.get("birthdate")
    weight = request.json.get("weight")
    weight_goal = request.json.get("weightGoal")
    height = request.json.get("height")
    is_male = request.json.get("isMale")

    if not name or not email or not password or not birthdate or not weight or not weight_goal or not height or is_male == None: 
        return(
            jsonify({"message": "Every text field must be completed"}), 400,
        ) 
    
    new_user = User(name = name, email = email, password = password, birthdate = birthdate, weight = weight, weight_goal =weight_goal, 
        height = height, is_male = is_male)
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    json_values = new_user.to_json()
    return(jsonify(json_values), 201,) 


@bp.route("/users", methods =["GET"])
def get_users():
    users = User.query.all()
    json_users = list(map(lambda x: x.to_json(), users))
    return(jsonify({"users": json_users}), 200)


@bp.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"message": "User Not Found"}), 404
    else:
        return user.to_json(), 201


# Do we need this method?
# @bp.route("/users/<int:id>", methods = ["PUT"])
    

@bp.route("/users/<int:id>", methods =["PATCH"])
def update_user():
    user = User.query.filter(User.id == id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    user.birthdate = data.get("birthdate", user.birthdate)
    user.weight = data.get("weight", user.weight)
    user.weight_goal = data.get("weightGoal", user.weight_goal)
    user.height = data.get("height", user.height)
    user.is_male = data.get("isMale", user.is_male)
    user.routines = data.get("routines", user.routines)
    user.eaten_food = data.get("eatenFood", user.eaten_food)

    db.session.commit()
    json_values = user.to_json()
    return(jsonify(json_values), 201) 


@bp.route("/users/<int:id>", methods =["DELETE"])
def delete_user(id):
    user = User.query.filter(User.id == id)

    if not user:
        return jsonify({"message": "User not found"}), 404
    
    db.session.delete(user)
    db.session.commit()
    return "", 204


# I think GitHub Documentation needs to be fixed.
# we don't need user id in the route for getting all routines
@bp.route("/routines", methods = ["GET"])
def get_routines():
    routines = Routine.query.all()
    routines_to_json = list(map(lambda x: x.to_json(), routines))
    return routines_to_json, 200


@bp.route("/users/<int:id>/routines", methods = ["GET"])
def get_routines_by(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"message": "User Not Found"}), 404
    else:
        routines_of_user = Routine.query.filter(Routine.user_id == id).all()
        routines_of_user_to_json = list(map(lambda x: x.to_json(), routines_of_user))
        return routines_of_user_to_json, 200


@bp.route("/users/<int:id>/routines", methods =["POST"])
def create_routine(id):
    name = request.json.get("name")
    exercises = request.json.get("exercises")
    user = User.query.filter(User.id == id).first()

    if not name: 
        return(
            jsonify({"message": "Invalid Inputs"}), 400,
        ) 
    
    new_routine = Routine(name = name, user = user)
    try:
        db.session.add(new_routine)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    if(exercises != None):
        for x in exercises:
            new_exercise = Exercise(name = exercises(x["name"]), type = exercises(x["type"]),
                            duration = exercises(x["duration"]), video_url = exercises(x["videoUrl"]), routine = new_routine)
            try:
                db.session.add(new_exercise)
                db.session.commit()
            except Exception as e:
                return jsonify({"message": str(e)}), 400
    
    json_values = new_routine.to_json()
    return(jsonify(json_values), 201) 


@bp.route("/users/<int:uid>/routines/<int:rid>", methods = ["DELETE"])
def delete_routine(uid, rid):
    user = User.query.filter(User.id == uid)

    if not user:
        return jsonify({"message": "User Not Found"}), 404
    
    else:
        routine_to_delete = session.get(Routine, {"id": rid, "user_id": uid})
        db.session.delete(routine_to_delete)
        db.session.commit()
        return jsonify({"message": "Routine deleted successfully"}), 204
