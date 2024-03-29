import pytest


@pytest.fixture
def expected_app_log():
    expected_app_log = """
##################################################################
    ___    __    __________     __________  ___    ____  ______
   /   |  / /   / ____/ __ \   /_  __/ __ \/   |  / __ \/ ____/
  / /| | / /   / / __/ / / /    / / / /_/ / /| | / / / / __/   
 / ___ |/ /___/ /_/ / /_/ /    / / / _, _/ ___ |/ /_/ / /___   
/_/  |_/_____/\____/\____/    /_/ /_/ |_/_/  |_/_____/_____/   
                                                               

##################################################################
This app aims to automatise trading through an algorythm
##################################################################
Author : Simon BARGHI
Date: 26/06/2023
##################################################################"""
    return expected_app_log


@pytest.fixture
def expected_logger_message():
    expected_logger_message = """

######################
test
######################"""
    return expected_logger_message
