import threading
import ctypes

class _Thread(threading.Thread):
     def __init__(self,Name :chr,  Process , args : list  = None) -> None:
         super().__init__()
         self.id= id
         self.Name = Name
         self.process = Process
         self.args = args
     
     def run(self) -> None:
         print("Starting Thread:",self.Name)
         self.process(*self.args)
         
     def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
  
     def terminate(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
        else : print("Thread : ", self.Name ,"forced to close")
           
