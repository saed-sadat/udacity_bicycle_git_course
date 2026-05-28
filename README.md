>**Note**: Please **fork** this Udacity repository so you have a **remote** repository in **your** GitHub account. Then you can clone the remote repository to your local machine. Later, as a part of the project, you will push your changes to the remote repository in your GitHub account.


# Explore US Bike Share Data

In this projekct we are exploring the bike sharing data provided by a Bike company to explore the data related to sharing data and 
calculate some statstics related to the most popular start and end stations as well as the mean time fo travel duration.

Further more the user can select between differnt cities or all 3 cities new york washinton and chicago to get the raw data.

## Information about how to use your project

In order to use the project you need to download the src folder. Put the csv files required in that particular folder and run the python script.
You need to have a python 3 installed on your local machine and a git version if you are intreste to use a version control system to track the changes. 

1.  install a python version on your computer. If possible get the latest version of Anaconda to be able to use a professional python environment
2. You need the Pandas libraries as well as numpy librraies to run the script 
3. This script will run on any platform such as Linux and Windows.
4.  For windows you should configure the Git bashand do the path configuration for bash.rc file

- In order to start the script you can use this command: python bikeshare_2.py from git bash or use an anconda Jupyter notebook or spyder environment
The code is divided in different functions and you can go throgh the functions and read the doc strings provided.

- If the csv file , which will be read by script is not available on your local machine the script will not run and will quit with a message accordingly.
If you need the csv files you may contact udacity providing you with this information or just sen me an email or message i will send it to you. Those files are currently ignored and are not uoloaded on github project.

- If you want to enhance the database you should uodate or enhance the following structures.

```python
import os
import time
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'all':'all'}
DAY_DATA=['monday','tuesday','wednesday', 'thursday','friday','saturday','sunday','all']
```
## Contribution guidelines

You are welcome to contribute to project. if you want so please fork the provided project and send a pull request.

- **Projket Voraussetzungen**
	- Python 3.10 or newer
	- PANDAS-Bibliothek instalado

- **Data Sources**
	- chicago.csv (local must be available)
	- new_york_city.csv (local must be available)
	- washington.csv(local must be available)


## Credits

In order to get to touch with the source of this project and ask for a traing contact see the link below

https://www.udacity.com/

## Date created

This project and also the readmefiles is created on Wedndeay 2026-05-27!