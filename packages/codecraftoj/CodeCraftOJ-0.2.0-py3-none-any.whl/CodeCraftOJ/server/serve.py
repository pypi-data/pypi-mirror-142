from pathlib import Path

from flask import Flask, request
from threading import Thread
from CodeCraftOJ.server.responses import *
from CodeCraftOJ.server.utils import *
from typing import List

PATH: Path = Path(".")

app = Flask(__name__)

tasks: List[Task] = []


@app.route("/api/status")
def hello_world():
    return {
        "code": 0,
        "data": {
            "path": str(PATH.absolute())
        },
        "msg": "Success"
    }


@app.route("/api/run", methods=["POST"])
def run_experiment():
    try:
        data = request.get_json()
        newTask = Task()
        newTask.from_scratch(data["name"], data["inputs"], data["cmd"])
        newTask.set_route(PATH)
        tasks.append(newTask)
        newThread = Thread(target=newTask.run)
        newThread.start()
        return SUCCESS_NONE
    except Exception as e:
        return ERROR_UNKNOWN(e.__repr__())


@app.route("/api/tasks/list", methods=["GET"])
def task_list():
    return {
        "code": 0,
        "data": [t.basic_information_as_json() for t in tasks],
        "msg": "Success"
    }


@app.route("/api/tasks/search", methods=["GET"])
def search():
    try:
        r = []
        for t in tasks:
            for key, value in request.args:
                if str(getattr(t, key)) != value:
                    continue
                r.append(t)
        return {
            "code": 0,
            "data": [t.basic_information_as_json() for t in r],
            "msg": "Success",
        }
    except Exception as e:
        return ERROR_UNKNOWN(e.__repr__())


@app.route("/api/tasks/metric", methods=["GET"])
def get_task_attr():
    try:
        r = []
        filter_task = request.args.getlist("filter_task[]")
        metric = request.args.get("metric")
        # 目前看来，好像没有必要维护一个全局的名字-任务映射 故用一个循环解决
        for t in tasks:
            if t.name in filter_task:
                r.append(t)
        return {
            "code": 0,
            "data": [{t.name: getattr(t, metric)} for t in r],
            "msg": "Success",
        }
    except Exception as e:
        return ERROR_UNKNOWN(e.__repr__())


def _recover_task_list():
    # 每次只应当运行一次，没有查重机制
    global tasks
    for t in PATH.glob("*.data"):
        with t.open("rb") as f:
            d = pickle.load(f)
            new_task = Task()
            new_task.from_dict(d)
            tasks.append(new_task)
        print("Loaded", t.absolute())


def backend(record_path: Path):
    global PATH
    PATH = record_path
    _recover_task_list()
    app.run(port=21574)
