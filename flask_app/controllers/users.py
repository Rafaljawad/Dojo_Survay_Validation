
from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import user


#has the form to be filled by user
@app.route('/')
def index():
    return render_template('survay.html')

#fill the form and once submit will take you to process route
@app.route('/process',methods=['POST'])
def process_form():
    #before creating data , we need to check if they are validated or not 
    #if they are not , so go to form and flash the error messages that we created in user.py ->validate_input method.
    if not user.User.validate_input(request.form):
        return redirect('/')
    #if all data are validated so, create all the inserted data 
    else:
        user.User.create_new_user(request.form)
        return redirect('/result')

@app.route('/result')
def get_user():
    this_user=user.User.get_each_user_with_info()# this will give us the last dictionary and limit 1 so, take this dictionary and
    #pass its key inside show_user.html.
    return render_template('show_user.html',this_user=this_user)
