from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class BaseModel():
    @classmethod
    def get_all(cls):
        return cls.query.all()
    

class Todos(db.Model,BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(120), unique=True, nullable=False)
    is_done= db.Column(db.Boolean(), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Todos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "label": self.label,
            "is_done": self.is_done
        }


    # def __init__(self,label,is_done=False):
    #     self.label=label
    #     self.is_done=is_done


    # @classmethod
    # def create_task(cls):
    #     # task=cls
    #     # task.get_body()
    #     return cls.get_body(body_json)

    @classmethod
    def set_body(cls,body_json):
        todo=cls()
        todo.label=body_json["label"]
        todo.is_done=body_json["is_done"]
        return todo

   