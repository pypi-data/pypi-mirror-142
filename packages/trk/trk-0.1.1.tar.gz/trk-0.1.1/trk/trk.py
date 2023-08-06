from pathlib import Path
from typing import Any, Dict, List, NamedTuple
import pandas as pd
from datetime import datetime
from dateutil import parser

from trk import DB_READ_ERROR
from trk.database import DatabaseHandler

class Tracker:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path) # DatabaseHandler component to facilitate direct communication with the to-do database

    def _check_last_event_status():
        pass

    def _get_min_duration(self, start_time, end_time):
        c = end_time - start_time
        minutes = c.total_seconds()/60
        return(minutes)
    def _string_to_date(self,str_date):
        date_date = parser.parse(str_date)
        #final_date = datetime.strftime(date_date, "%Y-%m-%d %H:%M:%S.%f" )
        return(date_date)

    def get_date_item(self, date, type):
        if type == "year":
            item = date.strftime("%Y")
        if type == "week":
            item = date.isocalendar()[1]
        if type == "month":
            item = date.strftime("%m")
        if type == "today":
            item = date.strftime("%Y/%m/%d")
        return(item)



    def start(self, event: str, start_time, project, client):
        """Add a new event to the database."""
        read = self._db_handler.read_events()
        if (start_time is None):
            start_time = datetime.now()   
        else:
            start_time =  self._string_to_date(start_time)

        year = self.get_date_item(start_time, "year")
        month = self.get_date_item(start_time, "month")
        week = self.get_date_item(start_time, "week")
        date = self.get_date_item(start_time, "today")

        event_trk = pd.DataFrame({"start_time" :[datetime.strftime(start_time, "%Y-%m-%d %H:%M:%S.%f" )],
            "end_time": [None],
            "duration_minutes": [None],
            "task":[event],
            "project":[project],
            "client":[client],
            "year": [year],
            "month": [month],
            "week":[week],
            "date":[date]})

        db_trk = pd.concat((read, event_trk),axis= 0)
        write = self._db_handler.write_event(db_trk)

    def end(self, end_time):
        """End the time for a event"""

        if (end_time is None):
            end_time = datetime.now()   
        else:
            end_time =  self._string_to_date(end_time) 


        read = self._db_handler.read_events()
        number_rows = read.shape[0]-1        
        read.at[number_rows, "end_time"] = end_time # record end time

        #end_time = read.iloc[number_rows]['end_time']
        start_time = datetime.strptime(read.iloc[number_rows]['start_time'], "%Y-%m-%d %H:%M:%S.%f")

        read.at[number_rows, "duration_minutes"] = self._get_min_duration(start_time, end_time)
              
        write = self._db_handler.write_event(read)     

    def list_unique(self, column):
        read = self._db_handler.read_events()
        read_unique = read.drop_duplicates(subset= column)[[column]]
        return(read_unique)

    def summary(self, columns):
        read = self._db_handler.read_events()
        summary_table = read.groupby(columns)["duration_minutes"].sum().reset_index()
        return(summary_table)




        


    


        
