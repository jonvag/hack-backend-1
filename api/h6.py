from flask import Blueprint, jsonify
from flask import request

#from api.sales import bp_sales

bp_h6 = Blueprint("h6", __name__)

@bp_h6.route("/h6", methods=["GET", "POST", "DELETE"])
def fn_h6():
    method = request.method
    return jsonify({
        "method": method,
        "payload": "success",
        "error": False
    })

@bp_h6.route("/h6", methods=["PUT"])
def fn_h6_else():
    return jsonify({
        "method": "type",
        "payload": None,
        "error": False
    })
