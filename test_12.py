# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

x = abs(int(input('Введите первое натуральное число X: ')))
y = abs(int(input('Введите второе натуральное число Y: ')))
Sum = x + y
print("Сумма двух загаданных чисел: ",Sum)
Proiz = x * y
print("Произведение двух загаданных чисел: ",Proiz)
y1 = int((Sum + ((-Sum) ** 2 - 4 * Proiz) ** 0.5) / 2)
x1 = int((Sum - ((-Sum) ** 2 - 4 * Proiz) ** 0.5) / 2)
print("Петя загадал числа: ", x1, y1)