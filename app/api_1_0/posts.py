from flask.ext.login import login_required

@api.route('/posts/')
@auth.login_required
def get_posts():
    pass