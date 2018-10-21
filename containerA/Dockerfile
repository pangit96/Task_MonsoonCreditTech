FROM ubuntu:latest
MAINTAINER pandit.utkarsh14@gmail.com
RUN apt-get update -y
RUN apt-get install apache2 apache2-utils -y
RUN a2enmod proxy
RUN a2enmod proxy_http
RUN sed -i '9 a ServerName domaina.monsoonfintech.com' /etc/apache2/sites-available/000-default.conf
COPY domainB.conf /etc/apache2/sites-available/domainB.conf
COPY domainC.conf /etc/apache2/sites-available/domainC.conf
WORKDIR /etc/apache2/sites-available/ 
RUN a2ensite domainB.conf
RUN a2ensite domainC.conf
CMD /usr/sbin/apachectl -DFOREGROUND
