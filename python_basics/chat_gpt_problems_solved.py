# flake8: noqa
# You have multiple test suites, each containing test cases with tester and result.
# Return a dict showing how many tests each tester failed in total across all suites.
# exp_result = {"John": 2, "Anna": 1}

from collections import Counter, defaultdict
import email

import test


suites = [
    {
        "suite_name": "Auth",
        "tests": [
            {"name": "test_login", "tester": "John", "result": "failed"},
            {"name": "test_signup", "tester": "Anna", "result": "passed"},
        ],
    },
    {
        "suite_name": "Profile",
        "tests": [
            {"name": "test_update", "tester": "John", "result": "failed"},
            {"name": "test_delete", "tester": "Anna", "result": "failed"},
        ],
    },
]


def count_failed_test(suites: list):

    result_dict = defaultdict(int)

    for suite in suites:
        tests = suite["tests"]
        for test in tests:
            if test["result"] == "failed":
                result_dict[test["tester"]] += 1
    return dict(result_dict)


# Given nested test results grouped by suite, return how many tests each tester failed per suite.
# exp = {
#     "auth_suite": {"John": 1, "Anna": 1},
#     "profile_suite": {"Anna": 2}
# }

data = {
    "auth_suite": [
        {"tester": "John", "result": "passed"},
        {"tester": "Anna", "result": "failed"},
        {"tester": "John", "result": "failed"},
    ],
    "profile_suite": [
        {"tester": "Anna", "result": "failed"},
        {"tester": "John", "result": "passed"},
        {"tester": "Anna", "result": "failed"},
    ],
}


def count(data: dict):

    result_dict = {}

    for suite, tests in data.items():
        result_dict[suite] = dict(
            Counter(test["tester"] for test in tests if test["result"] == "failed")
        )

    return result_dict


# You receive a list of API responses, each representing a user profile.
# Find all fields that are missing or have inconsistent types across profiles.
# exp = {
#     "email": ["missing_value"],
#     "age": ["type_mismatch"]
# }

profiles = [
    {"id": 1, "email": "a@test.com", "age": 25},
    {"id": 2, "email": "b@test.com", "age": "unknown"},
    {"id": 3, "email": None},
]


def check_responses(profiles: list):

    # union() running on dictionaries loops over keys as expected NOT values.
    all_keys = set().union(*profiles)
    final_dict = {}

    for key in all_keys:
        values = [p.get(key) for p in profiles]
        types = {type(val) for val in values}
        is_missing = True if None in values and len(types) <= 2 else False

        if is_missing:
            final_dict.setdefault(key, []).append("missing_value")
        elif len(types) > 1:
            final_dict.setdefault(key, []).append("type_mismatch")
    return final_dict


# You receive logs from multiple services. Each log contains an "errors" key — a list of messages.
# Return a sorted list of unique error messages across all services.
# exp = ["Invalid token", "Missing header", "Timeout"]

logs = [
    {"service": "auth", "errors": ["Invalid token", "Missing header"]},
    {"service": "profile", "errors": ["Missing header", "Timeout"]},
    {"service": "workspace", "errors": []},
]


def refine_logs(logs: list):
    result = set()

    for log in logs:
        result |= set(log.get("errors"))

    return list(result)

    # result = {}
    # for log in logs:
    #     result[log["service"]] = log["errors"]
    # return result


# Given nested test metadata, flatten it into a single-level dictionary where keys represent the path.

# exp = {
#     "suite.name": "Login Flow",
#     "suite.config.browser": "chrome",
#     "suite.config.retries": 2,
#     "test.id": 101,
#     "test.status": "passed"
# }

test_info = {
    "suite": {
        "name": "Login Flow",
        "config": {"browser": "chrome", "retries": 2},
    },
    "test": {"id": 101, "status": "passed"},
}


def flatten(test_info):
    result = {}
    stack = [(test_info, "")]

    while stack:
        current_point, prefix = stack.pop()

        if isinstance(current_point, dict):
            for key, value in current_point.items():
                new_prefix = f"{prefix}.{key}" if prefix else key
                stack.append((value, new_prefix))
        else:
            result[prefix] = current_point

    return result


# print(flatten(test_info))


# From a list of user responses, extract IDs of users who have verified email and an active subscription plan.
# Handle missing keys gracefully (ignore invalid entries).
responses = [
    {"user": {"id": 1, "email_verified": True, "plan": {"status": "active"}}},
    {"user": {"id": 2, "email_verified": False, "plan": {"status": "inactive"}}},
    {"user": {"id": 3, "plan": {"status": "active"}}},
    {"user": {"id": 4, "email_verified": True, "plan": {"status": "inactive"}}},
]

def handle_response(responses: list):

    result = []
    
    for response in responses:
        for elem in response:
            try:
                if response[elem].get("email_verified") is None or response[elem].get("plan") is None:
                    raise KeyError
                if response[elem].get("email_verified") is True and "active" in response[elem].get("plan").values():
                    result.append(response[elem]["id"])
            except KeyError:
                print(f"Missing key for user {response[elem]["id"]}")
        
    return result


# You have raw API performance data per test run.
# Compute the average response time per endpoint across all test runs.
# exp = {"signin": 200.0, "get_user": 120.0}

data = [
    {"run_id": 1, "responses": {"signin": 200, "get_user": 120}},
    {"run_id": 2, "responses": {"signin": 180, "get_user": 110}},
    {"run_id": 3, "responses": {"signin": 220, "get_user": 130}},
]

def compute_time(data):
    result = {}
    for item in data:
        responses = item["responses"]
        for endpoint in responses:
            result.setdefault(endpoint, []).append(responses[endpoint])

    for el in result:
        result[el] = sum(result[el]) / len(result[el])
    return result 

# You run a test suite and get results grouped by component
# Create a summary dict like:
# {"auth": {"passed": 1, "failed": 1}, "ui": {"passed": 1, "failed": 0}}

def refine_report():
    test_report = {
    "auth": [{"name": "test_login", "result": "passed"}, {"name": "test_logout", "result": "failed"}],
    "ui": [{"name": "test_button", "result": "passed"}]
}
    temp = {}
    # for test in test_report:
    #     tests = test_report[test]
    #     for item in tests:
    #         temp.setdefault(test, []).append(item["result"])
    
    #     temp[test] = dict(Counter(temp[test]))
    
    # for k, v in temp.items():
    #     print(temp.items())
    #     if "failed" not in v:
    #         temp[k].update({"failed": 0})

    for test in test_report:
        temp[test] = dict.fromkeys(["passed", "failed"], 0)
        tests = test_report[test]
        for item in tests:
            if item["result"] == "passed":
                temp[test]["passed"] += 1
            elif item["result"] == "failed":
                temp[test]["failed"] += 1    

    return temp

print(refine_report())
