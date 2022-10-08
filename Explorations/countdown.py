import time

def sec_countdown(n):
    """Timer function for seconds."""
    print(f"Counting down to 0 from {n} in seconds:")
    for i in range(n):
        time.sleep(1)
        print(f"{n}")
        n = n - 1
    print(f"Time is up!.")

def ms_countdown(n):
    """Timer function for seconds."""
    print(f"Counting down to 0 from {n} in milliseconds:")
    for i in range(n):
        time.sleep(.001)
        print(f"{n}")
        n = n - 1
    print(f"Time is up!.")

if __name__ == "__main__":
    ms_countdown(7200)
    sec_countdown(7200)
