| Install Pillow
  Since you are using ImageField, install Pillow:
  
.. code-block:: shell
  python -m pip install Pillow
 



| Make Migrations and Migrate Database

.. code-block:: shell
 python manage.py makemigrations
 python manage.py migrate

|Create a Superuser
 Run:

.. code-block:: shell
 python manage.py createsuperuser

| Enter your username, email, and password when prompted.

| Run Server and Add Products via Admin Panel
  Start server:

.. code-block:: shell
 python manage.py runserver

