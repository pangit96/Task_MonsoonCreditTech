FROM ubuntu:latest
MAINTAINER pandit.utkarsh14@gmail.com
RUN apt-get update -y
RUN apt-get install apache2 apache2-utils -y
RUN echo "Hello Container C" > /var/www/html/index.html
RUN sed -i '9 a ServerName domainc.monsoonfintech.com' /etc/apache2/sites-available/000-default.conf
CMD /usr/sbin/apachectl -DFOREGROUND

