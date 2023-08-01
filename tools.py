import psutil
import platform
# 这是水印： 2150810124 姚刘熙


def get_cpu_times():
    cpu_times = psutil.cpu_times()
    os_info = platform.system()
    if os_info == "Windows":
        cpu_times_info = {
            "user": cpu_times.user,
            "system": cpu_times.system,
            "idle": cpu_times.idle,
            "interrupt": cpu_times.interrupt,
            "dpc": cpu_times.dpc,
        }
    elif os_info == "Linux":
        cpu_times_info = {
            "user": cpu_times.user,
            "system": cpu_times.system,
            "idle": cpu_times.idle,
            "iowait": cpu_times.iowait,
        }
    return cpu_times_info


def get_cpu_count():
    cpu_count = psutil.cpu_count()
    return cpu_count


def get_cpu_physical_count():
    cpu_physical_count = psutil.cpu_count(logical=False)
    return cpu_physical_count


def getloadavg():
    loadavg = psutil.getloadavg()
    return loadavg

# 这也是水印： 2150810124 姚刘熙
def get_virtual_memory():
    virtual_memory = psutil.virtual_memory()
    os_info = platform.system()
    if os_info == "Windows":
        virtual_memory_info = {
            "total": virtual_memory.total,
            "available": virtual_memory.available,
            "percent": virtual_memory.percent,
            "used": virtual_memory.used,
            "free": virtual_memory.free,
        }
    elif os_info == "Linux":
        virtual_memory_info = {
            "buffers": virtual_memory.buffers,
            "cached": virtual_memory.cached,
            "shared": virtual_memory.shared,
            "slab": virtual_memory.slab,
        }
    return virtual_memory_info


def get_swap_memory():
    swap_memory = psutil.swap_memory()
    swap_memory_info = {
        "total": swap_memory.total,
        "used": swap_memory.used,
        "free": swap_memory.free,
        "percent": swap_memory.percent,
        "sin": swap_memory.sin,
        "sout": swap_memory.sout,
    }
    return swap_memory_info
