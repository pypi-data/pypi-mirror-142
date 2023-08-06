"""Class module to interface with Asana.
"""
import os

from aracnid_logger import Logger
import asana

# initialize logging
logger = Logger(__name__).get_logger()


class AsanaInterface:
    """Asana interface class.

    Environment Variables:
        ASANA_ACCESS_TOKEN: Access token for Asana.

    Attributes:
        client: Asana client.

    Exceptions:
        TBD
    """

    def __init__(self) -> None:
        """Initializes the interface.
        """
        logger.debug('working')

        # read environment variables
        asana_access_token = os.environ.get('ASANA_ACCESS_TOKEN')

        # initialize asana client
        self.client = asana.Client.access_token(asana_access_token)
