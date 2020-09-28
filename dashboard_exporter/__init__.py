import os

import requests
from requests import Response


def exporter(
    guid: str,
    file_type: str = "PDF",
    width: int = 2000,
    height: int = 2000,
    personal_api_key: str = None,
    new_relic_region: str = "US",
) -> Response:
    """
    New Relic Dashboard exporter.
    :param new_relic_region: Your account region.
    :param personal_api_key: Your New Relic Personal API key.
    :param guid: The New Relic dashboard GUID.
    :param file_type: The output file type. Choose either PDF or PNG.
    :param width: The width of the dashboard. Max is 2000.
    :param height: The height of the dashboard. Max is 2000.
    :return: API Response.
    """
    if not personal_api_key:
        raise Exception("A New Relic API key is required.")

    headers = {
        "Content-Type": "application/json",
        "API-Key": personal_api_key,
    }

    endpoint_url = (
        "https://api.eu.newrelic.com/graphql"
        if new_relic_region == "EU"
        else "https://api.newrelic.com/graphql"
    )

    if not guid or not guid.strip():
        raise Exception("Dashboard GUID required.")

    query = (
        """
    mutation {
        dashboardCreateSnapshotUrl(guid: "%s")
    }
    """
        % guid
    )

    req = requests.post(url=endpoint_url, json={"query": query}, headers=headers)

    if not req.ok:
        req.raise_for_status()

    resp = req.json()
    
    if "errors" in resp:
        raise Exception(resp["errors"][0]["message"])
        
    url = resp["data"]["dashboardCreateSnapshotUrl"]
    
    url = url.split("?", 1)[0] + "?format=%s&width=%s&height=%s" % (
        file_type,
        width,
        height,
    )

    resp = requests.get(url=url)
    return resp
