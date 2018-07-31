#!/usr/bin/python3
from datetime import datetime
from fabric.api import local, env, run, put

env.hosts = ["35.231.1.19", "35.229.28.8"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"


def do_pack():
    """ packs the web static into a tgz file
    """
    try:
        name = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        local("tar -cvzf versions/{}.tgz {}".format(
            name, "web_static/"))
        return "versions/{}.tgz".format(name)
    except:
        return None


def do_deploy(archive_path):
    """deploy the archive to your server
    """
    fd = archive_path.split("/")[1]
    try:
        put(archive_path, "/tmp/{}".format(fd))
        run("mkdir -p /data/web_static/releases/{}".format(fd))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(fd, fd))
        run("rm /tmp/{}".format(fd))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(fd, fd))
        run("rm -rf /data/web_static/releases/{}/web_static".format(fd))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/\
        /data/web_static/current".format(fd))
        print("Version successfully deployed!")
        return True
    except:
        print("Deployment failed.")
        return False


def deploy():
    # automates everything
    pack = do_pack()
    if pack is None:
        return False
    return do_deploy(pack)
