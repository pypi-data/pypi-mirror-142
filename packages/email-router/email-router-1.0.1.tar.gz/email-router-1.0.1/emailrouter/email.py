import html2text
import mailparser


class Email:
    def __init__(self, raw):
        self.raw = raw
        self.email = mailparser.parse_from_string(self.raw)

        self.message_id: str = self.email.message_id
        self.subject: str = self.email.subject or ''
        self.body: str = self.email.body

        self.recipients: list[str]
        self.recipient_names: list[str]
        self.senders: str
        self.sender_names: str
        self.cc: list[str]
        self.cc_names: list[str]
        self.bcc: list[str]
        self.bcc_names: list[str]
        self.reply_to: list[str]
        self.reply_to_names: list[str]

        def zip_if_nonempty(arr):
            return zip(*arr) if arr else ([], [])

        self.recipient_names, self.recipients = zip_if_nonempty(self.email.to)
        self.sender_names, self.senders = zip_if_nonempty(self.email.from_)
        self.cc_names, self.cc = zip_if_nonempty(self.email.cc)
        self.bcc_names, self.bcc = zip_if_nonempty(self.email.bcc)
        self.reply_to_names, self.reply_to = zip_if_nonempty(self.email.reply_to)

        self.date = self.email.date
        self.text_plain: str = '\n'.join(self.email.text_plain)
        self.text_html: str = '\n'.join(self.email.text_html)

        self.attachments = self.email.attachments
        self.headers = self.email.headers

        h = html2text.HTML2Text()
        h.ignore_images = True
        self.text_markdown: str = h.handle(self.text_html)

    @classmethod
    def from_file(cls, filename):
        with open(filename) as f:
            return cls(f.read())
