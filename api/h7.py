from flask import Blueprint, jsonify
from flask import request

#from api.sales import bp_sales

bp_h7 = Blueprint("h7", __name__)

@bp_h7.route("/h7", methods=["GET"])
def fn_h7():
    email = request.args.get("email")
    name = request.args.get("name")
    print(email)
    if email ==None or name == None:
        return jsonify({
                "payload":None,
                "error":True,
                "status":404
            })
    else:
        return jsonify({
                "payload":{"email":email, "name":name},
                "error":{"available":False,"err_msg":None},
                "status":200
            })