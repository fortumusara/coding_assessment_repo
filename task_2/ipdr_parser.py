import pandas as pd
from datetime import timedelta

# Helper function to clean datetime format
def fix_datetime_column(col):
    """Fixes datetime format by inserting a space between date and time if missing, then parses."""
    return pd.to_datetime(
        col.astype(str).str.replace(r'^(\d{4}-\d{2}-\d{2})(\d{2}:\d{2}:\d{2})$', r'\1 \2', regex=True),
        format='%Y-%m-%d %H:%M:%S',
        errors='coerce'
    )

def analyze_ipdr(file_path):
    # Load the Excel file
    df = pd.read_excel(file_path)

    # Fix the datetime columns (starttime and endtime)
    df['starttime'] = fix_datetime_column(df['starttime'])
    df['endtime'] = fix_datetime_column(df['endtime'])

    # Drop rows where conversion failed
    df.dropna(subset=['starttime', 'endtime'], inplace=True)

    # 1. Select MSISDN
    msisdn_list = df['msisdn'].unique()
    print(f"MSISDNs found: {msisdn_list}")

    # 2. Select specific start and end datetime domain/app wise
    print("Data Overview:")
    print(df[['starttime', 'endtime', 'domain']].head())

    # 3. Group rows into single call sessions (FDR logic)
    df.sort_values(by=['msisdn', 'domain', 'starttime'], inplace=True)
    
    # Add a column that calculates the time difference between consecutive calls
    df['time_diff'] = df.groupby(['msisdn', 'domain'])['starttime'].diff().shift(-1)
    
    # 4. Set a threshold to group FDRs into a single call (10 minutes idle gap threshold)
    df['call_group'] = (df['time_diff'] > timedelta(minutes=10)).cumsum()

    # 5. For each call group, calculate the first ST and adjusted ET
    call_groups = df.groupby(['msisdn', 'domain', 'call_group'])

    results = []

    for name, group in call_groups:
        # Find the earliest starttime (ST) and latest endtime (ET)
        ST = group['starttime'].min()
        ET = group['endtime'].max()
        
        # Adjust ET by subtracting 10 minutes if idle time exceeds the threshold
        adjusted_ET = ET if (ET - timedelta(minutes=10)) < ST else ET - timedelta(minutes=10)

        # Total volume in KB (convert UL/DL from Bytes to KB)
        total_volume_kb = (group['ulvolume'].sum() + group['dlvolume'].sum()) / 1024

        # Total duration in seconds
        total_duration_sec = (adjusted_ET - ST).total_seconds()

        # Calculate bitrate in kbps
        bitrate_kbps = (total_volume_kb * 8) / total_duration_sec if total_duration_sec > 0 else 0

        # Identify whether the call is audio or video
        is_audio = bitrate_kbps <= 200
        is_video = bitrate_kbps > 200

        results.append({
            'msisdn': name[0],
            'domain': name[1],
            'duration_sec': total_duration_sec,
            'fdr_count': len(group),
            'kbps': bitrate_kbps,
            'isAudio': is_audio,
            'isVideo': is_video
        })

    # Convert results to a DataFrame
    result_df = pd.DataFrame(results)

    # Filter out calls with bitrate less than 10 kbps
    result_df = result_df[result_df['kbps'] >= 10]

    # Save the results to a CSV file
    output_path = "output/call_analysis_results.csv"
    result_df.to_csv(output_path, index=False)

    print(f"Analysis saved to {output_path}")
    print(result_df.head())

if __name__ == "__main__":
    analyze_ipdr('data/Data-Engineer-ipdr.xlsx')
