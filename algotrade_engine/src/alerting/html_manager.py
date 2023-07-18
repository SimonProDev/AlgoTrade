from airium import Airium


class HTMLCreator:
    """
    Creates html string that will be the content
    of email alters
    """

    def __init__(self, tickers_to_send: list):
        self.tickers_to_send = tickers_to_send
        self.html = None

    def build_html(self) -> None:
        self.init_html()
        self.add_chart_images()
        self.html = str(self.html)

    def init_html(self) -> None:
        self.html = Airium()
        self.html('<!DOCTYPE html>')

    def add_chart_images(self) -> None:
        with self.html.body():
            for ticker in self.tickers_to_send:
                self.add_chart_image(ticker)

    def add_chart_image(self, ticker_name: str) -> None:
        self.html.img(src=f'cid:{ticker_name}', alt=ticker_name)