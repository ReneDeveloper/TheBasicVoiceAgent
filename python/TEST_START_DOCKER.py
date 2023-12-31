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

path_yaml_template = "D:/RSILVA_REPOS/the_basic_voice_bot/templates/docker/"
path_yaml_project_ = "C:/RSILVA_BASIC_BOTS/__BIN_CLONES__/DOCKER_TEST/"

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
        #RSILVA:20230127:fixing next line, because doesn't work 
        #os.mknod(log_path) #DOESN'T WORK
        fixed = open(log_path, "w") #WORKS
    return log_location, log_name, log_path

def _set_up_environment():
    log_location, log_name, log_path = _create_docker_log_file()
    client = docker.from_env()
    return client, log_path

def _replace_template(n_id_proyecto, n_puerto_http, n_puerto_bbdd):
    return _replace_template(str(n_id_proyecto),str(n_puerto_http),str(n_puerto_bbdd))

def _replace_template(project_id__, puerto_http, puerto_bbdd):
    """_replace_template"""
    log_location, log_name = "logs", "output.log"
    log_path = os.path.join(os.getcwd(), log_location, log_name)



    #project_id__ = "30"
    project_name = f"proyecto_{project_id__}"

    replacements = {'__PROJECT_NAME__':project_name, '__HTTP_PORT__':puerto_http, '__MYSQL_PORT__':puerto_bbdd}
    replacements_2 = {'zero':'0', 'temp':'bob', 'garbage':'nothing'}

    
    
    source_ = f'{path_yaml_template}TEMPLATE_DOCKER_GLPI_PARAMETRICO.yaml'
    try:

        os.mkdir(f"{path_yaml_project_}{project_name}")
    except:
        print("ya existe el dir")
    target_ = f"{path_yaml_project_}{project_name}/{project_name}.yaml"

    infile  = open(source_)
    outfile = open(target_, 'w') 

    with infile, outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)

    source_mysql_ = f'{path_yaml_template}mysql.env'
    target_mysql_ = f"{path_yaml_project_}{project_name}/mysql.env"
    infile  = open(source_mysql_)
    outfile = open(target_mysql_, 'w') 
    with infile, outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)

    _run_docker_compose(f"{path_yaml_project_}{project_name}/{project_name}.yaml", log_path)

    return "OK"

def main():
    client, log_path = _set_up_environment()
    project_id__ = "30"
    project_name = f"proyecto_{project_id__}"

    _run_docker_compose(f"{path_yaml_project_}{project_name}/{project_name}.yaml", log_path)
    #  EXAMPLE             
    # _run_docker_compose("C:/RSILVA_BASIC_BOTS/proyecto_30/proyecto_30.yaml",log_path)

if __name__ == "__main__":
    #main()
    _replace_template("40","8240","8340")
    #_replace_template("36","8236","8336")
    #_replace_template("37","8237","8337")
    #_replace_template("38","8238","8338")
    #_replace_template("39","8239","8339")
    #client, log_path = _set_up_environment()
    #_run_docker_compose(f"{path_yaml_template}TEMPLATE_DOCKER_GLPI.yaml",log_path)

    #path_yaml_project_
