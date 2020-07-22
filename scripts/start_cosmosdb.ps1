$location = Get-Location

Set-Location "C:\Program Files\Azure Cosmos DB Emulator"

.\CosmosDB.Emulator.exe /EnableMongoDbEndpoint

Set-Location $location