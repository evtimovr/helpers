# Помощни script-ове

Първоначален setup:

```sh
# clone the repo
git clone github:lazheshli/helpers
cd helpers

# create a python virtual environment
python3 -m venv venv
source venv/bin/activate

# install the dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

И после:

```sh
# activate the virtual environment, if not done already
source venv/bin/activate

# add an input file
cp ~/downloads/data.csv input.csv

# convert it to html using the template
python convert.py

# check the result
open output.html
```
