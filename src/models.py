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
    #metodos de clase
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def getId(cls,id):
        return cls.query.get(id)

     
class Todos(db.Model,BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(120), unique=True, nullable=False)
    is_done= db.Column(db.Boolean(), unique=False, nullable=False)

    #metodo de instancia %r lo sustituty por %self.id
    def __repr__(self):
        return '<Todos %r>' % self.id
    #metodo de instancia serializa el diccionario
    def serialize(self):
        return {
            "id": self.id,
            "label": self.label,
            "is_done": self.is_done
        }
    #metodo de instancia que obliga a que haya datos siempre que se llama       
    def __init__(self,label,is_done=False):
        self.label=label
        self.is_done=is_done

    def updateTodo(self,requestJson):
        self.label=requestJson["label"]
        self.is_done=requestJson["is_done"]

    # guardar datos en base de datos
    def save(self):
        db.session.add(self)
        return db.session.commit()
    
    # borrar linea en base de datos
    def delete(self):
        db.session.delete(self)
        return db.session.commit()
        

 
   