<img src="https://user-images.githubusercontent.com/45560312/130338826-f3c308ae-23b6-4fa3-b8db-78151861de8c.png" width="500" height="150">
<img src="https://user-images.githubusercontent.com/45560312/130338832-9a221ab5-cd4b-4194-87a2-4974e6400443.png" width="200" height="150">


# Heroku Configuration for Python - PYODBC

## To get you started writing your Microsoft SQL Server Application powered by Python/PyODBC and unixODBC.

### Introduction
#### Why did i make this templete for your? I was working on a Flask Application for one of my clients and it was a pain and nightmare to configure it.
<p> You know people make things so hard when it is a really simple solution hope this repo will help you to get your work done ASAP</p>

## Getting Started

#### Firstly you need to clone this repo / fork my repo.
<p>Once done with that follow these steps</p>
* Change your connection string in conn to your database - I filled in the connection string for you i made that into a templete for your :)

#### Troubleshooting
````
if you see Connection Failed - Check your connection string and Database else, if successful congratulations you have done the most important step so far.
````

#### Deployment
* Add the code to app.py which you are bootstrapping from else edit Proc to your app file
* Fire up GitHub and upload the files to your repo.
* Now in Heroku - Create a new Application
* Under the deployment tab
````
 - Select GitHub Deployment Method - Link up the repo to your Heroku
````
##### Final Step
###### In settings
* Add the buildpacks exactly in that order in the photo below

![image](https://user-images.githubusercontent.com/45560312/130338748-f1c2ed91-d21f-4e8a-83bd-d7bbaf42c191.png)


* If you want to copy and paste
````
https://github.com/heroku/heroku-buildpack-apt.git
https://github.com/heroku/heroku-buildpack-python.git
https://github.com/matt-bertoncello/python-pyodbc-buildpack.git
heroku/python
````

#### Build your App and happy coding.

### Guide crafted with <3 from ADG

### Author: Ashlin Darius Govindasamy 
#### ADGSTUDIOS : https://adgstudios.co.za

---------------------------------------------------
| Date            |  Changes                      |
|-----------------|-------------------------------|
| 2021/08/22      |  Added Initial Files          |
---------------------------------------------------
