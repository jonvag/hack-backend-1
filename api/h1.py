from flask import Blueprint, jsonify

#from api.sales import bp_sales

bp_h1 = Blueprint("h1", __name__)

@bp_h1.route("/h1", methods=["GET"])
def fn_h1():
    return jsonify({
        "payload":"get"
    })
