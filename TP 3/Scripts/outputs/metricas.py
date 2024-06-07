import csv

times_sec = []

# Reads times from csv file
with open('./time_sec.csv', 'r', encoding='utf-8') as timessec:
    reader = csv.reader(timessec)
    next(reader)
    row = next(reader)
    for i in range(1,5):
        times_sec.append(float(row[i]))

class Benchmark :
    def __init__(self, dim, bs, nucleos, time, comm):
        self.dim = dim
        self.bs = bs
        self.nucleos = nucleos
        self.time = time
        self.comm = comm
        if dim == 512:
            self.secuential = times_sec[0]
        elif dim == 1024:
            self.secuential = times_sec[1]
        elif dim == 2048:
            self.secuential = times_sec[2]
        elif dim == 4096:
            self.secuential = times_sec[3]

# ---------------------- MPI ----------------------
mpi_benchmarks = []
bs = 64
# Reads times from csv file
with open('./time_mpi.csv', 'r', encoding='utf-8') as times_mpi, open('./comm_mpi.csv', 'r', encoding='utf-8') as comm_mpi:
    reader = csv.reader(times_mpi)
    reader_comm = csv.reader(comm_mpi)
    next(reader)
    next(reader_comm)
    for row in reader:
        nucleos = int(row[0])
        row_comm = next(reader_comm)
        for i in range(1,5):
            dim = (2**(i+8))
            time = float(row[i])
            comm = float(row_comm[i])
            mpi_benchmarks.append(Benchmark(dim, bs, nucleos, time, comm))
# Write headers for efficiency and speedup 
with open('./speedup_mpi.csv', 'w', newline='', encoding='utf-8') as speedup_mpi, open('./efficiency_mpi.csv', 'w', newline='', encoding='utf-8') as eff_mpi, open('./overhead_mpi.csv', 'w', newline='', encoding='utf-8') as overhead_mpi:
    writer_s = csv.writer(speedup_mpi)
    writer_s.writerow(["Nucleos", "512 - 16", "1024 - 16", "2048 - 16", "4096 - 16"])
    writer_e = csv.writer(eff_mpi)
    writer_e.writerow(["Nucleos", "512 - 16", "1024 - 16", "2048 - 16", "4096 - 16"])
    writer_o = csv.writer(overhead_mpi)
    writer_o.writerow(["Nucleos", "512 - 16", "1024 - 16", "2048 - 16", "4096 - 16"])
    for i in range(0,3):
        nucleos = 2**(i)
        s_row = [f"{nucleos}"]
        e_row = [f"{nucleos}"]
        o_row = [f"{nucleos}"]
        for j in range(0,4):
            # Get to the right benchmark
            speedup = round(mpi_benchmarks[(i*4)+j].secuential / mpi_benchmarks[(i*4)+j].time, 6)
            efficiency = round(speedup / (mpi_benchmarks[(i*4)+j].nucleos * 8), 6)
            overhead = round((mpi_benchmarks[(i*4)+j].comm / mpi_benchmarks[(i*4)+j].time) * 100, 6)
            s_row.append(f"{speedup}")
            e_row.append(f"{efficiency}")
            o_row.append(f"{overhead}")
        writer_s.writerow(s_row)
        writer_e.writerow(e_row)
        writer_o.writerow(o_row)

# ---------------------- HIBRIDO ----------------------
hib_benchmarks = []
bs = 64
# Reads times from csv file
with open('./time_hibrido.csv', 'r', encoding='utf-8') as timeshibrido, open('./comm_hibrido.csv', 'r', encoding='utf-8') as commhibrido:
    reader = csv.reader(timeshibrido)
    reader_comm = csv.reader(commhibrido)
    next(reader)
    next(reader_comm)
    for row in reader:
        nucleos = int(row[0])
        row_comm = next(reader_comm)
        for i in range(1,5):
            dim = (2**(i+8))
            time = float(row[i])
            comm = float(row_comm[i])
            hib_benchmarks.append(Benchmark(dim, bs, nucleos, time, comm))
# Write headers for efficiency and speedup 
with open('./speedup_hibrido.csv', 'w', newline='', encoding='utf-8') as speedup_hib, open('./efficiency_hibrido.csv', 'w', newline='', encoding='utf-8') as eff_hib, open('./overhead_hibrido.csv', 'w', newline='', encoding='utf-8') as overhead_hib:
    writer_s = csv.writer(speedup_hib)
    writer_s.writerow(["Nucleos", "512 - 16", "1024 - 16", "2048 - 16", "4096 - 16"])
    writer_e = csv.writer(eff_hib)
    writer_e.writerow(["Nucleos", "512 - 16", "1024 - 16", "2048 - 16", "4096 - 16"])
    writer_o = csv.writer(overhead_hib)
    writer_o.writerow(["Nucleos", "512 - 16", "1024 - 16", "2048 - 16", "4096 - 16"])
    for i in range(0,2):
        nucleos = 2**(i)
        s_row = [f"{nucleos}"]
        e_row = [f"{nucleos}"]
        o_row = [f"{nucleos}"]
        for j in range(0,4):
            speedup = round(hib_benchmarks[(i*4)+j].secuential / hib_benchmarks[(i*4)+j].time, 6)
            efficiency = round(speedup / (hib_benchmarks[(i*4)+j].nucleos * 8), 6)
            overhead = round((hib_benchmarks[(i*4)+j].comm / hib_benchmarks[(i*4)+j].time) * 100, 6)
            s_row.append(f"{speedup}")
            e_row.append(f"{efficiency}")
            o_row.append(f"{overhead}")
        writer_s.writerow(s_row)
        writer_e.writerow(e_row)
        writer_o.writerow(o_row)

