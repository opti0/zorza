# Zorza

## About
An information service for schools with an advanced timetable interface.
Designed to look nice on many screens, be fast, comfortable to use, and solid.
Supports teacher substitutions, group absences, occasional schedule changes.
Includes a page for public displays and a tree of downloadable files/rich text.

## Setup
Install Django 2.0 or later and Python 3.4 or later.
For that, using Python virtual environments is recommended.

Now you can `git clone` the repository.
You will need to create a `zorza/localsettings.py` file and set `DEBUG`,
`SECRET_KEY`, `LANGUAGE_CODE`, `TIME_ZONE`.

The root (`/`) url is an alias for `/pages/home/`, which is a [Django flatpage](https://docs.djangoproject.com/en/2.0/ref/contrib/flatpages/). Create a flatpage with the URL `/home/` in Django administration (`/admin/`), otherwise you will get a 404. You have to create an account first with `./manage.py createsuperuser`.
In the footer there is a link to the flatpage with URL `/about/`.

Populating the timetable database should be done by scripts. The `zorza_scripts` repository is a collection of scripts for importing timetables generated by aSc TimeTables and tailoring the database for a specific usecase.

For a production setup, consult
https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
and
https://docs.djangoproject.com/en/2.0/howto/deployment/
.

The directories `mediafiles`, `staticfiles`, and favicons have to be served directly by the web server. Example nginx configuration for that:

```
	location /media  {
		alias /sites/zorza/mediafiles;
	}
	location /static {
		alias /sites/zorza/staticfiles;
	}
	location ~ ^/(android|apple-touch-icon|browserconfig|favicon|manifest|safari)(.*)\.(png|xml|ico|json|svg)$ {
		root /sites/zorza/staticfiles/favicons;
	}
```

This software is designed with response caching in mind because the content is mostly static and by nature not requiring urgent updates. Set `CACHE_MIDDLEWARE_SECONDS` in `localsettings.py` and configure your web server for response caching.

The page `/timetable/display/` displays remaining break/period time and teacher substitutions. It's intended to be run fullscreen in a browser on a public big screen.

## License
This project is licensed under GPLv3.

## Contributing
See CONTRIBUTING.md
