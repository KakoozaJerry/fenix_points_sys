This system calculates the total number of points obtained by employees per month

Within the base folder is the main app structure, it has the tests file which contains the core logic for prior calculation of the points for each employee from the employees db and the they are pushed to the Points table which has a passwordz field for each employees password, a points attained field, a current role field, and an employee id field. Initially each employee can login and view their individual points using their employee id , and default password as 123 which can be changed by the admin . On login , they are notified with their current number of points.
This system is built with django and you can run the requirements.txt file to view the libraries required to be installed.

move to the jerry folder and type in your commandline after installing required libraries 
> python manage.py runserver
Go to the local host within your browser and type in the url section localhost/hello
Enter a user id as the username e.g 3 and a password as 123 
You are then redirected to a page showing you your number of points

The admin has a custom super user account to edit points of each employee through the django admin platform 
they are also able to assign new passwords to different users
