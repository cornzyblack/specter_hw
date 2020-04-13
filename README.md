
# Specter Assignment

This repo contains details for the Specter Assignment. The following files are worth noting:

- [Specter HW Explanation.ipynb](https://github.com/cornzyblack/specter_hw/blob/master/Specter%20HW%20Explanation.ipynb) : Answers and explanation to the Assignment
- [scraper_1.py](https://github.com/cornzyblack/specter_hw/blob/master/scraper_2.py)  Basic Scraper
- [scraper_2.py](https://github.com/cornzyblack/specter_hw/blob/master/scraper_2.py) Improved Scraper


# Installation

This Project requires that you have Python 3.8.1 installed. If you do not have it installed, you can download it [here](https://www.python.org/downloads/release/python-381/).

To run the second scraper, you need to have Chrome and ChromeDriver installed. You can see here for how to download [Google Chrome](https://www.google.com/chrome/) and [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

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
python3 -m pip install -r requirements.txt
```
**NOTE**:
To run the second scraper (scraper_2.py), you need to have Google Chrome installed as well as Chromedriver on your Machine.

# Usage

To use the project:

1. Clone the project to your local machine
2. Create a virtual environment, named `env`, with `python3 -m env /env` in project root
3. Activate the virtual environment with steps highlighted above
4. Run any of the scrapers:
     
       python scraper_1.py
      
      or
      
       python scraper_2.py


The results are stored in **scraping_results_1.csv** and **scraping_results_2.csv** files
