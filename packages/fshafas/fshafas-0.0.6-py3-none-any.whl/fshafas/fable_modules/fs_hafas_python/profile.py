from __future__ import annotations
from typing import (Optional, Any, List)
from ..fs_hafas_python.parse.arrival_or_departure import (parse_arrival, parse_departure)
from ..fs_hafas_python.parse.common import parse_common
from ..fs_hafas_python.parse.date_time import parse_date_time
from ..fs_hafas_python.parse.hint import parse_hint
from ..fs_hafas_python.parse.icon import parse_icon
from ..fs_hafas_python.parse.journey import parse_journey
from ..fs_hafas_python.parse.journey_leg import (parse_journey_leg, parse_platform)
from ..fs_hafas_python.parse.line import parse_line
from ..fs_hafas_python.parse.location import parse_locations
from ..fs_hafas_python.parse.movement import parse_movement
from ..fs_hafas_python.parse.operator import parse_operator
from ..fs_hafas_python.parse.polyline import parse_polyline
from ..fs_hafas_python.parse.products_bitmask import parse_bitmask
from ..fs_hafas_python.parse.stopover import (parse_stopover, parse_stopovers)
from ..fs_hafas_python.parse.trip import parse_trip
from ..fs_hafas_python.parse.warning import parse_warning
from ..fs_hafas_python.parse.when import parse_when
from .context import (Profile__ctor_35A3D895, Context, CommonData, Platform, ParsedWhen, Profile)
from .types_hafas_client import (JourneysOptions, Alternative, Icon, FeatureCollection, Line, Journey, Leg, Movement, Operator, StopOver, Trip, IndexMap_2, Warning)
from .types_raw_hafas_client import (TripSearchRequest, RawCommon, RawJny, RawRem, RawIco, RawPoly, RawLoc, RawProd, RawOutCon, RawSec, RawOp, RawStop, RawHim)

def default_profile() -> Profile:
    def arrow_432(x: str) -> str:
        return x
    
    def arrow_433(_arg1: Optional[JourneysOptions], q: TripSearchRequest) -> TripSearchRequest:
        return q
    
    def arrow_434(ctx: Context, c: RawCommon) -> CommonData:
        return parse_common(ctx, c)
    
    def arrow_435(ctx_1: Context, d: RawJny) -> Alternative:
        return parse_arrival(ctx_1, d)
    
    def arrow_436(ctx_2: Context, d_1: RawJny) -> Alternative:
        return parse_departure(ctx_2, d_1)
    
    def arrow_437(ctx_3: Context, h: RawRem) -> Optional[Any]:
        return parse_hint(ctx_3, h)
    
    def arrow_438(ctx_4: Context, i: RawIco) -> Optional[Icon]:
        return parse_icon(ctx_4, i)
    
    def arrow_439(ctx_5: Context, poly: RawPoly) -> FeatureCollection:
        return parse_polyline(ctx_5, poly)
    
    def arrow_440(ctx_6: Context, loc_l: List[RawLoc]) -> List[Any]:
        return parse_locations(ctx_6, loc_l)
    
    def arrow_441(ctx_7: Context, p: RawProd) -> Line:
        return parse_line(ctx_7, p)
    
    def arrow_442(ctx_8: Context, j: RawOutCon) -> Journey:
        return parse_journey(ctx_8, j)
    
    def arrow_443(ctx_9: Context, pt: RawSec, date: str) -> Leg:
        return parse_journey_leg(ctx_9, pt, date)
    
    def arrow_444(ctx_10: Context, m: RawJny) -> Movement:
        return parse_movement(ctx_10, m)
    
    def arrow_445(ctx_11: Context, a: RawOp) -> Operator:
        return parse_operator(ctx_11, a)
    
    def arrow_446(ctx_12: Context, platf_s: Optional[str]=None, platf_r: Optional[str]=None, cncl: Optional[bool]=None) -> Platform:
        return parse_platform(ctx_12, platf_s, platf_r, cncl)
    
    def arrow_447(ctx_13: Context, st: RawStop, date_1: str) -> StopOver:
        return parse_stopover(ctx_13, st, date_1)
    
    def arrow_448(ctx_14: Context, stop_l: Optional[List[RawStop]], date_2: str) -> Optional[List[StopOver]]:
        return parse_stopovers(ctx_14, stop_l, date_2)
    
    def arrow_449(ctx_15: Context, j_1: RawJny) -> Trip:
        return parse_trip(ctx_15, j_1)
    
    def arrow_450(ctx_16: Context, date_3: str, time_s: Optional[str]=None, time_r: Optional[str]=None, tz_offset: Optional[int]=None, cncl_1: Optional[bool]=None) -> ParsedWhen:
        return parse_when(ctx_16, date_3, time_s, time_r, tz_offset, cncl_1)
    
    def arrow_451(ctx_17: Context, date_4: str, time: Optional[str]=None, tz_offset_1: Optional[int]=None) -> Optional[str]:
        return parse_date_time(ctx_17, date_4, time, tz_offset_1)
    
    def arrow_452(ctx_18: Context, bitmask: int) -> IndexMap_2[str, bool]:
        return parse_bitmask(ctx_18, bitmask)
    
    def arrow_453(ctx_19: Context, w: RawHim) -> Warning:
        return parse_warning(ctx_19, w)
    
    return Profile__ctor_35A3D895("de-DE", "Europe/Berlin", arrow_432, arrow_433, arrow_434, arrow_435, arrow_436, arrow_437, arrow_438, arrow_439, arrow_440, arrow_441, arrow_442, arrow_443, arrow_444, arrow_445, arrow_446, arrow_447, arrow_448, arrow_449, arrow_450, arrow_451, arrow_452, arrow_453)


