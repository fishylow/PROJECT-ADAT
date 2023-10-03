"""
I've created this class that is responsible for checking if a certain process is in the foreground to avoid possible bugs in the future when checking patterns or images on the screen.

It's in a testing version, using an example process, not the final version of the class.

Some comments are in Spanish, their translation will be added later.
"""

import win32gui
import win32api
import win32con
import psutil
import win32process
import time


PROCESS_NAME = "ShooterGame.exe"
WAIT_TIME = 2

class ProcessMonitor:
    def __init__(self, process_name) -> None:
        self.PROCESS_NAME = process_name
        
    def is_process_focused(self) -> bool:
        '''Prints 1 if the process is focused, 0 otherwise'''
        # Obtiene el handle de la ventana en primer plano
        foreground_window = self.get_foreground_window_handle()
        
        # Obtiene el ID del proceso de la ventana en primer plano
        foreground_process_id = win32process.GetWindowThreadProcessId(foreground_window)[1]
        
        # Obtiene el nombre del proceso a partir del ID
        process = psutil.Process(foreground_process_id)
        process_name = process.name()
        
        # Verifica si el nombre del proceso coincide con el nombre proporcionado
        return process_name == self.PROCESS_NAME
    
    def get_active_monitor(self) -> str:
        '''Returns monitor where the process is located'''
        # Obtiene el handle de la ventana en primer plano
        foreground_window = self.get_foreground_window_handle()
        
        # Obtiene el ID del monitor donde se encuentra la ventana del proceso
        monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromWindow(foreground_window, win32con.MONITOR_DEFAULTTONEAREST))
        monitor_id = monitor_info['Device'].strip('\\').split('\\')[-1]
        
        return monitor_id
    
    def get_foreground_window_handle(self) -> int:
        '''Returns the handle of the foreground window'''
        return win32gui.GetForegroundWindow()
    
    def run(self) -> None:
        while True:
            if self.is_process_focused():
                print(1)
            else:
                print(0)
            print(self.get_active_monitor())
            time.sleep(WAIT_TIME)




if __name__ == "__main__":
    monitor = ProcessMonitor(PROCESS_NAME)
    monitor.run()