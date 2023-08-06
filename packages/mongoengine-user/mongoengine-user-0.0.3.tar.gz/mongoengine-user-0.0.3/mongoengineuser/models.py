from mongoengine import StringField, Document, EmbeddedDocument, ListField, EmbeddedDocumentField, DateTimeField
from uuid import uuid4
from datetime import datetime

class User(Document):
    _id = StringField(primary_key=True, required=True, max_length=50, default=str(uuid4()))
    email = StringField(required=True, unique=True) # from mongoengine.errors import NotUniqueError
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    created = DateTimeField(required=True,default=datetime.utcnow)
    modified = DateTimeField(required=True,default=datetime.utcnow)
    meta = {'allow_inheritance': True}