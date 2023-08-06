from __future__ import annotations
from datetime import timedelta
import datetime
from dateutil import tz as tz_1
from typing import (Any, Optional, Tuple)
from ..fable_library.reflection import (TypeInfo, class_type)
from ..fable_library.string import (to_text, printf)

def DateTimeEx_formatDate(dt: Any, pattern: str) -> str:
    if "yyyyMMdd" == pattern:
        arg30 : int = (dt.day) or 0
        arg20 : int = (dt.month) or 0
        arg10 : int = (dt.year) or 0
        return to_text(printf("%04d%02d%02d"))(arg10)(arg20)(arg30)
    
    else: 
        raise Exception("nyi")
    


def DateTimeEx_formatTime(dt: Any, pattern: str) -> str:
    if "HHmm" == pattern:
        arg20 : int = (dt.minute) or 0
        arg10 : int = (dt.hour) or 0
        return to_text(printf("%02d%02d"))(arg10)(arg20)
    
    else: 
        raise Exception("nyi")
    


def expr_74() -> TypeInfo:
    return class_type("FsHafas.Extensions.DateTimeOffsetEx.DateTimeOffsetEx", None, DateTimeOffsetEx_DateTimeOffsetEx)


class DateTimeOffsetEx_DateTimeOffsetEx:
    def __init__(self, dt: Any, tzoffset_arg: Optional[int]=None, tz_arg: Optional[str]=None) -> None:
        self.dt = dt
        self.tzoffset_arg = tzoffset_arg
        self.tz_arg = tz_arg
    

DateTimeOffsetEx_DateTimeOffsetEx_reflection = expr_74

def DateTimeOffsetEx_DateTimeOffsetEx__ctor_26581FE8(dt: Any, tzoffset_arg: Optional[int]=None, tz_arg: Optional[str]=None) -> DateTimeOffsetEx_DateTimeOffsetEx:
    return DateTimeOffsetEx_DateTimeOffsetEx(dt, tzoffset_arg, tz_arg)


def DateTimeOffsetEx_DateTimeOffsetEx__get_DateTime(__: DateTimeOffsetEx_DateTimeOffsetEx) -> Any:
    return DateTimeOffsetEx_DateTimeOffsetEx__getDateTime(__)


def DateTimeOffsetEx_DateTimeOffsetEx__AddDays_5E38073B(__: DateTimeOffsetEx_DateTimeOffsetEx, days: float) -> DateTimeOffsetEx_DateTimeOffsetEx:
    return DateTimeOffsetEx_DateTimeOffsetEx__ctor_26581FE8(__.dt+timedelta(days=int(days)), __.tzoffset_arg, __.tz_arg)


def DateTimeOffsetEx_DateTimeOffsetEx__getDateTime(this: DateTimeOffsetEx_DateTimeOffsetEx) -> Any:
    match_value : Tuple[Optional[int], Optional[str]] = (this.tzoffset_arg, this.tz_arg)
    if match_value[0] is not None:
        tzoffset_arg : int = match_value[0] or 0
        return datetime.datetime((this.dt.year), (this.dt.month), (this.dt.day), (this.dt.hour), (this.dt.minute), (this.dt.second), tzinfo=(tz_1.tzoffset(None, tzoffset_arg)))
    
    elif match_value[1] is not None:
        tz : str = match_value[1]
        return datetime.datetime((this.dt.year), (this.dt.month), (this.dt.day), (this.dt.hour), (this.dt.minute), (this.dt.second), tzinfo=(tz_1.gettz(tz)))
    
    else: 
        return datetime.datetime((this.dt.year), (this.dt.month), (this.dt.day), (this.dt.hour), (this.dt.minute), (this.dt.second), tzinfo=(tz_1.gettz("Europe/Berlin")))
    


