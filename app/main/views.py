from . import main
import json
from flask import request, render_template


@main.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        a = request.get_data()
        print(type(a))
        print(a)
        return a
        # dict1 = json.loads(a)
        # print(dict1)
        # return json.dumps(dict1["username"])
    return render_template("login.html")
