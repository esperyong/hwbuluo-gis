import math

a = 6378245.0
ee = 0.00669342162296594323
pi = 3.14159265358979324

def out_of_china(lat,lon):
    if lon < 72.004 or lon > 137.8347:
        return True
    if lat < 0.8293 or lat > 55.8271:
        return True
    return False

def transformlat(x,y):
    result = -100.0 + 2.0*x + 3.0*y + 0.2*y*y + 0.1*x*y + 0.2*math.sqrt(abs(x))
    result += (20.0*math.sin(6.0*pi*x) + 20.0*math.sin(2.0*pi*x))*2.0/3.0
    result += (20.0*math.sin(pi*y) + 40.0*math.sin(pi/3.0*y))*2.0/3.0
    result += (160.0*math.sin(pi/12.0*y) + 320.0*math.sin(pi/30.0*y))*2.0/3.0
    return result

def transformlon(x,y):
    result = 300.0 + x + 2.0*y + 0.1*x*x + 0.1*x*y + 0.1*math.sqrt(abs(x))
    result += (20.0*math.sin(6.0*pi*x) + 20.0*math.sin(2.0*pi*x))*2.0/3.0
    result += (20.0*math.sin(pi*x) + 40.0*math.sin(pi/3.0*x))*2.0/3.0
    result += (150.0*math.sin(pi/12.0*x) + 300.0*math.sin(pi/30.0*x))*2.0/3.0
    return result

#http://open.map.qq.com/javascript_v2/case-run.html#sample-convertor-library
#http://open.map.qq.com/javascript_v2/doc/convertor.html

def wgs2gcj(wgslat,wgslon):
    if out_of_china(wgslat,wgslon):
        return (wgslat,wgslon)
    lat = transformlat(wgslon - 105.0,wgslat - 35.0)
    lon = transformlon(wgslon - 105.0,wgslat - 35.0)
    rad_lat = pi /180.0 * wgslat
    magic = math.sin(rad_lat)
    magic = 1 - ee*magic*magic
    sqrt_magic = math.sqrt(magic)
    lat = (180.0*lat) / (pi * (a*(1 - ee)) / (magic*sqrt_magic))
    lon = (180.0*lon) / (pi * a * math.cos(rad_lat) / sqrt_magic)
    chnlat = wgslat + lat
    chnlon = wgslon + lon
    return (chnlat,chnlon)
    
def gcj2wgs(chnlat,chnlon):
    lat,lon = wgs2gcj(chnlat, chnlon);
    wgslat = chnlat - (lat - chnlat);
    wgslon = chnlon - (lon - chnlon);
    return (wgslat,wgslon)


