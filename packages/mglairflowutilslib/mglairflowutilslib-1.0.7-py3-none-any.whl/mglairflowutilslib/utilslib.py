from enum import Enum
import requests
from json_logic.builtins import BUILTINS
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import datetime, date, timedelta
import dateutil.parser as parser
import string
import random
import shortuuid
DT_FMT_HMSf = '%H%M%S%f'


class HttpMethodEnum(Enum):
    POST = 'POST'
    PUT = 'PUT'
    GET = 'GET'
    DELETE = 'DELETE'


def invoke_http_request(endpoint, method, headers, payload=None, json_data=None, timeout=61):
    """ here two exception block. one is for request exception and other is for json decoder exception.
    RequestException raise when some error occur in API response
    JSONDecodeError: sometimes we don't know our API response is in json format or not so, when we return
    response.json() it raise error if it not json format.
    """
    _request = requests_retry_session()
    _request.headers.update({
        **headers
    })
    try:
        response = None
        if method == HttpMethodEnum.GET.value:
            response = _request.get(url=endpoint, data=payload, timeout=timeout)
        if method == HttpMethodEnum.POST.value:
            response = _request.post(url=endpoint, data=payload, json=json_data, timeout=timeout)
        if method == HttpMethodEnum.PUT.value:
            response = _request.put(url=endpoint, data=payload, timeout=timeout)
        if method == HttpMethodEnum.DELETE.value:
            response = _request.delete(url=endpoint, data=payload, timeout=timeout)
        log_failed_http_request(endpoint, response.text, response.status_code)
        return response.json(), response.status_code
    except requests.exceptions.RequestException:
        print('Error raised while invoking %s', endpoint)
        raise
    except json.decoder.JSONDecodeError:
        print('JSON Decode Error raised while invoking %s', endpoint)
        return response, response.status_code


def requests_retry_session(
        retries=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504),
        session=None):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def log_failed_http_request(endpoint, response, status_code):
    if not is_success_request(status_code):
        msg = 'Http {} | Error-{} : {}'.format(endpoint, status_code, response)
        print('Error raised ', msg)


def is_success_request(status_code):
    return 200 <= status_code <= 299


def date_within_next(date, number, period):
    if period == "days":
        return datetime.utcnow() <= str_to_datetime(date) <= (
                datetime.utcnow() + timedelta(days=int(number)))
    elif period == "weeks":
        return datetime.utcnow() <= str_to_datetime(date) <= (
                datetime.utcnow() + timedelta(weeks=int(number)))


def date_within_last(date, number, period):
    if period == "days":
        return (datetime.utcnow() - timedelta(
            days=int(number))) <= str_to_datetime(date) <= datetime.utcnow()
    elif period == "weeks":
        return (datetime.utcnow() - timedelta(
            weeks=int(number))) <= str_to_datetime(date) <= datetime.utcnow()


def str_to_datetime(date_time, str_format="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(date_time, str_format)


def get_datetime(date_string):
    """ this function will return datetime object with 2022-01-10 00:00:00 format"""
    return parser.parse(date_string)


def get_unique_key():
    """
    This method is used to get 32 bit unique key
    Steps:
        1. Get current timestamp in "%H%M%S%f" string format
        2. Select random string of 8 char and add with timestamp
        3. Generate 12 bit random string using shortuuid
    :return: 32 bit Unique key
    """

    timestamp = datetime.now().strftime(DT_FMT_HMSf)
    random_str = timestamp + ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(8))
    uuid_str = shortuuid.ShortUUID().random(length=12)
    return '{}{}'.format(uuid_str, random_str)


ops = {
    **BUILTINS,
    'starts_with': lambda data, a, b: a.startswith(b),
    'ends_with': lambda data, a, b: a.endswith(b),
    'date_between': lambda data, a, b, c: str_to_datetime(b) <= str_to_datetime(a) <= str_to_datetime(c),
    'date_within_next': lambda data, a, b, c: date_within_next(a, b, c),
    'date_within_last': lambda data, a, b, c: date_within_last(a, b, c),
    'date_after': lambda data, a, b: str_to_datetime(a) > str_to_datetime(b),
    'date_before': lambda data, a, b: str_to_datetime(a) < str_to_datetime(b),
    'date_yesterday': lambda data, a: str_to_datetime(a).date() == datetime.utcnow().date() - timedelta(days=1),
    'date_today': lambda data, a: str_to_datetime(a).date() == datetime.utcnow().date(),
    'date_tomorrow': lambda data, a: str_to_datetime(a).date() == datetime.utcnow().date() + timedelta(days=1),
    'date_is_empty': lambda data, a: a == ""
}


module_id_dict = {'Campaigns': '1', 'Invoice': '2', 'SalesOrder': '3', 'PurchaseOrder': '4', 'Quotes': '5', 'Faq': '6',
                  'Vendors': '7', 'PriceBooks': '8', 'Calendar': '9', 'Leads': '10', 'Accounts': '11', 'Contacts': '12',
                  'Potentials': '13', 'Products': '14', 'Documents': '15', 'Emails': '16', 'HelpDesk': '17',
                  'Events': '18', 'Users': '19', 'Groups': '20', 'Currency': '21', 'DocumentFolders': '22',
                  'CompanyDetails': '23', 'Services': '24', 'ServiceContracts': '25', 'PBXManager': '26',
                  'ProjectMilestone': '27', 'ProjectTask': '28', 'Project': '29', 'Assets': '30', 'ModComments': '31',
                  'SMSNotifier': '32', 'LineItem': '33', 'Tax': '34', 'ProductTaxes': '35', 'PolicyPlan': '36',
                  'Commission': '37', 'AgentCommission': '38', 'VTERoundRobin': '41', 'VTESLALog': '42',
                  'VTEButtons': '43', 'VTEEmailPreview': '46', 'VReports': '49', 'RepliedSMSLog': '51',
                  'VTELabelEditor': '55', 'ToolbarIcons': '68', 'VTEFeedback': '88', 'AgentCommissionCFG': '90',
                  'Predicting': '91', 'Notifications': '95'}


def buildquery(json_object):
    if 'field' in json_object.keys():
        # In this case the json_object is an object which describes a single query
        if json_object.get("operator") != 'BETWEEN':
            return json_object.get("field") + " " + json_object.get("operator") + " '" + json_object.get("value") + "' "
        else:
            return json_object.get("field") + " " + json_object.get("operator") + " '" + json_object.get("value") + "' " + 'AND' + " '" + json_object.get("value2")+ "' "

    # else it is an "condition+filters" JSON - Object
    else:
        i = 0
        # result = "("
        result = ""
        filter_array = json_object.get("filters")
        while i < len(filter_array):
            # Add (maybe nested) expression
            result += " " + buildquery(filter_array[i]) + " "

            # if we are already at the end of our filters array, do not add condition string
            # or we WOULD end up with something like ( a OR b OR c OR )

            if i != len(filter_array) - 1:
                result += json_object.get("condition")
            i = i + 1
        # result += ")"
        return result
