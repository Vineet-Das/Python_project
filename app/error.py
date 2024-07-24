from flask import Blueprint,jsonify # type: ignore

errors=Blueprint('errors',__name__)

@errors.app_errorhandler(404)
def not_found_error(error):
    return jsonify({"error" :"RESOURCE ARE NOT FOUND"}),404

@errors.app_errorhandler(400)
def bad_request_error(error):
    return jsonify({"error" : "RESOURCE ARE NOT FOUND"}),400

@errors.app_errorhandler(500)
def internal_error(error):
    return jsonify({"error ": "INTERNAL SERVER ERROR"}),500