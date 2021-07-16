# Football-players
we are a group of 5 members and we are working on football players domain.
# Description
The goal of this project is to automate the process of generation of wikipedia articles for football players in Telugu language.#
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

* Running the readDATA.py loads the dataset generates the sweetviz report and pickleDF.py

* Running the genXML.py initialises all the functions necessary for XML generation  

* Both the article and the XML file can then be generated by running the render.py file

This repository contains the details and data under TeWiki Project for Football players domain.
### Template 

> Github folder Link: https://github.com/indicwiki-iiit/Football-players/tree/main/template
> 
playerstemplate.j2 -- Contains the final Jinja2 Template for the male players article generation.

### Data

> Github folder Link: 
> 
* players.csv-- This is the dataset for the football players with all the attributes for them.

* female_players_dataset(final).csv-- This is the dataset for female football players with all the attributes for them.

### Scraping 

> Github folder Link:https://github.com/indicwiki-iiit/Football-players/tree/main/FOOTBALL%20MALE%20PLAYERS/Scraping%20files 
> 
* scraping.py-- This is the sraping code used for extracting national career,birth place,highest market value,full name,debuts,tags details.

* clubname_scraping.py-- This is the sraping code used for extracting clubname of a player.

* Extra_scraping.py-- This is the sraping code used for additional data  of a player.

### Sample article
> Github folder Link:https://github.com/indicwiki-iiit/Football-players/blob/main/FOOTBALL%20MALE%20PLAYERS/Male%20Football%20Players%20Sample%20Article.pdf
> 
This is the sample article for male football players 

> Github folder Link:https://github.com/indicwiki-iiit/Football-players/blob/main/FOOTBALL%20FEMALE%20PLAYERS/Female%20Football%20players%20Sample%20Article.pdf
> 
This is the sample for female football players 
### genXML.py
> Github folder Link:
>  
This file used in importing the standard format of xml of male football players.
> Github folder Link: 

This file used in importing the standard format of xml of female football players.

### render.py
>Github file Link:
>
This is the code used for rendering the football players articles using jinja2 template named playerstemplate.j2 file in male football players folder.
>Github file Link:

This is the code used for rendering the football players articles using jinja2 template named .j2 file in female football players folder.

## readData.py
>Github file Link: 
>
This contains all python code for generating football players sweetviz report,pickle and this the final code used for rendering the articles.
>Github file Link:
> 
This contains all python code for generating football players sweetviz report,pickle and this the final code used for rendering the articles.
## IndicWiki Summer Internship - [FOOTBALL_PLAYERS].pdf(report):

> Github file Link: 
This pdf file is about final report of the team regarding IndicWiki Summer Internship.

