def user_login(request):
    return {
        'user_first': request.session.get('user_first'),
        'user_last': request.session.get('user_last'),
        'user_admin': request.session.get('user_admin'),
        'user_login': request.session.get('user_login'),
    }
