# Task 2: IPDR Data Processing and Analysis

In this task, we process IPDR data to calculate key metrics for audio and video calls.

## Input Data

The input file `Data Engineer-ipdr.xlsx` has the following columns:

- **starttime**: Call start timestamp.
- **endtime**: Call end timestamp.
- **msisdn**: User identifier.
- **ulvolume**: Upload volume in bytes.
- **dlvolume**: Download volume in bytes.
- **domain**: The app used for the call.

## Tasks

1. **Select MSISDN**: Process call records for each user.
2. **Filter by Datetime/Domain**: Select calls based on start time, end time, and app/domain.
3. **Calculate Start and End Times (ST & ET)**: For each call, calculate start and end times.
4. **Exclude Idle Time**: Subtract 10 minutes from ET to remove idle time.
5. **Calculate Total Volume**: Total volume = `ulvolume + dlvolume` in KB.
6. **Calculate Duration**: Duration = `ET - ST` in seconds.
7. **Bit Rate Calculation**: Bit rate = `total volume / total duration`.
8. **Classify Calls**: Calls with:
   - **< 10 kbps**: Discarded.
   - **10-200 kbps**: Audio call.
   - **> 200 kbps**: Video call.

## Solution Approach

### 1. Data Preprocessing

Load the data from `sample_ipdr.xlsx` and filter valid records. Convert start and end times to datetime objects.

### 2. Calculations

- **Volume**: `total_volume = (ulvolume + dlvolume) / 1024` (converted to KB).
- **Duration**: `duration = (ET - ST).total_seconds()`.
- **Bit Rate**: `bit_rate_kbps = (total_volume * 8) / (duration * 1024)` (in kbps).

### 3. Classifying Calls

- Calls **< 10 kbps** are discarded.
- Calls **10-200 kbps** are audio.
- Calls **> 200 kbps** are video.

## Output

The output contains:

- **msisdn**: User identifier.
- **domain**: The app used.
- **duration**: Call duration in seconds.
- **fdr_count**: Number of CDRs per call.
- **kbps**: Bit rate in kbps.
- **isAudio**: Audio call (True/False).
- **isVideo**: Video call (True/False).

### Example Output:

```csv
msisdn,domain,duration,fdr_count,kbps,isAudio,isVideo
1,app1,100,2,15.3,True,False
2,app2,180,3,220.5,False,True
3,app3,50,1,8.9,False,False

Instructions for Running the Code

    Clone this repository.

    Install dependencies:

pip install -r requirements.txt

Run the script:

    python task_2/process_ipdr.py

    The results will be saved in output/output_file.csv.

Folder Structure

task_2/
│
├── data/
│   └── sample_ipdr.xlsx  # Input data
│
├── output/
│   └── output_file.csv  # Output results
│
└── process_ipdr.py  # Script to process data
└── README.md  # Task 2 README

Conclusion

The task processes IPDR data to calculate call metrics, classify calls, and generate a report on call characteristics like volume, duration, and bit rate.
