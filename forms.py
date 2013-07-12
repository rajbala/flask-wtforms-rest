from wtforms import Form, TextField, validators

class BetaListForm(Form):
    email_address = TextField('Email Address', [validators.Required(message=u'The Email field cannot be blank'), validators.Email()])