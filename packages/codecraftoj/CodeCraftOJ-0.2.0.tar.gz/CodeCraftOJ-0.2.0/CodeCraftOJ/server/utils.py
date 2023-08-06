import subprocess
import time
from pathlib import Path
import pickle

from CodeCraftOJ.server.interface import V1


class Task:
    version = "v1"
    path: Path = None
    process = None
    # 基本属性
    name = ""
    inputs: str = ""
    cmd = ""
    beginTime: float = 0
    endTime: float = 0
    result = []
    errors = []
    return_code = 0

    # Metric
    score = 0
    accuracy = None
    # 状态
    status = ""

    def __init__(self):
        pass

    def set_route(self, path):
        self.path = path / f"{self.name}.data"
        if self.path.exists():
            raise RuntimeError(f"{self.name} 已经存在")

    def from_scratch(self, name, inputs, cmd):
        self.name = name
        self.inputs = inputs
        self.cmd = cmd
        self.status = "Queue"

    def from_dict(self, data):
        for key in data:
            setattr(self, key, data[key])

    def run(self):
        self.status = "Running"
        self.beginTime = time.perf_counter()
        # TODO: Add timeout limitation
        self.process = subprocess.Popen(self.cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        text=True)
        self.result, self.errors = self.process.communicate(self._read_input())
        self.endTime = time.perf_counter()  # 计时器
        self.status = "Prepared"
        self.return_code = self.process.returncode
        if self.return_code != 0:
            self.status = "Failed"
        else:
            self._compute_metric()
            self.status = "Ready"
        self.save()

    def _compute_metric(self):
        self.accuracy = [1, 2, 3, 4, 5, 6, 7, 8]
        pass

    def save(self):
        # pickle不能直接保存thread.lock
        with self.path.open("wb") as f:
            pickle.dump(V1(self), f)
        print("Checkpoint Persisted!")

    def _read_input(self) -> str:
        #  TODO : Implement input method
        return self.inputs

    def basic_information_as_json(self) -> dict:
        return {
            "name": self.name,
            "beginTime": self.beginTime,
            "endTime": self.endTime,
            "returnCode": self.return_code,
            "score": self.score,
            "status": self.status,
        }
