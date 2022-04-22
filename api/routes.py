""" Contains the routes for the API """

from fastapi import HTTPException, Response

from api import app
from api.modals import Address
from api.logic import get_address_details


@app.get("/")
def home() -> None:
    """
    root api endpoint
    """
    return {"message": "Hello World!"}


@app.post("/getAddressDetails")
async def getAddressDetails(request: Address) -> Response:
    """
    returns the address details
    """
    address = request.address
    output_format = request.output_format

    try:
        response = get_address_details(address, output_format)
    except Exception as e:
        print('ERROR: {}'.format(e))
        raise HTTPException(
            status_code=400, 
            detail={
             'status': 'failed', 
             'message': 'error while getting address details'   
            })

    return response
