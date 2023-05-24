from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# flask object
app = Flask(__name__)

# db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://testdb:password@localhost/testdb'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f"<users {self.id}>"


# page
@app.route("/")
def home():
    html = ''
    for r in Users.query.all():
        html += f"<p>name: {r.name}</p>" \
                f"<p>email: {r.email}</p>"
    return html


if __name__ == '__main__':
    app.run(debug=True)
