import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import algotrade_engine.conf.settings as settings


class AlertingManager:
    """
    Manager alerts from financial markets to be sent by email (gmail account)
    """

    def __init__(self):
        self.gmail_address = settings.GMAIL_ADDRESS
        self.gmail_password = settings.GMAIL_PASSWORD
        self.message = None
        self.port = 0
        self.ctx = None

    def send_alerts(self) -> None:
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
        # Create the plain-text and HTML version of your message
        html = """\
        <html>
          <body>
            <img src='cid:image1' width=1000 height=800>
          </body>
        </html>
        """
        # <img src="../tmp_files/EURUSD=X_chart.png">
        # Turn these into html MIMEText objects
        html_content = MIMEText(html, "html")
        # Add html content to MIMEMultipart message
        self.message.attach(html_content)

        # add chart to html
        with open('../tmp_files/EURUSD=X_chart.jpg', 'rb') as img:
            chart_image = MIMEImage(img.read())
        # Define the image's ID as referenced above
        chart_image.add_header('Content-ID', '<image1>')
        self.message.attach(chart_image)
