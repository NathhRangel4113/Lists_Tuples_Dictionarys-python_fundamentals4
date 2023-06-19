#STRUCTURE:
#First of all we define each of the exercises proposed in the miscellaneous of exercises, then below we can find the structure of the code that will allow us to execute each one of them according to the choice of the end user.

#DEFINING
#1 (Operadores Lógicos)
def triangle_area():
      print('Running excercise 1 "Calcule el área de un triángulo"')
      #TRIANGLE AREA
      base1 = input("Enter the base of the triangle: ")
      height1 = input("Enter the height of the triangle: ")
      area1 = float(base1) * float(height1) / 2
      print("The result is: " + str(area1))
#2
def addition1():
      print('Running excercise 2 "Introducir dos números por teclado y sumarlos"')
      #ADDITION OF TWO NUMBERS
      print("Enter the first number: ")
      number1 = input()
      print("Enter the second number: ")
      number2 = input()
      number3= float(number1) + float(number2)
      print("The result of the addition is: ", float (number3))
#3
def squared_number():
      print('Running excercise 3 "introducir un número por teclado y visualizar el número elevado al cuadrado"')
      #SQUARED NUMBER
      print("Enter the number: ")
      number1= input()
      square= float(number1)**2
      print("The result of the operation is: ", float(square))
#4
def addition_of():
      print('Running excercise 4 "Imprima por pantalla la suma de 1234 y 532"')
      #ADDITION OF 1234 AND 532
      number1 = int(input("Enter the first number (1234 or 532): "))
      if int(number1) == 1234 or int(number1) == 532:
        #print(int(number1)) 
        number2 = int(input("Enter the second number (1234 or 532): "))
        if int(number2) == 1234 or int(number2) == 532:
          #print(int(number2)) 
          if int(number1) == int(number2):
            #print(int(number1), int(number2))
            print("Both numbers are the same")
          else:
            print("The addition is: ", int(number1)+int(number2))
        else:
          print("You must enter 1234 or 532")  
      else:
        print("You must enter 1234 or 532")  
#5
def subtraction_of():
      print('Running excercise 5 "Imprima por pantalla la resta de 1234 y 532"')
      #SUBTRACTION OF 1234 AND 532
      number1 = int(input("Enter the first number (1234 or 532): "))
      if int(number1) == 1234 or int(number1) == 532:
        #print(int(number1)) 
        number2 = int(input("Enter the second number (1234 or 532): "))
        if int(number2) == 1234 or int(number2) == 532:
          #print(int(number2)) 
          if int(number1) == int(number2):
            #print(int(number1), int(number2))
            print("Both numbers are the same")
          else:
            print("The diference is: ", int(number1)-int(number2))
        else:
          print("You must enter 1234 or 532")   
      else:
        print("You must enter 1234 or 532")    
#6
def multiplication_of():
      print('Running excercise 6 "Imprima por pantalla la multiplicación de 1234 y 532"')
      #MULTIPLICATION OF 1234 AND 532
      number1 = int(input("Enter the first number (1234 or 532): "))
      if int(number1) == 1234 or int(number1) == 532:
        #print(int(number1)) 
        number2 = int(input("Enter the second number (1234 or 532): "))
        if int(number2) == 1234 or int(number2) == 532:
          #print(int(number2)) 
          if int(number1) == int(number2):
            #print(int(number1), int(number2))
            print("Both numbers are the same")
          else:
            print("The result of the multiplication is: ", int(number1)*int(number2))
        else:
          print("You must enter 1234 or 532")    
      else:
        print("You must enter 1234 or 532")    
#7
def division_of():
      print('Running excercise 7 "Imprima por pantalla la división de 1234 entre 532"')
      #DIVISION OF 1234 AND 532
      number1 = int(input("Enter the first number (1234 or 532): "))
      if int(number1) == 1234 or int(number1) == 532:
        #print(int(number1)) 
        number2 = int(input("Enter the second number (1234 or 532): "))
        if int(number2) == 1234 or int(number2) == 532:
          #print(int(number2)) 
          if int(number1) == int(number2):
            #print(int(number1), int(number2))
            print("Both numbers are the same")
          else:
            print("The result of the division is: ", int(number1)/int(number2))
        else:
          print("You must enter 1234 or 532")    
      else:
        print("You must enter 1234 or 532")   
#8
def module_of():
      print('Running excercise 8 "Imprima por pantalla el módulo de 1234 entre 532"')
      #MODULE OF 1234 AND 532
      number1 = int(input("Enter the first number (1234 or 532): "))
      if int(number1) == 1234 or int(number1) == 532:
        #print(int(number1)) 
        number2 = int(input("Enter the second number (1234 or 532): "))
        if int(number2) == 1234 or int(number2) == 532:
          #print(int(number2)) 
          if int(number1) == int(number2):
            #print(int(number1), int(number2))
            print("Both numbers are the same")
          else:
            print("The module is: ", int(number1)%int(number2))
        else:
          print("You must enter 1234 or 532")   
      else:
        print("You must enter 1234 or 532")    
#9
def euro_converter():
      print('Running excercise 9 "Convierta de euros a dólares"')
      #EURO TO DOLLAR CONVERTER
      print("Enter the amount of Euros: ")
      euro_amount= input()
      trm_dollar= 1.10
      dollars= float(euro_amount)*float(trm_dollar)
      print("The amount of Euros equals to: ", float (dollars), " dollars")
#10
def rectangle_area():
      print('Running excercise 10 "Calcule el área de un rectángulo"')
      #TRIANGLE AREA
      width = input("Enter the width of the triangle: ")
      height = input("Enter the height of the triangle: ")
      area = float(width) * float(height)
      print("The result is: " + str(area))
#11
def square_area():
      print('Running excercise 11 "Pida el lado de un cuadrado y muestre el valor del área y del perímetro."')
      #AREA AND PERIMETER OF THE SQUARE
      side = input("Enter the value of one side of the square: ")
      perimeter = float(side) * 4
      area = float(side) * float(side)
      print("The area of the square is: " + str(area))
      print("The perimeter of the square is: " + str(perimeter))
#12
def cylinder_area():
      print('Running excercise 12 "Algoritmo que determine el área y el volumen de un cilindro"')    
      #AREA AND VOLUME OF THE CYLINDER
      #v= (pi*(radio**2))*height
      #a= (2*pi(radio))*height+(2*pi)*(radio**2) ó 2*pi(radio)(height+radio)
      radius = input("Enter the value of the radius of the cylinder: ")
      height = input("Enter the value of the height of the cylinder: ")
      pi= float(3.14159265358979323846)
      volume = (float(pi)* (float(radius)**2))*float(height)
      area = (2*float(pi))*float(radius)*(float(radius)+float(height))
      print("The volume of the cylinder is: " + str(volume))
      print("The area of the cylinder is: " + str(area))
#13
def circumference_area():
      print('Running excercise 13 "Algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma, y el área (Pi*R) ^2 del círculo inscrito"')
      #AREA Y LONGITUD DE LA CIRCUNFERENCIA
      #l= 2*(pi*r)
      #a= pi*(r**2)
      radius = input("Enter the value of the radius of the circumference: ")
      pi= float(3.14159265358979323846)
      length = 2*(float(pi)*float(radius))
      area =float(pi)*(float(radius))**2
      print("The length of the circle is: " + str(length))
      print("The area of the circle is: " + str(area))
#14 
def numbers_average3():
      print('Running excercise 14 "Calcular el promedio de tres números introducidos por teclado"')
      #PROMEDIO DE TRES NUMEROS
      print("Enter the first number: ")
      number1 = input()
      print("Enter the second number: ")
      number2 = input()
      print("Enter the third number: ")
      number3 = input()
      average= (float(number1), float(number2), float(number3))
      mean= sum(average)  / len(average)
      print("The average of the numbers is: ", mean)
#17 (Condicionales)
def positive_negative():
      print('Running excercise 17 "Código para saber si un número es positivo o negativo."')
      #POSITIVO O NEGATIVO
      #Entries
      number = float(input("Enter the number: "))
      #Process and outputs
      if number > 0:
        print(number, " is a positive number")
      elif number < 0:
        print(number, " is a negative number")
      else:
        print(number, " is a neutral number")
#18
def higher_lower2():
      print('Running excercise 18 "Programa que lea dos números del teclado y diga cuál es el mayor y cual el menor."')
      #MAYOR Y MENOR ENTRE 2 NUMEROS
      #Entries
      number1= float(input("Enter the first number: "))
      number2= float(input("Enter the second number: "))
      #Process and outputs
      if number1 > number2:
        print(number1, " is the higher number, and ", number2, "is the lower number")
      elif number1 < number2:
        print(number2, " is the higher number, and ", number1, "is the lower number")
      else:
        print("Both numbers are the same")
#19
def higher_lower3():
      print('Running excercise 19 "Programa que lea tres números enteros positivos, y que calcule e imprima en pantalla el menor y el mayor de todos ellos."')
      #MAYOR Y MENOR ENTRE 3
      #Entries
      number1= float(input("Enter the first number: "))
      number2= float(input("Enter the second number: "))
      number3= float(input("Enter the third number: "))
      #Process and outputs
      if number1 > number2 > number3:
        print(number1, " is the higher number, and ", number3, "is the lower number")
      elif number1 > number3 > number2:
        print(number1, " is the higher number, and ", number2, "is the lower number")
      elif number2 > number1 > number3:
        print(number2, " is the higher number, and ", number3, "is the lower number")
      elif number3 > number1 > number2:
        print(number3, " is the higher number, and ", number2, "is the lower number")
      elif number2 > number3 > number1:
        print(number2, " is the higher number, and ", number1, "is the lower number")
      else:
        print(number3, " is the higher number, and ", number1, "is the lower number")
#20
def worker_salary():
      print('Running excercise 20 "Calcular el sueldo de los empleados de una empresa."')
      #SUELDO
      #Entries
      worker_name= input("Enter the name of the worker: ")
      hours= float(input("Enter time worked in hours: "))
      extra_hours= float(input("Enter the EXTRA time worked in hours: "))
      #Process
      hour= float(4)
      hours*= hour
      extra_hours*= hour*2
      salary= hours+extra_hours
      #Output 
      print(worker_name, "´s salary is ", salary, "dollars")    
#21
def addition_subtraction():
      print('Running excercise 21 "Dados dos números A y B sumarlos si A es menor a B sino restarlos."')
      #SUMAR O RESTAR
      #Entries
      numberA= float(input("Enter the first number: "))
      numberB= float(input("Enter the second number: "))
      #Process and outputs
      if numberA > numberB:
        print("The substraction is: ",numberA-numberB)
      elif numberA < numberB:
        print("The addition is: ", numberA+numberB)
      else:
        print("Both numbers are the same")
#22
def quotient1():
      print('Running excercise 24 "Dadas las longitudes de los tres lados de un triángulo determinar si es equilátero o no."')
      #COCIENTE
      #Entries
      numberA= float(input("Enter the first number: "))
      numberB= float(input("Enter the second number: "))
      #Process and outputs
      if numberA and numberB !=0:
        quotient= numberA/numberB
        print("The qoutient of the division is: ", float(quotient))
      else:
        print("A number can´t be divided by 0, the division cannot be possible")
#23
def var_numDia():
      print('Running excercise 23 "numDia es una variable numérica que puede tomar 7 valores, ellos son 1, 2, 3, 4, 5, 6 o 7. Mostar el nombre el nombre del día de la semana que corresponde al valor de la variable numDia."')
      #Variable numDia
      #Entries
      numDia= float(input("Enter the number of the day of the week to name: "))
      #Process and outputs
      if numDia== 1:
        print("The day of the week is Monday")
      elif numDia== 2:
        print("The day of the week is Tuesday")
      elif numDia== 3:
        print("The day of the week is Wednesday")
      elif numDia== 4:
        print("The day of the week is Thursday")
      elif numDia== 5:
        print("The day of the week is Friday")
      elif numDia== 6:
        print("The day of the week is Saturday")
      elif numDia== 7:
        print("The day of the week is Sunday")
      else:
        numDia<1 or numDia>7
        print('Invalid option menu')
#24
def triangle_type():
      print('Running excercise 24 "Dadas las longitudes de los tres lados de un triángulo determinar si es equilátero o no."')
      #TIPO DE TRIANGULO SEGUN SUS LADOS
      #Entries
      first_side= float(input("Enter the measure of the first side: "))
      second_side= float(input("Enter the measure of the second side: "))
      third_side= float(input("Enter the measure of the third side: "))
      #Process and outputs
      if first_side == second_side and first_side == third_side:
        print("The triangle is equilateral since the measure of all its sides is ", first_side)
      elif first_side == second_side or first_side == third_side:
        print("The triangle is isosceles since the measure of two of its sides is ", first_side)
      elif second_side == third_side:
        print("The triangle is isosceles since the measure of two of its sides is ", second_side)
      elif first_side == 0 or second_side == 0 or third_side == 0:
        print("A triangle cannot have a side with a measure of 0")
      else:
        print("The triangle is scalene since the measure of all its sides is different.")
#25
def addition_multiplication():
      print('Running excercise 25 "Dados dos números A y B sumarlos si al menos uno de ellos es negativo en caso contrario multiplicarlos."')
      #SUMAR O MULTIPLICAR
      #Entries
      numberA= float(input("Enter the first number: "))
      numberB= float(input("Enter the second number: "))
      #Process and outputs
      if numberA < 0 or numberB < 0:
        print("The addition is: ",numberA+numberB)
      else:
        print("The multiplication is: ", numberA*numberB)
#26
def zodiac_sign():
      print('Running excercise 26 "Pidiendo el día y el mes de nacimiento mostrar el signo."')
      #SIGNO ZODIACAL
      #Entries
      month= int(input("Enter the number of your month of birth (1-12): "))
      day= int(input("Enter the day of your birth: "))
      #Process and Outputs
      while month == "":
        print("El mes no se puede dejar vacio")
        month= int(input("Enter a valid number of month (1-12): "))
        continue
        day= int(input("Enter the day of your birth2: "))
        date= int(day)+ "-"+ int(month)
      else: 
        date= str(day) + "-" + str(month)
        while month <= 0  or month >= 13: 
            #se valida si es un mes valido
            month= int(input("Enter a valid number of month (1-12): "))
        else:
          if month == 1:
            if day <= 0  or day > 31:
              day= int(print("Enter a valid date day number: "))
            elif day >= 1 and day <=20:
              print("Your date of birth is ", date, "and your zodiac sign is: ---> CAPRICORN <---") 
            else:
              day >= 21 and day <=31
              print("Your date of birth is ", date, "and your zodiac sign is: ---> AQUARIUS <---")
          elif month == 2:
            if day <= 0  or day > 29: 
              day= int(print("Enter a valid date day number: "))
            elif day >= 1 and day <= 19:
              print("Your date of birth is ", date, "and your zodiac sign is: ---> AQUARIUS <---")
            else:
              day >= 20 and day <= 29
              print("Your date of birth is ", date, "and your zodiac sign is: ---> PISCES <---")
          elif month == 3:
            if day <= 0  or day > 31: 
              day= int(print("Enter a valid date day number: "))
            elif day >= 1 and day <= 20:
              print("Your date of birth is ", date, "and your zodiac sign is: ---> PISCES <---")
            else:
              day >= 21 and day <= 31
              print("Your date of birth is ", date, "and your zodiac sign is: ---> ARIES <---")
          elif month == 4:
            if day <= 0  or day > 30: 
              day= int(print("Enter a valid date day number: "))
            elif day >= 1 and day <= 20:
              print("Your date of birth is ", date, "and your zodiac sign is: ---> ARIES <---")
            else:
              day >= 21 and day <= 30
              print("Your date of birth is ", date, "and your zodiac sign is: ---> TAURUS <---")
          elif month == 5:
            if day <= 0  or day > 31: 
              day= int(print("Enter a valid date day number: "))
            elif day >= 1 and day <= 20:
              print("Your date of birth is ", date, "and your zodiac sign is: ---> TAURUS <---")
            else:
              day >= 21 and day <= 31
              print("Your date of birth is ", date, "and your zodiac sign is: ---> GEMINI <---")
          elif month == 6:
            if day <= 0  or day > 30: 
              day= int(print("Enter a valid date day number: "))
            elif day >= 1 and day <= 20:
              print("Your date of birth is ", date, "and your zodiac sign is: ---> GEMINI <---")
            else:
              day >= 21 and day <= 30
              print("Your date of birth is ", date, "and your zodiac sign is: ---> CANCER <---")
          elif month == 7:
            if day <= 0  or day > 31: 
              day= int(print("Enter a valid date day number: "))
            elif day >= 1 and day <= 22:
              print("Your date of birth is ", date, "and your zodiac sign is: ---> CANCER <---")
            else:
              day >= 23 and day <= 31
              print("Your date of birth is ", date, "and your zodiac sign is: ---> LEO <---")
          elif month == 8:
            if day <= 0  or day > 31: 
              day= int(print("Enter a valid date day number: "))
            elif day >= 1 and day <= 23:
              print("Your date of birth is ", date, "and your zodiac sign is: ---> LEO <---")
            else:
              day >= 24 and day <= 31
              print("Your date of birth is ", date, "and your zodiac sign is: ---> VIRGO <---")
          elif month == 9:
            if day <= 0  or day > 30: 
              day= int(print("Enter a valid date day number: "))
            elif day >= 1 and day <= 22:
              print("Your date of birth is ", date, "and your zodiac sign is: ---> VIRGO <---")
            else:
              day >= 23 and day <= 31
              print("Your date of birth is ", date, "and your zodiac sign is: ---> LIBRA <---")
          elif month == 10:
            if day <= 0  or day > 31: 
              day= int(print("Enter a valid date day number: "))
            elif day >= 1 and day <= 23:
              print("Your date of birth is ", date, "and your zodiac sign is: ---> LIBRA <---")
            else:
              day >= 24 and day <= 31
              print("Your date of birth is ", date, "and your zodiac sign is: ---> SCORPIO <---")
          elif month == 11:
            if day <= 0  or day > 30: 
              day= int(print("Enter a valid date day number: "))
            elif day >= 1 and day <= 22:
              print("Your date of birth is ", date, "and your zodiac sign is: ---> SCORPIO <---")
            else:
              day >= 23 and day <= 31
              print("Your date of birth is ", date, "and your zodiac sign is: ---> SAGITTARIUS <---")
          else: 
            month == 12
            if day <= 0  or day > 31: 
              day= int(print("Enter a valid date day number: "))
            elif day >= 1 and day <= 21:
              print("Your date of birth is ", date, "and your zodiac sign is: ---> SAGITTARIUS <---")
            else:
              day >= 22 and day <= 31
              print("Your date of birth is ", date, "and your zodiac sign is: ---> CAPRICORN <---")
#27
def square_rectangle():
      print('Running excercise 27 "Pidiendo el ingreso de la base y la altura de un cuadrilátero, indicar si es cuadrado o rectángulo. Para cualquiera de los dos casos mostrar el perímetro y el área de la figura."')
      #RECTANGULO O CUADRADO
      base = float(input("Enter the base of the quadrilateral: "))
      height = float(input("Enter the height of the quadrilateral: "))
      area = float(base) * float(height)
      perimeter = (base*2)+(height*2)
      if base == height:
        print("the quadrilateral is a square")
        print('')
        print("the area is ", area, "and the perimeter is ", perimeter)
      elif base == 0 or height == 0:
        print("A quadrilateral cannot have a side that measures 0")
      else:
        base != height
        print("the quadrilateral is a square")
        print('')
        print("the area is ", area, "and the perimeter is ", perimeter)
#28
def sales_discount():
      print('Running excercise 28 "Un negocio hace descuentos en las ventas de sus productos. Si la compra es inferior a $100 el descuento es del 5%, si es mayor o igual a 100 y menor a 200 el descuento es del 10% sino será del 15%. Dado el precio de la venta mostrar el descuento realizado en pesos y el precio final con descuento."')
      #DESCUENTOS DEL NEGOCIO
      #Entries
      sales_value= float(input("Enter the sales value in dollars to apply the discount: "))
      #Process and outputs
      if sales_value > 0 and sales_value <= 100:
        discount1= float((sales_value/100)*5)
        print("The discount made is $", discount1)
        print("The final price is $", sales_value-discount1)
      elif sales_value > 100 and sales_value <= 200:
        discount2= float((sales_value/100)*10)
        print("The discount made is $", discount2)
        print("The final price is $", sales_value-discount2)
      elif sales_value > 200:
        discount3= float((sales_value/100)*15)
        print("The discount made is $", discount3)
        print("The final price is $", sales_value-discount3)
      else:
        sales_value<=0
        print("The value of sales entered does not apply to any discount.")
#29
def leap_year():
      print('Running excercise 29 "Realizar un algoritmo que determine si un año es bisiesto o no lo es."')
      #AÑO BISIESTO
      #Entries
      year = int(input("Enter the year: "))
      #process and Outputs
      if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
       print(str(year), " is a leap year.")
      elif year <=0:
        print("Invalid year")
      else:
        print(str(year) + " isn´t a leap year.")
#30 (Ciclos)
def multiple_of3():
      for multiple in range (3, 100, 3):
        print(multiple)
#31
def odd_number():
      for number in range(1, 100, 2):
        print(number)
#32
def pair_number():
      for number in range(0, 100, 2):
        print(number)
#33
def numbers_3():
      for number in range(1,4):
        print(number)
#34
def numbers_10():
      for number in range(10, 0, -1):
        print(number)
#35
def squared_numbers2():
      for number in range(1, 31):
        print(number**2)
#36
def sum_squaredn():
  sum_of=0
  for number in range(1, 101):
      sum_of += number **2
  print(sum_of)
#37
def sum_nextn():
  number=int(input("Enter the number: "))
  addition=0
  for _ in range(number, (number + 101)):
    addition += _
  print(addition)
#38
def factorial_of():
  number=int(input("Enter the number: "))
  multiplication=1
  for _ in range(1, (number +1)):
    multiplication *= _
  print(multiplication)
#39
def temperature():
  fahrenheit=int(input("Enter the number: "))
  while fahrenheit != 999:
    celsius= 5/9 * (fahrenheit - 32)
    print("The temperature in Celsius is" +str(celsius))
    temperature()
  else: 
    fahrenheit ==999
    print("Thanks, to re-enter run the program again")
#40
def prime_number():
    number=int(input("Enter the number: "))
    for _ in range(2, (number+1)):
        prime = True
        for i in range(2, int((_ ** 0.5)+1)):
            if _ % i == 0:
                prime = False
                break
        if prime:
            print(_)
#41
def multiplication_table():    
      number=int(input("Enter the number: "))
      for _ in range (11):
        print(number, " X ", _, "=", number*_)
#42
def group_average():
      suma = 0; counter = 0
      while True:
        number = int(input("Enter the number: "))
        if number <= 0:
              break
  
        suma += number
        counter += 1
  
      print("The average of the numbers is: ", (suma/counter))
#43
def upward_numbers():
      numberA= int(input("Enter the lowest number: "))
      numberB= int(input("Enter the highest number: "))
      if numberA < numberB:
        for final_number in range (numberA, (numberB+1)):
          print(final_number)
      else: 
        numberA > numberB
        print("The numbers are invalid, you must enter the lowest number first")
        return (upward_numbers())
#44
def dominoes():
      for _ in range(7):
        for i in range(7):
            print(_, ", ", i)
#45 (Listas-Tuplas-Diccinarios)
def sum_list():
  numbers = []
  sum_numbers = 0
  while True:
    numbers.append(int(input("Enter a number: ")))
    control= input("Did you want to add another number? (Yes)(No): ")
    if control.lower() == "no":
      break
  for _ in range(len(numbers)):
    sum_numbers += numbers[_]
  print(sum_numbers) 
#46
def prom_list():
  numbers = []
  prom_numbers = 0
  while True:
    numbers.append(int(input("Enter a number: ")))
    control= input("Did you want to add another number? (Yes)(No): ")
    if control.lower() == "no":
      break
  for _ in range(len(numbers)):
    prom_numbers += numbers[_]
  print(prom_numbers/len(numbers))
#47
def duplicate_list():
  numbers = []
  last = []
  while True:
    numbers.append(int(input("Enter a number: ")))
    control= input("Did you want to add another number? (Yes)(No): ")
    if control.lower() == "no":
      break
  for _ in range(len(numbers)):
    if numbers[_] not in last:
      last.append(numbers[_])
  print(last)
#48
def sortListComplete():
    def sortList(list):
        size = len(list)
        for _ in range(size):
            min = _
            for i in range(_ + 1, size):
                if list[i] < list[min]:
                    min = i
            list[], list[min] = list[min], list[]
    valores = []
    while True:
        valores.append(int(input("Enter valor: ")))
        control = input("Otro (Si)(No): ")
        if control.lower() == "no":
            break
    sortList(valores)
    print(valores)
#49
def longWordComplete():
    def longWord(tupla):
        longW = ''
        maxLong = 0
        for word in tupla:
            long = len(word)
            if long > maxLong:
                maxLong = long
                longW = word
        return longW
    valores = ("Jaime", "Angel", "Nathalia", "Sofia", "Jennifer")
    word = longWord(valores)
    print(word)
#50
def productComplete():
    def product(tupla):
        p = 1
        for _ in tupla:
            p *= _
        return p
    numbers = (2, 3, 4, 5)
    result = product(numbers)
    print(result)
#51
def minMaxComplete():
    def minMax(tupla):
        max = 0
        min = float('inf')
        for _ in tupla:
            if _ > max:
                max = _
            if _ < min:
                min = _
        return max, min
    numbers = (1, 3, 5, 7, 9, 12)
    max, min = minMax(numbers)
    print("Bigger:", max)
    print("Minor:", min)
#52
def iterationsComplete():
    def iterations(tupla):
        iterations = {}
        for _ in tupla:
            if _ in iterations:
                iterations[_] += 1
            else:
                iterations[_] = 1
        return iterations
    tupla = (1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 2, 4, 6, 8)
    dict = iterations(tupla)
    print(dict)
#53
def indicesComplete():
    def indices(tupla, element):
        ind = []
        for _ in range(len(tupla)):
            if tupla[_] == element:
                ind.append(_)
        return ind
    tupla = (2, 5, 4, 7, 8, 5, 1, 5, 3, 5, 5)
    number = 5
    result = indices(tupla, number)
    print(result)
#54
def vowelsComplete():
    def vowels(tupla):
        vowels = ('a', 'e', 'i', 'o', 'u')
        withVowels = []
        withoutVowels = []
        for word in tupla:
            if word[0].lower() in vowels:
                withVowels.append(word)
            else:
                withoutVowels.append(word)
        return tuple(withVowels), tuple(withoutVowels)
    words = ('Hola', 'Mundo', 'Apple', 'Python', 'openai')
    withVowels, withoutVowels = vowels(words)
    print("With vowels:", withVowels)
    print("Without vowels:", withoutVowels)
#55
def counterComplete():
    def counter(list):
        count = {}
        for word in list:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
        return count
    words = input("Enter a space-separated list of words: ").split()
    result = counter(words)
    print(result)
#56
def averageComplete():
    def average(students):
        ratings = 0
        amount = 0
        for _ in students.values():
            ratings += sum(_)
            amount += len(_)
        average = ratings / amount
        return average
    students = {}
    ammountStudents = int(input("Enter the number of students: "))
    for i in range(ammountStudents):
        name = input("Enter the name of student: ")
        ratings = input("Ingrese las calificaciones del estudiante separadas por espacios: ").split()
        ratings = [float(note) for note in ratings]
        students[name] = ratings
    average = average(students)
    print("The average is:", average)
#57
def valorComplete():
    def valor(dict, valor):
        dict2 = {}
        for key, v in dict.items():
            if v == valor:
                dict2[key] = v
        return dict2
    dict = {}
    ammount = int(input("Enter the number of couples: "))
    for i in range(ammount):
        key = input("Enter key: ")
        valor = input("Enter valor: ")
        dict[key] = valor
    search = int(input("Enter number search: "))
    result = valor(dict, search)
    print(result)
#58
def combineComplete():
    def combine(dict1, dict2):
        finalDict = {}
        for key, valor in dict1.items():
            finalDict[key] = valor
        for key, valor in dict2.items():
            if clave in finalDict:
                finalDict[key] += valor
            else:
                finalDict[key] = valor
        return finalDict
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    combine = combine(dict1, dict2)
    print(combine)
#59
def countComplete():
    def count(text):
        words = text.lower().split()
        count = {}
        for _ in words:
            if _ in count:
                count[_] += 1
            else:
                count[_] = 1
        return count
    text = "This is an example of text. This text has repeated words. repeated text"
    result = count(text)
    print(result)

#RUNNING
def menu1():
  menu= int(input("Enter the option to show (1-14 or 17-59): "))
  while menu < 1 and menu > 59 or menu >= 15 and menu <= 16 and menu != 99:
    menu= int(input("Invalid option, enter the option to show (1-14 or 17-59): "))
  else: 
    if menu == 1:
      triangle_area()
      print("")
      return(menu1())
    elif menu == 2:
      addition1()
      print("")
      return(menu1())
    elif menu == 3:
      squared_number()
      print("")
      return(menu1())
    elif menu == 4:
      addition_of()
      print("")
      return(menu1())
    elif menu == 5:
      subtraction_of()
      print("")
      return(menu1())
    elif menu == 6:
      multiplication_of()
      print("")
      return(menu1())
    elif menu == 7:
      division_of()
      print("")
      return(menu1())
    elif menu == 8:
      module_of()
      print("")
      return(menu1())
    elif menu == 9:
      euro_converter()
      print("")
      return(menu1())
    elif menu == 10:
      rectangle_area()
      print("")
      return(menu1())
    elif menu == 11:
      square_area()
      print("")
      return(menu1())
    elif menu == 12:
      cylinder_area()
      print("")
      return(menu1())
    elif menu == 13:
      circumference_area()
      print("")
      return(menu1())
    elif menu == 14:
      numbers_average3() 
      print("")
      return(menu1())
    elif menu == 17:
      positive_negative()
      print("")
      return(menu1())
    elif menu == 18:
      higher_lower2()
      print("")
      return(menu1())
    elif menu ==19:
      higher_lower3()
      print("")
      return(menu1())
    elif menu ==20:
      worker_salary()
      print("")
      return(menu1())
    elif menu ==21:
      addition_subtraction()
      print("")
      return(menu1())
    elif menu ==22:
      quotient1()
      print("")
      return(menu1())
    elif menu == 23:
      var_numDia()
      print("")
      return(menu1())
    elif menu == 24:
      triangle_type()
      print("")
      return(menu1())
    elif menu == 25:
      addition_multiplication()
      print("")
      return(menu1())
    elif menu == 26:
      zodiac_sign()
      print("")
      return(menu1())
    elif menu == 27:
      square_rectangle()
      print("")
      return(menu1())
    elif menu == 28:
      sales_discount()
      print("")
      return(menu1())
    elif menu == 29:
      leap_year()
      print("")
      return(menu1())
    elif menu == 30:
      multiple_of3()
      print("")
      return(menu1())
    elif menu == 31:
      odd_number()
      print("")
      return(menu1())
    elif menu == 32:
      pair_number()
      print("")
      return(menu1())
    elif menu == 33:
      numbers_3()
      print("")
      return(menu1())
    elif menu == 34:
      numbers_10()
      print("")
      return(menu1())
    elif menu == 35:
      squared_numbers2()
      print("")
      return(menu1())
    elif menu == 36:
      sum_squaredn()
      print("")
      return(menu1())
    elif menu == 37:
      sum_nextn()
      print("")
      return(menu1())
    elif menu == 38:
      factorial_of()
      print("")
      return(menu1())
    elif menu == 39:
      temperature()
      print("")
      return(menu1())
    elif menu == 40:
      prime_number()
      print("")
      return(menu1())
    elif menu == 41:
      multiplication_table()
      print("")
      return(menu1())
    elif menu == 42:
      group_average()
      print("")
      return(menu1())
    elif menu == 43:
      upward_numbers()
      print("")
      return(menu1())
    elif menu == 44:
      dominoes()
      print("")
      return(menu1())
    elif menu == 45:
      sum_list()
      print("")
      return(menu1())
    elif menu == 46:
      prom_list()
      print("")
      return(menu1())
    elif menu == 47:
      duplicate_list()
      print("")
      return(menu1())
    elif menu == 48:
      sortListComplete()
      print("")
      return(menu1())
    elif menu == 49:
      longWordComplete()
      print("")
      return(menu1())
    elif menu == 50:
      productComplete()
      print("")
      return(menu1())
    elif menu == 51:
      minMaxComplete()
      print("")
      return(menu1())
    elif menu == 52:
      iterationsComplete()
      print("")
      return(menu1())
    elif menu == 53:
      indicesComplete()
      print("")
      return(menu1())
    elif menu == 54:
      vowelsComplete()
      print("")
      return(menu1())
    elif menu == 55:
      counterComplete()
      print("")
      return(menu1())
    elif menu == 56:
      averageComplete()
      print("")
      return(menu1())
    elif menu == 57:
      valorComplete()
      print("")
      return(menu1())
    elif menu == 58:
      combineComplete()
      print("")
      return(menu1())
    elif menu == 59:
      countComplete()
      print("")
      return(menu1())
      
    else:
      menu == 99 or menu == 0 
      print("Thanks for seeing my exercises, to re-enter, run the program again")
menu1()
