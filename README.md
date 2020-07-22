---
page_type: sample
languages:
- javascript
- python
- html
products:
- azure
description: "Azure Cosmos DB is a fully managed globally distributed, multi-model database service, transparently replicating your data across any number of Azure regions."
urlFragment: CosmosDB-FastAPI-Motor-Sample
---

# Build a Flask app using Azure Cosmos DB for MongoDB API
Azure Cosmos DB is a fully managed globally distributed, multi-model database service, transparently replicating your data across any number of Azure regions. You can elastically scale throughput and storage, and take advantage of fast, single-digit-millisecond data access using the API of your choice backed by 99.999 SLA. This sample shows you how to use the Azure Cosmos DB for MongoDB API to store and access data from a Flask application.

## Prerequisites

- Download the [Azure Cosmos DB Emulator](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator). The emulator is currently only supported on Windows. The sample shows how to use the sample with a production key from Azure, which can be done on any platform.

- If you don’t already have Visual Studio Code installed, you can quickly install [VS Code](https://code.visualstudio.com/Download) for your platform (Windows, Mac, Linux).

- Be sure to add Python Language support by installing one of the popular Python extensions.
    1. Select an extension.
    2. Install the extension by typing `ext install` into the Command Palette `Ctrl+Shift+P`.

    The examples in this document use Don Jayamanne's popular and full featured [Python Extension](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python).

## Clone the sample application

Now let's clone the app, set the connection string, and run it.

1. Open a git terminal window, such as git bash, and `cd` to a working directory.
2. Clone this sample repository
3. Run the following command to install the python modules.
    ```bash
    pip install -r .\requirements.txt
    ```
4. Open the folder in Visual Studio Code or your IDE of choice.

## NOTES

This sample has been adopted from the [CosmosDB-Flask-Mongo-Sample](https://github.com/Azure-Samples/CosmosDB-Flask-Mongo-Sample) in the Azure-Samples repository
as a proof-of-concept to utilize FastAPI with Motor to asynconously work with CosmosDB.

So far, so good.