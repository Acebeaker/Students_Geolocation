from math import sin, cos, asin, sqrt, degrees, radians

RADIUS = 6371.0

def bounding_box(lat, lon, distance):
    dlat = distance / RADIUS
    dlon = asin(sin(dlat) / cos(radians(lat)))
    return degrees(dlat), degrees(dlon)

    
def studentsInClasses(student_list, classroom_list):
    for classroom in classroom_list:
        #Assumes we are far from the poles and the +/- 180 longitude
        dlat, dlong = bounding_box(classroom['latitude'],classroom['longitude'],10)
               
        maxlat = classroom['latitude'] + dlat
        minlat = classroom['latitude'] - dlat
        
        maxlong = classroom['longitude'] + dlong
        minlong = classroom['longitude'] - dlong
        
        
    return 1