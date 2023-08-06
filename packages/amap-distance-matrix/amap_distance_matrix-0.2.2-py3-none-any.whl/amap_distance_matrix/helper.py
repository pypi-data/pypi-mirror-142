# -*- coding: utf-8 -*- 
# Time: 2022-03-01 11:01
# Copyright (c) 2022
# author: Euraxluo


import datetime
import itertools
import geohash
from math import radians, cos, sin, asin, sqrt
from typing import *


def check_location(location: List[float]):
    if not location and len(location) < 2:
        return False
    if 73 < location[0] < 136 and 3 < location[1] < 54:
        return True
    return False


def loc_to_str(loc_list: list, revers=False) -> str:
    """
    坐标列表转字符串
    :param loc_list:[[float,float]]
    :param revers:False,是否翻转坐标 xy=>yx
    :return:str:'float,float'
    """
    if revers:
        loc_s_list = [str(loc[1]) + "," + str(loc[0]) for loc in loc_list]
    else:
        loc_s_list = [str(loc[0]) + "," + str(loc[1]) for loc in loc_list]
    loc_str = loc_s_list[0]
    for loc_s in loc_s_list[1:]:
        loc_str += ";" + loc_s
    return loc_str


def format_loc(loc_str: str, revers=False) -> list:
    """
    坐标字符串转换
    :param loc_str: str:'float,float'
    :param revers:False
    :return:[float,float]
    """
    if revers:
        return [float(i) for i in loc_str.split(',')[::-1]]
    return [float(i) for i in loc_str.split(',')[::]]


def wgs2gcj(Lon, Lat):
    from coord_convert.transform import wgs2gcj
    return wgs2gcj(wgsLon=Lon, wgsLat=Lat)


def gcj2wgs(Lon, Lat):
    from coord_convert.transform import gcj2wgs
    return gcj2wgs(gcjLon=Lon, gcjLat=Lat)


def haversine(loc1, loc2):
    """
    经纬度距离
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [loc1[0], loc1[1], loc2[0], loc2[1]])
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000


def time_slot_wmh(date_time: datetime.datetime = None):
    """
    时间段
    :param date_time:
    :return: w0m0h
    """
    if date_time is None:
        date_time = datetime.datetime.now()
    weekday = str(date_time.weekday() + 1)
    month = '0' + str(date_time.month) if date_time.month < 10 else str(date_time.month)
    hour = '0' + str(date_time.hour) if date_time.hour < 10 else str(date_time.hour)
    return weekday + month + hour


def geo_encode(lon: float, lat: float, precision=8):
    return geohash.encode(longitude=lon, latitude=lat, precision=8)


def geo_decode(hashcode: str):
    return geohash.decode(hashcode)


def point_pairing_sorted(*points: Union[List[float], Tuple[float]]) -> List[Tuple[Tuple[float], ...]]:
    """
    通过点的全排列,得到待排序的点对
    通过分配收集算法,将点对排序
    :param points:待排列的点序列
    :return:
    """
    # 1.去重
    distinct_point_set: Set[Tuple[float]] = set()

    for point in points:
        if isinstance(point, list):
            distinct_point_set.add(tuple(point))
            continue
        distinct_point_set.add(point)

    # 2. 获取全排列数据
    point_bucket: Dict[Tuple[float], Set[Tuple[Tuple[float]]]] = {}
    not_sorted_set = set()
    for point in itertools.permutations(distinct_point_set, 2):
        if point[0] not in point_bucket:
            point_bucket[point[0]] = set()
        point_bucket[point[0]].add(point)
        not_sorted_set.add(point)

    # 3.collection
    sorted_collection: List[Tuple[Tuple[float], ...]] = []
    while not_sorted_set:
        if not sorted_collection:
            # 如果结果集合为空,则随便取一个数据
            start_index = not_sorted_set.pop()
            # 从桶中移除开始索引
            point_bucket[start_index[0]].remove(start_index)
        else:
            # 获取结果集合的最后一个元素的终点,作为起点的key
            start_key = sorted_collection[-1][-1]
            # 据此key,获取并弹出start index
            start_index = point_bucket[start_key].pop()
            not_sorted_set.remove(start_index)
        sorted_collection.append(start_index)

    return sorted_collection
