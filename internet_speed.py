# File to test internet speed using ALICE

# Import necessary modules
import ai_speak  # Module for AI voice output
import speedtest  # Module for testing internet speed


# Function to perform speed test
def perform_speedtest():
    st = speedtest.Speedtest()

    dst = "Performing download speed test..."
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    dst_result = f"Download Speed: {download_speed:.2f} Mbps"

    ust = "Performing upload speed test..."
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
    ust_result = f"Upload Speed: {upload_speed:.2f} Mbps"

    response = dst + "\n" + dst_result + "\n" + ust + "\n" + ust_result
    return response
