# -*- coding: utf-8 -*-
import math
import requests
from string import Template

def get_distance_by_lonti_lati(p1,p2):
    dis = get_distance_by_lonti_lati_baidu(p1,p2)
    if dis is None:
        dis = cal_distance_by_lonti_lati(p1,p2)
    return dis

def cal_distance_by_lonti_lati(p1,p2):
    """
    根据经纬度计算出距离
    param p1 tuple
    param p2 tuple 
    p[0] lontitude p[1] latitude
    return 单位为米
    """
    _C_P = 0.0174532925199432957692222222222
    d = 0
    dlon = (p2[0] - p1[0]) * _C_P
    #弧度
    dlat = (p2[1] - p1[1]) * _C_P
    a = math.sin(0.5 * dlat) * math.sin(0.5 * dlat) + math.cos(p1[1] * _C_P) * math.cos(p2[1] * _C_P) * (math.sin(0.5*dlon) * math.sin(0.5*dlon))
    a = abs(a)
    if a > 1:
        s = "不合法数据:" + "a:" + a + ",P1:" + p1 + ",P2:" + p2

    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
    d = c * 6371008.77141506

    #此方法在当地图视角大于180跨度时计算有问题即此方法计算的是地球表面两点之间的最短距离，两点没有先后顺序
    if abs(p2[0]-p1[0])>180 or abs(p2[1]-p1[1])>180:
        d = 2 * math.pi * 6371008.77141506 - d
    d = math.ceil(d)
    return d

def get_distance_by_lonti_lati_baidu(p1,p2):
    url_template = "http://api.map.baidu.com/direction/v1/routematrix?output=json&origins=$originlati,$originlongti&destinations=$destlati,$destlongti&ak=jg1tLoS01KHugc1VZltMrTwC"
    url_tempt = Template(url_template)
    url = url_tempt.substitute(originlati=p1[1],originlongti=p1[0],
                                 destlati=p2[1],destlongti=p2[0])
    rp = requests.get(url)
    dis = rp.json()['result']['elements'][0]['distance']['value']
    return dis

#/**
# * Description: 获得点到之间距离
# * 
# * @param {Point}
# *           p1 第一个点
# * @param {Point}
# *           p2 第二个点
# * @return {Float} 
# * @private
# */
#getLineLength:function(p1,p2){
#	var d=new Number(0);
#	if(this._MapSpanScale ==1){//地图范围刻度 是不是经纬度的 ==1就是经纬度坐标
#		var dlon = (p2[0] - p1[0])*this._C_P;
#		//弧度
#		var dlat = (p2[1] - p1[1])*this._C_P;
#		var a = Math.sin(0.5*dlat)*Math.sin(0.5*dlat)+Math.cos(p1[1]*this._C_P)*Math.cos(p2[1]*this._C_P)*(Math.sin(0.5*dlon)*Math.sin(0.5*dlon));
#		a=Math.abs(a);
#
#		if(a>1){
#			alert("不合法数据:"+"a:"+a+",P1:"+p1.toString()+",P2:"+p2.toString());
#		}
#
#		var c = 2*Math.atan2(Math.sqrt(a),Math.sqrt(1-a));
#		d = c*6371008.77141506;
#
#		//此方法在当地图视角大于180跨度时计算有问题即此方法计算的是地球表面两点之间的最短距离，两点没有先后顺序 20100411
#		if(Math.abs(p2[0]-p1[0])>180 || Math.abs(p2[1]-p1[1])>180)d = 2*Math.PI*6371008.77141506 - d;
#
#	}
#	else{
#		var p2Len=(p2[0] - p1[0])*(p2[0] - p1[0])+(p2[1] - p1[1])*(p2[1] - p1[1]);
#		d=Math.sqrt(p2Len);
#	}
#
#	d=Math.ceil(d);
#
#	return d;
#	//单位是米
#}

