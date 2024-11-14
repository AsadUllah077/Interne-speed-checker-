import speedtest

def Speed_Test():
    # Initialize the Speedtest object
    test = speedtest.Speedtest()
    
    # Load server list and choose the best server based on ping
    test.get_best_server()
    
    print("Testing Download Speed...")
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)  # Convert from bits to Mbps
    print("Download Speed: ", down_speed, "Mbps")
    
    print("Testing Upload Speed...")
    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)  # Convert from bits to Mbps
    print("Upload Speed: ", up_speed, "Mbps")
    
    # Get ping result
    ping = test.results.ping
    print("Ping: ", ping, "ms")

# Run the speed test function
Speed_Test()
