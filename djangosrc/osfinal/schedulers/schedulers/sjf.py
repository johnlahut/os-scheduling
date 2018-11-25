
# all code has been adapted from
# http://www.plexinfo.com/2017/04/implementation-of-shortest-job-first-in-python.html


def sjf(n: int, burst_time: list):

    processes = [i+1 for i in range(n)]


    # sort by burst_time
    for i in range(0, len(burst_time) - 1):
        for j in range(0, len(burst_time) - i - 1):
            if burst_time[j] > burst_time[j + 1]:
                temp = burst_time[j]
                burst_time[j] = burst_time[j + 1]
                burst_time[j + 1] = temp
                temp = processes[j]
                processes[j] = processes[j + 1]
                processes[j + 1] = temp


    waiting_time = []
    avg_waiting_time = 0
    turn_around_time = []
    avg_turn_around_time = 0
    waiting_time.insert(0, 0)
    turn_around_time.insert(0, burst_time[0])


    for i in range(1, len(burst_time)):
        waiting_time.insert(i, waiting_time[i - 1] + burst_time[i - 1])
        turn_around_time.insert(i, waiting_time[i] + burst_time[i])
        avg_waiting_time += waiting_time[i]
        avg_turn_around_time += turn_around_time[i]
    avg_waiting_time = float(avg_waiting_time) / n
    avg_turn_around_time = float(avg_turn_around_time) / n

    response = dict(data=[], avg_wait_time=avg_waiting_time, avg_tat=avg_turn_around_time)


    for i in range(0, n):
        response['data'].append(
            dict(pid=processes[i], burst_time=burst_time[i], wait_time=waiting_time[i], turn_around_time=turn_around_time[i]))

    return response

