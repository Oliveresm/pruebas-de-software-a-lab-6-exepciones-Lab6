class MyException(Exception):
    pass


class ExceptionsDemo:
    def divide(self, a, b):
        try:
            result = a / b
            print("Division result:", result)
        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.")
        except TypeError:
            print("Error: los valores deben ser numéricos.")
        except Exception as e:
            print("Error inesperado:", e)

    def access_list(self, lst, index):
        try:
            print("Element:", lst[index])
        except IndexError:
            print("Error: el índice está fuera del rango de la lista.")
        except Exception as e:
            print("Error inesperado:", e)

    def access_dict(self, dic, key):
        try:
            print("Value:", dic[key])
        except KeyError:
            print(f"Error: la clave '{key}' no existe en el diccionario.")
        except Exception as e:
            print("Error inesperado:", e)

    def read_file(self, filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print(f"Error: el archivo '{filename}' no existe.")
        except Exception as e:
            print("Error inesperado:", e)

    def access_attribute(self, obj):
        try:
            print(obj.tnonexistent_attribue)
        except AttributeError:
            print("Error: el objeto no tiene ese atributo.")
        except Exception as e:
            print("Error inesperado:", e)

    def check_positive(self, number):
        try:
            if number < 0:
                raise MyException("The number must be positive.")
            else:
                print("Valid number:", number)
        except MyException as e:
            print("Error:", e)
        except TypeError:
            print("Error: el valor debe ser un número.")
        except Exception as e:
            print("Error inesperado:", e)