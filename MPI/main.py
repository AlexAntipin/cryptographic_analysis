import mpi4py
import numpy as np

comm = mpi4py.MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# размерность матрицы и вектора
n = 4

# инициализация матрицы и вектора
if rank == 0:
    A = np.random.rand(n, n)
    b = np.random.rand(n)
else:
    A = None
    b = None

# отправляем матрицу и вектор всем процессам
A = comm.bcast(A, root=0)
b = comm.bcast(b, root=0)

# решение СЛАУ
for k in range(n - 1):
    if k % size == rank:
        # выбираем главный элемент
        max_row = k
        for i in range(k + 1, n):
            if abs(A[i, k]) > abs(A[max_row, k]):
                max_row = i
        # меняем строки местами
        A[[k, max_row]] = A[[max_row, k]]
        b[[k, max_row]] = b[[max_row, k]]
        # обновляем матрицу и вектор
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]
    # передаем обновленные значения всем процессам
    A = comm.bcast(A, root=k % size)
    b = comm.bcast(b, root=k % size)

# обратный ход метода Гаусса
x = np.zeros(n)
for k in range(n - 1, -1, -1):
    if k % size == rank:
        x[k] = (b[k] - np.dot(A[k, k+1:], x[k+1:])) / A[k, k]
    # передаем обновленные значения всем процессам
    x = comm.bcast(x, root=k % size)

# вывод результата
if rank == 0:
    print("Матрица:")
    print(A)
    print("Вектор:")
    print(b)
    print("Решение:")
    print(x)