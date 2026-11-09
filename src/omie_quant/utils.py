
from datetime import date, timedelta


def date_range(start: date, end: date) -> list[date]:
    """Return every day from start to end, both included.

    Args:
        start: First day.
        end: Last day.

    Returns:
        Dates in chronological order in the format datetime.date(year, month, day)

    Raises:
        ValueError: If start is after end.
        
    Other functions with days: len(days)           
                               days[-1] - days[0]      
                               [d.strftime("%d%m%Y") for d in days]      
    """
    if start > end:
        raise ValueError(f"start ({start}) is after end ({end})")
    n_days = (end - start).days
    return [start + timedelta(days=i) for i in range(n_days + 1)]