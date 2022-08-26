import csv

import requests


status_dict = {"Website": "Status"}


def main():
  try:
    print("Checking website status ******")
    with open("websites.txt", "r") as fr:
        for line in fr:
            website = line.strip()
            status = requests.get(website).status_code
            status_dict[website] = "----------Alive" if status == 200 \
                else "------------------xxx Dead"
  except Exception as e:
   print("There is a problem with a URL make sure it isc orrectly typed in")
   raise e

    # print(status_dict)
  try:
   with open("website_status.csv", "w", newline="") as fw:
        print("Logging Status ******")
        csv_writers = csv.writer(fw)
        for key in status_dict.keys():
            csv_writers.writerow([key, status_dict[key]])
        print("****** PROGRAM FINISHED SUCCESSFULLY ******")
  except Exception as e:
    raise e


if __name__ == "__main__":
    main()
