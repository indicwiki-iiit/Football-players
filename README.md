# Football-players
We are a group of 5 members and we are working on football players domain.
# Description
The goal of this project is to automate the process of generation of wikipedia articles for football players in Telugu language.
## Installation

Create virtual environment in the project folder using the following commands.

```bash
$ pip install virtualenv
$ virtualenv -p python3.7 venv
```
After the successful creation of virtual environment (venv), clone the repository or download the zip folder of the project and extract it into the project folder.

Activate the virtual environment and headover to install the dependencies by following command.
```bash
$ pip install -r requirements.txt
```
requirements.txt comes along with the Project Directory.
## Guide to generate male football players articles and corresponding XML files
* Clone the repository into the local system.

* For generating an article, one need: players(dataset), render.py, playerstemplate and genXML.py. Make sure that these files are available.

* Running the readDATA.py loads the dataset generates the sweetviz report and pickleDF.pkl

* Running the genXML.py initialises all the functions necessary for XML generation  

* Both the article and the XML file can then be generated by running the render.py file

This repository contains the details and data under TeWiki Project for Football players domain.
### Template 
* playerstemplate.j2 -- Contains the final Jinja2 Template for the male players article generation.

### Data
* players.csv-- This is the dataset for the football players with all the attributes for them.

### Scraping 

* scraping.py-- This is the scraping code used for extracting national career,birth place,highest market value,full name,debuts,tags details.

* clubname_scraping.py-- This is the scraping code used for extracting clubname of a player.

* Extra_scraping.py-- This is the scraping code used for additional data  of a player.

### Male Football players sample article

* This is the sample article for male football players 
 
### genXML.py
  
* This file used in importing the standard format of xml of male football players.

### render.py

* This is the code used for rendering the football players articles using jinja2 template named playerstemplate.j2 file in male football players folder.

### readData.py

* This contains all python code for generating football players sweetviz report,pickle file.

## Guide to generate female football players articles and corresponding XML files
* Clone the repository into the local system.

* For generating an article, one need: players(dataset), render1.py, femaleplayers_template.j2 and genXML1.py. Make sure that these files are available.

* Running the readDATA1.py loads the dataset generates the sweetviz report and female_plyrsDF.pkl

* Running the genXML1.py initialises all the functions necessary for XML generation  

* Both the article and the XML file can then be generated by running the render1.py file

This repository contains the details and data under TeWiki Project for Football players domain.
### Template 
* femaleplayers_template.j2 -- Contains the final Jinja2 Template for the female players article generation.

### Data
* female_players_dataset(final).csv-- This is the dataset for female football players with all the attributes for them.
### Scraping 
* scraping_female.py This is the scraping code used for extracting all the attributes of a player.

### Sample article 
* This is the sample article for female football players 
### genXML1.py
* This file is used in importing the standard format of xml of female football players.

### render1.py
* This is the code used for rendering the female football players articles using jinja2 template named femaleplayers_template.j2 file in female football players folder.
### readData1.py 
* This contains all python code for generating female football players sweetviz report,pickle file.
### IndicWiki Summer Internship - [FOOTBALL_PLAYERS].pdf(report):
* This pdf file is about final report of our team regarding IndicWiki Summer Internship.
### requirements 
* This contains all the packages and libraries that are necessary for building this project.

