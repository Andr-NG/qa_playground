# flake8: noqa
# problems generated here https://chatgpt.com/c/68fb8ec8-438c-832d-aa10-1e6f8ba9270d

# You have an API response returning a list of folders, each containing files
# Write code that returns the total size of files per folder as a dict, e.g.:
# {"Docs": 400, "Images": 500}


from collections import defaultdict
from email.policy import default
from typing import Counter


def return_total():
    folders = [
        {
            "folder": "Docs",
            "files": [{"name": "A.txt", "size": 100}, {"name": "B.txt", "size": 300}],
        },
        {"folder": "Images", "files": [{"name": "photo.png", "size": 500}]},
    ]
    # Grouping / Counting
    # Nested iteration

    result2 = {f["folders"]: sum(file["size"] for file in f["files"]) for f in folders}
    return result2

    # # Aggregating necessary data in a separate dict
    # result = {folder["folder"]: folder["files"] for folder in folders}

    # # Performing required counting
    # for files in result:
    #     count = 0
    #     for item in result[files]:
    #         count += item["size"]
    #     result[files] = count
    # return result


# Given a list of test run results.
# Find which tester has the highest failure rate (percentage of failed vs total tests).


def find_failed_rate():
    testers = [
        {"tester": "Ann", "status": "passed"},
        {"tester": "Bob", "status": "failed"},
        {"tester": "Ann", "status": "failed"},
    ]
    result = {}

    for item in testers:
        tester_name = item["tester"]
        result.setdefault(tester_name, dict.fromkeys(["failed", "total"], 0))
        result[tester_name]["total"] += 1
        if item["status"] == "failed":
            result[tester_name]["failed"] += 1

    failure_rate = {
        tester: rates["failed"] / rates["total"] for tester, rates in result.items()
    }

    # selecting a DICT max based on values.
    return sorted(failure_rate, key=failure_rate.get)


# Write code that returns the differences between them in the form:
# [{"id": 2, "field": "name", "expected": "Dev", "actual": "Developer"}]
def return_diff():
    expected = [{"id": 1, "name": "QA"}, {"id": 2, "name": "Dev"}]
    actual = [{"id": 1, "name": "QA"}, {"id": 2, "name": "Developer"}]

    result_lst = []

    mapping_expected = {item["id"]: {"name": item["name"]} for item in expected}
    mapping_actual = {item["id"]: {"name": item["name"]} for item in actual}

    for key in mapping_expected:
        temp = {}
        if mapping_expected[key] != mapping_actual[key]:
            for item in mapping_expected[key]:
                temp["id"] = key
                temp["field"] = item
                temp["expected"] = mapping_expected[key][item]
                temp["actual"] = mapping_actual[key][item]
            result_lst.append(temp)

    return result_lst


# You receive JSON from /user/folders:
# Return a flat list of all folders belonging to all users:
# ["QA", "Docs", "Logs"]


def return_docs():
    docs = [
        {"user": "Alice", "folders": ["QA", "Docs"]},
        {"user": "Bob", "folders": ["Logs"]},
    ]

    lst = [f for el in docs for f in el["folders"]]
    # for el in docs:
    #   for f in el["folders"]:
    #       lst.append(f)

    return lst


# You have a list of API responses for the same request over time:
# Determine if the service is flaky — i.e., failed at least once but succeeded at least once.
# flaky = [200, 500]
# stable = []


def get_flaky_test():
    tests = [
        {"timestamp": "10:00", "status_code": 200},
        {"timestamp": "10:01", "status_code": 500},
        {"timestamp": "10:02", "status_code": 200},
    ]
    codes = Counter(test["status_code"] for test in tests)

    if codes[200] >= 1 and codes[500] >= 1:
        return "Flaky"


# Return the total number of files across all folders in all workspaces.


def total_files():
    files = [
        {"workspace": "A", "folders": [{"id": 1, "files": 3}, {"id": 2, "files": 5}]},
        {"workspace": "B", "folders": [{"id": 3, "files": 2}]},
    ]

    temp = {}
    for file in files:
        folders = file["folders"]
        for folder in folders:
            temp.setdefault(file["workspace"], []).append(folder["files"])
        temp[file["workspace"]] = sum(temp[file["workspace"]])

    return sum(temp.values())


# Return a dict mapping each endpoint to a list of unique status codes seen for it:
# {"/signin": [200], "/folders": [404, 200]}


def return_unique_codes():
    codes = [
        {"endpoint": "/signin", "status": 200},
        {"endpoint": "/folders", "status": 404},
        {"endpoint": "/folders", "status": 200},
    ]

    result = {}
    for code in codes:
        result.setdefault(code["endpoint"], []).append(code["status"])
    return result


# Given a list of user actions.
# Count how many times each user performed each action type.


def count_user_actions():
    user_data = [
        {"user": "Alice", "action": "create"},
        {"user": "Alice", "action": "delete"},
        {"user": "Bob", "action": "create"},
    ]

    result = {}

    for data in user_data:
        result.setdefault(data["user"], []).append(data["action"])

    for el in result:
        result[el] = Counter(result[el])
    return result


# Get a list of all folder IDs that are not archived


def get_unarchived_folders():
    data = [
        {
            "user": "Ann",
            "folders": [{"id": 1, "archived": True}, {"id": 2, "archived": False}],
        },
        {"user": "Bob", "folders": [{"id": 3, "archived": False}]},
    ]

    lst = [
        folder["id"]
        for item in data
        for folder in item["folders"]
        if folder["archived"] == False
    ]
    return lst


# You run a test suite and get results grouped by component.
# Return a dict like this
# {"auth": {"passed": 1, "failed": 1}, "ui": {"passed": 1, "failed": 0}}


def return_test_results():
    tests = {
        "auth": [
            {"name": "test_login", "result": "passed"},
            {"name": "test_logout", "result": "failed"},
        ],
        "ui": [{"name": "test_button", "result": "passed"}],
    }

    d = {}

    for key in tests:
        for el in tests[key]:
            d.setdefault(key, []).append(el["result"])
        d[key] = dict(Counter(d[key]))
        
    return d

print(return_test_results())