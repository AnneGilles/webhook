from pyramid.view import view_config
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'webhook'}

@view_config(route_name='translations_webhook', renderer='templates/translations.pt')
def translations_webhook(request):

    message = Message(
        subject="[translations webhook]",
        sender="noreply@c3s.cc",
        recipients=['c@c3s.cc'],
        body="foo!"
        )
    
    mailer = get_mailer(request)
    mailer.send(message)
    
    return {'project':'webhook',
            'message':'mail was sent!'}

