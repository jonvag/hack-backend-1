from flask import Blueprint, jsonify

#from api.sales import bp_sales

bp_h3 = Blueprint("h3", __name__)

@bp_h3.route("/h3", methods=["PUT"])
def fn_h3():
    return jsonify({
        "payload":"put"
    })
