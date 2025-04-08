# Task A - Parse Plain Text Call Durations

## 📄 Description

This task processes a plain text file containing call start and end times (one per line). The script calculates the duration of each call in seconds and returns an ordered list of those durations.

### 📥 Sample Input (plain text file)

07:00:00 14:30:00 08:00:00 17:30:00


### 📤 Sample Output (ordered list)

[ "27000", "34200" ]


---

## ▶️ How to Run

```bash
cd task_a
python3 main.py < input.txt


You can also test with the included sample data in sample_input.txt.
🧠 Logic Summary

    Read each line of input.

    Split start and end time.

    Convert to seconds since midnight.

    Compute the difference.

    Output a sorted list of call durations.

📦 Dependencies

    Python 3.x (Tested with 3.11+)

    No external libraries needed for this task.

📁 Files

    main.py: Main script to calculate durations.

    sample_input.txt: Sample input data for testing.

📬 Output Format

Returns a JSON array of durations in ascending order.

[ "25200", "88200" ]
