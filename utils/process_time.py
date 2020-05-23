# author : Charles Cavin <charles@cavinAI.com>
# license : MIT

from datetime import datetime as dt


class ProcessTime:
    """
    A class used to keep track of how long a process takes and estimate
    when it should complete.

    Attributes
    ----------
    _start_time : datetime
        the time that the process started
    _interim_time : datetime (duration)
        the time elapsed during which the last batch of units were processed,
        initially set to _start_time
    _total_units : int
        the total number of units to be processed, e.g., number of records
    _batch_size : the number of units to be processed in a batch

    Methods
    -------
    initiate()
        establishes and returns the _start_time
    interim_check(units, total_units)
        returns the time elapsed during which the last batch of units were
        processed, the total time of unit processing, and the projected
        time of completion
    end_proc()
        returns the total time taken by the process, and the time the process
        ended
    timedelta_fmt()
        returns a formatted timedelta
    datetime__fmt()
        returns a formatted datetime
    current_time()
        returns the current, formatted datetime


    """

    # TODO: add units name, e.g., 'records', 'iterations'
    def __init__(self, total_units, batch_size, beep=False):
        """
        Parameters
        ----------
        total_units : int
            the total number of units to be processed, e.g., number of records
        batch_size : int
            the number of units to be processed in a batch
        sound: boolean
            determines if the computer should beep after each batch of units is
            completed

        """

        self._total_units = total_units
        self.batch_size = batch_size
        self.beep = beep

    def initiate(self):
        """
        Parameters
        ----------
        None

        Attributes
        ----------
        _start_time : datetime
            the time that the process started
        _interim_time : datetime
            the time when the last batch of units were completed, initially
            set to _start_time

        Returns:
            _start_time
        """

        self._start_time = dt.now()
        self._interim_time = self._start_time
        return f"{self._start_time:%Y-%m-%d  %H:%M:%S}"

    def batch_timing(self):
        """
        Parameters
        ----------
        units : integer
            units processed, i.e., records, files, etc.

        Returns:
        --------
            time_for_batch : timedelta
                the time taken to process the last batch of units
            time_since_start : timedelta
                the total time taken since the start of the process
            projected_completion : the projected time of completion
        """

        if self.beep is True:
            print("\a")
        current_time = dt.now()
        time_since_start = current_time - self._start_time
        tss = f"{self.timedelta_fmt(time_since_start)}"
        time_for_batch = current_time - self._interim_time
        tfb = f"{self.timedelta_fmt(time_for_batch)}"
        self._interim_time = current_time
        time_per_unit = time_since_start / self.batch_size
        total_time_needed = time_per_unit * self._total_units
        projected_completion = total_time_needed + self._start_time
        pc = f"{projected_completion:%Y-%m-%d  %H:%M:%S}"
        return tfb, tss, pc

    def end_proc(self):
        """
        Parameters
        ----------
        none

        returns:  the total time taken to complete processing of all units, and
                  the time at which the process ended
        """

        end_time = dt.now()
        total_time = end_time - self._start_time
        return self.timedelta_fmt(total_time), self.datetime_fmt(end_time)

    def timedelta_fmt(self, time_delta, show_days=True):
        """
        Parameters
        ----------
        time_delta : datetime.time_delta

        show_days : boolena
            Determines if the number of days should be included in the format

        returns:  if show_days is True, a formatted timedelta,
            'd days, hours:minutes:seconds' otherwise 'hours:minutes:seconds'
        """

        if show_days is True:
            days = f"{time_delta.days},  "
        else:
            days = ""
        hours = time_delta.seconds // 3600
        mins = time_delta.seconds % 3600 // 60
        secs = (time_delta.seconds % 3600) % 60
        return f"{days}{hours}:{mins}:{secs}"

    def datetime_fmt(self, date_time):
        """
        Parameters
        ----------
        date_time : datetime.datetime

        returns:  a datetime formatted with '%Y-%m-%d  %H:%M:%S'
        """
        return f"{date_time:%Y-%m-%d  %H:%M:%S}"

    def current_time(self):
        """
        Parameters
        ----------
        none

        returns:  the current date formatted with '%Y-%m-%d  %H:%M:%S'
        """
        return self.datetime_fmt(dt.now())
