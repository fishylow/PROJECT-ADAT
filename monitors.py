from screeninfo import get_monitors


class MonitorController:
    def __init__(self) -> None:
        self.monitors_info = get_monitors()

    def get_monitors_resolution(self) -> list[tuple]:
        return [(monitor.width, monitor.height) for monitor in self.monitors_info]
