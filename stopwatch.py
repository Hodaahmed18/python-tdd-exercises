import time

input("Press Enter to start stopwatch")

start_time = time.time()

input("Press Enter to stop stopwatch")

end_time = time.time()

elapsed_time = end_time - start_time

print("Elapsed time:", elapsed_time, "seconds")
