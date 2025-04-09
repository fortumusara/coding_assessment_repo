from datetime import datetime, timedelta, timezone
import email.utils

def time_difference(t1, t2):
    dt1 = email.utils.parsedate_tz(t1)
    dt2 = email.utils.parsedate_tz(t2)
    
    # Convert to datetime and adjust for timezone offset
    dt1_utc = datetime(*dt1[:6], tzinfo=timezone(timedelta(seconds=dt1[9] or 0)))
    dt2_utc = datetime(*dt2[:6], tzinfo=timezone(timedelta(seconds=dt2[9] or 0)))
    
    return int(abs((dt1_utc - dt2_utc).total_seconds()))

# Read input
T = int(input())
for _ in range(T):
    t1 = input().strip()
    t2 = input().strip()
    print(time_difference(t1, t2))
