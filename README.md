# Website to learn german 
This is our private project about germany studies 
Hello Teams , i'm sharing with you source code to create website to learn Deutsch, you can at any time use the source code,


# Installation
```sh
conda create -n "Elearning" python=3.10
conda activate Elearning
pip install django
pip install Pillow
pip install mysqlclient
pip install colorama
```


#Configurations-DB
```sh
create user "elearning"@"localhost" IDENTIFIED BY "elearning
GRANT ALL PRIVILEGES ON * . * TO 'elearning'@'localhost';
flush privileges;
exit #we should exit MySQL server
mysql -u elearning -p <typePWD>

```
und Das ist Alles :)