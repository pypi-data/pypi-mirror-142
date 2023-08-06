def V1(t):
    return {
        "version": "v1",
        "path": t.path,
        "name": t.name,
        "inputs": t.inputs,
        "cmd": t.cmd,
        "beginTime": t.beginTime,
        "endTime": t.endTime,
        "result": t.result,
        "errors": t.errors,
        "return_code": t.return_code,
        "score": t.score,
        "status": t.status,
    }
