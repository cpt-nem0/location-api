# location-api

## Running locally
run the following command in the root dir

```uvicorn main:app --host 0.0.0.0 --port 8080```

<br>

## Using docker
- build the image

   ```docker build -t location-api .```

- run the image

   ```docker run -p 80:80 --name testing -it test-api```

<br>

## API Endpoints
| Endpoint | Request | Description|
| ----------- | ----------- | ----------- | 
|  / | GET | To check if the API is running or not |
| /getAddressDetails | POST | To get the location information for the given address |

<br>

## Sample request
<br>


**Request:**
```
{
    "address": "1, rue de la paix, 75008 Paris",
    "output_format": "json"
}
```
> **api_key** goes as the request parameter, example: `url?api_key=<api_key>` 
<br>

**Response:**
```
{
    "coordinates": {
        "lat": 48.8685708,
        "lng": 2.3302606
    },
    "address": "1 Rue de la Paix, 75002 Paris, France"
}
```