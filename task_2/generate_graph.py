import pandas as pd
import matplotlib.pyplot as plt

def generate_graph(file_path):
    # Read the data (use the analysis CSV or original data)
    df = pd.read_csv(file_path)

    # Plotting: Call duration vs. upload volume
    plt.figure(figsize=(10, 6))
    plt.scatter(df['call_duration'], df['ulvolume'], color='blue', label='Upload Volume')
    plt.xlabel('Call Duration (seconds)')
    plt.ylabel('Upload Volume')
    plt.title('Call Duration vs. Upload Volume')
    plt.legend()
    plt.savefig('output/call_duration_vs_ulvolume.png')
    plt.show()

    # Plotting: Call duration vs. download volume
    plt.figure(figsize=(10, 6))
    plt.scatter(df['call_duration'], df['dlvolume'], color='red', label='Download Volume')
    plt.xlabel('Call Duration (seconds)')
    plt.ylabel('Download Volume')
    plt.title('Call Duration vs. Download Volume')
    plt.legend()
    plt.savefig('output/call_duration_vs_dlvolume.png')
    plt.show()

if __name__ == "__main__":
    generate_graph('output/call_analysis_results.csv')
