"""
Request to backend api to please send us some data.
"""

import requests
import json
from abc import ABC, abstractmethod
from typing import Dict, Any


class RequestAPI(ABC):

    def __init__(
        self,
        url: str,
        headers: Dict[str, str],
    ) -> None:
        self.url = url
        self.headers = headers

    @abstractmethod
    def make_request(
        self,
        endpoint_spec: str,
    ) -> Dict[str, Any]:
        pass


class CinchRequester(RequestAPI):

    def make_request(
        self,
        endpoint_spec: str = '1',
    ) -> Dict[str, Any]:
        """Make request to cinch frontend API.

        Parameters
        ----------
        endpoint_spec : The page number you desire to scrape.

        Returns
        -------
        Dict[str, Any]
            Response from cinch.com containing all the data you crave
        """
        response = requests.request("GET", f'{self.url}{endpoint_spec}', headers=self.headers)

        return json.loads(response.text)
