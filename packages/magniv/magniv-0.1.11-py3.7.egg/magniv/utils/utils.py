import json


def _save_to_json(obj, filepath):
    with open(filepath, "w") as fo:
        json.dump(obj, fo)


def _get_tasks_json(filepath):
    with open(filepath, "r") as fo:
        task_list = json.load(fo)
    return task_list


def _get_function_from_json(key, filepath):
    f = open(filepath)
    task_info_list = json.load(f)
    for task in task_info_list:
        if task["key"] == key:
            break
    return task["location"], task["name"]
