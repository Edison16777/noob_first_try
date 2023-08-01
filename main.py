from fastapi import FastAPI
import tools

app = FastAPI()
# 这是水印： 2150810124 姚刘熙


@app.get("/cpu_times/")
def get_cpu_times_info():
    return tools.get_cpu_times()


@app.get("/cpu_count/")
def get_cpu_count_info():
    return tools.get_cpu_count()


@app.get("/cpu_physical_count/")
def get_cpu_physical_count_info():
    return tools.get_cpu_physical_count()


@app.get("/loadavg/")
def getloadavg_info():
    return tools.getloadavg()


@app.get("/virtual_memory/")
def get_virtual_memory_info():
    return tools.get_virtual_memory()


@app.get("/swap_memory/")
def get_swap_memory_info():
    return tools.get_swap_memory()
