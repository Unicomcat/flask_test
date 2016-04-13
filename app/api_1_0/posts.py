from flask.ext.login import login_required
from . import api


@api.route('/posts/')
@auth.login_required
def get_posts():
    pass