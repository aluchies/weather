weather
=======

print weather details via the command line
------------------------------------------

Why bother opening your browser to check the weather? Just type `weather` at the command line to see the daily forecast. Weather data is from wunderground.com via their API.

```
$ weather
> High: 73F
```

Installation
------------

Before installing, create a config.txt file in the project root directory with the following items:

```
api_key = xxxxxxxxxxxxx
zip_code = xxxxx
```

Then type the following to install:

```
python setup.py install
```