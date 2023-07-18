# from airium import Airium
#
#
# a = Airium()
# # Generating HTML file
# a('<!DOCTYPE html>')
# with a.html(lang="pl"):
#     with a.head():
#         a.meta(charset="utf-8")
#         a.title(_t="Example: How to use Airium library")
#     with a.body():
#         with a.h1(id="id23345225", kclass='main_header'):
#             a("Hello Finxters")
#             a.img(src='cid:image1', alt='alt text')
# # Casting the file to a string to extract the value
# html = str(a)
# # Casting the file to UTF-8 encoded bytes:
# html_bytes = bytes(a)
# print(html)

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


html_creator = HTMLCreator(['DAX', 'EURUSD', 'GOLD'])
html_creator.build_html()
