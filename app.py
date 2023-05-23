from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about')
def about():
    ret={"a": 1}
    return jsonify(ret)

if __name__ == "__main__":
    app.run(debug=True)