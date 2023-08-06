"""
Metadata API

Metadata Coverage

.. _Metadata Coverage:
   https://developer.salesforce.com/docs/metadata-coverage/53
"""

import threading

from zeep import Client, Settings

from SFDCAPI.Constant import SFDC_API_V

class Metadata:
    """Metadata class."""

    def __init__(self, access, wsdl):
        """Constructor

        Args:
            access (tuple): The Salesforce session ID / access token and
                server URL / instance URL tuple
            wsdl (str): The path to the WSDL file
        """

        # Unpack the tuple for session ID / access token and server URL / instance URL
        self.id_token, self.url = access

        # Create client with setting of disable strict mode, use recovery mode
        setting = Settings(strict=False)
        client = Client(wsdl=wsdl, settings=setting)
        # Create the service with custom binding and URL
        binding = '{urn:enterprise.soap.sforce.com}SoapBinding'
        self.service = client.create_service(binding, self.url)

        # Create the SOAP header (this is different than the HTTP header)
        self.soap_header = {
            "SessionHeader": {
                "sessionId": self.id_token
            }
        }