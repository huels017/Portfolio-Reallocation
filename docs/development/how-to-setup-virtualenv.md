# How to setup a `virtualenv` environment

## `virtualenv` allows us to isolate our Python project

`virtualenv` is used to isolate Python environments from each other. This is
useful for our application because it ensures we are working with the same version
of Python and the same Python packages.

I like to think of a `virtualenv` environment as a box that we can enter and exit. Inside the box we have all of our needed Python packages and Python version. In order to work, we need to be inside this box. When we want to work on other projects, we exit our box.

## How to use `virtualenv`

1. Install `virtualenv` (only needs to happen once):

	`sudo pip install virtualenv`

2. Create a virtual environment (only needs to happen once):

	1. Navigate to the directory you want the environment to be in. This is usually inside our git repository.

	`cd /path/to/git/repo`

	2. Create the virtual environment

	`virtualenv env`

	If you type `ls` you should see a folder called `env`. This is the environment you just created. However, we have not 'activated' or 'gone into' our environment yet.

3. Enter and exit the virtual environment:

	* To enter the virtual environment, type:

	`source env/bin/activate`

	* To end the environment session (exit the virtual environment), type:

		`deactivate`

## Additional Reading

[Pipenv & Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

[Virtualenv](https://virtualenv.pypa.io/en/stable/)
