import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask import Flask
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'hello.db')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

class MyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.String(255))
    field2 = db.Column(db.String(255))
    foreignkey_field = db.Column(db.Integer, db.ForeignKey('other_model.id'))

class MyModelForm(form.Form):
    field1 = fields.StringField('Field1')
    field2 = fields.StringField('Field2')
    foreignkey_field = fields.SelectField('Foreignkey Field', choices=[(obj.id, obj.name) for obj in OtherModel.query.all()])

class MyModelView(ModelView):
    form_columns = ('field1', 'field2', 'foreignkey_field')
    column_editable_list = ('field1', 'field2', ('foreignkey_field', get_foreignkey_default))

    def get_foreignkey_default(self):
        return self.foreignkey_field.query.first()

admin = Admin(app)
admin.add_view(MyModelView(MyModel, db.session))



