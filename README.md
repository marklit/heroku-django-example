= Django + Heroku + Bootstrap Example =

== Command cheatsheet ==

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
