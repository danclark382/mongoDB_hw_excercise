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

## Get your API key
1. Navigate to https://www.alphavantage.co/support/#api-key
2. Fill out the form and click 'GET FREE API KEY'
3. Once your key is generated, open keys.json
4. Copy and paste the generated key into the keys.json file where it says

    *INSERT ALPHA VANTAGE API KEY*
