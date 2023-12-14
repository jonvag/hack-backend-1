from flask import Flask, jsonify
from flask_cors import CORS
from flask import request

#endpoints
from api.h1 import bp_h1
from api.h2 import bp_h2
from api.h3 import bp_h3
from api.h4 import bp_h4
from api.h5 import bp_h5
from api.h6 import bp_h6
from api.h7 import bp_h7
from api.h8 import bp_h8
from api.h9 import bp_h9
from api.h10 import bp_h10

app = Flask(__name__)
CORS(app)

app.register_blueprint(bp_h1, url_prefix="/")
app.register_blueprint(bp_h2, url_prefix="/")
app.register_blueprint(bp_h3, url_prefix="/")
app.register_blueprint(bp_h4, url_prefix="/")
app.register_blueprint(bp_h5, url_prefix="/")
app.register_blueprint(bp_h6, url_prefix="/")
app.register_blueprint(bp_h7, url_prefix="/")
app.register_blueprint(bp_h8, url_prefix="/")
app.register_blueprint(bp_h9, url_prefix="/")
app.register_blueprint(bp_h10, url_prefix="/")

@app.route("/", methods=["GET"])
def fn_main():

    ct = request.method
    print(ct)
    return jsonify({
        "payload":"get",
        "section": "main"
    })

if __name__ == "__main__":
        app.run(debug=True)