import imaplib
import json
import urllib.parse
from urllib import request

from emailrouter.utils import ArgumentMixin, Base as Handler, Registry, load_module_from_file

HandlerRegistry = Registry()
register_handler = HandlerRegistry.register_class


@register_handler('python')
class PythonHandler(ArgumentMixin, Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.call_func = load_module_from_file(self.data['file']).handle

    def __call__(self, email):
        return self.call_func(email, *self.args, **self.kwargs)


@register_handler('placeholder', default=True)
class PlaceholderHandler(Handler):
    def __call__(self, email):
        pass


@register_handler('imap')
class IMAPHandler(ArgumentMixin, Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ssl = self.kwargs['ssl']
        url = urllib.parse.urlparse(self.kwargs['url'])
        default_port = 993 if ssl else 143

        self.mailbox = self.kwargs.get('mailbox')
        self.flags = self.kwargs.get('flags')
        self.imap = imaplib.IMAP4_SSL if ssl else imaplib.IMAP4
        self.credentials = {
            'host': url.hostname,
            'port': url.port or default_port,
            'username': url.username,
            'password': url.password,
        }

    def __call__(self, email):
        conn = self.imap(host=self.credentials['host'], port=self.credentials['port'])
        conn.login(self.credentials['username'], self.credentials['password'])
        conn.append(self.mailbox, self.flags, None, email.raw.encode('utf-8'))
        conn.logout()


class DiscordWebhook:
    MESSAGE_LIMIT = 2000

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def message(self, message):
        req = request.Request(
            self.webhook_url,
            data=json.dumps(message).encode('utf-8'),
            headers={'User-Agent': 'Python/3', 'Content-Type': 'application/json'},
        )
        request.urlopen(req)

    @staticmethod
    def escape(text):
        escape_chars = ('*', '_', '~', '`', '|')
        for ch in escape_chars:
            text = text.replace(ch, '\\' + ch)
        return text


@register_handler('discord')
class DiscordHandler(ArgumentMixin, Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.webhook = DiscordWebhook(self.kwargs['webhook_url'])
        self.payload = self.kwargs.get('payload', {})
        self.colour = self.kwargs.get('color', self.kwargs.get('colour', 0xeee))

    def __call__(self, email):
        subject = f'{email.subject}'
        message = email.text_plain

        fields = []
        for name, value in (
            ('From', email.sender),
            ('To', ', '.join(email.recipients)),
            ('CC', ', '.join(email.cc)),
            ('BCC', ', '.join(email.bcc)),
            ('Reply To', ', '.join(email.reply_to)),
        ):
            if value:
                fields.append({
                    'name': name,
                    'value': value,
                })

        self.webhook.message({
            **self.payload,
            'embeds': [
                {
                    'title': self.webhook.escape(subject),
                    'color': self.colour,
                    'timestamp': email.date.isoformat(),
                    'fields': fields,
                },
                {
                    'title': self.webhook.escape(subject),
                    'description': message[:self.webhook.MESSAGE_LIMIT],
                    'color': self.colour,
                    'timestamp': email.date.isoformat(),
                },
            ],
        })
