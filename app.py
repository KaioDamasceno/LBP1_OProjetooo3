from flask import Flask, session, flash, render_template
from controllers.geralController import geralController
from controllers.loginController import loginController

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Utilize uma chave secreta forte

app.register_blueprint(geralController)
app.register_blueprint(loginController)

@app.errorhandler(401)
def unauthorized(error):
    return render_template('401.html'), 401

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)
