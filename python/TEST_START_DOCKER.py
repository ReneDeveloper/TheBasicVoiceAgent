"""TEST_START_DOCKER.py"""
#WIN:20230127:1512:CREAR UN CONTAINER DE GLPI DESDE UN COMANDO PYTHON
#WIN:20230127:1512:CREAR UN CONTAINER DE MYSQL DESDE UN COMANDO PYTHON
#WIN:20230127:1512:CREAR UN CONTAINER DE DOLIBARR DESDE UN COMANDO PYTHON
"""
from python_on_whales import docker
output = docker.run("hello-world")
print(output)
#Hello from Docker! This message shows that your installation appears to be 
#working correctly.
from python_on_whales import DockerClient
docker = DockerClient(compose_files=["./my-compose-file.yml"])
docker.compose.build()
docker.compose.up()
#...
docker.compose.down()
""" # DESCARTADO: no funciona python_on_whales en cualquier versión de python

import docker
import subprocess
import os
import time

path_yaml = "D:/RSILVA_REPOS/the_basic_voice_bot/templates/docker/"

def main():
    client, log_path = _set_up_environment()
    _run_docker_compose(f"{path_yaml}TEMPLATE_DOCKER_GLPI.yaml", log_path)


def _run_docker_compose(docker_compose_name, log_path):
    bash_command = f"docker-compose -f {docker_compose_name} up -d"
    _execute_shell_command(bash_command, log_path)


def _execute_shell_command(bash_command, log_path):
    with open(log_path, "w") as output:
        subprocess.run(
            bash_command,
            shell=True,  # pass single string to shell, let it handle.
            stdout=output,
            stderr=output
        )
    while not output.closed:
        time.sleep(0.1)
    print(f"{os.linesep} COMMAND {bash_command} LOG OUTPUT:")
    with open(log_path, "r") as output:
        for line in output:
            print(line)


def _create_docker_log_file():
    log_location, log_name = "logs", "output.log"
    log_path = os.path.join(os.getcwd(), log_location, log_name)
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    assert os.path.isdir(os.path.dirname(log_path))
    if not os.path.isfile(log_path):
    	fixed = open(log_path, "w") #fixing next line, because doesn't work 
        #os.mknod(log_path)

    return log_location, log_name, log_path


def _set_up_environment():
    log_location, log_name, log_path = _create_docker_log_file()
    client = docker.from_env()
    return client, log_path

if __name__ == "__main__":
    main()