import csv
with open('trial.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(csv_file)
    next(csv_reader)

    for line in csv_reader:
        csv_writer.
