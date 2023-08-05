from os import getcwd
from os.path import realpath, dirname
from docker import from_env
from docker.errors import DockerException

def context():
    try: 
        return from_env()
    except DockerException:
        raise Exception(f'Docker Context Not Found! Check that Docker is running.')


def build(_ctx):
    return _ctx.images.build(
        tag='stout-runner',

        rm=True,
        forcerm=True,

        path=getcwd(),
        dockerfile=f'{dirname(realpath(__file__))}/dockerfile',
    )

def run(_ctx, _script):
    return _ctx.containers.run(
        image='stout-runner',
        environment=[f'SCRIPT={_script}'],
        name='stout-runner',
        remove=True,
    )