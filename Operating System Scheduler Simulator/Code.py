import random

# FCFS
def fcfs(plist):
    plist.sort(key=lambda x: x['arr'])
    t = 0
    wsum = 0
    ttsum = 0
    for p in plist:
        if p['arr'] > t:
            t = p['arr']
        wsum += t - p['arr']
        t += p['burst']
        ttsum += t - p['arr']
    return ttsum / len(plist), wsum / len(plist)

# Priority (Non-Preemptive)
def prio_np(plist):
    plist.sort(key=lambda x: (x['prio'], x['arr']))
    t = 0
    wsum = 0
    ttsum = 0
    for p in plist:
        if p['arr'] > t:
            t = p['arr']
        wsum += t - p['arr']
        t += p['burst']
        ttsum += t - p['arr']
    return ttsum / len(plist), wsum / len(plist)

# Priority (Preemptive)
def prio_p(plist):
    t = 0
    rem = {p['pid']: p['rem'] for p in plist}
    last = {p['pid']: p['arr'] for p in plist}
    done = 0
    wsum = 0
    ttsum = 0
    ready = []
    while done < len(plist):
        for p in plist:
            if p['arr'] == t:
                ready.append(p)
        if ready:
            ready.sort(key=lambda x: x['prio'])
            cur = ready[0]
            wsum += t - last[cur['pid']]
            rem[cur['pid']] -= 1
            t += 1
            last[cur['pid']] = t
            if rem[cur['pid']] == 0:
                ttsum += t - cur['arr']
                ready.pop(0)
                done += 1
        else:
            t += 1
    return ttsum / len(plist), wsum / len(plist)

# Round Robin
def rr(plist, q):
    queue = list(plist)
    t = 0
    rem = {p['pid']: p['rem'] for p in plist}
    last = {p['pid']: p['arr'] for p in plist}
    wsum = 0
    ttsum = 0
    while queue:
        p = queue.pop(0)
        wsum += max(0, t - last[p['pid']])
        s = min(q, rem[p['pid']])
        rem[p['pid']] -= s
        t += s
        last[p['pid']] = t
        if rem[p['pid']] == 0:
            ttsum += t - p['arr']
        else:
            queue.append(p)
    return ttsum / len(plist), wsum / len(plist)

# SJF (Non-Preemptive)
def sjf_np(plist):
    plist.sort(key=lambda x: (x['arr'], x['burst']))
    t = 0
    wsum = 0
    ttsum = 0
    done = []
    while len(done) < len(plist):
        available = [p for p in plist if p['arr'] <= t and p not in done]
        if not available:
            t = min(p['arr'] for p in plist if p not in done)
            continue
        cur = min(available, key=lambda x: x['burst'])
        wsum += t - cur['arr']
        t += cur['burst']
        ttsum += t - cur['arr']
        done.append(cur)
    return ttsum / len(plist), wsum / len(plist)

# Main and Testing
def main():
    num_processes = 5
    runs = 3
    templates = []
    for _ in range(runs):
        tpl = []
        for i in range(1, num_processes + 1):
            pid = f'P{i}'
            arr = random.randint(1, 10)
            burst = random.randint(1, 10)
            prio = random.randint(1, 10)
            tpl.append({'pid': pid, 'arr': arr, 'burst': burst, 'prio': prio, 'rem': burst})
        templates.append(tpl)

    q = 3
    algorithms = [
        ('FCFS', fcfs),
        ('Prio-NP', prio_np),
        ('Prio-P', prio_p),
        ('RR', lambda lst: rr(lst, q)),
        ('SJF-NP', sjf_np)
    ]
    results = {name: {'tat': [], 'wt': []} for name, _ in algorithms}

    for name, func in algorithms:
        for tpl in templates:
            plist = [dict(p) for p in tpl]
            tt, wt = func(plist)
            results[name]['tat'].append(tt)
            results[name]['wt'].append(wt)

    # Print results
    col_w = 12
    # header
    header = f"{'Algorithm':<10}"
    for i in range(runs):
        header += f"{'T'+str(i+1):>{col_w}}{'W'+str(i+1):>{col_w}}"
    header += f"{'Avg TAT':>{col_w}}{'Avg WT':>{col_w}}"
    print(header)
    print('-' * len(header))

    # Rows
    for name, _ in algorithms:
        tats = results[name]['tat']
        wts = results[name]['wt']
        avg_tat = sum(tats) / runs
        avg_wt = sum(wts) / runs
        line = f"{name:<10}"
        for i in range(runs):
            line += f"{tats[i]:{col_w}.2f}{wts[i]:{col_w}.2f}"
        line += f"{avg_tat:{col_w}.2f}{avg_wt:{col_w}.2f}"
        print(line)

if __name__ == '__main__':
    main()
