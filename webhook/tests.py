import unittest

from pyramid import testing

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_mailer.testing')

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'webhook')

    def test_translations_webhook(self):
        from .views import translations_webhook
        request = testing.DummyRequest()
        request.headers.environ = {'FOO': 'foo',
                                   'BAR': 'bar'}
        info = translations_webhook(request)
        self.assertEqual(len(mailer.outbox) == 1)
        self.assertEqual(mailer.outbox[0].subject == "hello world")
        self.assertEqual(info['project'], 'webhook')
