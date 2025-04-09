from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
import email.utils

# Create FastAPI app instance
app = FastAPI()

# Pydantic model for input validation
class TimestampRequest(BaseModel):
    input_text: str  # plain text with new lines

# Helper function to calculate time difference in seconds
def time_difference(t1: str, t2: str) -> str:
    dt1 = email.utils.parsedate_tz(t1)
    dt2 = email.utils.parsedate_tz(t2)
    
    dt1_utc = datetime(*dt1[:6], tzinfo=timezone(timedelta(seconds=dt1[9] or 0)))
    dt2_utc = datetime(*dt2[:6], tzinfo=timezone(timedelta(seconds=dt2[9] or 0)))
    
    return str(int(abs((dt1_utc - dt2_utc).total_seconds())))

# POST endpoint to compute time differences
@app.post("/compute-timestamp-differences")
async def compute_differences(data: TimestampRequest):
    lines = data.input_text.strip().split('\n')
    
    # Input validation: check if the first line is an integer
    try:
        t = int(lines[0])  # Number of test cases
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input format: first line must be an integer representing number of test cases.")
    
    results = []
    
    # Process each pair of timestamps
    for i in range(t):
        if len(lines) < 2 * (i + 1) + 1:
            raise HTTPException(status_code=400, detail=f"Invalid input format: missing timestamps for test case {i + 1}.")
        t1 = lines[1 + 2*i]
        t2 = lines[2 + 2*i]
        
        try:
            results.append(time_difference(t1, t2))
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing timestamps for test case {i + 1}: {str(e)}")
    
    return results
