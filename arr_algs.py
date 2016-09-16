a = [45, -17, 8, 34, 10]  # массив
i = 0          # индекс, счётчик
nmin = i       # номер минимального элемента
mini = a[nmin]  # минимальный элемент
nmax = i       # номер максимального элемента
maxi = a[nmax]  # максимальный элемент

razm = len(a) # установим размерность для среднего арифметического
summ = 0 # сумма всех элементов массива

print ("  *  Нахождение min и max")
while (i < len(a)): 
    if (a[i] < mini): 
        nmin = i
        mini = a[nmin]
    if (a[i] > maxi): 
        nmax = i
        maxi = a[nmax]
    summ = summ + a[i]
    i += 1
print ("  * min = ", mini)
print ("  * min = ", maxi)
print ("  *  Нахождение среднего арифметического из массива")
arif = summ/razm
print ("  * Sred =", arif)
