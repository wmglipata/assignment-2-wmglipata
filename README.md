# Assignment 2: Simple Distributed Message-Passing

## Project Overview
This project implements a Master-Worker architecture using `mpi4py`. 
- **Master (Rank 0):** Receives and displays messages from workers.
- **Workers (Rank 1-3):** Perform a summation task and send results to the Master.

## Implementation Details
Modified the starter code to include:
- Process rank and assigned task name.
- A computation task (summing a range of numbers).
- Dictionary-based message passing.

## How to Run (Google Colab)
```bash
!mpirun --allow-run-as-root --oversubscribe -n 4 python asgmnt2_pdc_lipatawilmar.py
```

## Guide Questions:

1. Why is message passing required in distributed systems?
Message passing is essential in distributed systems because individual processes run in isolated memory environments. Unlike a standard program where different parts of the code can access the same variables, distributed processes cannot directly read or write to each other's memory. These processes are often located on different physical hardware. Message passing acts as the vital communication bridge that allows these isolated islands to exchange data and coordinate their timing. This mechanism is what enables a system to scale across multiple machines. The processes communicate through a network protocol instead of relying on shared physical hardware.

2. What happens if one process fails?
In a typical MPI-based distributed system, the failure of a single process often results in a deadlock or the termination of the entire job. The Master-Worker model relies on synchronized communication. If a worker process crashes, the master may wait indefinitely for a message that will never arrive. This causes the entire system to hang. To prevent the waste of computational resources, most MPI implementations are designed to shut down all remaining processes as soon as one failure is detected. Without advanced fault tolerance or checkpointing, any data handled by the failed process is lost and the entire parallel task must usually be restarted from the beginning.

3. How does this model differ from shared-memory programming?
The primary difference between these two models lies in how data is stored and accessed. In shared-memory programming, multiple threads operate within a single memory space. This allows them to communicate almost instantly by reading and writing to the same variables. However, this method requires complex locks to prevent different threads from overwriting each other. In contrast, the message-passing model provides each process with its own private memory. This makes it inherently safer from direct memory conflicts. Shared-memory is limited to the resources of a single computer. The message-passing model is much more flexible because it allows thousands of processors to work together across a vast network. This makes it the standard for high-performance supercomputing.
