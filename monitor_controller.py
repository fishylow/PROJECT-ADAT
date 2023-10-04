from screeninfo import get_monitors


class MonitorController:
    def __init__(self) -> None:
        self.monitors_info = get_monitors()

    def get_monitor_resolutions(self) -> dict:
        '''Returns a dictionary with the resolution of each monitor in the system'''
        monitors = {}
        for i, monitor in enumerate(self.monitors_info):
            monitor_name = f"DISPLAY{i+1}" # Para que el nombre del monitor coincida con el de Windows
            monitors[monitor_name] = {"width": monitor.width, "height": monitor.height}

        return monitors
