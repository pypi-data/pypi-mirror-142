import os
import socket
import time
import psutil

from cloudmesh.common.Shell import Shell
from cloudmesh.common.console import Console
from cloudmesh.common.dotdict import dotdict
from cloudmesh.common.util import path_expand
from cloudmesh.common.util import readfile


class ServiceManager:

    # r = cloudmesh.common.SHell.run("uvicorn .... ")

    def __init__(self, name=None):
        """

        :param name:
        :type name:
        """
        self.name = name or "cloudmesh-catalog-service"
        self.path = path_expand("~/.cloudmesh/catalog")
        self.pid_file = f"{self.path}/{self.name}.pid"
        self.port = 8001
        self.reload = "--reload"

        Shell.mkdir(self.path)

    def is_port_in_use(self) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', self.port)) == 0

    def start(self):
        """

        :return:
        :rtype:
        """

        name = f"{self.path}/{self.name}"
        try:
            os.system(f"rm -f {name}.pid")
        except:
            pass
        command = f"nohup uvicorn cloudmesh.catalog.service:app --port={self.port} {self.reload} " \
                  f"> {name}.log 2>&1 & echo $! > {name}.pid"
        print(command)
        result = os.system(command)
        time.sleep(1)
        print(result)
        if result != 0:
            Console.error("The catalog server could not be started due to an error")
        try:
            content = readfile(f"{self.pid_file}")
            if "Address already in use" in content:
                Console.error("Address already in use")
            else:
                print(content)
        except:
            Console.error("pid file could not be found")

    def get_pid(self):
        """

        :return:
        :rtype:
        """
        try:
            pid = readfile(f"{self.pid_file}").strip()
            # if not psutil.pid_exists(pid):
            #    pid = None
        except:
            pid = None
        return pid

    def stop(self, pid=None):
        """

        :return:
        :rtype:
        """

        if pid is None:
            info = self.info()
            pid = info["pid"]

        for child in psutil.Process(pid).children():
            try:
                print(f"Deleting {child.pid} ", end="")
                p = psutil.Process(child.pid)
                p.kill()
                Console.green("deleted.")

            except psutil.Error:
                Console.red(". failed")

        print(f"Deleting {pid} ", end="")
        p = psutil.Process(pid)
        p.kill()
        Console.green("deleted.")
        os.remove(self.pid_file)

    def status(self):
        """

        :return:
        :rtype:
        """
        # for debug only
        probe = Shell.run(f"curl localhost:{self.port}")
        return '{"Cloudmesh Catalog":"running"}' in probe

    def pid_exists(self, pid):
        if pid is None:
            return False
        r = Shell.run(f"ps {pid}").strip().splitlines()
        return len(r) > 1


    def info(self):
        """

        :return:
        :rtype:
        """

        data = dotdict({
            "pid": None,
            "children": None,
            "status": False,
            "port": self.port
        })
        try:
            data.pid = int(self.get_pid())
            if self.pid_exists(data.pid):
                Console.ok(f"The process with pid {data.pid} exists")
            else:
                Console.error(f"The process with pid does not {data.pid} exists")
                try:
                    Console.warning(f"Removing PID file: {self.pid_file}")
                    os.remove(self.pid_file)
                except:
                    pass
        except:
            pass
        try:
            data.status = self.status()
        except:
            pass
        try:
            data.children = [child.pid for child in psutil.Process(data.pid).children()]
        except Exception as e:
            pass

        return data
