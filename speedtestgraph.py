import csv

import speedtest

servers = []
s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()

results = s.results.dict()

with open('results.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([results["timestamp"], results["download"], results["upload"], results["ping"]])
