
from flask import Flask, render_template, request
from forms import BetaListForm
from RestModule import RestWrapper

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def beta_signup():
    form = BetaListForm(request.form)
    
    if request.method == 'POST' and form.validate():
        email_address = request.form['email_address']

        api = RestWrapper.BetaUser()
        resp = api.add_to_beta(email_address)

        response, server_error = resp[0], resp[1]
        
        if server_error:
            return render_template('beta_signup.html', form=form, server_error=server_error)
        
        else:
            return render_template('beta_signup_completed.html', form=form)
    
    else:
        return render_template('beta_signup.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
