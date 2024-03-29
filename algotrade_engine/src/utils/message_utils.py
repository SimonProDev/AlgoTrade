from pyfiglet import Figlet


def create_app_logo() -> str:
    figlet = Figlet(font='slant')
    separator = '##################################################################'
    app_logo = f"""
{separator}
{figlet.renderText('ALGO TRADE')}
{separator}
This app aims to automatise trading through an algorythm
{separator}
Author : Simon BARGHI
Date: 26/06/2023
{separator}"""
    return app_logo


def create_logger_message(text: str) -> str:
    separator = '######################'
    logger_message = f'\n\n{separator}\n{text}\n{separator}'
    return logger_message
