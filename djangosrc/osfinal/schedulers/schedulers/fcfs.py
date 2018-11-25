# all code has been adapted from
# http://www.plexinfo.com/2017/04/implementation-of-first-come-first-serve-python.html


def fcfs(n: int, burst_time: list):

    burst_time = list(map(int, burst_time))
    wait_time = []
    avg_wait_time = 0
    turn_around_time = []
    avg_turn_around_time = 0
    wait_time.insert(0, 0)
    turn_around_time.insert(0, burst_time[0])

    # no sorting needed, first come first serve
    for i in range(1, len(burst_time)):
        wait_time.insert(i, wait_time[i - 1] + burst_time[i - 1])
        turn_around_time.insert(i, wait_time[i] + burst_time[i])
        avg_wait_time += wait_time[i]
        avg_turn_around_time += turn_around_time[i]
    avg_wait_time = float(avg_wait_time) / n
    avg_turn_around_time = float(avg_turn_around_time) / n

    results = dict(data=[], avg_tat=avg_turn_around_time, avg_wait_time=avg_wait_time)

    for i in range(0, n):
        results['data'].append(
            dict(pid=i+1, burst_time=burst_time[i], wait_time=wait_time[i], turn_around_time=turn_around_time[i]))

    return results
