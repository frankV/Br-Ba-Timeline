The [Br]eaking [Ba]d Timeline
=============

####This project aims to create a visual timeline representation of AMC's Breaking Bad.

##Episode Data Collected From:
Data for Epsiodes up to Season 5 - Part 1
<br>[A Year in the Life of Walter White: A Breaking Bad Timeline](http://blog.thegreenfieldgroup.org/a-year-in-the-life-of-walter-white-a-breaking-bad-timeline/)
<br>by Sean Aranda

Data for Episodes up to Season 3
<br>[How Much Time Has Passed on Breaking Bad?](http://www.vulture.com/2011/07/breaking_bad_calendar.html)
<br>by Ray Rahman

Epsiode meta-data collected from [IMDb](http://imdb.com) using [IMDbPy](http://imdbpy.sourceforge.net/)


##Running the Episode Scraper
```bash
$ python scrape-eps.py data/seasons_time_guide.html
Walt's birthday = 1957-09-07
Walt's 50th = 2007-09-07
First calendar day in show = (2007, 36, 5)


1.1: "Pilot," (3 weeks) Calendar Duration: 2007-09-07 to 2007-09-28
1.2: "Cat’s in the Bag … " (3 weeks, 2 days)  Calendar Duration: 2007-09-28 to 2007-09-10
...
5.3: "Hazard Pay," (50 weeks) Calendar Duration: 2008-08-01 to 2008-08-22
5.4: "Fifty-One," (52 weeks)  Calendar Duration: 2008-08-22 to 2008-09-05
```


##Running the Flask App
```bash
$ python manage.py runserver
 * Running on http://0.0.0.0:5000/
```

##Running the Angular App
**THIS WILL COME OUT LATER**
```bash
$ grunt server
Running "server" task

Running "configureProxies" task
Proxy created for: /bb.timeline to localhost:5000

Running "connect:livereload" (connect) task
Started connect web server on 127.0.0.1:9000.

Running "watch" task
Waiting...
```


##Stack
[Flask][Flask]
<br>[Angularjs][Angularjs]
<br>[MongoDB][MongoDB]
<br>[IMDbPy][IMDbPy]
<br>[Bootstrap][Bootstrap]
<br> - Modified 'Minimal' theme by [BlackTie.co][blacktie.co]

###Breaking Bad Logo
Entirely CSS and SVG. Created by [Tim Pietrusky][timpietrusky.com] and adapted from his [codepen][http://codepen.io/TimPietrusky/pen/Bsegb]


##Project Creators
[Emily Morehouse](/emilyemorehouse)
<br>
[Frank Valcarcel](/frankv)


[Flask]: http://flask.pocoo.org/
[Angularjs]: http://angularjs.org/
[MongoDB]: http://mongodb.org
[IMDbPy]: http://imdbpy.sourceforge.net/
[Bootstrap]: https://getbootstrap.com
[blacktie.co]: http://www.blacktie.co/