import json
import simplexml

import googlemaps
from fastapi import Response


def get_google_client(api_key: str) -> googlemaps.Client:
    """
    Returns the google client.
    """
    return googlemaps.Client(key=api_key)

def generate_response(response: dict, output_format: str) -> dict:
    """
    Generates the response to be sent to the client.
    """
    address = ''.join(response[0]["formatted_address"])
    coordinates = response[0]["geometry"]["location"]
    
    body = {"coordinates": coordinates, "address": address }
    
    if output_format == "json":
        body = json.dumps(body)
        return Response(
            content=body, 
            media_type="application/json"
        )
    
    elif output_format == "xml":
        body = simplexml.dumps({"root": body})
        return Response(
            content=body, 
            media_type="application/xml"
        )


def get_address_details(api_key: str, address: str, output_format: str) -> dict:
    """
    Gets the address details from the blockchain.
    """
    response = get_google_client(api_key).geocode(address)
    return generate_response(response, output_format)
