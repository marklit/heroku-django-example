# Django + Heroku + Bootstrap Example

This is a small example of a [Django](https://www.djangoproject.com/) app which uses Twitter's [bootstrap](http://twitter.github.com/bootstrap/) for it's front end templates and runs on [Heroku](http://www.heroku.com/). You can see a working example [here](http://falling-ice-3499.herokuapp.com/). The `https` version can be seen [here](https://falling-ice-3499.herokuapp.com/).

## Command cheat sheet

Setting up the git repo:

    $ git remote show origin
    $ git remote rm origin
    $ git remote show origin
    $ git remote add origin git@github.com:marklit/heroku-django-example.git
    $ git remote add heroku git@heroku.com:falling-ice-3499.git

Load DB and fixtures:

    $ python manage.py syncdb
    $ python manage.py loaddata people

Creating admin users:

    $ heroku run python manage.py shell
    ...
    >>> from django.contrib.auth.models import User
    >>> admin_user = User.objects.create_superuser('mark', 'admin@test.co', 'pass')
    >>> admin_user.save()

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