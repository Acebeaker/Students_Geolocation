**Students Geolocation**

The functions are located inside `app\packages\functions.py` and are imported inside `main.py` for an app and `test.py` for unit tests.
These functions are:

* **studentsInClasses**
  Evaluate and determines if a student is inside a classroom
  * Params:
    * 'student_list': A list containing the students in this format:
      ```yaml
        {
          name,
          latitude,
          longitude
        }
      ```
    * 'classroom_list': A list containing the classrooms in this format:
      ```yaml
        {
          name,
          latitude,
          longitude
        }
      ```
  * Return Value
    Returns a list with al the students found inside a classroom
    
    
* **studentsInClasses**
  Evaluate and determines if a student is inside a classroom with other students
  * Params:
    * 'student_list': A list containing the students in this format:
      ```yaml
        {
          name,
          latitude,
          longitude
        }
      ```
    * 'classroom_list': A list containing the classrooms in this format:
      ```yaml
        {
          name,
          latitude,
          longitude
        }
      ```
  * Return Value
    Returns a list with al the students found inside a classroom if this classroom contains two or more students

* **Execution**

The unit tests can be executed by executing the `test.py` file inside the `app` folder.
The `main.py` file is intended for further development around this functions.
