# Specter Assignment

This repo contains details for the Specter Assignment
Organiza

# Install

This Project requires that you have Python 3.8.1 installed. If you do not have it installed, you can download it [here](https://www.python.org/downloads/release/python-381/).

## To Setup a Python 3  Virtual  Environment

```python3 -m venv /path/to/new/virtual/environment```

Example:

```python3 -m venv venv```

## Activate Virtual Environment

### For Windows
```bash
source /path/to/new/virtual/environment/Scripts/activate
```
Example:
```bash
venv/Scripts/activate
```

### For Linux and MacOS
```bash
source /path/to/new/virtual/environment/Scripts/activate
```
Example:

```bash
source venv/Scripts/activate
```

### Install necessary Libraries

```bash
python3 pip install -r requirements.txt
```
To run the second scraper (scraper_2.py), you need to have Google Chrome installed as well as Chromedriver on your laptop. Assuming

# Usage

To use the project:

1. Clone the project to your local machine
2. Create a virtual environment, named `env`, with `python3 -m env /env` in project root
3. Activate the virtual environment with `source env/bin/activate`
4. Run any of the scrapers `python scraper_1.py` or `python scraper_2.py`
