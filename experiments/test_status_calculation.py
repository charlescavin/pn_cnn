# author : Charles Cavin <charles@cavinAI.com>
#
# license : MIT

from datetime import datetime, timedelta

total_rcds = 377110
start_time = datetime.now()
interval_time = start_time

now = datetime.now()
td = timedelta(0, 5)

total_time_taken = now - start_time
interval_time = now

for rcd_ctr in range(1, 5):
    print(f"Record written:      {rcd_ctr}")

    now = interval_time + td
    print(f"now:                 {now}")

    interval_time_taken = now - interval_time
    print(f"interval_time_taken: {interval_time_taken}")

    interval_time = now
    print(f"interval_time:       {now}")

    total_time_taken = now - start_time
    print(f"total_time_taken:    {total_time_taken}")

    time_taken_per_rcd = total_time_taken / rcd_ctr
    print(f"time_take_per_rcd:   {time_taken_per_rcd}")

    print(
        f"Projected time of completion: {(((time_taken_per_rcd * total_rcds) - total_time_taken) + now)}")

    print()
    print("======================================")
    print()
