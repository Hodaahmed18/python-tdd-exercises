import time

print("Welcome to the Stopwatch!")

running = True

while running:

    input("Press Enter to start the stopwatch...")
    start_time = time.time()

    input("Press Enter to stop the stopwatch...")
    end_time = time.time()

    elapsed_time = end_time - start_time

    print("Elapsed time:", elapsed_time, "seconds")

    answer = input("Would you like to run the stopwatch again? (yes/no): ")

    if answer == "no":
        running = False

print("Goodbye!")
