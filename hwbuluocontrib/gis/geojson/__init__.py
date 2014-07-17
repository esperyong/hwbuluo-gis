# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

def simple_pointset_togeojson(queryset,properties):
    """
    将一个django point集合转换为geojson格式
    对象必须包含有名为point的字段,并且有x,y,z属性
    
    """
    result = {"type": "FeatureCollection","features":[]}
    if queryset and queryset.count() != 0:
        for instance in queryset:
            for field_name in properties:
                field_value = getattr(instance,field_name,'')
    features = [ {'type':'Feature',
                  "geometry": {
                      "type": "Point",
                      "coordinates": [getattr(instance.point,i) 
                               for i in ('x','y','z') if getattr(instance.point,i)]
                  },
                  'properties':{ field_name:getattr(instance,field_name,'') 
                                                    for field_name in properties}} 
                                                          for instance in queryset]
    result['features'] = features
    return json.dumps(result)

