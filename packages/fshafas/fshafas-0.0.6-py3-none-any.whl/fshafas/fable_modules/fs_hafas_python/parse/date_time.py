from __future__ import annotations
from typing import (Optional, Any, Tuple)
from ...fable_library.date import create
from ...fable_library.double import parse
from ...fable_library.int32 import parse as parse_1
from ...fable_library.string import (to_console, printf, substring)
from ...fs_hafas_python.context import (Profile, Context)
from ...fs_hafas_python.extensions import (DateTimeOffsetEx_DateTimeOffsetEx__ctor_26581FE8, DateTimeOffsetEx_DateTimeOffsetEx, DateTimeOffsetEx_DateTimeOffsetEx__get_DateTime, DateTimeOffsetEx_DateTimeOffsetEx__AddDays_5E38073B)

def parse_date_time_with_offset(profile: Profile, year: int, month: int, day: int, hour: int, minute: int, seconds: int, tz_offset: Optional[int]=None) -> DateTimeOffsetEx_DateTimeOffsetEx:
    try: 
        dt : Any = create(year, month, day, hour, minute, seconds)
        return DateTimeOffsetEx_DateTimeOffsetEx__ctor_26581FE8(dt, None, None) if (tz_offset is None) else DateTimeOffsetEx_DateTimeOffsetEx__ctor_26581FE8(dt, tz_offset * 60, None)
    
    except Exception as ex:
        arg10 : str = str(ex)
        to_console(printf("error parseDateTimeWithOffset: %s"))(arg10)
        raise Exception(str(ex))
    


def ToIsoString(dto: DateTimeOffsetEx_DateTimeOffsetEx) -> str:
    dt : Any = DateTimeOffsetEx_DateTimeOffsetEx__get_DateTime(dto)
    return dt.isoformat()


def parse_date_time_ex(profile: Profile, date: str, time: Optional[str]=None, tz_offset: Optional[int]=None) -> Tuple[Optional[Any], Optional[str]]:
    try: 
        if time is None:
            return (None, None)
        
        else: 
            time_1 : str = time
            pattern_input : Tuple[str, float] = ((substring(time_1, len(time_1) - 6, 6), parse(substring(time_1, 0, 2)))) if (len(time_1) > 6) else ((time_1, 0))
            time6 : str = pattern_input[0]
            dto : DateTimeOffsetEx_DateTimeOffsetEx = DateTimeOffsetEx_DateTimeOffsetEx__AddDays_5E38073B(parse_date_time_with_offset(profile, parse_1(substring(date, 0, 4), 511, False, 32), parse_1(substring(date, 4, 2), 511, False, 32), parse_1(substring(date, 6, 2), 511, False, 32), parse_1(substring(time6, 0, 2), 511, False, 32), parse_1(substring(time6, 2, 2), 511, False, 32), parse_1(substring(time6, 4, 2), 511, False, 32), tz_offset), pattern_input[1])
            return (DateTimeOffsetEx_DateTimeOffsetEx__get_DateTime(dto), ToIsoString(dto))
        
    
    except Exception as ex:
        to_console(printf("parseDateTimeEx: %A"))(ex)
        return (None, None)
    


def parse_date_time(ctx: Context, date: str, time: Optional[str]=None, tz_offset: Optional[int]=None) -> Optional[str]:
    return parse_date_time_ex(ctx.profile, date, time, tz_offset)[1]


