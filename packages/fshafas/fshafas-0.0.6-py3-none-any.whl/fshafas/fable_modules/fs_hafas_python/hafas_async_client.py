from __future__ import annotations
from typing import (Optional, List, Any, Tuple, TypeVar)
from ..fable_library.array import (filter, fold)
from ..fable_library.async_builder import (singleton, Async)
from ..fable_library.reflection import (TypeInfo, class_type)
from ..fable_library.util import IDisposable
from ..fs_hafas_python.format.format_request import (journey_request, reconstruction_request, search_on_trip_request, trip_request, station_board_request, location_request, loc_details_request, loc_geo_pos_request, loc_geo_reach_request, journey_geo_pos_request, journey_match_request, him_search_request, line_match_request, server_info_request)
from ..fs_hafas_python.lib.transformations import (MergeOptions_JourneysOptions, Default_Journey, MergeOptions_JourneysFromTripOptions, Default_Trip, MergeOptions_LocationsOptions, MergeOptions_NearByOptions)
from ..fs_hafas_python.parse.arrival_or_departure import (DEP, ARR)
from ..fs_hafas_python.parse.journey import distance_of_journey
from .context import (Profile__get_cfg, Profile__get_baseRequest, Profile__get_salt, Profile)
from .hafas_raw_client import (HafasRawClient__Dispose, HafasRawClient__ctor_6D5FF7F7, HafasRawClient__AsyncTripSearch_Z4E830477, HafasRawClient__AsyncReconstruction_Z53F036CE, HafasRawClient__AsyncSearchOnTrip_1713A0E8, HafasRawClient__AsyncJourneyDetails_39A8152A, HafasRawClient__AsyncStationBoard_49AFED38, HafasRawClient__AsyncLocMatch_324CF02B, HafasRawClient__AsyncLocDetails_659C62DA, HafasRawClient__AsyncLocGeoPos_765D46F9, HafasRawClient__AsyncLocGeoReach_78598228, HafasRawClient__AsyncJourneyGeoPos_Z27E4B537, HafasRawClient__AsyncJourneyMatch_Z2BB017E5, HafasRawClient__AsyncHimSearch_Z2A604406, HafasRawClient__AsyncLineMatch_Z23F97D3B, HafasRawClient__AsyncServerInfo_4E60E31B)
from .parser import (parse_journeys, parse_common, default_options, parse_journey, parse_journeys_array, parse_trip, parse_departures_arrivals, parse_locations, parse_location, parse_durations, parse_movements, parse_trips, parse_warnings, parse_lines, parse_server_info)
from .types_hafas_client import (ProductType, IndexMap_2, IndexMap_2__set_Item_541DA560, IndexMap_2__ctor_2B594, JourneysOptions, Journeys, RefreshJourneyOptions, Journey, StopOver, JourneysFromTripOptions, TripOptions, Trip, DeparturesArrivalsOptions, Alternative, LocationsOptions, StopOptions, Location, NearByOptions, ReachableFromOptions, Duration, BoundingBox, RadarOptions, Movement, TripsByNameOptions, RemarksOptions, Warning, LinesOptions, Line, ServerOptions, ServerInfo, Log_Print)
from .types_raw_hafas_client import (Cfg, RawRequest, RawCommon, RawResult, RawOutCon, RawJny, RawLoc, RawPos, RawHim, RawLine)

_A_ = TypeVar("_A_")

def expr_459() -> TypeInfo:
    return class_type("FsHafas.Api.HafasAsyncClient", None, HafasAsyncClient)


class HafasAsyncClient(IDisposable):
    def __init__(self, profile: Profile) -> None:
        self.profile = profile
        cfg_1 : Cfg
        match_value : Optional[Cfg] = Profile__get_cfg(self.profile)
        if match_value is None:
            raise Exception("profile.cfg")
        
        else: 
            cfg_1 = match_value
        
        base_request_1 : RawRequest
        match_value_1 : Optional[RawRequest] = Profile__get_baseRequest(self.profile)
        if match_value_1 is None:
            raise Exception("profile.baseRequest")
        
        else: 
            base_request_1 = match_value_1
        
        self.http_client = HafasRawClient__ctor_6D5FF7F7(self.profile.endpoint, Profile__get_salt(self.profile), cfg_1, base_request_1)
    
    def Dispose(self) -> None:
        __ : HafasAsyncClient = self
        HafasRawClient__Dispose(__.http_client)
    

HafasAsyncClient_reflection = expr_459

def HafasAsyncClient__ctor_Z3AB94A1B(profile: Profile) -> HafasAsyncClient:
    return HafasAsyncClient(profile)


def HafasAsyncClient_initSerializer() -> None:
    pass


def HafasAsyncClient_productsOfMode(profile: Profile, mode: str) -> IndexMap_2[str, bool]:
    def predicate(p: ProductType, profile: Profile=profile, mode: str=mode) -> bool:
        if p.mode == mode:
            return p.name != "Tram"
        
        else: 
            return False
        
    
    array_1 : List[ProductType] = filter(predicate, profile.products)
    def folder(m: IndexMap_2[str, bool], p_1: ProductType, profile: Profile=profile, mode: str=mode) -> IndexMap_2[str, bool]:
        IndexMap_2__set_Item_541DA560(m, p_1.id, True)
        return m
    
    return fold(folder, IndexMap_2__ctor_2B594(False), array_1)


def HafasAsyncClient__AsyncJourneys(__: HafasAsyncClient, from_: Any=None, to: Any=None, opt: Optional[JourneysOptions]=None) -> Async[Journeys]:
    def arrow_461(__: HafasAsyncClient=__, from_: Any=from_, to: Any=to, opt: Optional[JourneysOptions]=opt) -> Async[Journeys]:
        def arrow_460(_arg1: Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawOutCon]]]) -> Async[Journeys]:
            return singleton.Return(parse_journeys(_arg1[2], parse_common(__.profile, MergeOptions_JourneysOptions(default_options, opt), _arg1[0], _arg1[1])))
        
        return singleton.Bind(HafasRawClient__AsyncTripSearch_Z4E830477(__.http_client, journey_request(__.profile, from_, to, opt)), arrow_460)
    
    return singleton.Delay(arrow_461)


def HafasAsyncClient__AsyncRefreshJourney(__: HafasAsyncClient, refresh_token: str, opt: Optional[RefreshJourneyOptions]=None) -> Async[Journey]:
    def arrow_463(__: HafasAsyncClient=__, refresh_token: str=refresh_token, opt: Optional[RefreshJourneyOptions]=opt) -> Async[Journey]:
        def arrow_462(_arg2: Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawOutCon]]]) -> Async[Journey]:
            return singleton.Return(parse_journey(_arg2[2], parse_common(__.profile, default_options, _arg2[0], _arg2[1])))
        
        return singleton.Bind(HafasRawClient__AsyncReconstruction_Z53F036CE(__.http_client, reconstruction_request(__.profile, refresh_token, opt)), arrow_462) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.refresh_journey) else singleton.Return(Default_Journey)
    
    return singleton.Delay(arrow_463)


def HafasAsyncClient__AsyncJourneysFromTrip(__: HafasAsyncClient, from_trip_id: str, previous_stop_over: StopOver, to: Any=None, opt: Optional[JourneysFromTripOptions]=None) -> Async[List[Journey]]:
    def arrow_465(__: HafasAsyncClient=__, from_trip_id: str=from_trip_id, previous_stop_over: StopOver=previous_stop_over, to: Any=to, opt: Optional[JourneysFromTripOptions]=opt) -> Async[List[Journey]]:
        def arrow_464(_arg3: Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawOutCon]]]) -> Async[List[Journey]]:
            return singleton.Return(parse_journeys_array(_arg3[2], parse_common(__.profile, MergeOptions_JourneysFromTripOptions(default_options, opt), _arg3[0], _arg3[1])))
        
        return singleton.Bind(HafasRawClient__AsyncSearchOnTrip_1713A0E8(__.http_client, search_on_trip_request(__.profile, from_trip_id, previous_stop_over, to, opt)), arrow_464) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.journeys_from_trip) else singleton.Return([])
    
    return singleton.Delay(arrow_465)


def HafasAsyncClient__AsyncTrip(__: HafasAsyncClient, id: str, name: str, opt: Optional[TripOptions]=None) -> Async[Trip]:
    def arrow_467(__: HafasAsyncClient=__, id: str=id, name: str=name, opt: Optional[TripOptions]=opt) -> Async[Trip]:
        def arrow_466(_arg4: Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawJny]]) -> Async[Trip]:
            return singleton.Return(parse_trip(_arg4[2], parse_common(__.profile, default_options, _arg4[0], _arg4[1])))
        
        return singleton.Bind(HafasRawClient__AsyncJourneyDetails_39A8152A(__.http_client, trip_request(__.profile, id, name, opt)), arrow_466) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.trip) else singleton.Return(Default_Trip)
    
    return singleton.Delay(arrow_467)


def HafasAsyncClient__AsyncDepartures(__: HafasAsyncClient, name: Any=None, opt: Optional[DeparturesArrivalsOptions]=None) -> Async[List[Alternative]]:
    def arrow_469(__: HafasAsyncClient=__, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Async[List[Alternative]]:
        def arrow_468(_arg5: Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]) -> Async[List[Alternative]]:
            return singleton.Return(parse_departures_arrivals(DEP, _arg5[2], parse_common(__.profile, default_options, _arg5[0], _arg5[1])))
        
        return singleton.Bind(HafasRawClient__AsyncStationBoard_49AFED38(__.http_client, station_board_request(__.profile, DEP, name, opt)), arrow_468)
    
    return singleton.Delay(arrow_469)


def HafasAsyncClient__AsyncArrivals(__: HafasAsyncClient, name: Any=None, opt: Optional[DeparturesArrivalsOptions]=None) -> Async[List[Alternative]]:
    def arrow_471(__: HafasAsyncClient=__, name: Any=name, opt: Optional[DeparturesArrivalsOptions]=opt) -> Async[List[Alternative]]:
        def arrow_470(_arg6: Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]) -> Async[List[Alternative]]:
            return singleton.Return(parse_departures_arrivals(ARR, _arg6[2], parse_common(__.profile, default_options, _arg6[0], _arg6[1])))
        
        return singleton.Bind(HafasRawClient__AsyncStationBoard_49AFED38(__.http_client, station_board_request(__.profile, ARR, name, opt)), arrow_470)
    
    return singleton.Delay(arrow_471)


def HafasAsyncClient__AsyncLocations(__: HafasAsyncClient, name: str, opt: Optional[LocationsOptions]=None) -> Async[List[Any]]:
    def arrow_473(__: HafasAsyncClient=__, name: str=name, opt: Optional[LocationsOptions]=opt) -> Async[List[Any]]:
        def arrow_472(_arg7: Tuple[Optional[RawCommon], Optional[RawResult], List[RawLoc]]) -> Async[List[Any]]:
            return singleton.Return(parse_locations(_arg7[2], parse_common(__.profile, MergeOptions_LocationsOptions(default_options, opt), _arg7[0], _arg7[1])))
        
        return singleton.Bind(HafasRawClient__AsyncLocMatch_324CF02B(__.http_client, location_request(__.profile, name, opt)), arrow_472)
    
    return singleton.Delay(arrow_473)


def HafasAsyncClient__AsyncStop(__: HafasAsyncClient, stop: Any=None, opt: Optional[StopOptions]=None) -> Async[Any]:
    def arrow_475(__: HafasAsyncClient=__, stop: Any=stop, opt: Optional[StopOptions]=opt) -> Async[Any]:
        def arrow_474(_arg8: Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawLoc]]) -> Async[Any]:
            return singleton.Return(parse_location(_arg8[2], parse_common(__.profile, default_options, _arg8[0], _arg8[1])))
        
        return singleton.Bind(HafasRawClient__AsyncLocDetails_659C62DA(__.http_client, loc_details_request(__.profile, stop, opt)), arrow_474)
    
    return singleton.Delay(arrow_475)


def HafasAsyncClient__AsyncNearby(__: HafasAsyncClient, l: Location, opt: Optional[NearByOptions]=None) -> Async[List[Any]]:
    def arrow_477(__: HafasAsyncClient=__, l: Location=l, opt: Optional[NearByOptions]=opt) -> Async[List[Any]]:
        def arrow_476(_arg9: Tuple[Optional[RawCommon], Optional[RawResult], List[RawLoc]]) -> Async[List[Any]]:
            return singleton.Return(parse_locations(_arg9[2], parse_common(__.profile, MergeOptions_NearByOptions(default_options, opt), _arg9[0], _arg9[1])))
        
        return singleton.Bind(HafasRawClient__AsyncLocGeoPos_765D46F9(__.http_client, loc_geo_pos_request(__.profile, l, opt)), arrow_476)
    
    return singleton.Delay(arrow_477)


def HafasAsyncClient__AsyncReachableFrom(__: HafasAsyncClient, l: Location, opt: Optional[ReachableFromOptions]=None) -> Async[List[Duration]]:
    def arrow_479(__: HafasAsyncClient=__, l: Location=l, opt: Optional[ReachableFromOptions]=opt) -> Async[List[Duration]]:
        def arrow_478(_arg10: Tuple[Optional[RawCommon], Optional[RawResult], List[RawPos]]) -> Async[List[Duration]]:
            return singleton.Return(parse_durations(_arg10[2], parse_common(__.profile, default_options, _arg10[0], _arg10[1])))
        
        return singleton.Bind(HafasRawClient__AsyncLocGeoReach_78598228(__.http_client, loc_geo_reach_request(__.profile, l, opt)), arrow_478) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.reachable_from) else singleton.Return([])
    
    return singleton.Delay(arrow_479)


def HafasAsyncClient__AsyncRadar(__: HafasAsyncClient, rect: BoundingBox, opt: Optional[RadarOptions]=None) -> Async[List[Movement]]:
    def arrow_481(__: HafasAsyncClient=__, rect: BoundingBox=rect, opt: Optional[RadarOptions]=opt) -> Async[List[Movement]]:
        def arrow_480(_arg11: Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]) -> Async[List[Movement]]:
            return singleton.Return(parse_movements(_arg11[2], parse_common(__.profile, default_options, _arg11[0], _arg11[1])))
        
        return singleton.Bind(HafasRawClient__AsyncJourneyGeoPos_Z27E4B537(__.http_client, journey_geo_pos_request(__.profile, rect, opt)), arrow_480) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.radar) else singleton.Return([])
    
    return singleton.Delay(arrow_481)


def HafasAsyncClient__AsyncTripsByName(__: HafasAsyncClient, line_name: str, opt: Optional[TripsByNameOptions]=None) -> Async[List[Trip]]:
    def arrow_483(__: HafasAsyncClient=__, line_name: str=line_name, opt: Optional[TripsByNameOptions]=opt) -> Async[List[Trip]]:
        def arrow_482(_arg12: Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]) -> Async[List[Trip]]:
            return singleton.Return(parse_trips(_arg12[2], parse_common(__.profile, default_options, _arg12[0], _arg12[1])))
        
        return singleton.Bind(HafasRawClient__AsyncJourneyMatch_Z2BB017E5(__.http_client, journey_match_request(__.profile, line_name, opt)), arrow_482) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.trips_by_name) else singleton.Return([])
    
    return singleton.Delay(arrow_483)


def HafasAsyncClient__AsyncRemarks_7D671456(__: HafasAsyncClient, opt: Optional[RemarksOptions]=None) -> Async[List[Warning]]:
    def arrow_485(__: HafasAsyncClient=__, opt: Optional[RemarksOptions]=opt) -> Async[List[Warning]]:
        def arrow_484(_arg13: Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawHim]]]) -> Async[List[Warning]]:
            return singleton.Return(parse_warnings(_arg13[2], parse_common(__.profile, default_options, _arg13[0], _arg13[1])))
        
        return singleton.Bind(HafasRawClient__AsyncHimSearch_Z2A604406(__.http_client, him_search_request(__.profile, opt)), arrow_484) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.remarks) else singleton.Return([])
    
    return singleton.Delay(arrow_485)


def HafasAsyncClient__AsyncLines(__: HafasAsyncClient, query: str, opt: Optional[LinesOptions]=None) -> Async[List[Line]]:
    def arrow_487(__: HafasAsyncClient=__, query: str=query, opt: Optional[LinesOptions]=opt) -> Async[List[Line]]:
        def arrow_486(_arg14: Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawLine]]]) -> Async[List[Line]]:
            return singleton.Return(parse_lines(_arg14[2], parse_common(__.profile, default_options, _arg14[0], _arg14[1])))
        
        return singleton.Bind(HafasRawClient__AsyncLineMatch_Z23F97D3B(__.http_client, line_match_request(__.profile, query, opt)), arrow_486) if HafasAsyncClient__enabled_6FCE9E49(__, __.profile.lines) else singleton.Return([])
    
    return singleton.Delay(arrow_487)


def HafasAsyncClient__AsyncServerInfo_70DF6D02(__: HafasAsyncClient, opt: Optional[ServerOptions]=None) -> Async[ServerInfo]:
    def arrow_489(__: HafasAsyncClient=__, opt: Optional[ServerOptions]=opt) -> Async[ServerInfo]:
        def arrow_488(_arg15: Tuple[Optional[RawCommon], Optional[RawResult]]) -> Async[ServerInfo]:
            res : Optional[RawResult] = _arg15[1]
            return singleton.Return(parse_server_info(res, parse_common(__.profile, default_options, _arg15[0], res)))
        
        return singleton.Bind(HafasRawClient__AsyncServerInfo_4E60E31B(__.http_client, server_info_request()), arrow_488)
    
    return singleton.Delay(arrow_489)


def HafasAsyncClient__distanceOfJourney_1E546A4(__: HafasAsyncClient, j: Journey) -> float:
    return distance_of_journey(j)


def HafasAsyncClient__log(this: HafasAsyncClient, msg: str, o: _A_) -> None:
    Log_Print(msg, o)


def HafasAsyncClient__enabled_6FCE9E49(this: HafasAsyncClient, value: Optional[bool]=None) -> bool:
    if value is None:
        return False
    
    else: 
        return value
    


