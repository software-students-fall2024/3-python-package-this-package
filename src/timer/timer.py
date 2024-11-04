import time
import random

def timer(countdown_time=20):
    remaining = countdown_time
    if random.random() < 0.7:
        while remaining > 0:
            print(f"Time left: {remaining} seconds")
            time.sleep(1)
            remaining -= 1
        print("Done!")

    else:
        while remaining > 0:
            mode = random.choices(["normal", "three_sec_jump", "three_jumps_per_sec", "early_stop"], weights=[30, 30, 30, 10])[0]
            if mode == "normal":
                print(f"Time left: {remaining} seconds")
                time.sleep(1)
                remaining -= 1

            elif mode == "three_sec_jump":
                print(f"Time left: {remaining} seconds")
                time.sleep(3)  
                remaining -= 1

            elif mode == "three_jumps_per_sec":
                for _ in range(3):
                    if remaining <= 0:
                        break
                    print(f"Time left: {remaining} seconds")
                    time.sleep(0.33)
                    remaining -= 1

            elif mode == "early_stop":
                print("Done!")
                return
        print("Done!")

