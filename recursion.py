from datetime import datetime
import time
import os



def find_time(retries=10):
  divisible_by = os.environ.get("DIVISIBLE_BY", 10)
  try:
    divisible_by = int(divisible_by)
  except ValueError:
    print(f"The value '{divisible_by}' is not an integer")
    return
  current_time = datetime.now()
  if current_time.minute % divisible_by == 0:
    print(f"This minute in time ({current_time}) is divisible by {divisible_by}")
    return
  else:
    if retries <= 0:
      print(f"We were unable to find a time divisble by {divisible_by}")
      return
    else:
        time.sleep(1)
        print("Retrying ...")
        return find_time(retries - 1)


if __name__ == "__main__":
  find_time()
