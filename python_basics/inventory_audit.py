
# flake8: Noqa

# Task: audit_inventory(inventory_list)
# The function must determine if an item is "High Compliance" or "Low Compliance" based on the following three checks:
# The item must have a positive stock level (stock>0) AND the count of successful shipments (True values in 'ship_history') must be greater than or equal to 3.
# The item's 'tags' must contain at least one required safety tag from a predefined set: required_tags = {"Fragile", "HandleWithCare", "Hazardous"}.
# The item's 'name' must not contain the substring 'OLD' and must have a length of at least 5 characters.

# Compliance Definition:
# An item is "High Compliance" if ALL THREE checks pass (Stock Check, Tag Check, AND Name Check).
# Otherwise, the item is "Low Compliance".
# Output:
# The function should return a new list of dictionaries. Each dictionary in the new list should contain:

# The item's 'id'
# The item's 'name'
# A new key 'compliance_status' with the string value "High Compliance" or "Low Compliance".


inventory = [
    {
        "id": 101,
        "name": "Widget Pro 2024",
        "stock": 12,
        "tags": {"Electronics", "New", "Fragile"},
        "ship_history": [True, True, True, False],
    },
    {
        "id": 102,
        "name": "OLD Capacitor",
        "stock": 5,
        "tags": {"Component"},
        "ship_history": [True, True],
    },
    {
        "id": 103,
        "name": "Small Box",
        "stock": 0,
        "tags": {"Paper", "HandleWithCare"},
        "ship_history": [True, False, True, True, True],
    },
    {
        "id": 104,
        "name": "Heavy Machinery 500",
        "stock": 20,
        "tags": {"Industrial", "Hazardous"},
        "ship_history": [True, True, True, True],
    },
]

required_tags = {"Fragile", "HandleWithCare", "Hazardous"}


def audit(inventory_list: list):
    temp = []
    for item in inventory_list:
        temp_dict = {}
        temp_dict["id"] = item["id"]
        temp_dict["name"] = item["name"]

        name_check = True if "OLD" not in item["name"] and len(item["name"]) >= 5 else False
        tag_check = True if required_tags & item["tags"] else False
        stock_check = (
            True if sum(item["ship_history"]) >= 3 and item["stock"] > 0 else False
        )

        if all([name_check, tag_check, stock_check]):
            temp_dict["compliance_status"] = "High Compliance"
        else:
            temp_dict["compliance_status"] = "Low Compliance"
        temp.append(temp_dict)
    return temp


print(audit(inventory))
