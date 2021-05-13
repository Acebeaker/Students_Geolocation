import unittest
from packages.functions import *


class functionTest(unittest.TestCase):
    def test_studentsInClasses_1(self):
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
        self.assertEqual(studentsInClasses(student_list, classroom_list), [{'name': 'Jane Graham', 'latitude': 34.069601, 'longitude': -118.441862}, {'name': 'Pam Bam', 'latitude': 34.071513, 'longitude': -118.441181}, {'name': 'John Wilson', 'latitude': 34.069149, 'longitude': -118.442639}])
        
    def test_studentsInClasses_2(self):
        engineering_classroom = { 'name': 'Principles of computational geo-location analysis', 'latitude': 34.069140, 'longitude': -118.442689 }
        geology_classroom = { 'name': 'Sedimentary Petrology', 'latitude': 34.069585, 'longitude': -118.441878 }
        psychology_classroom = { 'name': 'Introductory Psychobiology', 'latitude': 34.069742, 'longitude': -118.441312 }
        music_classroom = { 'name': 'Art of Listening', 'latitude': 34.070223, 'longitude': -118.440193 }
        humanities_classroom = { 'name': 'Art Hitory', 'latitude': 34.071528, 'longitude': -118.441211 }

        john_student = { 'name': 'John Wilson', 'latitude': 34.069849, 'longitude': -118.443539 } # engineering
        jane_student = { 'name': 'Jane Graham', 'latitude': 34.069901, 'longitude': -118.441562 } # geology
        pam_student = { 'name': 'Pam Bam', 'latitude': 34.071523, 'longitude': -118.441171 } # humanities

        classroom_list = [geology_classroom,psychology_classroom,music_classroom,humanities_classroom,engineering_classroom]

        student_list = [john_student,jane_student,pam_student]

        self.assertEqual(studentsInClasses(student_list, classroom_list), [{ 'name': 'Pam Bam', 'latitude': 34.071523, 'longitude': -118.441171 }])
        
    def test_studentClustersInClasses_1(self):
        engineering_classroom = { 'name': 'Principles of computational geo-location analysis', 'latitude': 34.069140, 'longitude': -118.442689 }
        geology_classroom = { 'name': 'Sedimentary Petrology', 'latitude': 34.069585, 'longitude': -118.441878 }
        psychology_classroom = { 'name': 'Introductory Psychobiology', 'latitude': 34.069742, 'longitude': -118.441312 }
        music_classroom = { 'name': 'Art of Listening', 'latitude': 34.070223, 'longitude': -118.440193 }
        humanities_classroom = { 'name': 'Art Hitory', 'latitude': 34.071528, 'longitude': -118.441211 }

        john_student = { 'name': 'John Wilson', 'latitude': 34.069849, 'longitude': -118.443539 } # engineering
        jane_student = { 'name': 'Jane Graham', 'latitude': 34.069901, 'longitude': -118.441562 } # geology
        pam_student = { 'name': 'Pam Bam', 'latitude': 34.071523, 'longitude': -118.441171 } # humanities

        classroom_list = [geology_classroom,psychology_classroom,music_classroom,humanities_classroom,engineering_classroom]

        student_list = [john_student,jane_student,pam_student]

        self.assertEqual(studentClustersInClasses(student_list, classroom_list), [])   
        
    def test_studentClustersInClasses_2(self):
        engineering_classroom = { 'name': 'Principles of computational geo-location analysis', 'latitude': 34.069140, 'longitude': -118.442689 }
        geology_classroom = { 'name': 'Sedimentary Petrology', 'latitude': 34.069585, 'longitude': -118.441878 }
        psychology_classroom = { 'name': 'Introductory Psychobiology', 'latitude': 34.069742, 'longitude': -118.441312 }
        music_classroom = { 'name': 'Art of Listening', 'latitude': 34.070223, 'longitude': -118.440193 }
        humanities_classroom = { 'name': 'Art History', 'latitude': 34.071528, 'longitude': -118.441211 }

        john_student = { 'name': 'John Wilson', 'latitude': 34.069549, 'longitude': -118.441830 } # engineering
        jane_student = { 'name': 'Jane Graham', 'latitude': 34.069601, 'longitude': -118.441862 } # geology
        pam_student = { 'name': 'Pam Bam', 'latitude': 34.071513, 'longitude': -118.441181 } # humanities

        student_list = [john_student,jane_student,pam_student]
        classroom_list = [geology_classroom,psychology_classroom,music_classroom,humanities_classroom,engineering_classroom]

        self.assertEqual(studentClustersInClasses(student_list, classroom_list), [{'name': 'John Wilson', 'latitude': 34.069549, 'longitude': -118.44183}, {'name': 'Jane Graham', 'latitude': 34.069601, 'longitude': -118.441862}])  
        
if __name__ == '__main__':
    unittest.main()