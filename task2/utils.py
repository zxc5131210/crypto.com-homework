from datetime import datetime, timedelta


def get_day_after_tomorrow():
    """
    Get the date of the day after tomorrow.
    """
    current_date = datetime.now()
    day_after_tomorrow = current_date + timedelta(days=2)
    day_after_tomorrow_str = day_after_tomorrow.strftime("%Y%m%d")
    return day_after_tomorrow_str
