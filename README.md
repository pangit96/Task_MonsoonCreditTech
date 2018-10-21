# Monsoon CreditTech Task

- Setup Apache Server in 3 docker-containers (A,B,C)
- Confiure Apache-proxy in container A to map the requests made for **domainB.monsoonfintech.com** and **domainC.monsoonfintech.com** to container B and C respectively.
- Limit Access to selective IP's


### In Repository

- Dockerfiles of respective containers (A,B,C) are in directories containerA, containerB, containerC.
- Directory of containerA contains two apache-proxy configuration files **domainB.conf** and **domainC.conf** which required to copied to the apache directory in container A 
- Executable file **task.py** does the following task <br />
  <>Builds all the dokcer Dockerfile (cont_a:v1, cont_b:v1, cont_c:v1) <br />
  <>Runs respective containers (conta, contb, contc): <br />
  <>Finds the IP's of all the containers and makes their DNS entry in **/etc/hosts** file

### Port Addressing
Make 3 containers. PAT them in this way:
```
Port 80 of base system   -> Port 80 of container A
Port 8082 of base system -> Port 80 of container B
Port 8083 of base system -> Port 80 of container C
```


## STEPS

### Configure apache and proxy server in container A
```
#docker run -it -p 80:80 --name conta ubuntu:latest

Install Apache:
#docker apt-get install apache2 apache2-utils -y

Enable a2enmod scrpit
#a2enmod proxy
#a2enmod proxy_http

Create your virtual-host file
##Copy virtual-host files domainB.conf domainC.conf from base-system to /etc/apache2/sites-available/
                    <VirtualHost *:80>
                    ServerName domainb.monsoonfintech.com
                    <Proxy *>
                    Order allow,deny
                    Allow from 13.67.117.251
                    Allow from 52.187.31.90
                    Deny from all
                    </Proxy>
                    ProxyPass / http://localhost:8082/
                    </VirtualHost>
Only two IP's are allowed to pass this proxy, rest are denied the access.


Enable the virtual host configuration
#a2ensite domainB.conf domainC.conf

Restart apache services to run in the background of the container A
#/usr/sbin/apachectl -DFOREGROUND
```
### Configure apache in container B
```
#docker run -it -p 8082:80 --name contb ubuntu:latest

#docker apt-get install apache2 apache2-utils -y

Set container's ServerName to domainb.monsoonfintech.com in file /etc/apache2/sites-available/000-default.conf

#/usr/sbin/apachectl -DFOREGROUND

(Follow the same steps for container C with port 8083 and ServerName domainC.monsoonfintech.com)
```
## Your proxy server configuration is completed
```
open web browser and make the access request on server of container A
#firefox http://domainb.monsoonfintech.com
This will redirect to index page of container B which displays "Hello Container B".
``` 
### I repeated the above steps with the help of Dockerfiles.
```
Container A Dockerfile:
               FROM ubuntu:latest
               MAINTAINER pandit.utkarsh14@gmail.com
               RUN apt-get update -y
               RUN apt-get install apache2 apache2-utils -y
               RUN a2enmod proxy
               RUN a2enmod proxy_http
               COPY domainB.conf /etc/apache2/sites-available/domainB.conf
               COPY domainC.conf /etc/apache2/sites-available/domainC.conf
               WORKDIR /etc/apache2/sites-available/
               RUN a2ensite domainB.conf
               RUN a2ensite domainC.conf
               CMD /usr/sbin/apachectl -DFOREGROUND
    
Build the docker file:
#docker build /home/test_user/task/containerA/ -t cont_a:v1
    
Run the container in the background silently
#docker run --name conta -dit -p 80:80 cont_a:v1
```


### <br /><br /><br />RUN THE SCRIPT **task.py** TO SAVE THE EFFORTS <br /><br /><br /><br /><br /><br /><br />
   
    
    
####  Submission By
###### UTKARSH PANDIT
###### pandit.utkarsh14@gmail.com
    
   
     
