from algotrade_engine.src.alerting.alerting_manager import AlertingManager


class AlgoTradeManager:
    """
    Manager class that run AlgoTrade Application
    """

    def __init__(self):
        self.alerting_manager = AlertingManager()

    def run_algotrade_app(self):
        self.run_alerting()

    def run_alerting(self):
        alterting_manager = AlertingManager()
        alterting_manager.create_alters()
        alterting_manager.send_alerts()
