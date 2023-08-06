import unittest
from email.message import EmailMessage

from emailrouter import Email, Router


def handle(email):
    raise ValueError()


class TestRouter(unittest.TestCase):
    def test_basic(self):
        r = Router({
            'handlers': {
                'handler': {
                    'type': 'imap',
                    'kwargs': {
                        'ssl': True,
                        'url': 'imap://a:a@127.0.0.1',
                        'mailbox': 'Trash',
                    },
                },
            },
            'filters': {
                'name': {
                    'type': 'true',
                },
            },
            'routes': [
                {
                    'name': 'main',
                    'handlers': [
                        {
                            'type': 'python',
                            'file': __file__,
                        },
                        {
                            'type': 'named',
                            'name': 'handler',
                        },
                    ],
                    'condition': {
                        'type': 'all',
                        'conditions': [
                            {
                                'type': 'named',
                                'name': 'name',
                            },
                            {
                                'type': 'equal',
                                'field': 'subject',
                                'value': 'RE:',
                            },
                            {
                                'type': 'length',
                                'field': 'subject',
                                'value': 3,
                            },
                        ],
                    },
                },
            ],
        })
        msg = EmailMessage()
        msg['Subject'] = 'RE:'
        msg['To'] = 'a@gmail.com'
        msg['From'] = 'b@gmail.com'
        with self.assertRaises(ValueError):
            r.execute(Email(msg.as_string()))
