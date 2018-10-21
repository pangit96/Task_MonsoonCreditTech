#!/usr/bin/python2

import commands as cm
print("""	 *********** MONSOON CREDITTECH *********** 

         -----------    DO NOT HURRY    -----------  

          wait  for  the  process  to  complete .
               do not press any button .
        """)


print(cm.getoutput("sudo docker build containerA/ -t cont_a:v1"))
print(cm.getoutput("sudo docker run --name conta -dit -p 80:80 cont_a:v1"))


print(cm.getoutput("sudo docker build containerB/ -t cont_b:v1"))
print(cm.getoutput("sudo docker run --name contb -dit -p 8082:80 cont_b:v1"))

print(cm.getoutput("sudo docker build containerC/ -t cont_c:v1"))
print(cm.getoutput("sudo docker run --name contc -dit -p 8083:80 cont_c:v1"))

ipb=cm.getoutput("sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' contb")
ipc=cm.getoutput("sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' contc")

f1=open('hosts','w')
f1.write("""127.0.0.1 localhost
{} domainb.monsoonfintech.com
{} domainc.monsoonfintech.com""".format(ipb,ipc))
f1.close()


cm.getoutput("sudo cat hosts >> /etc/hosts")
