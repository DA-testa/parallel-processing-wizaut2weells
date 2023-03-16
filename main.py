# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    heap = [(0,i) for i in range(n)]
    heapq.heapify(heap)
    for i,t in enumerate(data):
        start_time, thread_index = heapq.heappop(heap)
        output.append((thread_index, start_time))
        heapq.heappush(heap, (start_time+t,thread_index))

    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    data = []
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    for i in range(m):
        print(result[i][0],result[i][1])
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
