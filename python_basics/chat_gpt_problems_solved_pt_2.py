# flake8: noqa
# You get test execution data for multiple builds.
# Return all tests that were flaky — i.e., the same test had both “passed” and “failed” across builds.
# ["login", "signup"]


import re


def get_flaky_tests():
    builds = [
        {
            "build": "B1",
            "tests": [
                {"name": "login", "status": "passed"},
                {"name": "signup", "status": "failed"},
                {"name": "password_recovery", "status": "passed"},
            ],
        },
        {
            "build": "B2",
            "tests": [
                {"name": "login", "status": "failed"},
                {"name": "signup", "status": "failed"},
                {"name": "password_recovery", "status": "passed"},
            ],
        },
        {
            "build": "B3",
            "tests": [
                {"name": "login", "status": "passed"},
                {"name": "signup", "status": "passed"},
                {"name": "password_recovery", "status": "passed"},
            ],
        },
    ]

    temp = {}

    for build in builds:
        tests = build["tests"]
        for test in tests:
            temp.setdefault(test["name"], set()).add(test["status"])

    return [item for item in temp if len(temp[item]) == 2]


# You have users with assigned workspaces and folder metadata.
# Produce a dict showing for each user:
# Total number of folders
# Number of archived folders
# Number of active folders

# {
#     "Ann": {"total": 2, "archived": 1, "active": 1},
#     "Bob": {"total": 1, "archived": 1, "active": 0},
#     "Eve": {"total": 0, "archived": 0, "active": 0}
# }


def get_user_data():
    data = [
        {
            "user": "Ann",
            "workspaces": [
                {
                    "id": 10,
                    "folders": [
                        {"id": 1, "archived": False},
                        {"id": 2, "archived": True},
                    ],
                }
            ],
        },
        {
            "user": "Bob",
            "workspaces": [{"id": 11, "folders": [{"id": 3, "archived": True}]}],
        },
        {"user": "Eve", "workspaces": []},
    ]
    temp = {}

    for elem in data:
        workspaces = elem["workspaces"]
        stats = {"total": 0, "archived": 0, "active": 0}
        for ws in workspaces:
            for folder in ws["folders"]:
                stats["total"] = len(folder)
                if folder["archived"]:
                    stats["archived"] += 1
                else:
                    stats["active"] += 1
        temp[elem["user"]] = stats

    return temp


# Given historical API performance data
# Return endpoints that consistently exceeded 300 ms in every run


def get_slow_endpoints():
    metrics = [
        {"endpoint": "/login", "runs": [120, 230, 110]},
        {"endpoint": "/folders", "runs": [400, 500, 300]},
        {"endpoint": "/logout", "runs": [100, 200, 150]},
    ]
    lst = []
    for metric in metrics:
        runs = metric["runs"]
        if any(run > 300 for run in runs):
            lst.append(metric["endpoint"])
    return lst


# Find all plan upgrades (free → pro) and all new users added.


def compare_snapshots():
    before = [
        {"id": 1, "email": "a@x.com", "plan": "free"},
        {"id": 2, "email": "b@x.com", "plan": "pro"},
    ]

    after = [
        {"id": 1, "email": "a@x.com", "plan": "pro"},
        {"id": 2, "email": "b@x.com", "plan": "pro"},
        {"id": 3, "email": "c@x.com", "plan": "free"},
    ]

    result = {}
    before_adjusted = {item["id"]: item["plan"] for item in before}

    for after_item in after:
        user_id = after_item["id"]
        before_plan = before_adjusted.get(user_id)
        email = after_item["email"]
        if before_plan:
            after_plan = after_item["plan"]
            if user_id in before_adjusted and before_plan != after_plan:
                update = {"id": user_id, "from": before_plan, "to": after_plan}
                result.setdefault("updated", []).append(update)
        else:
            result.setdefault("new_users", []).append({"id": user_id, "email": email})

    return result


def return_flakes():
    cases = [
        {
            "name": "delete_user",
            "results": {"dev": "passed", "staging": "passed", "prod": "passed"},
        },
        {
            "name": "update_user",
            "results": {"dev": "failed", "staging": "failed", "prod": "failed"},
        },
        {
            "name": "create_user",
            "results": {"dev": "passed", "staging": "failed", "prod": "passed"},
        },
    ]
    for case in cases:
        test_results = case["results"].values()
        if len(set(test_results)) > 1:
            return [case["name"]]

# Find all profiles that reference missing users.

def return_missing_profiles():
    users = [{"id": 1, "email": "a@x.com"}, {"id": 2, "email": "b@x.com"}]

    profiles = [{"user_id": 1, "bio": "QA Engineer"}, {"user_id": 3, "bio": "DevOps"}]

    users_new = {item["id"]: item["email"] for item in users}

    for profile in profiles:
        if profile["user_id"] not in users_new:
            return profile
print(return_missing_profiles())
