from flask import Blueprint, jsonify
from flask import request

#from api.sales import bp_sales

bp_h8 = Blueprint("h8", __name__)

@bp_h8.route("/h8", methods=["POST"])
def fn_h8():
    data = request.json
    email = data.get("email")
    alias = data.get("alias")
    print(alias)
    print(email)
    if email == None or alias == None:
        return jsonify({
                "payload":None,
                "error":True,
                "status":405
            })
    else:
        return jsonify({
                "payload":{"email":email, "alias":alias},
                "error":{"available":False,"err_msg":None},
                "status":200
            })