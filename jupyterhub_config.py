import os

## Generic
c.JupyterHub.admin_access = True
#c.Spawner.default_url = '/lab'

## Authenticator
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.DummyAuthenticator.password = 'xmu2019'

c.Authenticator.whitelist = {
        'a01',
        'a02',
        'a03',
        'a04',
        'a05',
        'a06',
        'a07',
        'a08',
        'a09',
        'a10',
        'a11',
        'a12',
        'a13',
        'a14',
        'a15',
        }

c.Authenticator.admin_users = { 'aihub', 'windwood' }


## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

c.DockerSpawner.extra_create_kwargs = { 'runtime': 'nvidia' }
c.DockerSpawner.extra_host_config = { 'runtime': 'nvidia' }

os.environ['NVIDIA_VISIBLE_DEVICES'] = '0'
os.environ['CUDA_VISIBLE_DEVICES'] = '1'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
#c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
#c.DockerSpawner.image = 'jupyter/tensorflow-notebook'
c.DockerSpawner.image = 'tensorflow-notebook:2.0.0-gpu'


# tell the user containers to connect to our docker network
# if the hub using docker container
#c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
#c.DockerSpawner.network_name = 'aihub_default'

# delete containers when the stop
c.DockerSpawner.remove = True

# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py

# we need the hub to listen on all ips when it is in a container
#c.JupyterHub.hub_ip = os.environ['HUB_IP']
c.JupyterHub.hub_ip = '0.0.0.0'


# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
# where the hub is
#c.JupyterHub.hub_connect_ip = 'aihub_default'
c.JupyterHub.hub_connect_ip = '172.17.0.1'


## Services
#c.JupyterHub.services = [
#    {
#        'name': 'cull_idle',
#        'admin': True,
#        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
#    },
#]

## Read-only volumes
c.DockerSpawner.read_only_volumes = { 
        '/opt/srv/gtraining': '/home/jovyan/gtraining',
        '/opt/srv/dot-keras': '/home/jovyan/.keras',
        }

## User data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

## Other stuff
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '10G'

