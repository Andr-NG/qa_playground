# flake8: noqa


# You receive raw server logs and need to aggregate the total time taken for each unique service
# endpoint and flag any endpoint whose total time exceeds a warning threshold.

# Values are dictionaries containing:
# 'total_time_ms': The sum of all time_ms for that endpoint.
# 'count': The total number of requests for that endpoint.
# 'is_anomaly': A boolean, True if 'total_time_ms' is strictly greater than the threshold_ms, otherwise False.

# The function must return a dictionary where:
# Keys are the unique endpoint strings.


from collections import defaultdict


exp = {
    "/api/users": {"total_time_ms": 700, "count": 3, "is_anomaly": False},
    "/api/data": {"total_time_ms": 1020, "count": 2, "is_anomaly": True},
    "/api/status": {"total_time_ms": 50, "count": 1, "is_anomaly": False},
}


log_data = [
    {"timestamp": "10:00:01", "endpoint": "/api/users", "time_ms": 150},
    {"timestamp": "10:00:05", "endpoint": "/api/data", "time_ms": 900},
    {"timestamp": "10:00:10", "endpoint": "/api/users", "time_ms": 250},
    {"timestamp": "10:00:15", "endpoint": "/api/data", "time_ms": 120},
    {"timestamp": "10:00:20", "endpoint": "/api/status", "time_ms": 50},
    {"timestamp": "10:00:25", "endpoint": "/api/users", "time_ms": 300},
]
WARNING_THRESHOLD = 700

# Create a resulting dict
# Loop through the log_data


def process_logs(log_data, warning):
    # result_dict = {}

    # for item in log_data:
    #     if item["endpoint"] not in result_dict:
    #         result_dict[item["endpoint"]] = {}
    #         total_time = sum(
    #             map(
    #                 lambda el: (
    #                     el.get("time_ms")
    #                     if el.get("endpoint") == item["endpoint"]
    #                     else 0
    #                 ),
    #                 log_data,
    #             )
    #         )
    #         count = list(map(lambda el: el.get("endpoint"), log_data))
    #         result_dict[item["endpoint"]]["count"] = count.count(item["endpoint"])
    #         result_dict[item["endpoint"]]["total_time_ms"] = total_time
    #         result_dict[item["endpoint"]]["is_anomaly"] = (
    #             True if total_time > warning else False
    #         )

    # return result_dict

    # defaultdict(lambda: [0, 0]) means [0, 0] will be the value to every key created.
    # aggregated_data["a"] = [0, 0], aggregated_data[1] = [0, 0], aggregated_data["cas"] = [0, 0] 
    aggregated_data = defaultdict(lambda: [0, 0])

    for item in log_data:
        endpoint = item["endpoint"]
        time = item["time_ms"]

        # Aggregating endpoint count
        aggregated_data[endpoint][0] += 1

        # Aggregating endpoint time
        aggregated_data[endpoint][1] += time

        # aggregated_data = {"/api/users": [3, 700]}

    final_data = {}

    for ind, val in aggregated_data.items():
        count, total_time = val
        final_data[ind] = {
            "count": count,
            "total_time_ms": total_time,
            "is_anomaly": total_time > warning,
        }

    return final_data


print(process_logs(log_data, WARNING_THRESHOLD))
print(process_logs(log_data, WARNING_THRESHOLD) == exp)
