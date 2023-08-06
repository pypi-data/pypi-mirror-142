""" Method to invoke endpoint http API"""
import requests


def call_csv_endpoint(
    endopint_url: str,
    csv_input_file_name: str,
    call_timeout: int = 15,
):
    """Receive CSV input and send it to a microservice HTTP endpoint, then return all data collection from json result"""
    with open(csv_input_file_name, encoding="utf-8") as csv_file:
        files = {"file": ("input_data.csv", csv_file, "text/csv")}
        response_from_api = requests.post(
            endopint_url, timeout=call_timeout, files=files
        )
    # raise error if there was a problem calling the endpoint
    response_from_api.raise_for_status()

    # read result as json
    result = response_from_api.json()

    # count number of business exceptions
    b_exceptions = result["data_collection"]["businessExceptions"]
    b_exceptions_data = []
    for b_excep in b_exceptions:
        b_exceptions_data.append({"exception_comment": b_excep["exceptionComment"]})

    # read names of additional data sets
    data_sets = result["data_collection"]["resultAdditionalData"]
    data_sets_names = []
    # data_sets_results = []
    for d_set in data_sets:
        data_set_name = d_set["inputFormatName"]
        data_sets_names.append(data_set_name)
        # get data set rows
        # input_object = d_set["inputObject"]
        # for ikey in input_object.keys():
        #    data_sets_results.append({data_set_name: input_object[ikey]})

    # prepare information to return
    result_data = {
        "business_exceptions_quantity": len(b_exceptions),
        "business_exceptions_data": b_exceptions_data,
        "data_sets_names": data_sets_names,
        # "data_sets_results": data_sets_results,
    }
    return result_data


def call_csv_endpoint_read_data_set(
    endopint_url: str,
    csv_input_file_name: str,
    data_set_name_to_return: str,
    call_timeout: int = 15,
):
    """Receive CSV input and send it to a microservice HTTP endpoint, then return all data collection from json result"""
    with open(csv_input_file_name, encoding="utf-8") as csv_file:
        files = {"file": ("input_data.csv", csv_file, "text/csv")}
        response_from_api = requests.post(
            endopint_url, timeout=call_timeout, files=files
        )
    # raise error if there was a problem calling the endpoint
    response_from_api.raise_for_status()

    # read result as json
    result = response_from_api.json()

    # read names of additional data sets
    data_sets = result["data_collection"]["resultAdditionalData"]
    for d_set in data_sets:
        data_set_name = d_set["inputFormatName"]
        if data_set_name == data_set_name_to_return:
            input_object = d_set["inputObject"]
            for ikey in input_object.keys():
                return input_object[ikey]

    # if reach this point the data set name was not found
    return {}
