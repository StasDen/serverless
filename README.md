# serverless

Azure serverless queue trigger function

Implementing serverless queue trigger function for university lab

**Using:**  
Python 3.10  
Azure services: Function App, Service Bus, IoT Central Application, Container Instance

Download
-
Download [Python 3.10](https://www.python.org/downloads/)  
Download [Visual Studio Code](https://code.visualstudio.com/)  
Install "Azure Functions" extension

Usage
-
To use the function locally you need to:  
* Create Function App
* Create a queue in Service Bus
* Set up data export to queue for the device in IoT Central Application
* Create a database using Azure database services
* **IMPORTANT!** Create a new database and table based on your device data export

See [Azure](https://learn.microsoft.com/en-us/azure/?product=popular) and [MySQL](https://dev.mysql.com/doc/) documentations for help

Then: 
* Run `pip3.10 install azure-functions` to install azure-functions lib
* Run `pip3.10 install azure-servicebus` to install azure-servicebus lib
* Run `pip3.10 install mysql-connector-python` to install mysql-connector-python lib
* Create env variables in `local.settings.json` file(AZ_DB_HOST, AZURE_SERVICEBUS_CONNECTION_STRING etc)
* **IMPORTANT!** Change object properties to send based on your device data export
* Debug the function using the "Attach to Python Functions" option

**Useful:**  
If there are dead letters, debug "dlq.py" to handle them as well  
To use it on Azure, deploy the function using Function App Deployment Center

Gallery
-
"function.app" debug terminal output

<img width="1020" alt="Screenshot 2023-12-01 at 09 54 04" src="https://github.com/StasDen/serverless/assets/93178776/5e063324-d17f-4eca-9c78-650fff8b0a7b">
