print(
    f"Nazwa: Pudzian band\n\
    Rola: SCRUM master\n\
    Github ID: Yibux - Jakub Szewczyk\n\
    Github ID: lilskywalkr\n\
    Jakub Sońta: Jakup27\n\
    Github ID: Aveniss\n\
    Jakub Tutka: JakubTuta"
)
# Klasa do dzielenia dwóch liczb
class ArithmeticsDiv:
    @staticmethod
    def Division(A, B):
        # Sprawdzenie warunku
        if B != 0:
            return A / B
        else:
            # Wyrzucenie błędu
            raise ValueError("Nie można dzielić przez 0")

class ArithmeticsDiff:
    @staticmethod
    def Difference(liczba1, liczba2):
        return liczba1 - liczba2

class IArithmeticMult:
    @staticmethod
    def Multiplication(a, b):
        return a * b

class IArithmeticsAdd:
    @staticmethod
    def Addition(number1,number2):
        return number1+number2

