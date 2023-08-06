import os, sys
import click
import time
import pkg_resources

from cookiecutter.main import cookiecutter
from functools import reduce
from subprocess import Popen, PIPE

import yaml
from phobos import __version__ as version

from phobos.cli.utils import datalab, get_all_tasks_eu, get_task_details_eu, export_annotations_eu, DataLab
from phobos.grain import expand

def checkValidRoot():
    root_path = os.curdir
    required_files = ['train.py', 'metadata.yaml']
    return reduce(
        lambda x, y: x and y,
        [os.path.exists(
            os.path.join(root_path, fl)
            ) for fl in required_files])

def exec(command, forward=False, pipe=True, in_=""):
    '''
    Popen support with input,out and error support 
    
    Params:
    ---
    command: string     Command to execute.
    forward: bool       Doen't wait for command to complete.
    pipe: bool          If True runs command in backend, else truns command interactively.     
    in_: string         Stdin for PIPEd process call.
    '''
    if pipe:
        stdout, stdin, stderr = PIPE, PIPE, PIPE
    else:
        stdout = sys.stdout
        stdin = sys.stdin
        stderr = sys.stderr
    while True:
        p = Popen(command, shell=True, stdout=stdout, stderr=stderr, stdin=stdin)
        out, err = "", ""
        if not pipe:
            p.wait()
            return out, err
        if len(in_) > 0:
            out, err = p.communicate(input=in_.encode('utf-8'))
            out, err = out.decode('utf-8'), err.decode('utf-8')
            if "pip install" in out.lower():
                continue
            return out, err
        if not forward and len(in_) == 0:
            p.wait()
            out, err = p.stdout.read().decode('utf-8'), p.stderr.read().decode('utf-8')
            return out, err
        else:
            time.sleep(1)
            return "", ""

def getExpConfigs(meta):
    project, deployment = meta['project'], meta['deployment']

    expmap = getExperimentsMap(project)
    polymap = getPolyAxonFileMap(deployment)
    url = deployment['url']

    return expmap, polymap, url

def getPolyAxonFileMap(meta):
    pmeta = meta['run']

    distributed = meta['distributed']

    polymap = {}

    polymap['version'] = 1.1
    polymap['kind'] = 'component'
    polymap['name'] = meta['name']

    run = {}
    container = {}
    container['name'] = meta['name']
    container['image'] = pmeta['container']['image']
    container['command'] = ['/bin/bash', 'run.sh']
    
    container['resources'] = {}
    
    container['resources']['limits'] = {}
    container['resources']['requests'] = {}

    container['resources']['limits']['nvidia.com/gpu'] = pmeta['container']['resources']['limits']
    container['resources']['requests']['nvidia.com/gpu'] = pmeta['container']['resources']['requests']

    container['workingDir'] = '{{ globals.run_artifacts_path }}/code'

    environment = {}
    environment['nodeSelector'] = {}
    environment['nodeSelector']['arche'] = pmeta['nodepool']

    if not distributed:
        run['kind'] = 'job' if not pmeta['kind'] else pmeta['kind']
        run['connections'] = pmeta['connections']
        run['container'] = container
        run['environment'] = environment
    else:
        run['cleanPodPolicy'] = 'All'
        run['kind'] = 'pytorchjob' if not pmeta['kind'] else pmeta['kind']

        master, worker = {}, {}
        master['connections'] = pmeta['connections']
        worker['connections'] = pmeta['connections']
        master['container'] = container
        worker['container'] = container

        master['environment'] = environment
        worker['environment'] = environment

        master['replicas'] = pmeta['replicas']['master']
        worker['replicas'] = pmeta['replicas']['worker']

        run['master'] = master
        run['worker'] = worker

    polymap['run'] = run

    return polymap

def getExperimentsMap(meta):
    expmap = {}

    expmap['name'] = meta['name']
    expmap['description'] = meta['description']
    if len(meta['tags']) > 0:
        expmap['tags'] = meta['tags']
        
    return expmap
    
@click.group()
@click.version_option(version, message='%(version)s')
def cli():
    pass

@click.command()
@click.option('--project_name', required=True, help='Project directory name, Project Id for Arche')
@click.option(
    '--description',
    required=False,
    default="",
    help='Short description about the project')
@click.option(
    '--tags',
    required=False,
    type=str,
    default="",
    help='tags related to the project')
def init(project_name,
        description,
        tags):
    '''
    phobos init

    Initializes template repository with provided project attributes

    Params:
    --- project specific ---
    project_name:           Project directory name, Arche project ID.
    description:            (Optional) Description string.
    tags:                   (Optional) Project tags eg, phobos-stabalize.
    '''
    if not os.path.exists(project_name):
        click.echo("Creating template project directory!")
        cookiecutter(
            pkg_resources.resource_filename("phobos", "cli/cookiecutter-phobos-project"), 
            extra_context={
                'project_name': project_name,
            },
            no_input=True)
        with open(os.path.join(os.path.curdir, project_name, 'metadata.yaml'), 'r') as fp:
            config = yaml.safe_load(fp)
        
        config['project']['name'] = project_name
        config['project']['description'] = description
        config['project']['tags'] = tags.split(',')

        with open(os.path.join(os.path.curdir, project_name, 'metadata.yaml'), 'w') as fp:
            yaml.dump(config, fp, sort_keys=False)
        
        exec(f"cd {project_name}")
    else:
        click.echo(f"{project_name} already exist locally.")

@click.command()
@click.option('--dry_run', is_flag=True, help="Use dryrun i.e. local run on non-distributed mode")
def run(dry_run):
    '''
    phobos run

    Runs an Arche experiment, If any of the mentioned args is not provided then default ars are used.

    Params:
    ------
    dry_run:         (Optional) Use dryrun i.e. local run on non-distributed mode.
    '''
    config_file = 'polyaxonfile.yaml'

    with open('metadata.yaml', 'r') as fp:
        meta = dict(yaml.safe_load(fp.read()))
        meta = expand(meta, meta)
    expmap, polymap, url = getExpConfigs(meta)
    
    yaml.Dumper.ignore_aliases = lambda *args : True
    with open('polyaxonfile.yaml', 'w') as fp:
        yaml.dump(polymap, fp, sort_keys=False)
    
    if not checkValidRoot():
        click.echo("To run this command. Make sure you are inside project directory.")
        return
    if dry_run:
        exec("POLYAXON_NO_OP=true python3 train.py", pipe=False)
        return

    click.echo("Run the project. Make sure you are inside project directory.")
    print(f'Running: {config_file}')

    datalabClient = DataLab(url)
    datalabClient.createRun(
        project=expmap,
        polyaxon_file=config_file
    )

@click.command()
@click.option(
    '--uuid',
    required=True,
    help='"uuid" for single uuid or "uuid-1,..,uuid-n" for multiple uuids')
def tensorboard(uuid):
    '''
    phobos tensorboard

    Runs tensorboard for a given uuid/project

    Params:
    ------
    uuid:           Experiment uuid/uuid1,..,uuidn
    '''
    if not checkValidRoot():
        click.echo("To run this command the project. Make sure you are inside project directory.")
        return
    
    with open('metadata.yaml', 'r') as fp:
        meta = dict(yaml.safe_load(fp.read()))
        meta = expand(meta, meta)

    expmap, polymap, url = getExpConfigs(meta)

    uuids = uuid.split(',')
    
    datalabClient = DataLab()

    datalabClient.run_tensorboard(project=expmap, uuid=uuids)
            
@click.command()
@click.option('--all', is_flag=True, help='To retrieve all tasks')
@click.option('--details', is_flag=True, help='To retrieve details of a particular task')
@click.option('--url', required=False, default="api.granular.ai", help='base URL for Europa APIs')
@click.option('--email', required=True, default="", help="email id for Europa access")
@click.option('--passwd', required=True, default="", help="password for Europa access")
@click.option('--task', required=False, default="", help="task id")
def get(all, details, url, email, passwd, task):
    '''
    phobos get

    Accesses Europa APIs to list tasks, task details and retrieve annotations

    Params:
    -------
    all     :   to retrieve all tasks (optional)
    details :   to retrieve details of a particular task (optional)
    url     :   base URL for Europa APIs   
    email   :   email id for Europa access
    passwd  :   password for Europa access
    task    :   task id (optional)
    '''
    if email == "" or passwd == "":
        print('please provide credentials through options \'email\' and \'passwd\'')
        return
    if all:
        get_all_tasks_eu(url=url, email=email, passwd=passwd)
        return
    if task == "":
        print('please provide task id')
        return
    else:
        if details:
            get_task_details_eu(id=task, url=url, email=email, passwd=passwd)
            return
        else:
            export_annotations_eu(id=task, url=url, email=email, passwd=passwd)
            

cli.add_command(init)
cli.add_command(run)
cli.add_command(get)
cli.add_command(tensorboard)


if __name__ == "__main__":
    cli()
