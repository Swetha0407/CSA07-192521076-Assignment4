# CSA07 Assignment 4 – CO4

This package contains Python implementations, completed code/configuration TODOs, calculations, design notes, diagrams and captured local program outputs for all six tasks.

## Environment used
- OS: Linux x86_64 (execution container)
- Python: 3.13.5
- Matplotlib: 3.10.8
- Cisco Packet Tracer: not installed in the execution environment

## Run
From this folder:
```bash
python run_all.py
```
Individual scripts are in `Task01/` through `Task06/`. Task 5 includes Cisco IOS configurations in `Task05/q5_vlan_configs.txt`.

## Folder contents
- `Task01`–`Task06`: runnable programs and switch/router configuration.
- `TASK_ANSWERS.md`: worked explanations, calculations and design justifications.
- `diagrams/`: logical/physical topology diagrams (PNG).
- `graphs/`: calculation visuals.
- `results/`: stdout captured from the executed scripts.
- `configs/`: Packet Tracer build notes and verification commands.

## Important execution note
Python programs were executed locally. Packet Tracer was unavailable, so this ZIP does **not** claim to contain executed `.pkt` files, live Packet Tracer ping results, physical cable tests or real RF/WAN measurements. The configurations and build steps are prepared for you to enter and validate in Packet Tracer. Add your actual `.pkt` files, screenshots, GitHub link and progressive commits before submission. The assignment requires repository name `CSA07-<RegisterNumber>-Assignment4` and one folder per task.
