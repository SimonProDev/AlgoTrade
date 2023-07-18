from datetime import datetime, timedelta


def calculate_start_date(days_delta=90):
    return (datetime.now() - timedelta(days=days_delta)).strftime('%Y-%m-%d')
