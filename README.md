# E-Learning

### Projects Description
During my third semester at the University Moulay Ismail, I collaborated with two other students on a project aimed at helping people learn German more effectively. We developed a platform that offers exercises for reading, listening, grammar, and writing. Users can interact and correct each other's work, making the learning process more engaging and efficient.

### Technologies Used
- Django/Python
- Java Script/ Html / CSS
- MySQL
- Anaconda Venv

### Requirements
- Python 3.10
- MySQL8 Database
- Anaconda Installed


### Installation
- Source code configuration

```sh
conda create -n "Elearning" python=3.10
conda activate Elearning
pip install django
pip install Pillow
pip install mysqlclient
pip install colorama
```

- Database configuration

```sql
create user "elearning"@"localhost" IDENTIFIED BY "elearning
GRANT ALL PRIVILEGES ON * . * TO 'elearning'@'localhost';
flush privileges;
```

- Run the code

```sh
python manage.py runserver
```
