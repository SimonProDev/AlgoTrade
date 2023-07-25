import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import algotrade_engine.conf.settings as settings
from algotrade_engine.src.alerting.html_manager import HTMLCreator


class AlertingManager:
    """
    Manager alerts from financial markets to be sent by email (gmail account)
    """

    def __init__(self, tickers_with_trade_signal: list):
        self.gmail_address = settings.GMAIL_ADDRESS
        self.gmail_password = settings.GMAIL_PASSWORD
        self.tickers_to_send = tickers_with_trade_signal
        self.message = None
        self.port = 0
        self.ctx = None

    def send_alerts(self) -> None:
        settings.logger.info('SEND ALERT EMAIL')
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.ctx) as server:
            server.login(self.gmail_address,
                         self.gmail_password)
            server.sendmail(self.gmail_address,
                            self.gmail_address,
                            self.message.as_string())

    def create_alters(self) -> None:
        self.init_message()
        self.set_port()
        self.set_context()
        self.set_subject()
        self.set_message()

    def set_port(self, port: int = 465) -> None:
        self.port = port

    def set_context(self, ctx: ssl.SSLContext = ssl.create_default_context()) -> None:
        self.ctx = ctx

    def init_message(self, message_name: str = 'algotrade_alerts') -> None:
        self.message = MIMEMultipart(message_name)

    def set_subject(self, subject: str = 'AlgoTrade alerts') -> None:
        self.message['Subject'] = subject

    def set_message(self) -> None:
        # create html of email content
        html = HTMLCreator(self.tickers_to_send)
        html.build_html()
        # transform into html MIMEText objects
        html_content = MIMEText(html.get_html(), "html")
        # Add html content to MIMEMultipart message
        self.message.attach(html_content)

        for ticker in self.tickers_to_send:
            # add chart to html
            with open(f'tmp/{ticker}_chart.jpg', 'rb') as img:
                ticker_img = MIMEImage(img.read())
                # Define the image's ID as referenced in HTMLCreator
                ticker_img.add_header('Content-ID', ticker)
                self.message.attach(ticker_img)
