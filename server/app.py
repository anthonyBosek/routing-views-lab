#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:param>")
def print_string(param):
    print(param)
    return param


@app.route("/count/<int:num>")
def count(num):
    nums = f""
    for n in range(num):
        nums += f"{n}\n"
    return nums


@app.route("/math/<int:n1>/<string:oper>/<int:n2>")
def math(n1, n2, oper):
    if oper == "+":
        return str(n1 + n2)
    elif oper == "-":
        return str(n1 - n2)
    elif oper == "*":
        return str(n1 * n2)
    elif oper == "div":
        return str(n1 / n2)
    elif oper == "%":
        return str(n1 % n2)
    else:
        return "Invalid operator!"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
