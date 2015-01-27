# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

def simple_point_to_dict(point_instance,properties):
    """
    将一个django point转换为python dict格式
    对象必须包含有名为point的字段,并且有x,y,z属性
    """
    result = {"type": "Feature",
              "geometry":{"type":"Point",
                          "coordinates": [getattr(point_instance.point,i) for i in ('x','y','z') if getattr(point_instance.point,i)]},
              "properties":{ field_name:getattr(point_instance,field_name,'') for field_name in properties}
              }
    return result


def simple_point_togeojson(point_instance,properties):
    """
    将一个django point转换为geojson格式
    对象必须包含有名为point的字段,并且有x,y,z属性
    """
    return json.dumps(simple_point_to_dict(point_instance, properties))


def simple_pointset_to_dict(points,properties):
    result = {"type": "FeatureCollection","features":[]}
    if points:
        result['features'] = [ {'type':'Feature',
                      "geometry": {
                          "type": "Point",
                          "coordinates": [getattr(instance.point,i) 
                               for i in ('x','y','z') if getattr(instance.point,i)]
                       },
                      "properties":{ field_name:getattr(instance,field_name,'') 
                                                    for field_name in properties}} 
                                                          for instance in points]
    return result

def simple_pointset_togeojson(points,properties):
    """
    将一个django point集合转换为geojson格式
    对象必须包含有名为point的字段,并且有x,y,z属性
    """
    return json.dumps( simple_pointset_to_dict(points, properties) )
