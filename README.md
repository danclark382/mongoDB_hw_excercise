# mongoDB_hw_excercise
### Prerequisties 
  * Python3
  * Virtual Environments
  * Installing Python Packages
  * Some Git
## Steps for setting up your virtual environment
1. Create a new directory for this homework and cd into it
    ```
    mkdir mongodb_hw
    cd mongodb_hw
    ```
2. Create a virtual environment in Python 3+
   ```
   # This creates a new virutal environemnt in python3 called venv
   python 3 -m venv venv
   ```
3. Activate the virtual environment
   ```
   source venv/bin/activate
   ```
4. Install the required dependencies (packages)
    ```
    pip install beautifulsoup4 requests alpha-vantage pymongo pandas
    ```
## Resources for documentation on the various technologies
### Python & Python Packages
| | |
|----|:----:|
|[PyMongo](https://api.mongodb.com/python/current/)|[Alpha-Vantage](https://alpha-vantage.readthedocs.io/en/latest/)|
|[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)|[Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html)
|[Requests](https://2.python-requests.org/en/master/)|[JSON](https://docs.python.org/3/library/json.html#basic-usage)|
|[Python3](https://docs.python.org/3/tutorial/)|[Web Scraping](https://www.dataquest.io/blog/web-scraping-tutorial-python/)
### MongoDB References
  * [MongoDB Documentation](https://docs.mongodb.com/)
  * [MongoDB Compass](https://docs.mongodb.com/compass/master/)
  * [MongoDB Atlas](https://docs.atlas.mongodb.com/)
  * [MongoDB Tutorial](https://www.tutorialspoint.com/mongodb/index.htm)
## Follow the steps below prior to editing any code!
## Git
1. If you are familiar with Git and the command line, cd into your homework directory and run this command in your terminal
    ```
    git clone git@github.com:danclark382/mongoDB_hw_excercise.git
    ```
2. If you are new to Git, take a look at [this](https://www.atlassian.com/git/tutorials) quickstart at some point. For now, navigate [here](https://github.com/danclark382/mongoDB_hw_excercise). On the right, click clone/download and download the zip. Unzip all the files to your homework directory.
## Download MongoDB Compass
1. Navigate [Here](https://www.mongodb.com/download-center/compass)
2. Keep the default version
3. Change your platform to match the OS you are using
4. Click download
5. Navigate [Here](https://docs.mongodb.com/compass/master/install/) and follow the rest of the installation instructions
## Create your MongoDB Atlas Account
1. Navigate [Here](https://www.mongodb.com/cloud/atlas/register)
2. Register for a free account using your school email address
3. Create a starter cluster (the free option)
4. Keep all defaults for this page and click next
5. Next is the main page for the Atlas Cloud
6. Click Database Access from the left panel (under security), then add a new user
7. Create a new username and password for yourself  with admin access. Save these in the keys.json file under the keys mongodb_username, mongodb_password.
8. Below Database Access, click Network Access then Add IP Address
9. Click Allow Access from anywhere, then click confirm
## Connect Compass to Atlas Cloud
1. Go to the homepage of your Atlas Cloud
2. From the left panel, click Clusters under Atlas
3. Under your cluster name in the sandbox section, click Connect
4. Click connect to Compass (last option)
5. Since you've downloaded Compass, click 'I have Compass'
6. Leave the default Version
7. Copy the connection string and open your Compass application
8. On the top left ribbon of Compass, click Connect, then Connect To
9. MongoDB will detect the connection string in your clipboard and fill out the form
10. Enter your password, then click Connect
11. This connection will be available under the recent category when you reopen Compass
12. For troubleshooting, visit [Here](https://docs.atlas.mongodb.com/compass-connection/)
## Connect MongoDB Atlas to Python
1. Go to the homepage of your Atlas Cloud
2. From the left panel, click Clusters under Atlas
3. Under your cluster name in the sandbox section, click Connect
4. Click Connect to Application
5. Under Driver click Python, then input your Python version
6. Copy the Connection String and input it into the connection_uri key in keys.json
## Get your API key
1. Navigate [Here](https://www.alphavantage.co/support/#api-key)
2. Fill out the form and click Get Free API Key
3. Once your key is generated, open the keys.json you downloaded from Git
4. Copy and paste the generated key into the keys.json file under the key alphavantage_api_key
### Initial Setup Complete!
## In the python files, you will find a lot of documentation of the code. Use the documentation to see what is happening under the hood. The instructions for completing the assignment can be found in the assignment.md file. 