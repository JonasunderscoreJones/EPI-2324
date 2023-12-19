'''EPRE Übung 7 Aufgabe 3'''
__author__ = "7987847, Werner"

import concurrent.futures
import timeit
from main import greedy_approach, recursive_optimal_path, gen_matrix

def measure_runtime(function, matrix):
    '''Misst die Laufzeit von function mit matrix als Argument

    Args:
        function (function): Funktion, deren Laufzeit gemessen werden soll
        matrix (list(list(int))): Matrix, die als Argument an function übergeben wird

        Returns:
            float: Laufzeit von function mit matrix als Argument'''
    runtime = timeit.timeit(lambda: function(matrix), number=100)
    return runtime

def compare_runtimes_parallel(sizes, max_workers=16):
    '''Vergleicht die Laufzeiten von greedy_approach und recursive_optimal_path für
    verschiedene Matrixgrößen

    Args:
        sizes (list(int)): Liste mit Matrixgrößen
        max_workers (int, optional): Maximale Anzahl an Threads. Defaults to 16.

    Returns:
        list(float), list(float): Listen mit Laufzeiten von greedy_approach und
        recursive_optimal_path
    '''
    greedy_runtimes = []
    recursive_runtimes = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for size in sizes:
            matrix = gen_matrix(size)

            # Greedy-Ansatz
            greedy_future = executor.submit(measure_runtime, greedy_approach, matrix)
            futures.append((greedy_future, "Greedy", size))

            # Rekursiver optimaler Pfad
            recursive_future = executor.submit(measure_runtime, recursive_optimal_path, matrix)
            futures.append((recursive_future, "Recursive", size))

        for future, label, size in futures:
            runtime = future.result()
            print(f"Size: {size}, {label} Runtime: {runtime:.6f} seconds")
            if label == "Greedy":
                greedy_runtimes.append(runtime)
            else:
                recursive_runtimes.append(runtime)

    return greedy_runtimes, recursive_runtimes

def plot_results(sizes, greedy_runtimes, recursive_runtimes):
    '''Plottet die Laufzeiten von greedy_approach und recursive_optimal_path für
    verschiedene Matrixgrößen

    Args:
        sizes (list(int)): Liste mit Matrixgrößen
        greedy_runtimes (list(float)): Liste mit Laufzeiten von greedy_approach
        recursive_runtimes (list(float)): Liste mit Laufzeiten von recursive_optimal_path
    '''
    plt.plot(sizes, greedy_runtimes, label="Greedy Approach")
    plt.plot(sizes, recursive_runtimes, label="Recursive Optimal Path")
    plt.xlabel("Matrix Size")
    plt.ylabel("Runtime (seconds)")
    plt.title("Comparison of Runtimes")
    plt.legend()
    plt.xticks(range(min(sizes), max(sizes)+1))
    plt.show()

if __name__ == "__main__":
    matrix_sizes = list(range(1, 6))

    greedy_runtimes, recursive_runtimes = compare_runtimes_parallel(matrix_sizes)

    print("Greedy runtimes:")
    for size, runtime in zip(matrix_sizes, greedy_runtimes):
        print(f"Size: {size}, Runtime: {runtime:.6f} seconds")

    print("Recursive runtimes:")
    for size, runtime in zip(matrix_sizes, recursive_runtimes):
        print(f"Size: {size}, Runtime: {runtime:.6f} seconds")

    print("Recursive runtimes:")
    for size, runtime in zip(matrix_sizes, recursive_runtimes):
        print(f"Size: {size}, Runtime: {runtime:.6f} seconds")
        print(f"Size: {size}, Runtime: {runtime:.6f} seconds")

    try:
        import matplotlib.pyplot as plt

        plot_results(matrix_sizes, greedy_runtimes, recursive_runtimes)

    except ImportError:
        print("matplotlib not installed. Skipping plotting of results.")
