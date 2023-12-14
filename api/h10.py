from flask import Blueprint, jsonify
from flask import request

#from api.sales import bp_sales

bp_h10 = Blueprint("h10", __name__)

@bp_h10.route("/h10", methods=["POST"])
def fn_h10():
    lista =  ["foo","bar","baz","qux","fred"]
    hallar = False
    data = request.json
    alias = data.get("alias")

    for x in lista:
        if x == alias:
            hallar = True
    
    if hallar == True:
        return jsonify({
            "payload":alias
            })
    else:
        return jsonify({
            "payload":"not found"
            })