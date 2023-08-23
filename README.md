Project:
Develop a web application with Django

Project Description:
This application was created to host a book blog.

How to run the program:

	1)Please use a virtual environment 
 
	2)Place your command line in /YOUR_FOLDER and then "git clone https://github.com/Alexandre-Kolobov/Projet_9.git"
	
	3)In the folder make "pip install -r requirements.txt" to set up the right configuration
	
	4)Now you are ready to launch the web app. In the commande line go to /YOUR_FOLDER and make "python manage.py runserver".
	
	
Users for demo:

	Login (superuser): Alex
	Mdp: 123456789
	
	Login: Claire
	Mdp: Test1234!
	
	Login: Raphaël
	Mdp: Test1234!
	
	Login: Thibault
	Mdp: Test1234!
 


How to generate and check an flake8 html report:
- Please use this command in your prompt : "flake8 --format=html --htmldir=flake8-report" (This will generate a new html report in flake8-report repository.)
- To open it, plase use your web browser to open the file index.html

Additional:
- If you need to create a new super user please put in the commande line "python manage.py createsuperuser"
- If you need to use Django's shell please put in the commande line "python manage.py shell"
- If you need to remove all data from database please put in the commande line "python manage.py flush"
