from heapq import heappush,heappop,heapify
from datetime import datetime,timedelta
import time


class EmptyQueue(Exception):
    pass


class EventExecution(object):
    def __init__(self,start_time=0):
        self.heap=[]
        self.now=start_time
        self.time_scheduled=datetime.now()
        
    def schedule(self,event,time):
        sch_time=time 
        #print("schedule time",sch_time)
        heappush(self.heap,(sch_time,event))

    def pop_event(self):
        try:
            self.time_scheduled,self.event_1=heappop(self.heap)
            #print("Time Scheduled:",self.time_scheduled)
        except IndexError:
            raise EmptyQueue() 
            pass
        return self.event_1
    
    def step(self):
        event=self.pop_event()
        event.execute()

    def run(self):
        try:
            while True:
                self.step()
                #result= self.step()
                #print("Result in Event Loop", result)
        except EmptyQueue:
            print("Queue Complete")


class Event():
    def __init__(self,env):
        self.env=env

    def schedule(self,time):
        self.env.schedule(self,time)
        self.time=time
        
    def execute(self):
        print("Executing Event")
        pass


class ConstFrequencyEvent(Event):
    def __init__(self,env,freq):
        super().__init__(env)
        self.freq=freq

    def execute(self):
        self._execute()
        self.time_scheduled=self.time+timedelta(minutes=self.freq)
        self.schedule(self.time_scheduled)

    def _execute(self):
        raise NotImplementedError("ERROR: Subclasses of ConstFrequencyEvent must overload _execute() or execute()")


class EndEvent(Event):
    def __init__(self,env):
        super().__init__(env)

    def execute(self):
        print("End Event")
        raise EmptyQueue()
        pass
        

