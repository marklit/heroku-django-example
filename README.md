= Django + Heroku + Bootstrap Example =

This is a small example of a [Django](https://www.djangoproject.com/) app which uses Twitter's [bootstrap](http://twitter.github.com/bootstrap/) for it's front end templates and runs on [Heroku](http://www.heroku.com/).

== Command cheat sheet ==

Setting up the git repo:

    $ git remote show origin
    $ git remote rm origin
    $ git remote show origin
    $ git remote add origin git@github.com:marklit/heroku-django-example.git
    $ git remote add heroku git@heroku.com:falling-ice-3499.git

Load DB and fixtures:

    $ python manage.py syncdb
    $ python manage.py loaddata people

Pushing to github and heroku:

    $ git push -u origin master
    $ git push -u heroku master

Setting up Heroku:

    $ heroku run python manage.py syncdb
    $ heroku run python manage.py loaddata people

`.git/config` contents:

    [core]
    	repositoryformatversion = 0
    	filemode = true
    	bare = false
    	logallrefupdates = true
    [remote "heroku"]
    	url = git@heroku.com:falling-ice-3499.git
    	fetch = +refs/heads/*:refs/remotes/heroku/*
    [remote "origin"]
    	url = git@github.com:marklit/heroku-django-example.git
    	fetch = +refs/heads/*:refs/remotes/origin/*
    [branch "master"]
    	remote = origin
    	merge = refs/heads/master

Celery processor:

    $ foreman start
    $ heroku ps:scale celeryd=1