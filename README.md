## Installing packages

We don't use virtualenv. Instead an app-engine approach is used of including packages in subdirectory. See https://cloud.google.com/appengine/docs/python/tools/using-libraries-python-27

```
pip install -t python_packages -r requirements.txt
```


## Deploying

```
rsync -av --exclude={*.pyc,.DS_Store,.git} ./ me@example.com:djangotest/
ssh me@example.com 'pkill python'
```
