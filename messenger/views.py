from flask import render_template, request

from messenger import APP

@APP.route('/')
def index():
    return render_template(
        'index.html'
    )

@APP.route('/inbox')
def inbox():
    return render_template(
        'inbox.html'
    )

@APP.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # TODO process form
        pass

    return render_template(
        'login.html'
    )
