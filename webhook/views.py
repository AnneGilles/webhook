from pyramid.view import view_config
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'webhook'}

@view_config(route_name='translations_webhook', renderer='templates/translations.pt')
def translations_webhook(request):

    #print(dir(request))
    #print("-- request.GET --")
    #print(request.GET)
    #print("-- request.POST --")
    #print(request.POST)
    #print("-- request.ResponseClass --")
    #print(request.ResponseClass)
    print("-- request.headers.environ --")
    #print(dir(request.headers))

    if request.headers.environ:
        import pprint
        pp = pprint.PrettyPrinter()
    
        pp.pprint((request.headers.environ))
        # print((request.headers.items))

    request.session.flash("foo")

    mail_message = Message(
        subject="[translations webhook]",
        sender="noreply@c3s.cc",
        recipients=['c@c3s.cc'],
        body="foo!"
        )
    
    mailer = get_mailer(request)
    mailer.send(mail_message)
    
    return {'project':'webhook',
            'message':'mail was sent!'}

