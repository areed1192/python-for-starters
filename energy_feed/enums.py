from enum import Enum

class Months(Enum):
    """Represents all the Months that can
    be used to query differnt news feed reports.

    ### Usage:
    ----
        >>> from energy_feed.enums import Months
        >>> Months.April.value
    """

    Janurary = 'Jan'
    Feburary = 'Feb'
    March = 'Mar'
    April = 'Apr'
    May = 'May'
    June = 'Jun'
    July = 'Jul'
    August = 'Aug'
    October = 'Oct'
    November = 'Nov'
    December = 'Dec'
