# Copied from psf/requests repository
# This file contains API-related functionality

import requests

def get(url, params=None, **kwargs):
    """Sends a GET request."""
    return requests.request('get', url, params=params, **kwargs)

def post(url, data=None, json=None, **kwargs):
    """Sends a POST request."""
    return requests.request('post', url, data=data, json=json, **kwargs)

def put(url, data=None, **kwargs):
    """Sends a PUT request."""
    return requests.request('put', url, data=data, **kwargs)

def delete(url, **kwargs):
    """Sends a DELETE request."""
    return requests.request('delete', url, **kwargs)
