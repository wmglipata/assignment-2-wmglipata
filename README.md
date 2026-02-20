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
