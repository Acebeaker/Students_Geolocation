import json
import haversine as hs
from packages.functions import *


engineering_classroom = { 'name': 'Principles of computational geo-location analysis', 'latitude': 34.069140, 'longitude': -118.442689 }
geology_classroom = { 'name': 'Sedimentary Petrology', 'latitude': 34.069585, 'longitude': -118.441878 }
psychology_classroom = { 'name': 'Introductory Psychobiology', 'latitude': 34.069742, 'longitude': -118.441312 }
music_classroom = { 'name': 'Art of Listening', 'latitude': 34.070223, 'longitude': -118.440193 }
humanities_classroom = { 'name': 'Art History', 'latitude': 34.071528, 'longitude': -118.441211 }

john_student = { 'name': 'John Wilson', 'latitude': 34.069149, 'longitude': -118.442639 } # engineering
jane_student = { 'name': 'Jane Graham', 'latitude': 34.069601, 'longitude': -118.441862 } # geology
pam_student = { 'name': 'Pam Bam', 'latitude': 34.071513, 'longitude': -118.441181 } # humanities

student_list = [john_student,jane_student,pam_student]
classroom_list = [geology_classroom,psychology_classroom,music_classroom,humanities_classroom,engineering_classroom]

if __name__ == "__main__":
    print(studentsInClasses(student_list, classroom_list))
    