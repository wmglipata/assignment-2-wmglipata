from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print("Master process started\n")
    for i in range(1, size):
        result = comm.recv(source=i)
        print(f"Received from process {result['rank']} | Task: {result['task']} | Sum: {result['sum']}")
else:
    # Each worker calculates a unique sum based on its rank
    task = f"Data chunk {rank}"
    total_sum = sum(range(rank * 100, (rank + 1) * 100))
    comm.send({"rank": rank, "task": task, "sum": total_sum}, dest=0)
