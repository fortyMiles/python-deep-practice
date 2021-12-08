"""
“have the teaser file email.py. Python will load this email.py instead of the one in the standard library and will not find the message submodule in it.

The lesson here: don’t use module names already taken by the standard library. ☺

Python’s import mechanism is pretty complex. Apart from .py files, it can import the following:

Built-in modules (e.g., sys is “baked” into Python)
Directories with __init__.py file in them
Shared libraries (.so, .dll, .dyld …)
.pyc byte-compiled files (found in __pycache__ directory)
And more”


"""