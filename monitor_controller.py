from screeninfo import get_monitors


class MonitorController:
    def __init__(self) -> None:
        self.monitors_info = get_monitors()
        self.monitors_amount = len(self.monitors_info)

    def get_monitors_resolutions(self) -> dict:
        '''Returns a dictionary with the resolution of each monitor in the system'''
        monitors = {}
        monitors_names = self.get_monitors_names()
        for i in range(len(self.monitors_amount)):
            monitors[monitors_names[i]] = {"width": self.monitors_info[i].width, "height": self.monitors_info[i].height}

        return monitors
    
    def get_monitors_names(self) -> list:
        '''Returns a list with the names of the monitors in the system'''
        monitors_names = []
        for i in range(self.monitors_amount):
            monitor_name = f"DISPLAY{i+1}"
            monitors_names.append(monitor_name)
        
        return monitors_names
