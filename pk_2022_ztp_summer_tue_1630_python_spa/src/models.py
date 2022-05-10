from datetime import datetime
from app import db


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(120))
    note_type = db.Column(db.Integer,
                          db.ForeignKey("note_types.id"))
    important = db.Column(db.Boolean)
    is_task = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def columns(self):
        return {col.name for col in self.__table__.columns}

    def to_json(self):
        return {
            col.name: getattr(self, col.name)
            for col in self.__table__.columns
        }


class NoteType(db.Model):
    __tablename__ = "note_types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def to_json(self):
        return {
            col.name: getattr(self, col.name)
            for col in self.__table__.columns
        }
