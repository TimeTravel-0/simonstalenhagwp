# simonstalenhagwp
downloads current simonstalenhag artwork to a local file if the website gets updated so it can be used as wallpaper 

Don't know Simon Stalenhag? See his work at http://simonstalenhag.se/ and get his books (e.g. Tales from the Loop)  at Amazon to support him!


This script tries to be light on the server, so there are multiple mechanisms to achieve this:
- No local file? Ok, load it.
- If the local file is newer than 1 hour, do not even ask.
- If the local file is older than 1 hour, ask for the main site date-modified. If in the past, dont download full page.
- If the main site is newer, get the first high resolution image (from bilderbig folder)

As the main site itself contians various images and loads approx 85MB (!) in ~300 requests right now, it should save some bandwidth ;)

Run it as cron or in "deamon mode" within your windowmanager autostart script, e.g.
(sleep 10; ~/git/simsonstalenhagwp/wp.py d) &


This script was created as a way to get the up-to-date artwork of Simon Stalenhag as wallpaper, no more, no less.
In no way I try to take credit for the images - it is great that they are provided in high resolution and without annoying watermarks so usage as wallpaper is possible - thanks!


## sample output:

```
rawe@hal9000:~$ ~/git/simsonstalenhagwp/wp.py d &
[1] 28777
now time: 2016-04-27 12:17:09.056514
loc file: 2016-04-08 09:49:36.571245
rem file: 2016-04-22 09:55:48
download check.
remote file:  http://simonstalenhag.se/bilderbig/by_crossing_2560.jpg
download start.
download end.

```
