from os import system, name
import io


# CLEARS CLI WINDOW
def clear():
    system('cls' if name == 'nt' else 'clear')


# SORT A LIST WITHIN A LIST BASED ON CONTENT OF INDEX OF INNER LIST
def sort_list_in_list(index: int, list_of_list_to_be_sorted=None, reverse:bool=False):
    return sorted(list_of_list_to_be_sorted, key=lambda x: x[index], reverse=reverse)


# STORE CONTENT TO FILE AND PRINT
def custom_print(store_to_file, data_to_print):
    if store_to_file:
        with io.open("./solution.txt", "a", encoding="utf-8") as solution:
            solution.write(data_to_print+"\n")
    print(data_to_print)


# GET AND PROCESS USER INPUT
def grab_inputs(total_processes, processes):
    if total_processes == None:
        if processes == None:
            clear()
            total_processes = int(
                input("Enter the total number of processes: "))
            processes = []
            for process_number in range(total_processes):
                process = []
                clear()
                process.append(process_number+1)
                process.append(
                    int(input("Enter the Arrival Time for P{}: ".format(process_number+1))))
                process.append(
                    int(input("Enter the Service/Burst Time for P{}: ".format(process_number+1))))
                processes.append(process)
            return total_processes, processes
        else:
            return len(processes), processes
    else:
        return total_processes, processes
