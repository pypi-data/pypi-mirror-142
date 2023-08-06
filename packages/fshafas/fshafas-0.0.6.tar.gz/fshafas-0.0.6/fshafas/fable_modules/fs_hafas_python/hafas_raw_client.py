from __future__ import annotations
from typing import (Any, Optional, List, Tuple, TypeVar)
from ..fable_library.async_builder import (singleton, Async)
from ..fable_library.list import (FSharpList, last)
from ..fable_library.map import (of_seq, FSharpMap__TryFind)
from ..fable_library.option import default_arg
from ..fable_library.reflection import (TypeInfo, class_type)
from ..fable_library.reg_exp import replace as replace_1
from ..fable_library.string import (to_text, printf, to_console, replace, substring)
from ..fable_library.util import compare_primitives
from ..fable_simple_json_python.json_converter import (Convert_serialize, Convert_fromJson)
from ..fable_simple_json_python.simple_json import (SimpleJson_toString, SimpleJson_mapKeysByPath, SimpleJson_parseNative)
from ..fable_simple_json_python.type_info_converter import create_type_info
from ..fs_hafas_python.lib.request import (HttpClient__ctor, HttpClient__Dispose, HttpClient__PostAsync)
from .types_hafas_client import Log_Print
from .types_raw_hafas_client import (Cfg, RawRequest, LocMatchRequest, RawResult, RawMatch, RawCommon, RawLoc, TripSearchRequest, RawOutCon, JourneyDetailsRequest, RawJny, StationBoardRequest, ReconstructionRequest, JourneyMatchRequest, LocGeoPosRequest, LocGeoReachRequest, RawPos, LocDetailsRequest, JourneyGeoPosRequest, HimSearchRequest, RawHim, LineMatchRequest, RawLine, SearchOnTripRequest, SvcReq, Cfg_reflection, LocMatchRequest_reflection, TripSearchRequest_reflection, JourneyDetailsRequest_reflection, StationBoardRequest_reflection, ReconstructionRequest_reflection, JourneyMatchRequest_reflection, LocGeoPosRequest_reflection, LocGeoReachRequest_reflection, LocDetailsRequest_reflection, JourneyGeoPosRequest_reflection, HimSearchRequest_reflection, LineMatchRequest_reflection, SearchOnTripRequest_reflection, RawRequestClient_reflection, RawRequestAuth_reflection, RawResponse_reflection, RawResponse, SvcRes)

_A_ = TypeVar("_A_")

def expr_306() -> TypeInfo:
    return class_type("FsHafas.Api.HafasRawClient", None, HafasRawClient)


class HafasRawClient:
    def __init__(self, endpoint: str, salt: str, cfg: Cfg, base_request: RawRequest) -> None:
        self.endpoint = endpoint
        self.salt = salt
        self.cfg = cfg
        self.base_request = base_request
        self.http_client = HttpClient__ctor()
        class ObjectExpr305:
            @property
            def Compare(self) -> Any:
                def arrow_304(x: str, y: str) -> int:
                    return compare_primitives(x, y)
                
                return arrow_304
            
        self.replacements = of_seq([("a_cncl", "aCncl"), ("a_out_r", "aOutR"), ("a_out_s", "aOutS"), ("a_platf_ch", "aPlatfCh"), ("a_platf_r", "aPlatfR"), ("a_platf_s", "aPlatfS"), ("a_pltf_r", "aPltfR"), ("a_pltf_s", "aPltfS"), ("a_prod_x", "aProdX"), ("a_prog_type", "aProgType"), ("a_tzoffset", "aTZOffset"), ("a_time_r", "aTimeR"), ("a_time_s", "aTimeS"), ("add_name", "addName"), ("aff_prod_ref_l", "affProdRefL"), ("age_of_report", "ageOfReport"), ("arr_loc_l", "arrLocL"), ("button_text", "buttonText"), ("c_crd", "cCrd"), ("c_type", "cType"), ("calc_date", "calcDate"), ("calc_time", "calcTime"), ("cat_code", "catCode"), ("cat_in", "catIn"), ("cat_out", "catOut"), ("cat_out_l", "catOutL"), ("cat_out_s", "catOutS"), ("cat_ref_l", "catRefL"), ("cn_loc_x", "cnLocX"), ("con_subscr", "conSubscr"), ("crd_enc_f", "crdEncF"), ("crd_enc_s", "crdEncS"), ("crd_enc_yx", "crdEncYX"), ("crd_enc_z", "crdEncZ"), ("crd_sys_x", "crdSysX"), ("ctx_recon", "ctxRecon"), ("d_cncl", "dCncl"), ("d_dir_flg", "dDirFlg"), ("d_dir_txt", "dDirTxt"), ("d_in_r", "dInR"), ("d_in_s", "dInS"), ("d_platf_r", "dPlatfR"), ("d_platf_s", "dPlatfS"), ("d_pltf_r", "dPltfR"), ("d_pltf_s", "dPltfS"), ("d_prod_x", "dProdX"), ("d_prog_type", "dProgType"), ("d_tzoffset", "dTZOffset"), ("d_time_r", "dTimeR"), ("d_time_s", "dTimeS"), ("d_trn_cmp_sx", "dTrnCmpSX"), ("date_b", "dateB"), ("dep_loc_l", "depLocL"), ("dir_geo", "dirGeo"), ("dir_l", "dirL"), ("dir_ref_l", "dirRefL"), ("dir_txt", "dirTxt"), ("e_date", "eDate"), ("e_time", "eTime"), ("edge_ref_l", "edgeRefL"), ("entry_loc_l", "entryLocL"), ("err_txt", "errTxt"), ("event_ref_l", "eventRefL"), ("ext_cont", "extCont"), ("ext_id", "extId"), ("f_date", "fDate"), ("f_idx", "fIdx"), ("f_loc_x", "fLocX"), ("f_time", "fTime"), ("fare_l", "fareL"), ("fare_set_l", "fareSetL"), ("fp_b", "fpB"), ("fp_e", "fpE"), ("get_ist", "getIST"), ("get_iv", "getIV"), ("get_pois", "getPOIs"), ("get_pt", "getPT"), ("get_passlist", "getPasslist"), ("get_polyline", "getPolyline"), ("get_stops", "getStops"), ("get_tariff", "getTariff"), ("gis_fltr_l", "gisFltrL"), ("grid_l", "gridL"), ("him_fltr_l", "himFltrL"), ("him_l", "himL"), ("him_msg_cat_l", "himMsgCatL"), ("him_msg_edge_l", "himMsgEdgeL"), ("him_msg_event_l", "himMsgEventL"), ("him_x", "himX"), ("ico_crd", "icoCrd"), ("ico_l", "icoL"), ("ico_x", "icoX"), ("is_bookable", "isBookable"), ("is_from_price", "isFromPrice"), ("is_main_mast", "isMainMast"), ("is_rchbl", "isRchbl"), ("is_sot_con", "isSotCon"), ("is_upsell", "isUpsell"), ("item_l", "itemL"), ("jny_cl", "jnyCl"), ("jny_fltr_l", "jnyFltrL"), ("jny_l", "jnyL"), ("l_mod_date", "lModDate"), ("l_mod_time", "lModTime"), ("layer_x", "layerX"), ("line_id", "lineId"), ("line_l", "lineL"), ("ll_crd", "llCrd"), ("loc_data", "locData"), ("loc_fltr_l", "locFltrL"), ("loc_l", "locL"), ("loc_mode", "locMode"), ("loc_x", "locX"), ("m_mast_loc_x", "mMastLocX"), ("m_sec", "mSec"), ("match_id", "matchId"), ("max_c", "maxC"), ("max_chg", "maxChg"), ("max_dist", "maxDist"), ("max_dur", "maxDur"), ("max_jny", "maxJny"), ("max_loc", "maxLoc"), ("max_num", "maxNum"), ("min_c", "minC"), ("min_chg_time", "minChgTime"), ("min_dist", "minDist"), ("msg_l", "msgL"), ("msg_ref_l", "msgRefL"), ("n_cols", "nCols"), ("n_rows", "nRows"), ("num_c", "numC"), ("num_f", "numF"), ("only_rt", "onlyRT"), ("op_l", "opL"), ("opr_x", "oprX"), ("out_con_l", "outConL"), ("out_ctx_scr_b", "outCtxScrB"), ("out_ctx_scr_f", "outCtxScrF"), ("out_date", "outDate"), ("out_frwd", "outFrwd"), ("out_time", "outTime"), ("p_cls", "pCls"), ("p_loc_x", "pLocX"), ("p_ref_l", "pRefL"), ("per_size", "perSize"), ("per_step", "perStep"), ("planrt_ts", "planrtTS"), ("poly_enc", "polyEnc"), ("poly_g", "polyG"), ("poly_l", "polyL"), ("poly_xl", "polyXL"), ("pos_l", "posL"), ("pp_idx", "ppIdx"), ("pp_loc_ref_l", "ppLocRefL"), ("proc_abs", "procAbs"), ("prod_ctx", "prodCtx"), ("prod_l", "prodL"), ("prod_x", "prodX"), ("pub_ch_l", "pubChL"), ("rec_state", "recState"), ("redtn_card", "redtnCard"), ("region_ref_l", "regionRefL"), ("rem_l", "remL"), ("rem_x", "remX"), ("req_mode", "reqMode"), ("res_recommendation", "resRecommendation"), ("res_state", "resState"), ("rt_mode", "rtMode"), ("s_d", "sD"), ("s_date", "sDate"), ("s_days", "sDays"), ("s_days_b", "sDaysB"), ("s_days_i", "sDaysI"), ("s_days_l", "sDaysL"), ("s_days_r", "sDaysR"), ("s_t", "sT"), ("s_time", "sTime"), ("sec_l", "secL"), ("sect_x", "sectX"), ("show_arslink", "showARSLink"), ("sot_ctxt", "sotCtxt"), ("sot_mode", "sotMode"), ("sot_rating", "sotRating"), ("status_code", "statusCode"), ("stb_fltr_equiv", "stbFltrEquiv"), ("stb_loc", "stbLoc"), ("stb_stop", "stbStop"), ("stc_output_x", "stcOutputX"), ("stop_l", "stopL"), ("stop_loc_l", "stopLocL"), ("svc_req_l", "svcReqL"), ("svc_res_l", "svcResL"), ("t_date", "tDate"), ("t_idx", "tIdx"), ("t_loc_x", "tLocX"), ("t_time", "tTime"), ("tag_l", "tagL"), ("target_ctx", "targetCtx"), ("tc_m", "tcM"), ("tcoc_l", "tcocL"), ("tcoc_x", "tcocX"), ("ticket_l", "ticketL"), ("time_b", "timeB"), ("train_pos_mode", "trainPosMode"), ("trf_req", "trfReq"), ("trf_res", "trfRes"), ("tvlr_prof", "tvlrProf"), ("txt_n", "txtN"), ("txt_s", "txtS"), ("ur_crd", "urCrd"), ("via_loc_l", "viaLocL")], ObjectExpr305())
    

HafasRawClient_reflection = expr_306

def HafasRawClient__ctor_6D5FF7F7(endpoint: str, salt: str, cfg: Cfg, base_request: RawRequest) -> HafasRawClient:
    return HafasRawClient(endpoint, salt, cfg, base_request)


def HafasRawClient__Dispose(__: HafasRawClient) -> None:
    HttpClient__Dispose(__.http_client)


def HafasRawClient__AsyncLocMatch_324CF02B(__: HafasRawClient, loc_match_request: LocMatchRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], List[RawLoc]]]:
    def arrow_308(__: HafasRawClient=__, loc_match_request: LocMatchRequest=loc_match_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], List[RawLoc]]]:
        def arrow_307(_arg5: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], List[RawLoc]]]:
            res : RawResult = _arg5
            match_value : Optional[RawMatch] = res.match
            if match_value is not None:
                match : RawMatch = match_value
                return singleton.Return((res.common, res, match.loc_l))
            
            else: 
                return singleton.Return((None, None, []))
            
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "LocMatch", loc_match_request)), arrow_307)
    
    return singleton.Delay(arrow_308)


def HafasRawClient__AsyncTripSearch_Z4E830477(__: HafasRawClient, trip_search_request: TripSearchRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawOutCon]]]]:
    def arrow_310(__: HafasRawClient=__, trip_search_request: TripSearchRequest=trip_search_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawOutCon]]]]:
        def arrow_309(_arg6: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawOutCon]]]]:
            res : RawResult = _arg6
            return singleton.Return((res.common, res, res.out_con_l))
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "TripSearch", trip_search_request)), arrow_309)
    
    return singleton.Delay(arrow_310)


def HafasRawClient__AsyncJourneyDetails_39A8152A(__: HafasRawClient, journey_details_request: JourneyDetailsRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawJny]]]:
    def arrow_312(__: HafasRawClient=__, journey_details_request: JourneyDetailsRequest=journey_details_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawJny]]]:
        def arrow_311(_arg7: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawJny]]]:
            res : RawResult = _arg7
            return singleton.Return((res.common, res, res.journey))
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "JourneyDetails", journey_details_request)), arrow_311)
    
    return singleton.Delay(arrow_312)


def HafasRawClient__AsyncStationBoard_49AFED38(__: HafasRawClient, station_board_request: StationBoardRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]]:
    def arrow_314(__: HafasRawClient=__, station_board_request: StationBoardRequest=station_board_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]]:
        def arrow_313(_arg8: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]]:
            res : RawResult = _arg8
            return singleton.Return((res.common, res, res.jny_l))
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "StationBoard", station_board_request)), arrow_313)
    
    return singleton.Delay(arrow_314)


def HafasRawClient__AsyncReconstruction_Z53F036CE(__: HafasRawClient, reconstruction_request: ReconstructionRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawOutCon]]]]:
    def arrow_316(__: HafasRawClient=__, reconstruction_request: ReconstructionRequest=reconstruction_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawOutCon]]]]:
        def arrow_315(_arg9: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawOutCon]]]]:
            res : RawResult = _arg9
            return singleton.Return((res.common, res, res.out_con_l))
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "Reconstruction", reconstruction_request)), arrow_315)
    
    return singleton.Delay(arrow_316)


def HafasRawClient__AsyncJourneyMatch_Z2BB017E5(__: HafasRawClient, journey_match_request: JourneyMatchRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]]:
    def arrow_318(__: HafasRawClient=__, journey_match_request: JourneyMatchRequest=journey_match_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]]:
        def arrow_317(_arg10: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]]:
            res : RawResult = _arg10
            return singleton.Return((res.common, res, res.jny_l))
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "JourneyMatch", journey_match_request)), arrow_317)
    
    return singleton.Delay(arrow_318)


def HafasRawClient__AsyncLocGeoPos_765D46F9(__: HafasRawClient, loc_geo_pos_request: LocGeoPosRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], List[RawLoc]]]:
    def arrow_320(__: HafasRawClient=__, loc_geo_pos_request: LocGeoPosRequest=loc_geo_pos_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], List[RawLoc]]]:
        def arrow_319(_arg11: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], List[RawLoc]]]:
            res : RawResult = _arg11
            match_value : Optional[List[RawLoc]] = res.loc_l
            if match_value is not None:
                loc_l : List[RawLoc] = match_value
                return singleton.Return((res.common, res, loc_l))
            
            else: 
                return singleton.Return((None, None, []))
            
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "LocGeoPos", loc_geo_pos_request)), arrow_319)
    
    return singleton.Delay(arrow_320)


def HafasRawClient__AsyncLocGeoReach_78598228(__: HafasRawClient, loc_geo_reach_request: LocGeoReachRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], List[RawPos]]]:
    def arrow_322(__: HafasRawClient=__, loc_geo_reach_request: LocGeoReachRequest=loc_geo_reach_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], List[RawPos]]]:
        def arrow_321(_arg12: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], List[RawPos]]]:
            res : RawResult = _arg12
            match_value : Optional[List[RawPos]] = res.pos_l
            if match_value is not None:
                pos_l : List[RawPos] = match_value
                return singleton.Return((res.common, res, pos_l))
            
            else: 
                return singleton.Return((None, None, []))
            
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "LocGeoReach", loc_geo_reach_request)), arrow_321)
    
    return singleton.Delay(arrow_322)


def HafasRawClient__AsyncLocDetails_659C62DA(__: HafasRawClient, loc_details_request: LocDetailsRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawLoc]]]:
    def arrow_324(__: HafasRawClient=__, loc_details_request: LocDetailsRequest=loc_details_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawLoc]]]:
        def arrow_323(_arg13: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[RawLoc]]]:
            res : RawResult = _arg13
            match_value : Optional[List[RawLoc]] = res.loc_l
            (pattern_matching_result, loc_l_1) = (None, None)
            if match_value is not None:
                if len(match_value) > 0:
                    pattern_matching_result = 0
                    loc_l_1 = match_value
                
                else: 
                    pattern_matching_result = 1
                
            
            else: 
                pattern_matching_result = 1
            
            if pattern_matching_result == 0:
                return singleton.Return((res.common, res, loc_l_1[0]))
            
            elif pattern_matching_result == 1:
                return singleton.Return((None, None, None))
            
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "LocDetails", loc_details_request)), arrow_323)
    
    return singleton.Delay(arrow_324)


def HafasRawClient__AsyncJourneyGeoPos_Z27E4B537(__: HafasRawClient, journey_geo_pos_request: JourneyGeoPosRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]]:
    def arrow_326(__: HafasRawClient=__, journey_geo_pos_request: JourneyGeoPosRequest=journey_geo_pos_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]]:
        def arrow_325(_arg14: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawJny]]]]:
            res : RawResult = _arg14
            return singleton.Return((res.common, res, res.jny_l))
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "JourneyGeoPos", journey_geo_pos_request)), arrow_325)
    
    return singleton.Delay(arrow_326)


def HafasRawClient__AsyncHimSearch_Z2A604406(__: HafasRawClient, him_search_request: HimSearchRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawHim]]]]:
    def arrow_328(__: HafasRawClient=__, him_search_request: HimSearchRequest=him_search_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawHim]]]]:
        def arrow_327(_arg15: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawHim]]]]:
            res : RawResult = _arg15
            return singleton.Return((res.common, res, res.msg_l))
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "HimSearch", him_search_request)), arrow_327)
    
    return singleton.Delay(arrow_328)


def HafasRawClient__AsyncLineMatch_Z23F97D3B(__: HafasRawClient, line_match_request: LineMatchRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawLine]]]]:
    def arrow_330(__: HafasRawClient=__, line_match_request: LineMatchRequest=line_match_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawLine]]]]:
        def arrow_329(_arg16: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawLine]]]]:
            res : RawResult = _arg16
            return singleton.Return((res.common, res, res.line_l))
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "LineMatch", line_match_request)), arrow_329)
    
    return singleton.Delay(arrow_330)


def HafasRawClient__AsyncServerInfo_4E60E31B(__: HafasRawClient, server_info_request: Any=None) -> Async[Tuple[Optional[RawCommon], Optional[RawResult]]]:
    def arrow_332(__: HafasRawClient=__, server_info_request: Any=server_info_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult]]]:
        def arrow_331(_arg17: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult]]]:
            res : RawResult = _arg17
            return singleton.Return((res.common, res))
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "ServerInfo", server_info_request)), arrow_331)
    
    return singleton.Delay(arrow_332)


def HafasRawClient__AsyncSearchOnTrip_1713A0E8(__: HafasRawClient, search_on_trip_request: SearchOnTripRequest) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawOutCon]]]]:
    def arrow_334(__: HafasRawClient=__, search_on_trip_request: SearchOnTripRequest=search_on_trip_request) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawOutCon]]]]:
        def arrow_333(_arg18: RawResult) -> Async[Tuple[Optional[RawCommon], Optional[RawResult], Optional[List[RawOutCon]]]]:
            res : RawResult = _arg18
            return singleton.Return((res.common, res, res.out_con_l))
        
        return singleton.Bind(HafasRawClient__asyncPost_737B0FC(__, HafasRawClient__makeRequest(__, "SearchOnTrip", search_on_trip_request)), arrow_333)
    
    return singleton.Delay(arrow_334)


def HafasRawClient__log(this: HafasRawClient, msg: str, o: _A_) -> None:
    Log_Print(msg, o)


def HafasRawClient__makeRequest(this: HafasRawClient, meth: str, parameters: Any=None) -> RawRequest:
    input_record : RawRequest = this.base_request
    return RawRequest(input_record.lang, [SvcReq(this.cfg, meth, parameters)], input_record.client, input_record.ext, input_record.ver, input_record.auth)


def HafasRawClient__toUndashed_7F866359(this: HafasRawClient, xs: FSharpList[str]) -> Optional[str]:
    match_value : Optional[str] = FSharpMap__TryFind(this.replacements, last(xs))
    if match_value is None:
        return None
    
    else: 
        return match_value
    


def HafasRawClient__encodeSvcReq_509B8449(this: HafasRawClient, svc_req: SvcReq) -> str:
    cfg : str = Convert_serialize(svc_req.cfg, create_type_info(Cfg_reflection()))
    req : str
    match_value : Any = svc_req.req
    req = Convert_serialize(match_value, create_type_info(LocMatchRequest_reflection())) if isinstance(match_value, LocMatchRequest) else (Convert_serialize(match_value, create_type_info(TripSearchRequest_reflection())) if isinstance(match_value, TripSearchRequest) else (Convert_serialize(match_value, create_type_info(JourneyDetailsRequest_reflection())) if isinstance(match_value, JourneyDetailsRequest) else (Convert_serialize(match_value, create_type_info(StationBoardRequest_reflection())) if isinstance(match_value, StationBoardRequest) else (Convert_serialize(match_value, create_type_info(ReconstructionRequest_reflection())) if isinstance(match_value, ReconstructionRequest) else (Convert_serialize(match_value, create_type_info(JourneyMatchRequest_reflection())) if isinstance(match_value, JourneyMatchRequest) else (Convert_serialize(match_value, create_type_info(LocGeoPosRequest_reflection())) if isinstance(match_value, LocGeoPosRequest) else (Convert_serialize(match_value, create_type_info(LocGeoReachRequest_reflection())) if isinstance(match_value, LocGeoReachRequest) else (Convert_serialize(match_value, create_type_info(LocDetailsRequest_reflection())) if isinstance(match_value, LocDetailsRequest) else (Convert_serialize(match_value, create_type_info(JourneyGeoPosRequest_reflection())) if isinstance(match_value, JourneyGeoPosRequest) else (Convert_serialize(match_value, create_type_info(HimSearchRequest_reflection())) if isinstance(match_value, HimSearchRequest) else (Convert_serialize(match_value, create_type_info(LineMatchRequest_reflection())) if isinstance(match_value, LineMatchRequest) else (Convert_serialize(match_value, create_type_info(SearchOnTripRequest_reflection())) if isinstance(match_value, SearchOnTripRequest) else "{}"))))))))))))
    return to_text(printf("{\"cfg\":%s, \"meth\":\"%s\", \"req\":%s}"))(cfg)(svc_req.meth)(req)


def HafasRawClient__encode_737B0FC(this: HafasRawClient, request: RawRequest) -> str:
    try: 
        svcreql : str = ("[" + HafasRawClient__encodeSvcReq_509B8449(this, request.svc_req_l[0])) + "]"
        client : str = Convert_serialize(request.client, create_type_info(RawRequestClient_reflection()))
        auth : str = Convert_serialize(request.auth, create_type_info(RawRequestAuth_reflection()))
        def f(xs: FSharpList[str]) -> Optional[str]:
            return HafasRawClient__toUndashed_7F866359(this, xs)
        
        return SimpleJson_toString(SimpleJson_mapKeysByPath(f, SimpleJson_parseNative(replace(replace(to_text(printf("{\"lang\":\"%s\", \"svcReqL\":%s, \"client\":%s, \"ext\":\"%s\", \"ver\":\"%s\", \"auth\":%s}"))(request.lang)(svcreql)(client)(request.ext)(request.ver)(auth), ", \"meta\": null", ""), ",\"name\":null", ""))))
    
    except Exception as e:
        arg10_1 : str = str(e)
        to_console(printf("error encode: %s"))(arg10_1)
        raise Exception(str(e))
    


def HafasRawClient__dashify(this: HafasRawClient, separator: str, input: str) -> str:
    def arrow_335(m: Any, this: HafasRawClient=this, separator: str=separator, input: str=input) -> str:
        return m[0].lower() if (len(m[0]) == 1) else ((substring(m[0], 0, 1) + separator) + substring(m[0], 1, 1).lower())
    
    return replace_1(input, "[a-z]?[A-Z]", arrow_335)


def HafasRawClient__toDashed_7F866359(this: HafasRawClient, xs: FSharpList[str]) -> Optional[str]:
    return HafasRawClient__dashify(this, "_", last(xs))


def HafasRawClient__decode_Z721C83C5(this: HafasRawClient, input: str) -> RawResponse:
    try: 
        def f(xs: FSharpList[str]) -> Optional[str]:
            return HafasRawClient__toDashed_7F866359(this, xs)
        
        return Convert_fromJson(SimpleJson_mapKeysByPath(f, SimpleJson_parseNative(input)), create_type_info(RawResponse_reflection()))
    
    except Exception as e:
        arg10 : str = str(e)
        to_console(printf("error decode: %s"))(arg10)
        raise Exception(str(e))
    


def HafasRawClient__asyncPost_737B0FC(this: HafasRawClient, request: RawRequest) -> Async[RawResult]:
    json : str = HafasRawClient__encode_737B0FC(this, request)
    HafasRawClient__log(this, "request:", json)
    def arrow_349(this: HafasRawClient=this, request: RawRequest=request) -> Async[RawResult]:
        def arrow_348(_arg3: str) -> Async[RawResult]:
            result : str = _arg3
            HafasRawClient__log(this, "response:", result)
            def arrow_345(__unit: Any=None) -> Async[RawResult]:
                if len(result) == 0:
                    def arrow_336(__unit: Any=None) -> RawResult:
                        raise Exception("invalid response")
                    
                    return singleton.Return(arrow_336())
                
                else: 
                    response : RawResponse = HafasRawClient__decode_Z721C83C5(this, result)
                    svc_res_l : List[SvcRes] = default_arg(response.svc_res_l, [])
                    if len(svc_res_l) == 1:
                        svc_res : SvcRes = svc_res_l[0]
                        match_value : Tuple[Optional[str], Optional[str]] = (svc_res.err, svc_res.err_txt)
                        (pattern_matching_result, err_1, err_txt_1) = (None, None, None)
                        if match_value[0] is not None:
                            if match_value[1] is not None:
                                def arrow_339(__unit: Any=None) -> bool:
                                    err_txt : str = match_value[1]
                                    return match_value[0] != "OK"
                                
                                if arrow_339():
                                    pattern_matching_result = 0
                                    err_1 = match_value[0]
                                    err_txt_1 = match_value[1]
                                
                                else: 
                                    pattern_matching_result = 1
                                
                            
                            else: 
                                pattern_matching_result = 1
                            
                        
                        else: 
                            pattern_matching_result = 1
                        
                        if pattern_matching_result == 0:
                            def arrow_337(__unit: Any=None) -> RawResult:
                                raise Exception((err_1 + ":") + err_txt_1)
                            
                            return singleton.Return(arrow_337())
                        
                        elif pattern_matching_result == 1:
                            (pattern_matching_result_1, err_3) = (None, None)
                            if match_value[0] is not None:
                                if match_value[0] != "OK":
                                    pattern_matching_result_1 = 0
                                    err_3 = match_value[0]
                                
                                else: 
                                    pattern_matching_result_1 = 1
                                
                            
                            else: 
                                pattern_matching_result_1 = 1
                            
                            if pattern_matching_result_1 == 0:
                                def arrow_338(__unit: Any=None) -> RawResult:
                                    raise Exception(err_3)
                                
                                return singleton.Return(arrow_338())
                            
                            elif pattern_matching_result_1 == 1:
                                return singleton.Return(svc_res.res)
                            
                        
                    
                    else: 
                        match_value_1 : Tuple[Optional[str], Optional[str]] = (response.err, response.err_txt)
                        def arrow_341(__unit: Any=None) -> Async[RawResult]:
                            err_4 : str = match_value_1[0]
                            err_txt_2 : str = match_value_1[1]
                            def arrow_340(__unit: Any=None) -> RawResult:
                                raise Exception((err_4 + ":") + err_txt_2)
                            
                            return singleton.Return(arrow_340())
                        
                        def arrow_343(__unit: Any=None) -> Async[RawResult]:
                            err_5 : str = match_value_1[0]
                            def arrow_342(__unit: Any=None) -> RawResult:
                                raise Exception(err_5)
                            
                            return singleton.Return(arrow_342())
                        
                        def arrow_344(__unit: Any=None) -> RawResult:
                            raise Exception("invalid response")
                        
                        return (arrow_341() if (match_value_1[1] is not None) else arrow_343()) if (match_value_1[0] is not None) else singleton.Return(arrow_344())
                    
                
            
            def arrow_347(_arg4: Exception) -> Async[RawResult]:
                arg10_1 : str = str(_arg4)
                to_console(printf("error: %s"))(arg10_1)
                def arrow_346(__unit: Any=None) -> RawResult:
                    raise Exception("invalid response")
                
                return singleton.Return(arrow_346())
            
            return singleton.TryWith(singleton.Delay(arrow_345), arrow_347)
        
        return singleton.Bind(HttpClient__PostAsync(this.http_client, this.endpoint, this.salt, json), arrow_348)
    
    return singleton.Delay(arrow_349)


