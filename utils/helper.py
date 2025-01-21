from datetime import datetime


def convert_datetime_to_iso(dt: datetime) -> str:
    dt.isoformat()
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
