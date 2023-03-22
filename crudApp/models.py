from crudApp import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name.capitalize()}, EMAIL: {self.email}"
