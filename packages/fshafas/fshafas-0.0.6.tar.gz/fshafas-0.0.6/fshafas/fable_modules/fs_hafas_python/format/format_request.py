from __future__ import annotations
from typing import (Any, TypeVar, Optional, Callable, List, Tuple)
from ...fable_library.array import (fold, filter)
from ...fable_library.date import create
from ...fable_library.int32 import parse
from ...fable_library.option import (value as value_6, map)
from ...fable_library.string import substring
from ...fable_library.util import int32_to_string
from ...fs_hafas_python.context import (Profile, Profile__get_formatStation, Profile__get_departuresGetPasslist, Profile__get_departuresStbFltrEquiv, Profile__get_journeysOutFrwd, Profile__get_transformJourneysQuery)
from ...fs_hafas_python.extensions import (DateTimeEx_formatDate, DateTimeEx_formatTime)
from ...fs_hafas_python.lib.transformations import (Default_LocationsOptions, Coordinate_fromFloat, Default_DeparturesArrivalsOptions, Default_RefreshJourneyOptions, Default_NearByOptions, Default_ReachableFromOptions, Default_RadarOptions, Default_TripOptions, Default_RemarksOptions, Default_JourneysOptions, Default_JourneysFromTripOptions)
from ...fs_hafas_python.types_hafas_client import (IndexMap_2, ProductType, IndexMap_2__get_Item_2B595, LocationsOptions, Location, Stop, Station, DeparturesArrivalsOptions, RefreshJourneyOptions, TripsByNameOptions, StopOptions, NearByOptions, ReachableFromOptions, BoundingBox, RadarOptions, TripOptions, LinesOptions, RemarksOptions, JourneysOptions, StopOver, JourneysFromTripOptions)
from ...fs_hafas_python.types_raw_hafas_client import (JnyFltr, Loc, LocMatchInput, LocMatchRequest, StationBoardRequest, ReconstructionRequest, JourneyMatchRequest, LocDetailsRequest, RawcCrd, RawRing, LocGeoPosRequest, LocGeoReachRequest, RawCrd, RawRect, JourneyGeoPosRequest, JourneyDetailsRequest, LineMatchRequest, HimSearchRequest, LocViaInput, TripSearchRequest, LocData, SearchOnTripRequest)

_A = TypeVar("_A")

_B = TypeVar("_B")

def ParseIsoString(datetime: str) -> Any:
    year : int = parse(substring(datetime, 0, 4), 511, False, 32) or 0
    month : int = parse(substring(datetime, 5, 2), 511, False, 32) or 0
    day : int = parse(substring(datetime, 8, 2), 511, False, 32) or 0
    hour : int = parse(substring(datetime, 11, 2), 511, False, 32) or 0
    minute : int = parse(substring(datetime, 14, 2), 511, False, 32) or 0
    tz_offset : int = (60 * parse(substring(datetime, 20, 2), 511, False, 32)) or 0
    return create(year, month, day, hour, minute, 0)


def maybe_get_option_value(opt: Optional[_A], getter: Callable[[_A], Optional[_B]]) -> Optional[_B]:
    if opt is None:
        return None
    
    else: 
        return getter(value_6(opt))
    


def get_option_value(opt: Optional[_A], getter: Callable[[_A], Optional[_B]], default_opt: _A) -> _B:
    default_value : _B
    match_value : Optional[_B] = getter(default_opt)
    if match_value is None:
        raise Exception("getOptionValue: value expected")
    
    else: 
        default_value = value_6(match_value)
    
    if opt is None:
        return default_value
    
    else: 
        match_value_1 : Optional[_B] = getter(value_6(opt))
        if match_value_1 is None:
            return default_value
        
        else: 
            return value_6(match_value_1)
        
    


def format_date(dt: Any) -> str:
    return DateTimeEx_formatDate(dt, "yyyyMMdd")


def format_time(dt: Any) -> str:
    return DateTimeEx_formatTime(dt, "HHmm") + "00"


def format_products_bitmask(profile: Profile, products: IndexMap_2[str, bool]) -> int:
    def folder(bitmask: int, p_1: ProductType, profile: Profile=profile, products: IndexMap_2[str, bool]=products) -> int:
        return p_1.bitmasks[0] | bitmask
    
    def predicate(p: ProductType, profile: Profile=profile, products: IndexMap_2[str, bool]=products) -> bool:
        return IndexMap_2__get_Item_2B595(products, p.id)
    
    return fold(folder, 0, filter(predicate, profile.products))


def make_filters(profile: Profile, products: IndexMap_2[str, bool]) -> List[JnyFltr]:
    bitmask : int = format_products_bitmask(profile, products) or 0
    if bitmask != 0:
        return [JnyFltr("PROD", "INC", int32_to_string(bitmask), None)]
    
    else: 
        return []
    


def location_request(profile: Profile, name: str, opt: Optional[LocationsOptions]=None) -> LocMatchRequest:
    def arrow_352(v: LocationsOptions, profile: Profile=profile, name: str=name, opt: Optional[LocationsOptions]=opt) -> Optional[bool]:
        return v.fuzzy
    
    def arrow_353(v_1: LocationsOptions, profile: Profile=profile, name: str=name, opt: Optional[LocationsOptions]=opt) -> Optional[int]:
        return v_1.results
    
    return LocMatchRequest(LocMatchInput(Loc("ALL", name + ("?" if get_option_value(opt, arrow_352, Default_LocationsOptions) else ""), None), get_option_value(opt, arrow_353, Default_LocationsOptions), "S"))


def make_loc_ltype_s(profile: Profile, id: str) -> Loc:
    return Loc("S", None, ("A=1@L=" + Profile__get_formatStation(profile)(id)) + "@")


def make_locl_type_a(location: Location) -> Loc:
    x : int
    match_value : Optional[float] = location.longitude
    if match_value is None:
        raise Exception("location.longitude")
    
    else: 
        x = Coordinate_fromFloat(match_value)
    
    y : int
    match_value_1 : Optional[float] = location.latitude
    if match_value_1 is None:
        raise Exception("location.latitude")
    
    else: 
        y = Coordinate_fromFloat(match_value_1)
    
    xs : str = int32_to_string(x)
    ys : str = int32_to_string(y)
    match_value_2 : Optional[str] = location.address
    if match_value_2 is None:
        return Loc("A", None, ((("A=1@X=" + xs) + "@Y=") + ys) + "@")
    
    else: 
        name : str = match_value_2
        return Loc("A", name, ((((("A=2@O=" + name) + "@X=") + xs) + "@Y=") + ys) + "@")
    


def make_loc_type(profile: Profile, s: Any=None) -> Loc:
    (pattern_matching_result, v_1, v_2) = (None, None, None)
    if str(type(s)) == "\u003cclass \u0027str\u0027\u003e":
        pattern_matching_result = 0
        v_1 = s
    
    elif isinstance(s, Station):
        if s.id is not None:
            pattern_matching_result = 1
            v_2 = s
        
        else: 
            pattern_matching_result = 2
        
    
    else: 
        pattern_matching_result = 2
    
    if pattern_matching_result == 0:
        return make_loc_ltype_s(profile, v_1)
    
    elif pattern_matching_result == 1:
        return make_loc_ltype_s(profile, value_6(v_2.id))
    
    elif pattern_matching_result == 2:
        (pattern_matching_result_1, v_4) = (None, None)
        if isinstance(s, Stop):
            if s.id is not None:
                pattern_matching_result_1 = 0
                v_4 = s
            
            else: 
                pattern_matching_result_1 = 1
            
        
        else: 
            pattern_matching_result_1 = 1
        
        if pattern_matching_result_1 == 0:
            return make_loc_ltype_s(profile, value_6(v_4.id))
        
        elif pattern_matching_result_1 == 1:
            (pattern_matching_result_2, v_6) = (None, None)
            if isinstance(s, Location):
                if s.id is not None:
                    pattern_matching_result_2 = 0
                    v_6 = s
                
                else: 
                    pattern_matching_result_2 = 1
                
            
            else: 
                pattern_matching_result_2 = 1
            
            if pattern_matching_result_2 == 0:
                return make_loc_ltype_s(profile, value_6(v_6.id))
            
            elif pattern_matching_result_2 == 1:
                if isinstance(s, Location):
                    return make_locl_type_a(s)
                
                else: 
                    raise Exception("makeLocType")
                
            
        
    


def station_board_request(profile: Profile, type: str, name: Any=None, opt: Optional[DeparturesArrivalsOptions]=None) -> StationBoardRequest:
    def arrow_354(v: DeparturesArrivalsOptions, profile: Profile=profile, type: str=type, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Optional[Any]:
        return v.when
    
    dt : Any = get_option_value(opt, arrow_354, Default_DeparturesArrivalsOptions)
    date : str = format_date(dt)
    time : str = format_time(dt)
    def arrow_355(v_1: DeparturesArrivalsOptions, profile: Profile=profile, type: str=type, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Optional[int]:
        return v_1.duration
    
    duration : int = get_option_value(opt, arrow_355, Default_DeparturesArrivalsOptions) or 0
    def arrow_356(v_2: DeparturesArrivalsOptions, profile: Profile=profile, type: str=type, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Optional[bool]:
        return v_2.stopovers
    
    stopovers : bool = get_option_value(opt, arrow_356, Default_DeparturesArrivalsOptions) if Profile__get_departuresGetPasslist(profile) else False
    def arrow_357(v_3: DeparturesArrivalsOptions, profile: Profile=profile, type: str=type, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Optional[bool]:
        return v_3.include_related_stations
    
    include_related_stations : bool = get_option_value(opt, arrow_357, Default_DeparturesArrivalsOptions) if Profile__get_departuresStbFltrEquiv(profile) else False
    def arrow_358(v_4: DeparturesArrivalsOptions, profile: Profile=profile, type: str=type, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_4.products
    
    filters : List[JnyFltr] = make_filters(profile, get_option_value(opt, arrow_358, Default_DeparturesArrivalsOptions))
    return StationBoardRequest(type, date, time, make_loc_type(profile, name), filters, duration)


def reconstruction_request(profile: Profile, refresh_token: str, opt: Optional[RefreshJourneyOptions]=None) -> ReconstructionRequest:
    def arrow_359(v: RefreshJourneyOptions, profile: Profile=profile, refresh_token: str=refresh_token, opt: Optional[RefreshJourneyOptions]=opt) -> Optional[bool]:
        return v.polylines
    
    polylines : bool = get_option_value(opt, arrow_359, Default_RefreshJourneyOptions)
    def arrow_360(v_1: RefreshJourneyOptions, profile: Profile=profile, refresh_token: str=refresh_token, opt: Optional[RefreshJourneyOptions]=opt) -> Optional[bool]:
        return v_1.stopovers
    
    def arrow_361(v_2: RefreshJourneyOptions, profile: Profile=profile, refresh_token: str=refresh_token, opt: Optional[RefreshJourneyOptions]=opt) -> Optional[bool]:
        return v_2.tickets
    
    return ReconstructionRequest(True, get_option_value(opt, arrow_360, Default_RefreshJourneyOptions), polylines, get_option_value(opt, arrow_361, Default_RefreshJourneyOptions), refresh_token)


def journey_match_request(profile: Profile, line_name: str, opt: Optional[TripsByNameOptions]=None) -> JourneyMatchRequest:
    def arrow_362(dt: Any, profile: Profile=profile, line_name: str=line_name, opt: Optional[TripsByNameOptions]=opt) -> str:
        return format_date(dt)
    
    def arrow_363(v: TripsByNameOptions, profile: Profile=profile, line_name: str=line_name, opt: Optional[TripsByNameOptions]=opt) -> Optional[Any]:
        return v.when
    
    return JourneyMatchRequest(line_name, map(arrow_362, maybe_get_option_value(opt, arrow_363)))


def loc_details_request(profile: Profile, stop: Any=None, opt: Optional[StopOptions]=None) -> LocDetailsRequest:
    def arrow_364(profile: Profile=profile, stop: Any=stop, opt: Optional[StopOptions]=opt) -> str:
        raise Exception("Stop expected")
    
    return LocDetailsRequest([make_loc_ltype_s(profile, (value_6(stop.id) if (stop.id is not None) else arrow_364()) if isinstance(stop, Stop) else stop)])


def loc_geo_pos_request(profile: Profile, location: Location, opt: Optional[NearByOptions]=None) -> LocGeoPosRequest:
    def arrow_365(v: NearByOptions, profile: Profile=profile, location: Location=location, opt: Optional[NearByOptions]=opt) -> Optional[int]:
        return v.results
    
    results : int = get_option_value(opt, arrow_365, Default_NearByOptions) or 0
    def arrow_366(v_1: NearByOptions, profile: Profile=profile, location: Location=location, opt: Optional[NearByOptions]=opt) -> Optional[bool]:
        return v_1.stops
    
    stops : bool = get_option_value(opt, arrow_366, Default_NearByOptions)
    def arrow_367(v_2: NearByOptions, profile: Profile=profile, location: Location=location, opt: Optional[NearByOptions]=opt) -> Optional[int]:
        return v_2.distance
    
    distance : int = get_option_value(opt, arrow_367, Default_NearByOptions) or 0
    def arrow_368(v_3: NearByOptions, profile: Profile=profile, location: Location=location, opt: Optional[NearByOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_3.products
    
    filters : List[JnyFltr] = make_filters(profile, get_option_value(opt, arrow_368, Default_NearByOptions))
    def arrow_369(profile: Profile=profile, location: Location=location, opt: Optional[NearByOptions]=opt) -> int:
        match_value : Optional[float] = location.longitude
        if match_value is None:
            raise Exception("location.longitude")
        
        else: 
            return Coordinate_fromFloat(match_value)
        
    
    def arrow_370(profile: Profile=profile, location: Location=location, opt: Optional[NearByOptions]=opt) -> int:
        match_value_1 : Optional[float] = location.latitude
        if match_value_1 is None:
            raise Exception("location.latitude")
        
        else: 
            return Coordinate_fromFloat(match_value_1)
        
    
    return LocGeoPosRequest(RawRing(RawcCrd(arrow_369(), arrow_370()), distance, 0), filters, False, stops, results)


def loc_geo_reach_request(profile: Profile, location: Location, opt: Optional[ReachableFromOptions]=None) -> LocGeoReachRequest:
    def arrow_371(v: ReachableFromOptions, profile: Profile=profile, location: Location=location, opt: Optional[ReachableFromOptions]=opt) -> Optional[Any]:
        return v.when
    
    dt : Any = get_option_value(opt, arrow_371, Default_ReachableFromOptions)
    date : str = format_date(dt)
    time : str = format_time(dt)
    def arrow_372(v_1: ReachableFromOptions, profile: Profile=profile, location: Location=location, opt: Optional[ReachableFromOptions]=opt) -> Optional[int]:
        return v_1.max_duration
    
    max_duration : int = get_option_value(opt, arrow_372, Default_ReachableFromOptions) or 0
    def arrow_373(v_2: ReachableFromOptions, profile: Profile=profile, location: Location=location, opt: Optional[ReachableFromOptions]=opt) -> Optional[int]:
        return v_2.max_transfers
    
    max_transfers : int = get_option_value(opt, arrow_373, Default_ReachableFromOptions) or 0
    def arrow_374(v_3: ReachableFromOptions, profile: Profile=profile, location: Location=location, opt: Optional[ReachableFromOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_3.products
    
    filters : List[JnyFltr] = make_filters(profile, get_option_value(opt, arrow_374, Default_ReachableFromOptions))
    return LocGeoReachRequest(make_locl_type_a(location), max_duration, max_transfers, date, time, 120, filters)


def journey_geo_pos_request(profile: Profile, rect: BoundingBox, opt: Optional[RadarOptions]=None) -> JourneyGeoPosRequest:
    if rect.north <= rect.south:
        raise Exception("north must be larger than south.")
    
    if rect.east <= rect.west:
        raise Exception("east must be larger than west.")
    
    def arrow_375(v: RadarOptions, profile: Profile=profile, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Optional[Any]:
        return v.when
    
    dt : Any = get_option_value(opt, arrow_375, Default_RadarOptions)
    date : str = format_date(dt)
    time : str = format_time(dt)
    def arrow_376(v_1: RadarOptions, profile: Profile=profile, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Optional[int]:
        return v_1.results
    
    results : int = get_option_value(opt, arrow_376, Default_RadarOptions) or 0
    def arrow_377(v_2: RadarOptions, profile: Profile=profile, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Optional[int]:
        return v_2.duration
    
    duration : int = get_option_value(opt, arrow_377, Default_RadarOptions) or 0
    def arrow_378(v_3: RadarOptions, profile: Profile=profile, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Optional[int]:
        return v_3.frames
    
    frames : int = get_option_value(opt, arrow_378, Default_RadarOptions) or 0
    def arrow_379(v_4: RadarOptions, profile: Profile=profile, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_4.products
    
    filters : List[JnyFltr] = make_filters(profile, get_option_value(opt, arrow_379, Default_RadarOptions))
    return JourneyGeoPosRequest(results, False, date, time, RawRect(RawCrd(Coordinate_fromFloat(rect.west), Coordinate_fromFloat(rect.south), None), RawCrd(Coordinate_fromFloat(rect.east), Coordinate_fromFloat(rect.north), None)), duration * 1000, (duration // frames) * 1000, True, filters, "CALC")


def trip_request(profile: Profile, id: str, name: str, opt: Optional[TripOptions]=None) -> JourneyDetailsRequest:
    def arrow_380(v: TripOptions, profile: Profile=profile, id: str=id, name: str=name, opt: Optional[TripOptions]=opt) -> Optional[bool]:
        return v.polyline
    
    return JourneyDetailsRequest(id, name, get_option_value(opt, arrow_380, Default_TripOptions))


def line_match_request(profile: Profile, query: str, opt: Optional[LinesOptions]=None) -> LineMatchRequest:
    return LineMatchRequest(query)


def server_info_request() -> Any:
    return None


def him_search_request(profile: Profile, opt: Optional[RemarksOptions]=None) -> HimSearchRequest:
    def arrow_381(v: RemarksOptions, profile: Profile=profile, opt: Optional[RemarksOptions]=opt) -> Optional[Any]:
        return v.from_
    
    dt : Any = get_option_value(opt, arrow_381, Default_RemarksOptions)
    date : str = format_date(dt)
    time : str = format_time(dt)
    def arrow_382(v_1: RemarksOptions, profile: Profile=profile, opt: Optional[RemarksOptions]=opt) -> Optional[int]:
        return v_1.results
    
    results : int = get_option_value(opt, arrow_382, Default_RemarksOptions) or 0
    def arrow_383(v_2: RemarksOptions, profile: Profile=profile, opt: Optional[RemarksOptions]=opt) -> Optional[bool]:
        return v_2.polylines
    
    polylines : bool = get_option_value(opt, arrow_383, Default_RemarksOptions)
    def arrow_384(v_3: RemarksOptions, profile: Profile=profile, opt: Optional[RemarksOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_3.products
    
    return HimSearchRequest(make_filters(profile, get_option_value(opt, arrow_384, Default_RemarksOptions)), polylines, results, date, time)


def journey_request(profile: Profile, from_: Any=None, to: Any=None, opt: Optional[JourneysOptions]=None) -> TripSearchRequest:
    if opt is None:
        pass
    
    else: 
        opt_1 : JourneysOptions = opt
        if (not Profile__get_journeysOutFrwd(profile)) if (opt_1.arrival is not None) else False:
            raise Exception("opt.arrival is unsupported")
        
        if opt_1.earlier_than is not None:
            raise Exception("opt.earlierThan nyi")
        
        if opt_1.later_than is not None:
            raise Exception("opt.laterThan nyi")
        
    
    def arrow_386(profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Any:
        opt_v_1 : JourneysOptions = opt
        return value_6(opt_v_1.arrival)
    
    def arrow_387(v: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[Any]:
        return v.departure
    
    def arrow_388(v: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[Any]:
        return v.departure
    
    dt : Any = (arrow_386() if (opt.arrival is not None) else get_option_value(opt, arrow_387, Default_JourneysOptions)) if (opt is not None) else get_option_value(opt, arrow_388, Default_JourneysOptions)
    date : str = format_date(dt)
    time : str = format_time(dt)
    out_frwd : bool = False if ((value_6(opt).arrival is not None) if (opt is not None) else False) else True
    def arrow_389(v_1: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[int]:
        return v_1.results
    
    results : int = get_option_value(opt, arrow_389, Default_JourneysOptions) or 0
    def arrow_390(v_2: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[bool]:
        return v_2.stopovers
    
    stopovers : bool = get_option_value(opt, arrow_390, Default_JourneysOptions)
    def arrow_391(v_3: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[int]:
        return v_3.transfer_time
    
    transfer_time : int = get_option_value(opt, arrow_391, Default_JourneysOptions) or 0
    def arrow_392(v_4: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[bool]:
        return v_4.tickets
    
    tickets : bool = get_option_value(opt, arrow_392, Default_JourneysOptions)
    def arrow_393(v_5: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[bool]:
        return v_5.polylines
    
    polylines : bool = get_option_value(opt, arrow_393, Default_JourneysOptions)
    def arrow_394(v_6: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_6.products
    
    filters : List[JnyFltr] = make_filters(profile, get_option_value(opt, arrow_394, Default_JourneysOptions))
    via_loc_l : Optional[List[LocViaInput]]
    def arrow_395(v_7: JourneysOptions, profile: Profile=profile, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Optional[str]:
        return v_7.via
    
    match_value : Optional[str] = maybe_get_option_value(opt, arrow_395)
    via_loc_l = None if (match_value is None) else [LocViaInput(make_loc_ltype_s(profile, match_value))]
    return Profile__get_transformJourneysQuery(profile)(opt)(TripSearchRequest(stopovers, -1, transfer_time, [make_loc_type(profile, from_)], via_loc_l, [make_loc_type(profile, to)], filters, [], tickets, True, True, False, polylines, date, time, results, out_frwd, None))


def search_on_trip_request(profile: Profile, trip_id: str, previous_stopover: StopOver, to: Any=None, opt: Optional[JourneysFromTripOptions]=None) -> SearchOnTripRequest:
    prev_stop_id : str
    match_value : Optional[Any] = previous_stopover.stop
    (pattern_matching_result, station_1) = (None, None)
    if match_value is not None:
        if isinstance(value_6(match_value), Station):
            if value_6(match_value).id is not None:
                pattern_matching_result = 0
                station_1 = value_6(match_value)
            
            else: 
                pattern_matching_result = 1
            
        
        else: 
            pattern_matching_result = 1
        
    
    else: 
        pattern_matching_result = 1
    
    if pattern_matching_result == 0:
        prev_stop_id = value_6(station_1.id)
    
    elif pattern_matching_result == 1:
        (pattern_matching_result_1, stop_1) = (None, None)
        if match_value is not None:
            if isinstance(value_6(match_value), Stop):
                if value_6(match_value).id is not None:
                    pattern_matching_result_1 = 0
                    stop_1 = value_6(match_value)
                
                else: 
                    pattern_matching_result_1 = 1
                
            
            else: 
                pattern_matching_result_1 = 1
            
        
        else: 
            pattern_matching_result_1 = 1
        
        if pattern_matching_result_1 == 0:
            prev_stop_id = value_6(stop_1.id)
        
        elif pattern_matching_result_1 == 1:
            raise Exception("previousStopover.stop must be a valid stop or station.")
        
    
    dep_at_prev_stop : Any
    match_value_1 : Tuple[Optional[str], Optional[str]] = (previous_stopover.departure, previous_stopover.planned_departure)
    if match_value_1[0] is not None:
        dep_at_prev_stop = ParseIsoString(match_value_1[0])
    
    elif match_value_1[1] is not None:
        dep_at_prev_stop = ParseIsoString(match_value_1[1])
    
    else: 
        raise Exception("previousStopover.(planned)departure is invalid.")
    
    def arrow_396(v: JourneysFromTripOptions, profile: Profile=profile, trip_id: str=trip_id, previous_stopover: StopOver=previous_stopover, to: Any=to, opt: Optional[JourneysFromTripOptions]=opt) -> Optional[bool]:
        return v.tickets
    
    tickets : bool = get_option_value(opt, arrow_396, Default_JourneysFromTripOptions)
    def arrow_397(v_1: JourneysFromTripOptions, profile: Profile=profile, trip_id: str=trip_id, previous_stopover: StopOver=previous_stopover, to: Any=to, opt: Optional[JourneysFromTripOptions]=opt) -> Optional[int]:
        return v_1.transfer_time
    
    transfer_time : int = get_option_value(opt, arrow_397, Default_JourneysFromTripOptions) or 0
    def arrow_398(v_2: JourneysFromTripOptions, profile: Profile=profile, trip_id: str=trip_id, previous_stopover: StopOver=previous_stopover, to: Any=to, opt: Optional[JourneysFromTripOptions]=opt) -> Optional[bool]:
        return v_2.polylines
    
    polylines : bool = get_option_value(opt, arrow_398, Default_JourneysFromTripOptions)
    def arrow_399(v_3: JourneysFromTripOptions, profile: Profile=profile, trip_id: str=trip_id, previous_stopover: StopOver=previous_stopover, to: Any=to, opt: Optional[JourneysFromTripOptions]=opt) -> Optional[bool]:
        return v_3.stopovers
    
    stopovers : bool = get_option_value(opt, arrow_399, Default_JourneysFromTripOptions)
    def arrow_400(v_4: JourneysFromTripOptions, profile: Profile=profile, trip_id: str=trip_id, previous_stopover: StopOver=previous_stopover, to: Any=to, opt: Optional[JourneysFromTripOptions]=opt) -> Optional[IndexMap_2[str, bool]]:
        return v_4.products
    
    filters : List[JnyFltr] = make_filters(profile, get_option_value(opt, arrow_400, Default_JourneysFromTripOptions))
    return SearchOnTripRequest("JI", trip_id, LocData(make_loc_ltype_s(profile, prev_stop_id), "DEP", format_date(dep_at_prev_stop), format_time(dep_at_prev_stop)), [make_loc_type(profile, to)], filters, stopovers, polylines, transfer_time, tickets)


