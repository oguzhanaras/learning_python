# FONKSİYONLARIN ÖZELLİKLERİ

# 1. Fonksiyonlar bir nesnedir (object)
def shout(text: str):
    return text.upper()


print(shout("Hello"))
print(type(shout))

yell = shout
print(type(yell))

id(shout)
id(yell)

yell("Hello")


# 2. Fonksiyonlar başka bir fonksiyona (metoda) argüman olarak geçilebilir.
def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def calculator(a: float, b: float, operation):
    return operation(a, b)


print(calculator(3, 5, add))
print(calculator(3, 5, multiply))

print(list(filter(lambda x: x % 2 == 0, range(20))))


# 3. Bir fonksiyon diğer bir fonksiyonu döndürebilir
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add5 = create_adder(5)  # function factory
print(type(add5))

print(add5(10))

add10 = create_adder(10)
print(add10(10))

add15 = create_adder(15)
add20 = create_adder(25)

create_adder(25)(10)


# 4. Fonksiyon süsleme (decoration)
def make_pretty(func):
    def inner():
        print("I got decorated.")
        print(func())

    return inner


def ordinary():
    return "I am an ordinary function."


print(ordinary())

decorated_function = make_pretty(ordinary)
print(type(decorated_function))
decorated_function()  # calling a function


# 5. @ sembolü ile fonksiyon süslemek

def smart_divide(f):
    def inner(a, b):
        print(f"I am going to divide {a} by {b}")
        if b == 0:
            return "Sorry! Can not divide!"
        return f(a, b)

    return inner


@smart_divide
def divide(a, b):
    return a / b


print(divide(10, 5))
print(divide(10, 0))


#zincirleme decoratorler

def star(f):

    def wrapper(*args, **kwargs):
        print("*" * 15)
        f(*args, **kwargs)
        print("*" * 15)
    return wrapper








def percent(f):

    def wrapper(*args, **kwargs):
        print("%" * 15)
        f(*args, **kwargs)
        print("%" * 15)
    return wrapper


@star
@percent
def printer(text):
    print(text)


printer("hello world")
