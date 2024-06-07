import csv

times_sec = []

# Reads times from csv file
with open('./time_sec.csv', 'r', encoding='utf-8') as timessec:
    reader = csv.reader(timessec)
    next(reader)
    row = next(reader)
    for i in range(1,5):
        times_sec[i-1] = float(row[i])

class Benchmark :
    def __init__(self, dim, bs, threads, time):
        self.dim = dim
        self.bs = bs
        self.threads = threads
        self.time = time
        if dim == 512:
            self.secuential = times_sec[0]
        elif dim == 1024:
            self.secuential = times_sec[1]
        elif dim == 2048:
            self.secuential = times_sec[2]
        elif dim == 4096:
            self.secuential = times_sec[3]

# ---------------------- PThreads ----------------------
pt_benchmarks = []
bs = 64
# Reads times from csv file
with open('./time_pt.csv', 'r', encoding='utf-8') as timespt:
    reader = csv.reader(timespt)
    next(reader)
    for row in reader:
        threads = int(row[0])
        for i in range(1,5):
            dim = (2**(i+8))
            time = float(row[i])
            pt_benchmarks.append(Benchmark(dim, bs, threads, time))
# Write headers for efficiency and speedup 
with open('./speedup_pt.csv', 'w', newline='', encoding='utf-8') as speeduppt, open('./efficiency_pt.csv', 'w', newline='', encoding='utf-8') as efficiencypt:
    writer_s = csv.writer(speeduppt)
    writer_s.writerow(["Threads", "512 - 64", "1024 - 64", "2048 - 64", "4096 - 64"])
    writer_e = csv.writer(efficiencypt)
    writer_e.writerow(["Threads", "512 - 64", "1024 - 64", "2048 - 64", "4096 - 64"])
    for i in range(0,3):
        threads = 2**(i + 1)
        s_row = [f"{threads}"]
        e_row = [f"{threads}"]
        for j in range(0,4):
            # Get to the right benchmark
            speedup = round(pt_benchmarks[(i*4)+j].secuential / pt_benchmarks[(i*4)+j].time, 6)
            efficiency = round(speedup / pt_benchmarks[(i*4)+j].threads, 6)
            s_row.append(f"{speedup}")
            e_row.append(f"{efficiency}")
            # print()
            # print(pt_benchmarks[(i*4)+j].dim)
            # print(pt_benchmarks[(i*4)+j].time)
            # print(pt_benchmarks[(i*4)+j].secuential)
            # print(speedup)
            # print(efficiency)
        writer_s.writerow(s_row)
        writer_e.writerow(e_row)

# ---------------------- OpenMP ----------------------
omp_benchmarks = []
bs = 64
# Reads times from csv file
with open('./time_omp.csv', 'r', encoding='utf-8') as timesomp:
    reader = csv.reader(timesomp)
    next(reader)
    for row in reader:
        threads = int(row[0])
        for i in range(1,5):
            dim = (2**(i+8))
            time = float(row[i])
            omp_benchmarks.append(Benchmark(dim, bs, threads, time))
# Write headers for efficiency and speedup 
with open('./speedup_omp.csv', 'w', newline='', encoding='utf-8') as speedupomp, open('./efficiency_omp.csv', 'w', newline='', encoding='utf-8') as efficiencyomp:
    writer_s = csv.writer(speedupomp)
    writer_s.writerow(["Threads", "512 - 64", "1024 - 64", "2048 - 64", "4096 - 64"])
    writer_e = csv.writer(efficiencyomp)
    writer_e.writerow(["Threads", "512 - 64", "1024 - 64", "2048 - 64", "4096 - 64"])
    for i in range(0,3):
        threads = 2**(i + 1)
        s_row = [f"{threads}"]
        e_row = [f"{threads}"]
        for j in range(0,4):
            speedup = round(omp_benchmarks[(i*4)+j].secuential / omp_benchmarks[(i*4)+j].time, 6)
            efficiency = round(speedup / omp_benchmarks[(i*4)+j].threads, 6)
            s_row.append(f"{speedup}")
            e_row.append(f"{efficiency}")
        writer_s.writerow(s_row)
        writer_e.writerow(e_row)
