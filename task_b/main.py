from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
from datetime import datetime, timedelta, timezone
import email.utils

app = FastAPI()

class TimestampRequest(BaseModel):
    input_text: str  # plain text with new lines

def time_difference(t1: str, t2: str) -> str:
    dt1 = email.utils.parsedate_tz(t1)
    dt2 = email.utils.parsedate_tz(t2)
    
    dt1_utc = datetime(*dt1[:6], tzinfo=timezone(timedelta(seconds=dt1[9] or 0)))
    dt2_utc = datetime(*dt2[:6], tzinfo=timezone(timedelta(seconds=dt2[9] or 0)))
    
    return str(int(abs((dt1_utc - dt2_utc).total_seconds())))

@app.post("/compute-timestamp-differences")
async def compute_differences(data: TimestampRequest):
    lines = data.input_text.strip().split('\n')
    t = int(lines[0])
    results = []

    for i in range(t):
        t1 = lines[1 + 2*i]
        t2 = lines[2 + 2*i]
        results.append(time_difference(t1, t2))
    
    return results
