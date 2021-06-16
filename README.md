# Hotel-Management

Instructions 

1.Set up your virtual environment 
  - $ virtualenv venv 
  - $ source venv/bin/activate

2.Install Django 
  - $ python -m pip install Django


3.Set up database in HotelManagement/setting.py 

<img width="726" alt="Screen Shot 2564-06-16 at 23 14 00" src="https://user-images.githubusercontent.com/48642147/122255660-8a27af80-cef8-11eb-8705-a745131faacc.png">

**Note if you are using mySQL server via xampp, type is command first **

  - $ brew install mysql-client
  - $ echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile
  - $ export PATH="/usr/local/opt/mysql-client/bin:$PATH"
  - $ pip install mysqlclient

After finish setting up the database

  - Add information from the hotel.sql file to your database 
  - $ python3 manage.py inspectdb >hms/models.py
  - $ python manage.py makemigrations
  - $ python manage.py migrate


4.Runserver $ python manage.py migrate
