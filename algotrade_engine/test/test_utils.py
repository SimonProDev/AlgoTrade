from datetime import datetime, timedelta

from algotrade_engine.src.utils.config_utils import calculate_start_date
from algotrade_engine.src.utils.message_utils import create_app_logo, \
    create_logger_message


def test_calculate_start_date():
    expected_result = (datetime.now() - timedelta(days=120)).strftime('%Y-%m-%d')
    assert calculate_start_date(120) == expected_result


def test_create_logger_msg(expected_app_log):
    assert expected_app_log == create_app_logo()
