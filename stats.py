# extra func for DRY
def update_group_stats(group_stats: dict, entry: dict):
    # Set default values for group stats if they don't exist yet
    group_stats.setdefault("count", 0)
    group_stats.setdefault("amount", 0)
    group_stats.setdefault("num_items", 0)

    # Update group stats based on the entry
    group_stats["count"] += 1
    group_stats["amount"] += entry["amount"]
    group_stats["num_items"] += entry["num_items"]


def add_entry_to_stats(stats: dict, entry: dict) -> dict:
    # Here I check only empty entry and raise an error if it is empty, but why
    # I do it instead of checking required keys as in comment below. The
    # reason is provided tests - in first test, stats do not contain some
    # groups which are required in my opinion.

    # In my point "gender", "amount", "num_items", "currency",
    # "week_of_year", "country_code" are required in entry dict otherwise it
    # doesnt make sense adding gender but not adding the currency and
    # country_code to stats(as an example). So I have commented the code below
    # which is checking all required(in my opinion) keys in entry.
    # Also I have commented test case in tests.py which checks if entry dict
    # contains all of the required keys. Test name is "test_invalid_entry"

    # required_keys = ["gender", "amount", "num_items", "currency",
    #                  "week_of_year", "country_code"]
    # for key in required_keys:
    #     if key not in entry:
    #         raise ValueError(f"Entry dictionary missing required key: {key}")

    if not entry:
        raise ValueError("Entry dictionary cannot be empty.")

    # Update overall stats
    update_group_stats(stats, entry)

    # Update other groups stats
    for group, value in entry.items():
        if group in ["gender", "currency", "amount", "num_items"]:
            continue

        # Create nested dicts
        groups = group.split(".")
        group_stats = stats
        for g in groups:
            group_stats = group_stats.setdefault(g, {})

        # Set default values for the group stats
        group_stats = group_stats.setdefault(
            value, {"count": 0, "amount": 0, "num_items": 0}
        )
        # Update the group stats based on the entry
        update_group_stats(group_stats, entry)

    # Update gender stats
    gender = entry.get("gender")
    if gender is not None:
        # Commented part of code is necessary to uncomment in case if needed to
        # validate the gender
        # Also I have commented test case in tests.py which checks the gender
        # validation. Test name is "test_add_invalid_gender"

        # if gender not in ["F", "M"]:
        #     raise ValueError(
        #     "Invalid gender value. Only 'F' or 'M' allowed.
        #     ")

        gender_stats = stats.setdefault("gender", {}).setdefault(
            gender, {"count": 0, "amount": 0, "num_items": 0}
        )
        update_group_stats(gender_stats, entry)

    # Update currency stats
    currency = entry.get("currency")
    if currency is not None:
        currency_stats = stats.setdefault("currency", {}).setdefault(
            currency, {"count": 0, "amount": 0, "num_items": 0}
        )
        update_group_stats(currency_stats, entry)

    return stats


def merge_stats(*args: dict) -> dict:
    # Checking if all arguments are dictionaries
    for arg in args:
        if not isinstance(arg, dict):
            raise TypeError(
                f"All inputs to merge_stats must be dictionaries, "
                f"but {type(arg).__name__} was provided."
            )
    result = {}
    # Merge stats for all args
    for stat in args:
        # If the current stat is a dict, iterate over its key-value pairs
        # If it's a tuple or list, iterate over its elements
        for key, value in (stat.items() if isinstance(stat, dict) else stat):
            if key in result:
                if isinstance(value, dict):
                    # Recursively merge nested stats
                    result[key] = merge_stats(result[key], value)
                else:
                    # Add the values for non-dict stats
                    result[key] += value
            else:
                # Add the new key-value pair to the result
                result[key] = value
    return result
