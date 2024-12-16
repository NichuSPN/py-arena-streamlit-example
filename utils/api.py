from arena.api.apiHandler import APIHandler

apiHandler = APIHandler("https://api.covidtracking.com")

def getHistoricValues(onSuccess, onError):
    apiHandler.runAPIWithCallbacks({
            "method": "get",
            "endpoint": "/v1/us/daily.json"
        },
        onSuccess,
        onError)

def getMetricOfADate(date, onSuccess, onError):
    apiHandler.runAPIWithCallbacks({
            "method": "get",
            "endpoint": f"/v1/us/{date}.json"
        },
        onSuccess,
        onError)

