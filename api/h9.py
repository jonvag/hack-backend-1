from flask import Blueprint, jsonify
from flask import request

#from api.sales import bp_sales

bp_h9 = Blueprint("h9", __name__)

@bp_h9.route("/h9", methods=["GET"])
def fn_h9():
    lista = ["foo","bar","baz","qux","fred"] 
    hallar = False
    print(len(lista))
    alias = request.args.get("alias")

    for x in lista:
        if x == alias:
            hallar = True
    
    if hallar == True:
        return jsonify({
                "payload":alias,
                "error":{"available":False,"err_msg":None},
                "status":200
            })
    else:
        return jsonify( {
            "payload":"not found",
            "error":{"available":False,"err_msg":None},
            "status":404
          })