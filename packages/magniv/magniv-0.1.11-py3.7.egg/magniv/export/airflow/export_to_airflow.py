import os
import shutil
import fileinput
import docker
from io import BytesIO



def export_to_airflow(task_list):
    dag_template_filename = "dag-template.py"
    dag_template_directory = "{}/{}".format(
        os.path.dirname(__file__), dag_template_filename
    )
    for task_info in task_list:
        print("starting task .... ")
        new_filename = "dags/{}/{}.py".format(task_info["owner"], task_info["key"])
        print(new_filename)
        if not os.path.exists("dags/"):
            os.mkdir("dags")
        if not os.path.exists("dags/{}/".format(task_info["owner"])):
            os.mkdir("dags/{}/".format(task_info["owner"]))
        shutil.copyfile(dag_template_directory, new_filename)
        dockername = _create_docker_image(task_info["python_version"], task_info["requirements_location"], task_info["key"])
        with fileinput.input(new_filename, inplace=True) as f:
            for line in f:
                line = (
                    line.replace("dag_id", "'{}'".format(task_info["key"]))
                    .replace("ownertoreplace", "'{}'".format(task_info["owner"]))
                    .replace("scheduletoreplace", "'{}'".format(task_info["schedule"]))
                    .replace(
                        "imagetoreplace",
                        "'{}'".format(dockername)
                    )
                    .replace(
                        "filetoreplace", task_info["location"].split("/")[-1]
                    )
                    .replace(
                        "functiontoreplace", task_info["name"]
                    )
                )
                print(line, end="")


def _create_docker_image(python_version, requirments, key):
    client = docker.from_env()
    dockerfile = """
                # syntax=docker/dockerfile:1

                FROM python:{}
                COPY requirements.txt requirements.txt
                RUN pip3 install -r requirements.txt

                COPY . .

                """.format(
                    python_version
             )
    path = "/".join(requirments.split("/")[:-1])
    with open("{}/Dockerfile".format(path), 'w') as fo:
        fo.write(dockerfile) 
    dockername = "{}dockerimage".format(key)
    client.images.build(path=path, tag=dockername)
    return dockername
