class Herramientas:

    def __init__(self, listaa):

        self.listaa = listaa

    def __NumeroPrimo(self, num):
        for i in range(2, num):
            if (num % i == 0):
                return (True)
            break
        else:
            return (False)

    def DevuelveSoloPrimos(self):
        lista2 = []
        for elemento in self.listaa:
            if (self.__NumeroPrimo(int(elemento))):
                lista2.append(elemento)
                return lista2

    def elNuemeroQueMasSeRepite(self):
    
        dicc = {}

        for num in self.listaa:
            clave = str(num)

            if not clave in dicc:
                dicc[clave] = 1
            else:
                dicc[clave] += 1

        a = input('maximo o minimo')

        if (a == 'maximo'):
            dicc.get(clave)
            return 'el maximo valor repetido es', max(dicc, key=dicc.get)
        elif (a == 'minimo'):
            return 'el minimo valor repetido es', min(dicc, key=dicc.get)

    def Temperatura(self, celcius, GradosCambio, Destino):
        if (GradosCambio > 0 and Destino == 'F'):
            return 'Farenheit', round(((celcius* 9/5) + 32), 2)
        elif (GradosCambio > 0 and Destino == str('K')):
            return 'Kelvin', round((celcius + 273.15), 2)

    def Factorial(self):

        if (type(self.listaa) != int):
            return 'no es un numero entero'
        elif (self.listaa < 0):
            return 'no es un numero positivo'
        elif (self.listaa > 0):
            n = 0
            Factorial = 1
            while (n < self.listaa):
                n += 1
                Factorial *= n
            return Factorial