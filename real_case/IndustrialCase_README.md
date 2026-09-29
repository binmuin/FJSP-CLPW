# Ship Shafting Component Production Scheduling Case

> Industrial case for ship shafting component production: Flexible Job Shop Scheduling with AGV transportation resources (FJSP-AGV)

This case is based on the production of ship shafting components and defines a flexible job shop scheduling instance consisting of **5 job types, 8 processing machines, and 2 heavy-duty AGVs**. Each job follows the same sequence of six operations: **forging → heat treatment → rough turning → finish turning → grinding → boring/milling**. Two alternative machines are available for each operation, with corresponding baseline processing times.

The case also incorporates the workshop layout and AGV transportation times, and can be used to evaluate flexible job shop scheduling algorithms that consider material transportation constraints.

---

## 1. Repository Files

The processed instance data and layout data are provided in the current directory:

```text
.
├── IndustrialCase.txt
├── IndustrialCase_LayoutM8.txt
└── IndustrialCase_README.md
```

- `IndustrialCase.txt`: FJSP processing instance containing the number of jobs, number of machines, operation information, alternative machines, and processing times.
- `IndustrialCase_LayoutM8.txt`: **AGV transportation-time matrix** for the workshop layout. The node order is `MW, M1, M2, ..., M8`.
- `IndustrialCase_README.md`: Documentation for this industrial case.

> **All processing and transportation times are expressed in minutes (min).** Workshop coordinates and physical distances are expressed in meters (m).

---

## 2. Problem Scale

### 2.1 Jobs

| Job | Component | Size |
|---|---|---|
| Job 1 | Stern Shaft | Large |
| Job 2 | Intermediate Shaft | Medium |
| Job 3 | Thrust Shaft | Large |
| Job 4 | Small Propeller Shaft | Small |
| Job 5 | Flange Shaft | Medium |

All jobs follow the same process route:

```text
Forging → Heat Treatment → Rough Turning → Finish Turning → Grinding → Boring/Milling
```

### 2.2 Basic Parameters

| Parameter | Value |
|---|---:|
| Number of jobs | 5 |
| Number of machines | 8 |
| Operations per job | 6 |
| Number of AGVs | 2 |
| AGV type | Heavy-duty modular transporter |
| AGV speed | 0.5 m/s = 30 m/min |

Therefore, the case contains:

```text
5 jobs × 6 operations/job = 30 operations
```

---

## 3. Machine Configuration

| Machine | Equipment Type | Capable Operations | Description |
|---|---|---|---|
| M1 | Large Forging Press | Forging | Suitable for large shafts |
| M2 | Medium Forging Press | Forging | Suitable for small and medium shafts |
| M3 | Large Heat-Treatment Furnace | Heat treatment | Suitable for large shafts |
| M4 | Medium Heat-Treatment Furnace | Heat treatment | Suitable for small and medium shafts |
| M5 | Heavy-Duty Turn-Mill Center | Rough turning, finish turning, boring/milling | Supports multiple operations in a single setup |
| M6 | Medium-Duty Turn-Mill Center | Rough turning, finish turning, boring/milling | Suitable for small and medium shafts |
| M7 | Large Precision Grinding Machine | Grinding | Intended for large-shaft grinding |
| M8 | Medium Precision Grinding Machine | Grinding | Intended for small- and medium-shaft grinding |

The basic correspondence between operation types and alternative machines is:

| Operation | Alternative Machines |
|---|---|
| Forging | M1 / M2 |
| Heat Treatment | M3 / M4 |
| Rough Turning | M5 / M6 |
| Finish Turning | M5 / M6 |
| Grinding | M7 / M8 |
| Boring/Milling | M5 / M6 |

---

## 4. Processing-Time Data

All processing times below are baseline processing times, expressed in **min**.

### 4.1 Job 1 — Stern Shaft (Large)

| Operation | Alternative Machines | Processing Time (min) |
|---|---|---|
| Forging | M1 / M2 | 180 / 220 |
| Heat Treatment | M3 / M4 | 240 / 280 |
| Rough Turning | M5 / M6 | 150 / 190 |
| Finish Turning | M5 / M6 | 90 / 120 |
| Grinding | M7 / M8 | 75 / 95 |
| Boring/Milling | M5 / M6 | 110 / 140 |

### 4.2 Job 2 — Intermediate Shaft (Medium)

| Operation | Alternative Machines | Processing Time (min) |
|---|---|---|
| Forging | M1 / M2 | 150 / 170 |
| Heat Treatment | M3 / M4 | 200 / 230 |
| Rough Turning | M5 / M6 | 120 / 150 |
| Finish Turning | M5 / M6 | 75 / 95 |
| Grinding | M7 / M8 | 60 / 75 |
| Boring/Milling | M5 / M6 | 90 / 110 |

### 4.3 Job 3 — Thrust Shaft (Large)

| Operation | Alternative Machines | Processing Time (min) |
|---|---|---|
| Forging | M1 / M2 | 200 / 250 |
| Heat Treatment | M3 / M4 | 260 / 300 |
| Rough Turning | M5 / M6 | 160 / 200 |
| Finish Turning | M5 / M6 | 100 / 130 |
| Grinding | M7 / M8 | 80 / 100 |
| Boring/Milling | M5 / M6 | 120 / 150 |

### 4.4 Job 4 — Small Propeller Shaft (Small)

| Operation | Alternative Machines | Processing Time (min) |
|---|---|---|
| Forging | M1 / M2 | 100 / 80 |
| Heat Treatment | M3 / M4 | 140 / 120 |
| Rough Turning | M5 / M6 | 80 / 60 |
| Finish Turning | M5 / M6 | 50 / 40 |
| Grinding | M7 / M8 | 40 / 30 |
| Boring/Milling | M5 / M6 | 60 / 45 |

### 4.5 Job 5 — Flange Shaft (Medium)

| Operation | Alternative Machines | Processing Time (min) |
|---|---|---|
| Forging | M1 / M2 | 160 / 180 |
| Heat Treatment | M3 / M4 | 210 / 240 |
| Rough Turning | M5 / M6 | 130 / 160 |
| Finish Turning | M5 / M6 | 85 / 105 |
| Grinding | M7 / M8 | 65 / 80 |
| Boring/Milling | M5 / M6 | 130 / 160 |

---

## 5. Workshop Layout

### 5.1 Coordinates

| Location | Coordinates (x, y), m | Description |
|---|---:|---|
| MW | (-60, 15) | Raw-material/finished-goods warehouse located to the left of the workshop |
| M1 | (0, 0) | Lower row, position 1 from the left |
| M2 | (20, 0) | Lower row, position 2 from the left |
| M3 | (40, 0) | Lower row, position 3 from the left |
| M4 | (60, 0) | Lower row, position 4 from the left |
| M5 | (0, 30) | Upper row, position 1 from the left |
| M6 | (20, 30) | Upper row, position 2 from the left |
| M7 | (40, 30) | Upper row, position 3 from the left |
| M8 | (60, 30) | Upper row, position 4 from the left |

A simplified representation of the workshop layout is:

```text
                         Workshop

       M5          M6          M7          M8
     (0,30)      (20,30)     (40,30)     (60,30)

MW
(-60,15)

       M1          M2          M3          M4
      (0,0)       (20,0)      (40,0)      (60,0)
```

The straight-line distance from MW to the nearest machines, M1 and M5, is approximately 61.8 m.

### 5.2 Distance Calculation

The Euclidean distance between any two locations `a` and `b` is calculated as:

```text
d(a,b) = sqrt((x_a - x_b)^2 + (y_a - y_b)^2)
```

For example:

```text
Distance(MW, M1)
= sqrt((0 - (-60))^2 + (0 - 15)^2)
≈ 61.8 m
```

---

## 6. AGV Transportation-Time Matrix

The AGV speed is:

```text
v = 0.5 m/s = 30 m/min
```

Therefore, the theoretical one-way transportation time from node `a` to node `b` is:

```text
t(a,b) = d(a,b) / 30
```

`IndustrialCase_LayoutM8.txt` stores the **9 × 9 one-way transportation-time matrix** obtained from the above distances and AGV speed. The values are expressed in **min**, and the node order is fixed as follows:

```text
0: MW
1: M1
2: M2
3: M3
4: M4
5: M5
6: M6
7: M7
8: M8
```

For example:

```text
MW → M1: 61.8 / 30 = 2.06 min
M1 → M2: 20.0 / 30 ≈ 0.667 min
M1 → M5: 30.0 / 30 = 1.00 min
```

The matrix is symmetric and all diagonal elements are zero. This assumes identical travel distances in both directions between any two nodes and zero transportation time within the same location.

> The current layout file contains only the basic travel times between nodes. If an algorithm also considers AGV loading/unloading, waiting, collision avoidance, charging, or traffic congestion, these factors must be defined separately in the scheduling model.

---

## 7. `IndustrialCase.txt` Data Format

The first line of the file is:

```text
5 8
```

which represents:

```text
<number_of_jobs> <number_of_machines>
```

Specifically:

- `5`: number of jobs;
- `8`: number of machines.

Each subsequent line corresponds to one job, in the order from Job 1 to Job 5.

The general structure of each job line is:

```text
<number_of_operations>
<k_1> <machine_1> <time_1> ... <machine_k> <time_k>
<k_2> <machine_1> <time_1> ...
...
```

where:

- `number_of_operations = 6`;
- `k_i` denotes the number of alternative machines for operation `i`;
- each operation in this case has `2` alternative machines, so all `k_i = 2`;
- machine IDs use **0-based indexing**;
- processing times are expressed in **min**.

The machine-ID mapping is:

| Machine ID in File | Physical Machine |
|---:|---|
| 0 | M1 |
| 1 | M2 |
| 2 | M3 |
| 3 | M4 |
| 4 | M5 |
| 5 | M6 |
| 6 | M7 |
| 7 | M8 |

For example, the beginning of the Job 1 record is:

```text
6 2 0 180 1 220 2 2 240 3 280 ...
```

which can be interpreted as:

```text
6                     # Job 1 contains 6 operations
2 0 180 1 220         # O11: M1=180, M2=220
2 2 240 3 280         # O12: M3=240, M4=280
...
```

This format can be directly parsed by data readers designed for common FJSP benchmark-style instances.

---

## 8. `IndustrialCase_LayoutM8.txt` Data Format

The first line of the file is:

```text
9
```

indicating that the layout contains nine nodes:

```text
MW + M1 + M2 + ... + M8
```

This is followed by a `9 × 9` matrix:

```text
t_00 t_01 ... t_08
t_10 t_11 ... t_18
...
t_80 t_81 ... t_88
```

where `t_ij` denotes the basic AGV transportation time from node `i` to node `j`, expressed in **min**.

For example, the first row is:

```text
0  2.06  2.713  3.37  4.03  2.06  2.713  3.37  4.03
```

which gives the transportation times from MW to all nodes.

---

## 9. Scheduling Interpretation

During scheduling, the typical routing of a job is:

```text
MW
 ↓ AGV
Operation 1: Forging
 ↓ AGV
Operation 2: Heat Treatment
 ↓ AGV
Operation 3: Rough Turning
 ↓ AGV
Operation 4: Finish Turning
 ↓ AGV
Operation 5: Grinding
 ↓ AGV
Operation 6: Boring/Milling
 ↓ AGV
MW
```

If two consecutive operations are assigned to different machines, an AGV must be scheduled according to the transportation time between the corresponding nodes. Under the convention adopted in this case, no material transfer is required when consecutive operations are processed on the same machine, and the transportation time for that transition is therefore set to zero. Transportation from MW to the first operation and from the final operation back to MW should both be included in the objective calculation, consistently with the decoder and experimental settings used.

---

## 10. Notes for Reproducibility

When using this case, the following experimental conventions should be specified consistently to ensure comparability across different algorithms:

1. All processing and transportation times use minutes as the common time unit.
2. Machine IDs in `IndustrialCase.txt` range from `0–7`, corresponding to physical machines `M1–M8`.
3. Node IDs in `IndustrialCase_LayoutM8.txt` range from `0–8`, corresponding to `MW, M1–M8`.
4. The number of AGVs is fixed at 2, and the AGV speed is fixed at `0.5 m/s`.
5. Transportation times in the layout file are converted from straight-line distances using a speed of `30 m/min` and are rounded to a limited number of decimal places.
6. Additional constraints such as loading/unloading time, AGV conflicts, route blocking, and charging are not included in the base data files and should be introduced separately by the scheduling model when required.
7. When comparing different algorithms, the treatment of transportation from `MW → first operation` and from `final operation → MW` should be kept consistent.

---

## 11. Case Summary

This instance has the following characteristics:

- **Realistic manufacturing context**: the jobs represent typical ship shafting components.
- **Operation flexibility**: each operation can be processed by alternative machines with different processing times.
- **Machine heterogeneity**: large and medium machines exhibit different processing efficiencies.
- **Spatial transportation constraints**: each machine has explicit two-dimensional coordinates, and transportation time varies with machine assignment.
- **Limited AGV resources**: only 2 heavy-duty AGVs are available, enabling the study of integrated production and transportation scheduling.
- **Moderate problem size**: the instance contains 30 processing operations and is suitable for algorithm validation, ablation studies, and schedule visualization.

The dataset can be used as an industrial test instance for flexible job shop scheduling algorithms that explicitly consider AGV transportation resources.
