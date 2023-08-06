import json
import logging
from typing import Dict, List, Optional, Union

from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from arcane.core.exceptions import BadRequestError

class GoogleAnalyticsAccountLostAccessException(Exception):
    """ Raised when we cannot access to an account """
    pass

class GoogleAnalyticsServiceDownException(Exception):
    """ Raised when we cannot access to an account """
    pass


def get_exception_message(view_id: str, access_token: Optional[str] = None) -> str:
    if access_token:
        return F"We cannot access your view with the id: {view_id}. Are you sure you have access and entered correct ID?"
    else:
        return F"We cannot access your view with the id: {view_id} from the Arcane account. Are you sure you granted access and gave the correct ID?"


def get_metrics_from_view(ga_view: str,
                          adscale_key: str,
                          date_ranges: Dict=None,
                          metrics: List=None,
                          **optional_params):
    """
    helper to call the Google Analytics Core Reporting API. More information on the following link :
    https://developers.google.com/analytics/devguides/reporting/core/v4/basics
    """

    if metrics is None:
        metrics = [{'expression': 'ga:transactions'}]
    if date_ranges is None:
        date_ranges = [{'startDate': '30daysAgo', 'endDate': 'yesterday'}]

    required_params = {
        'viewId': ga_view,
        'dateRanges': date_ranges,
        'metrics': metrics
        }

    body = {'reportRequests': [{**required_params, **optional_params}]}

    scopes = ['https://www.googleapis.com/auth/analytics.readonly']
    credentials = service_account.Credentials.from_service_account_file(adscale_key, scopes=scopes)

    service = build('analyticsreporting', 'v4', credentials=credentials)

    try:
        res = service.reports().batchGet(body=body).execute()
    except HttpError as err:
        message = json.loads(err.content).get('error').get('message')
        raise BadRequestError(f'Error while getting data from GA. "{message}"') from err
    logging.info(res)
    return res


def get_view_name(
    view_id: str,
    adscale_key: Optional[str] = None,
    access_token: Optional[str] = None
) -> Optional[str]:
    """
        From an view id check if user has access to it and return the name of view

        adscale_key or access_token must be specified
    """
    # Create service to access the Google Analytics API

    scopes = ['https://www.googleapis.com/auth/analytics.readonly']
    if access_token:
        credentials = Credentials(access_token, scopes=scopes[0])
    elif adscale_key:
        credentials = service_account.Credentials.from_service_account_file(adscale_key, scopes=scopes)
    else:
        raise ValueError('one of the following arguments must be specified: adscale_key or access_token')

    service = build('analytics', 'v3', credentials=credentials)
    if 'ga:' in view_id:
        view_id = view_id.replace('ga:', '')

    try:
        views = service.management().profiles().list(accountId='~all', webPropertyId='~all').execute()
    except HttpError as err:
        if err.resp.status >= 400 and err.resp.status < 500:
            raise GoogleAnalyticsAccountLostAccessException(get_exception_message(view_id, access_token))
        else:
            raise GoogleAnalyticsServiceDownException(f"The Google Analytics API does not respond. Thus, we cannot check if we can access your Google Analytics account with the id: {view_id}. Please try later" )

    if view_id not in [view.get('id') for view in views.get('items', [])]:
        raise GoogleAnalyticsAccountLostAccessException(get_exception_message(view_id, access_token))

    for view in views.get('items', []):
        if view.get('id') == view_id:
            return view.get('name', '')
