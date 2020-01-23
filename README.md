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
## Python Package Documentation
| | |
|----|:----:| ----:|
|[PyMongo](https://api.mongodb.com/python/current/)|[Alpha-Vantage](https://alpha-vantage.readthedocs.io/en/latest/)|
|[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)|[Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html)
|[Requests](https://2.python-requests.org/en/master/)|[JSON](https://docs.python.org/3/library/json.html#basic-usage)|
## Create your MongoDB Atlas Account
1. Navigate [Here](https://www.mongodb.com/cloud/atlas/register)
2. Register for a free account using your school email address
3. Create a starter cluster (The only free option)
4. Keep all defaults for this page and click next
5. Next is the main page for the Atlas Cloud
6. Click Database Access from the left panel (under security), then add a new user
7. Create a new username and password for yourself  with admin access. Save these in the keys.json file under the keys mongodb_username, mongodb_password.
8. Below Database Access, Click Network Access then Add IP Address
9. Click Allow Access from anywhere, then hit confirm

## Download MongoDB Compass
1. Navigate [Here](https://www.mongodb.com/download-center/compass)
2. Keep the default version
3. Change your Platform to match the OS you are using
4. Click download
5. Navigate [Here](https://docs.mongodb.com/compass/master/install/) and follow the rest of the installation instructions

## Connect Compass to Atlas Cloud
1. Go to the homepage of your Atlas Cloud
2. From the left panel, click Clusters under Atlas
3. Under your cluster name in the sandbox section, click connect
4. Click the last option to connect to Compass
5. Click I have Compass
6. Leave the default version
7. Copy the connection string and open your Compass application
8. On the top left ribbon of Compass, click connect
9. MongoDB will detect the connection string in your clipboard and fill out the form
10. For troubleshooting, visit [Here](https://docs.atlas.mongodb.com/compass-connection/)


## Get your API key
1. Navigate [Here](https://www.alphavantage.co/support/#api-key)
2. Fill out the form and click 'GET FREE API KEY'
3. Once your key is generated, open keys.json
4. Copy and paste the generated key into the keys.json file under the key alphavantage_api_key
