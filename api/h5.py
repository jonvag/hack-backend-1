from flask import Blueprint, jsonify

#from api.sales import bp_sales

bp_h5 = Blueprint("h5", __name__)

@bp_h5.route("/h5", methods=["GET"])
def fn_h5():
    return jsonify({
        "payload":"success",
        "error": False
    })

@bp_h5.route("/h5", methods=["PUT", "POST", "DELETE"])
def fn_h5_else():
    return jsonify({})
