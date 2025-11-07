# flake8: noqa


# You receive a list of dictionaries representing API responses.
# Each must contain "id", "name", and "status".
# Your task: filter out invalid responses and return only valid ones.

from collections import Counter, defaultdict


data = [
    {"id": 1, "name": "Alice", "status": "active"},
    {"id": 2, "status": "inactive"},
    {"name": "Charlie", "status": "active"},
    {"id": 3, "name": "Eve", "status": "pending"},
]

exp = [
    {"id": 1, "name": "Alice", "status": "active"},
    {"id": 3, "name": "Eve", "status": "pending"},
]


def filter_response(data):

    lst = [
        item for item in data if all(["id" in item, "name" in item, "status" in item])
    ]
    return lst


# From a dictionary of test names and their results, return a count of how many failed tests each tester has.
test_runs = [
    {"tester": "John", "result": "passed"},
    {"tester": "Anna", "result": "failed"},
    {"tester": "John", "result": "failed"},
    {"tester": "Anna", "result": "failed"},
]

exp_1 = {"John": 1, "Anna": 2}


def get_test_results(test_runs: list):

    result = defaultdict(int)
    for test in test_runs:
        if test["result"] == "failed":
            result[test["tester"]] += 1

    # result = Counter(test["tester"] for test in test_runs if test["result"] == "failed")
    return result


# You receive raw API logs as strings.
# Each log line: "timestamp | user_id | status_code".
# Return a list of dicts with correctly typed data.
exp_3 = [
    {"timestamp": "2025-10-21 10:00:01", "user_id": 123, "status_code": 200},
    {"timestamp": "2025-10-21 10:02:33", "user_id": 124, "status_code": 500},
]
logs = [
    "2025-10-21 10:00:01 | 123 | 200",
    "2025-10-21 10:02:33 | 124 | 500",
]

def refine_logs(logs: list):
    result = []

    for log in logs:
        timestamp, user_id, status_code = log.split(" | ")
        result.append({"timestamp": timestamp, "user_id": int(user_id), "status_code": int(status_code)})
    return result
    
print(refine_logs(logs) == exp_3)
