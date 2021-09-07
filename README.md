# Covid19 Vaccine Availability Finder

In the Spring this year, I noticed that my community around me was vocalizing the fact that it was hard for them to find available covid vaccine centers in April and there are sites with available spots unknown to them. This results in two big problems - 
* People who want to get vaccines could not find the available sites. They have to manually check all sites known to them constantly for availability. There are two problems with this manual check - 
  * They don’t know all available sites
  * They have to constantly polling the sites for checking availability (a very painful time consuming process).
* Some vaccine sites could not utilize all capacities to deliver vaccines.

To address this mismatch of demands and supplies and those pain points, I decided to create a website to scan all vaccine sites in our area for availability and notify registered users when a spot becomes available.  

Essentially, this is how our web service works  -
1. People who want to get a vaccine shot go register at our website http://vaccine19.us/. (It is done with Python Flask framework.)
2. Our backend process (a Python web crawler managed by a cron job) scans all vaccine sites every 5 minutes for availability. And display availability on the website.
3. If there are openings, another Python backend process will notify registered users via email detailing the available time slots and locations. 

Without further ado, after I laid out the plan for this web service, I got straight away cracking at it. In my free time, whenever I wasn’t in class, I would be grinding away to make this web service a reality. After two weeks of non-stop hard work and debugging, we finally had a functional website. I am glad that I finished in early April. 

The Covid Vaccine Finder I developed helped 400+ users in Portland finding their vaccine shots. 150+ of them directly contacted me to appreciate how much time my web service has saved them. It warms my heart to know that I made an impact in people’s lives especially during the dreadful times of the pandemic.

Here is the website link: http://vaccine19.us/. I know by no means does the website look aesthetically exceptional, but the mission wasn’t to make a colorfully designed website since the focus was on the functionality of the web service as soon as possible in the emergency of the pandemic. 

I open-sourced my code for the project, so here is the GitHub for the project: https://github.com/RiptideStar/Covid19VaccineFinder  (You are here right now)



# TechNotes: Create and Run App as service and cron job

## Create and Run an app as a service on Ubuntu Server:

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

2. Create and Manage flask app service

Follow the instructions described here:
* https://devstudioonline.com/article/deploy-python-flask-app-on-linux-server

```
systemctl start vaccine19.service
systemctl status vaccine19.service
systemctl stop vaccine19.service
```
Note: Whenever app code is updated, need to restart the app service.

3. List all services
* https://www.tecmint.com/list-all-running-services-under-systemd-in-linux/
```
systemctl --type=service 

systemctl --type=service --state=active

# check a specific service
systemctl --type=service | grep lineups

# list all system services
service --status-all
```

## Create cron job to run an app automatically

Run it every 3 mins:
```
> crontab -e
*/2 * * * * python3 /alidata/www/covid19signupStatus/linuxcovid19OSExtract.py >> covidsignup.log 2>&
```
