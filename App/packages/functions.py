from math import sin, cos, asin, sqrt, degrees, radians

RADIUS = 6371.0

def calculateDeltas(lat, lng, distance):
    dlat = distance / RADIUS
    dlng = asin(sin(dlat) / cos(radians(lat)))
    return degrees(dlat), degrees(dlng)

def bounding_box(lat, lng, distance):
    dlat, dlng = calculateDeltas(lat, lng, distance)
    
    maxlat = lat + dlat
    minlat = lat - dlat
    
    maxlong = lng + dlng
    minlong = lng - dlng
    return maxlat,minlat,maxlong,minlong
    
def studentsInClasses(student_list, classroom_list):
    result = []
    for classroom in classroom_list:
        #Assumes we are far from the poles and the +/- 180 longitude
        latitude = classroom['latitude']
        longitude = classroom['longitude']
        maxlat,minlat,maxlong,minlong = bounding_box(latitude,longitude,0.01)
        for student in student_list:
            if (minlat <= student['latitude'] <= maxlat) and (minlong <= student['longitude'] <= maxlong):
                if student not in result:
                    result.append(student)
                
    return result

def studentClustersInClasses(student_list, classroom_list):
    result = []
    for classroom in classroom_list:
        tmp = []
        #Assumes we are far from the poles and the +/- 180 longitude
        latitude = classroom['latitude']
        longitude = classroom['longitude']
        maxlat,minlat,maxlong,minlong = bounding_box(latitude,longitude,0.01)
        for student in student_list:
            if (minlat <= student['latitude'] <= maxlat) and (minlong <= student['longitude'] <= maxlong):
                tmp.append(student)
        #print(tmp)                
        [result.append(item) for item in tmp if len(tmp)>=2 and item not in result]
        #print("\n{0}\n".format(classroom))        
        
    return result