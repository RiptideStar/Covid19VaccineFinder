# Covid19 Vaccine Availability Finder

https://cutt.ly/myshot

The website will keep searching / checking / reporting covid19 vaccine sign-up sites for availability continuously (some spots might become available due to any cancellations). If available spots are found, registered users are notified thru email immediately.

The website - 
1. lists a number of sign-up sites and their availability status
2. allowss users to register their emails to be notified when a spot of covid19 vaccine is available at a specific site
3. or unregister their emails from the site.

#
# TechNotes:
## Make Finder a service on Ubuntu Server:

1. Enable the port flask is running on (e.g. 5001) -- run with sudo or as root.
```
> ufw enable

> ufw allow 5001

> ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
20/tcp                     ALLOW IN    Anywhere
21/tcp                     ALLOW IN    Anywhere
22/tcp                     ALLOW IN    Anywhere
80/tcp                     ALLOW IN    Anywhere
888/tcp                    ALLOW IN    Anywhere
8888/tcp                   ALLOW IN    Anywhere
39000:40000/tcp            ALLOW IN    Anywhere
5001                       ALLOW IN    Anywhere
20/tcp (v6)                ALLOW IN    Anywhere (v6)
21/tcp (v6)                ALLOW IN    Anywhere (v6)
22/tcp (v6)                ALLOW IN    Anywhere (v6)
80/tcp (v6)                ALLOW IN    Anywhere (v6)
888/tcp (v6)               ALLOW IN    Anywhere (v6)
8888/tcp (v6)              ALLOW IN    Anywhere (v6)
39000:40000/tcp (v6)       ALLOW IN    Anywhere (v6)
5001 (v6)                  ALLOW IN    Anywhere (v6)
```

2. create and start flask app service
https://devstudioonline.com/article/deploy-python-flask-app-on-linux-server

```
systemctl start lineups.service
systemctl status lineups.service
systemctl stop lineups.service
```


## Create cron job to run the check

Run it every 3 mins:
```
root@iZ238n5r3z9Z:~$ crontab -e
*/2 * * * * python3 /alidata/www/covid19signupStatus/linuxcovid19OSExtract.py >> covidsignup.log 2>&
```
