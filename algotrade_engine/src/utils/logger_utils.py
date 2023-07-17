from pyfiglet import Figlet


def create_logger_msg(text: str, font: str) -> Figlet:
    figlet = Figlet(font=font)
    return figlet.renderText('\n' + text)
