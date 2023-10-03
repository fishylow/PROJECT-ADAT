"""
I've created this class that is responsible for checking if a certain process is in the foreground to avoid possible bugs in the future when checking patterns or images on the screen.

It's in a testing version, using an example process, not the final version of the class.

Some comments are in Spanish, their translation will be added later.
"""

import win32gui
import psutil
import win32process
import time


PROCESS_NAME = "LeagueClientUx.exe"

class ProcessMonitor:
    def __init__(self, process_name) -> None:
        self.PROCESS_NAME = process_name
        
    def is_process_focused(self) -> bool:
        # Obtiene el handle de la ventana en primer plano
        foreground_window = win32gui.GetForegroundWindow()
        
        # Obtiene el ID del proceso de la ventana en primer plano
        foreground_process_id = win32process.GetWindowThreadProcessId(foreground_window)[1]
        
        # Obtiene el nombre del proceso a partir del ID
        process = psutil.Process(foreground_process_id)
        process_name = process.name()
        
        # Verifica si el nombre del proceso coincide con el nombre proporcionado
        return process_name == self.PROCESS_NAME
    
    def run(self) -> None:
        while True:
            if self.is_process_focused():
                print(f"{self.PROCESS_NAME} is focused!")                
            else:
                print(f"{self.PROCESS_NAME} is not focused!")
            time.sleep(5)




if __name__ == "__main__":
    monitor = ProcessMonitor(PROCESS_NAME)
    monitor.run()