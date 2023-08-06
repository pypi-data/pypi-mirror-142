import asyncio
import os
import threading
import time
from functools import partial
from pprint import pprint as pp, pformat

import socketio

from maxoptics.config import Config
from maxoptics.error import TaskFailError
from maxoptics.utils.base import error_print
from maxoptics.visualizer import get_task_handler


def monitor_on(proj, task, func, token, mode):
    result = get_task_handler(task["task_type"])(task["id"], proj)
    thread0 = threading.Thread(
        target=peek_task_status, args=(proj, task, func, result), name="Task: " + str(task)
    )
    thread0.setDaemon(True)
    thread0.start()
    return result


def peek_task_status(project, task_info, callback_function, whale_client_res):
    task_id = task_info["id"]
    task_type = task_info["task_type"]

    project_id = project.id
    project_name = project.name

    localtime = lambda: time.asctime(time.localtime(time.time()))

    log_folder = project.log_folder
    destination = log_folder / f"{str(project_name)}_{str(task_id)}" / "log"
    os.makedirs(destination, exist_ok=True)
    with open(destination / "terminal.log", "w") as fs:
        fs.write("Waiting for response...")

    # Create socketIO client
    sio = socketio.AsyncClient()
    fs = open(destination / "terminal.log", "w")
    pprint = partial(pp, stream=fs)

    # On Connect
    @sio.event
    async def connect():
        whale_client_res.start_time = localtime()
        whale_client_res.start_time_raw = time.time()
        pprint("Connected")
        # Immediately emit registration information
        await sio.emit("res_client", [{"tid": task_id, "pid": project_id}])

    # On disconnect
    @sio.event
    async def disconnect():
        pprint("Disconnect")

    @sio.event
    async def terminal(res):
        fs.write("\n")
        pprint("Terminal")
        pprint(res)
        whale_client_res.status = 1

    @sio.event
    async def update(res):
        for k, v in res.items():
            # begin, end, progress, status, etc.
            setattr(whale_client_res, k, v)

    @sio.event
    async def error(res):
        whale_client_res.end_time = localtime()
        whale_client_res.end_time_raw = time.time()

        error_print(pformat(res))

        fs.write("\n")
        pprint("ERROR")
        pprint(res)

        whale_client_res.status = -2
        whale_client_res.error = TaskFailError(pformat(res))
        if not fs.closed:
            fs.close()

        await sio.emit("disconnect")
        exit(1)

    for solver_type in [
        "FDE",
        "FDE_SWEEP_DONE",
        "FDTD",
        "FDTD_SWEEP_DONE",
        "FDTD_SMATRIX_DONE",
        "EME_FDE_DONE",
        "EME_EME_DONE",
        "EME_SWEEP_DONE",
        "MODE_EXPANSION_DONE",
        "INDEX_MONITOR_DONE"
    ]:
        on_msg = "{}_DONE".format(solver_type)

        @sio.on(on_msg)
        async def _done(res):
            whale_client_res.end_time = localtime()
            whale_client_res.end_time_raw = time.time()

            # success_print(pformat(res))

            fs.write("\n")
            pprint(on_msg)
            pprint(res)

            whale_client_res.status = 2
            if not fs.closed:
                fs.close()

            await sio.emit("disconnect")
            exit(0)


    async def sio_main():
        sio_url = Config.OctopusSIOTemplate.format(Config.SERVERAPI)
        await sio.connect(sio_url)
        await sio.wait()

    asyncio.run(sio_main())
