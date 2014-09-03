.. django-milcam
.. README.rst

A django-milcam documentation
=============================

    *django-milcam is a backend and frontend for Military Camera project*

.. contents::

Installation
------------
* Obtain your copy of source code from git repository: ``git clone https://github.com/anonymous-ukrainian-patriot/django-milcam.git``. Or download latest release from https://github.com/anonymous-ukrainian-patriot/django-milcam/tags.
* Run ``python ./setup.py install`` from repository source tree or unpacked archive. Or use pip: ``pip install django-milcam``.
* You will then want to create the necessary tables. If you are using south for schema migrations, you'll want to:

::

    python manage.py migrate milcam

* For those who are not using south, a normal ``syncdb`` will work:

::

    python manage.py syncdb

Configuration
-------------
Add ``'uuidfield'``, ``'geoposition'``, ``'sorl.thumbnail'``, ``'milcam'`` and ``'tastypie'`` to ``settings.INSTALLED_APPS``.

    INSTALLED_APPS = (
        ...,

        'uuidfield',
        'geoposition',
        'sorl.thumbnail',
        'tastypie',
        'milcam',

        ...,

    )

And to ``urls.py``.

    urlpatterns = patterns('',
        ...,

        url(r'^milcam/', include('milcam.urls')),

        ...,

    )

Licensing
---------
django-milcam is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.
All rights to all the libraries are located in the ``milcam/static/milcam/lib`` directory belong to their authors.

Contacts
--------
**Project Website**: https://github.com/anonymous-ukrainian-patriot/django-milcam

**Author**: Anonymous Ukrainian Patriot <anonymous.ukrainian.patriot@gmail.com>
