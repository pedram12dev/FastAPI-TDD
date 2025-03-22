import docker
import time
import os
import docker.errors


def is_container_ready(container):
    container.reload()
    return container.status == "running"

def wait_for_stable_status(container,stable_duration=3,interval=1):
    start_time = time.time()
    stable_count = 0
    while time.time() - start_time < stable_duration:
        if is_container_ready(container):
            stable_count += 1 
        else:
            stable_count = 0 
        
        if stable_count >= stable_duration / interval:
            return True
        
        time.sleep(interval)
    return False


def start_database_container():
    client = docker.from_env()
    container_name = "test-db"
    scripts_dir = os.path.abspath("./scripts")


    try:
        existing_container =client.containers.get(container_name)
        print(f"container {container_name} exists. stoping and removing...")
        existing_container.stop()
        existing_container.remove()
        print(f"container {container_name} stopped and removed")

    except docker.errors.NotFound:
        print(f"container {container_name} does not exists")

    # container configuration 
    container_config = {    
        "name" : container_name,
        "image": "postgres:16.1-alpine3.19",
        "detach" : True,
        "ports":{"5432":"5433"},
        "environment": {
            "POSTGRES_USER": "postgres",
            "POSTGRES_PASSWORD": "postgres",
        },
        "volumes":[f"{scripts_dir}:/docker-entrypoint-initdb.d"],
        "network_mode": "fastapi-tdd_default",
    }

    # start container
    container = client.containers.run(**container_config)
    while not is_container_ready(container):
        time.sleep(1)

    if not wait_for_stable_status(container):
        raise RuntimeError("container did not stabilize whitin the specified time")
    return container