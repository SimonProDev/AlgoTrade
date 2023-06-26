import smtplib
import ssl
import algotrade_engine.conf.settings as settings


class AlertingManager:
    """
    Manager alerts from financial markets to be sent by email (gmail account)
    """

    def __init__(self):
        self.gmail_address = settings.GMAIL_ADDRESS
        self.gmail_password = settings.GMAIL_PASSWORD
        self.port = 0
        self.ctx = None
        self.subject = ''
        self.message = ''

    def send_alerts(self) -> None:
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.ctx) as server:
            server.login(self.gmail_address,
                         self.gmail_password)
            server.sendmail(self.gmail_address,
                            self.gmail_address,
                            self.message)

    def create_alters(self) -> None:
        self.set_port()
        self.set_context()
        self.set_subject()
        self.set_message()

    def set_port(self, port: int = 465) -> None:
        self.port = port

    def set_context(self, ctx: ssl.SSLContext = ssl.create_default_context()) -> None:
        self.ctx = ctx

    def set_subject(self, subject: str = 'Subject: AlgoTrade\n') -> None:
        self.subject = subject

    def set_message(self, message: str = 'Hello World !') -> None:
        self.message = self.subject + message
