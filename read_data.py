def load_data(path):
    with open(path) as f:
        lines = f.read().splitlines()

    num_machine_header = int(lines[0].split()[1])
    J_raw, P, all_machine_ids = [], [], []

    for line in lines[1:]:
        data = line.split()
        if not data: continue

        it = iter(map(int, data))
        num_op = next(it)

        job, proc = [], []
        for _ in range(num_op):
            k = next(it)
            m_list, p_list = [], []
            for _ in range(k):
                m = next(it)
                p = next(it)
                m_list.append(m)
                p_list.append(p)
                all_machine_ids.append(m)
            job.append(m_list)
            proc.append(p_list)

        J_raw.append(job)
        P.append(proc)

    zero_based = 0 in all_machine_ids
    J = J_raw if zero_based else [[[m - 1 for m in op] for op in job] for job in J_raw]
    num_machine_data = max(all_machine_ids) + (1 if zero_based else 0)

    return J, P, max(num_machine_header, num_machine_data)


def load_travel_time(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    # n = int(lines[0].strip())
    matrix = []
    for line in lines[1:]:
        row = list(map(float, line.strip().split()))
        matrix.append(row)
    return matrix


def main(file, layout):
    J, P, n = load_data(file)
    travel_time = load_travel_time(layout)
    print(n, J, P, travel_time, sep="\n========\n")

if __name__ == '__main__':
    data_dir = r"datasets/"
    main(data_dir+"FJSPT01.txt", data_dir+"Layout.txt")  # A simple example
