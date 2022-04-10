def convert(m):
    return m*100
convert(2)

def area_of_circle(r):
	return r*r*3.14
    
area_of_circle(30)

def print_func(string, n=2):
	print (string * n)
	print()
print_func('rerer!!!')

#def fancy_print(text, color, background, style, justify):
 #Кожного разу, коли ми викликаємо цю функцію (зараз нам не дуже важливо, що вона робить, ми просто розглядаємо сигнатуру функції), нам потрібно знати правильний порядок аргументів. Так, ми спочатку задамо текстове значення, потім колір, фон, стиль та вирівнювання. Однак Python дозволяє нам іменувати аргументи при виклику функції, як показано у наступних прикладах:   
