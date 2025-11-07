# Function Signature: generate_unique_ids(candidate_names: list[str], existing_ids: set[str]) -> dict[str, str]

# ID Generation Rule: The base ID is the first 4 letters of the candidate's name (lowercase). If the name is shorter, use the whole name.

# Collision Rule: If the generated base ID already exists in the existing_ids set or has already been generated in the current batch, append a two-digit counter (starting at 01) to the base ID.

# Example: If 'jdoe' is taken, the next one is 'jdoe01', then 'jdoe02', etc.

# ER
# {
#     'John': 'john',
#     'JaneDoe': 'jane',
#     'JANE': 'jane01',
#     'JOHNNY': 'john01',
#     'Al': 'al'
# }

# flake8: noqa
candidate_names = ["John", "JaneDoe", "JANE", "JOHNNY", "Al", "JANEMORE", "JANEMMM", "Johnah"]
existing_ids = {"johnd", "janed", "al01"}


def generate_unique_ids(
    candidate_names: list[str], existing_ids: set[str]
) -> dict[str, str]:
    data = {}
    collision_count = {}

    for name in candidate_names: 
        base_id = name.lower() if len(name) <= 4 else name.lower()[:4]

        # Collision not detected, adding the key-value pair to the resulting dict
        # adding base_id to the existing ids and assign collision count for that base_id to 1
        if not base_id in existing_ids:
            data[name] = base_id
            existing_ids.add(base_id)
            collision_count[base_id] = 1
        else:

            # Collision detected, creating a suffix to have a leading 0
            # creating the final_id and incrementing the collision count by 1
            suffix = str(collision_count[base_id]).zfill(2)
            final_id =  base_id + suffix
            collision_count[base_id] += 1
            data[name] = final_id
            existing_ids.add(final_id)
    return data


print(generate_unique_ids(candidate_names, existing_ids))
