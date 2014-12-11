# Blackbird
***Note, Blackbird is not ready for production use!***
Blackbird can be run on a Django test server locally, and is fully functional in that regard, but please do not use it in production! 

## Project Purpose: 
To create a barebones template from Bootstrap that can be used to build a personal website as quickly as possible. 

## Running Blackbird
For people experienced with Django and have a running installation of Django on their ‘nix based computer, this project should simply be: 
`git clone https://github.com/kevinjcliao/Blackbird`

`cd Blackbird`

`python manage.py runserver`

Note, this is only for debugging or testing purposes. ***do not use this in production***

If you have no experience with running Django apps on your computer, you’ll need to follow these steps (depending on your platform.)

### Mac OS X: 
Note, this is only for debugging or testing purposes. ***do not use this in production***
Head over to the [Python Downloads](https://www.python.org/downloads/mac-osx/) website and download the latest version of Python 2 if you haven’t already. Install that. 

[Install Git](http://git-scm.com/download/mac)

[Install pip.](https://pip.pypa.io/en/latest/installing.html#install-pip)

Install Django. 
`pip install Django`

Clone the git repository. 
`git clone https://github.com/kevinjcliao/Blackbird`

Open a terminal in the directory the git repository was cloned into and run: 
`python manage.py runserver`

Now go to: 
`http://localhost:8000/` in your browser. Enjoy! 

### Ubuntu: 
***To be written***

## Using Blackbird: 
To write a new webpage, please consult the separate README (Yet to be created.)

To use the blog, simply go to: `http://localhost:8000/admin` and login with username: admin password: password. It’s important to change those sometime before deployment but this is really just a toy right now. 

The admin interface is really ugly right now, but unfortunately it’s what Django ships with. 

## License: 

The placeholder content (fish themed text and images) in the blog has been taken from Wikipedia. Either the Wikimedia foundation or the respective owners of the photographs reserve their rights. Do not deploy Blackbird without removing these. 
