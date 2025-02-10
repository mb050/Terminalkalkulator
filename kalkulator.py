from math import sin, cos, tan, log, log10, sqrt, pi, prod 
from sys import exit

# tupler som blir kalt på underveis i enten en eller flere funksjoner.
advanced_func = ('sqrt', 'sin', 'cos', 'tan', 'log', 'log10', 'fact')
operator_list = ('add', 'sub', 'mul', 'div', 'perc') + advanced_func
break_list = ('stop', 'cancel', 'break', 'quit')
char = ('*', '(', ')')

def help_func():
    print('\nchoose one of the possible operations by writing the '
          'shortened version:\nadd, sub, mul, div, sqrt, perc, sin, cos, '
          'tan, log, log10, fact\n\n'
          'First number given is represented as x, '
          'Second number is represented as y\n'
          'Example: add 1 2 --> 1 + 2 = 3\n'
          '\n\tvalid operators:'
          '\n\tsub --> subtraction'
          '\n\tadd --> addition'
          '\n\tmul --> multiplication'
          '\n\tdiv --> division'
          '\n\tsqrt --> square root of first number'
          '\n\tperc --> percentage:'
          '\n\t\t example: x% of y --> 5% of 100 = 5\n'
          '\n\tsin --> sine of x, x is given in radians'
          '\n\tcos --> cosine of x, x is given in radians'
          '\n\ttan --> tangent of x, x is given in radians'
          '\n\tlog --> base e logarithm of x'
          '\n\tlog10sin --> base 10 logarithm of x'
          '\n\tfact --> the factorial of x, or simply x!'
          '\n\nEnter a valid operator:', end=' ')

def cancel_func(custom=''):
    """
    mulighet til å legge inn spsifikk melding, i tillegg til å printe ut en 
    beskjed om at kalkuleringen ble avbrutt.
    """
    
    print(custom + 'Type "cancel" to stop the current calculation:', end=' ')
    return             

def get_valid_operator():
    """
    Ser om den matematiske operasjonen som brukeren ønsker er tilgjengelig,
    og om brukeren har skrevet det riktig. korrigerer potensielle feil og 
    returnerer en string som styrer hvilken operator som skal brukes av koden.
    
    funksjonen informerer om hvordan de ulike operatorene skal skriver, og
    kan gi mer informasjon dersom 'help' blir brukt.
    
    returns:
        str: en forkortet versjon av operatoren som skal brukes videre.
    """
    
    message = '\nRequested operator is not available, type a valid operator.\n'
    print('Mathematical operation to use:')
    for i in operator_list:
        print(i, end=', ')
    print('help: ', end='')
    
    operator = input().lower()
    while not(operator in operator_list):
        if operator in break_list:
            print('\nNo valid operation given, canceling current calculation')
            exit()
        if operator == 'help':
            help_func()
            operator = input().lower()
        else:
            cancel_func(message)
            operator = input().lower()
    return operator 


def replace_characters(removal, char_tuple=char):
    """
    Tar inn en string og fjerner tilsvarende tegn som er i char_tuple.
    ser etter om 'pi' er innkludert og vil legge det til etter at tallene
    i 'removal' multipliseres sammen.

    ved utvidelse så er det her man kan legge inn for filtrering av andre 
    tegn og bokstaver som har spesifikk verdi, slik som tallet e.
    
    args:
        removal (str): verdi som skal behandles.
        char_tuple (tuple): mulighet til å endres på ved behov.

    Returns:
        (float), dersom argumentet er gyldig, (str) hvis det ikke er gyldig.
    """
    
    pi_factor = 1
    for i in char_tuple:
        removal = removal.replace(i, ' ')
    
    if 'pi' in removal:
        removal = removal.replace('pi', '')
        pi_factor *= pi
    
    try:
        removal = prod(map(float, removal.split()))
        removal *= pi_factor
    except:
        pass
    
    return removal

def check_number_advanced(x):
    """
    tar inn x, ser om det inneholder brøktegn. splitter til teller og nevner
    hvis det inneholder brøktegn. 
    
    args:
        x (str): verdi som skal gjøres om til (float).
    
    returns:
        (float), dersom argumentet er gyldig, (str) hvis det ikke er gyldig.
    """
    
    if '/' in x:
        idx = x.find('/')
        if idx == 0 or idx == len(x) - 1:
            return ''
        else:
            numerator = replace_characters(x[:idx])
            denominator = replace_characters(x[idx + 1:])
            try:
                numerator = float(numerator)
                denominator = float(denominator)
            except:
                return ''
            return numerator / denominator
    return replace_characters(x)


def check_number(x):
    """
    tar inn x (str) og gjør den om til en (float).
    
    args:
        x (str): verdien som skal gjøres om til float.

    returns:
        float: returnerer x av type float.
    """
        
    message = '\nNot a valid input, enter a new number.\n'
    while not(isinstance(x, float)):
        try:
            x = float(check_number_advanced(x))
        except:
            if x.lower() in break_list:
                exit()
            
            cancel_func(message)
            x = input()            
    return x

def get_numbers(operator):
    """
    henter to tall fra brukeren, og returnerer en liste med de to tallene.
    
    vil bare spørre om et tall dersom utregningen som er ønsket ikke 
    krever mer enn et tall.
    
    args:
        operator (str): hvilken operator som skal brukes.
        
    returns:
        list: en liste med 2 elementer.
    """
    
    num = [0] * 2
    for i in range(2):
        print('\nEnter a number: ', end='')
        num[i] = check_number(input())
        if operator in advanced_func:
            break
    return num
    
    
def subtraction(x, y):
    return x - y
    
def check_division(y):
    """
    ser om verdien i nevneren er 0, og vil si ifra og be om å avbryte 
    kalkulasjonen eller å endre verdien.
    
    args:
        y (float): verdien til nevneren i divisjonen.
    
    returns:
        float: korrigert verdi.
    """ 
    
    message = '\nCannot divide by 0.\nEnter a new value for y.\n'       
    try:
        1 / y
    except:
        cancel_func(message)
              
        y = input()
        if y.lower() in break_list:
            raise 
        return check_number(y)

def division(x, y):
    """
    utfører divisjon, og sjekker om verdi for nevner er lik 0.
    
    args:
        x (float): verdi for teller.
        y (float): verdi for nevner.
    """
    
    if y == 0:
        while y == 0 or not(isinstance(y, float)):
            y = check_division(y)            
        num[1] = y
    return x / y

def squareroot(x):
    """
    utfører kvadratrot, og sjekker om x ikke er negativt.
    
    returns:
        (str) dersom x er negativt, og (float) dersom x er mer eller lik 0.
    """
    
    if x < 0:
        print (f'No real roots for sqrt of {x}')
        exit() 
    else:
        return sqrt(x)

def calculate_tan(x):
    """
    utfører utregning for tangent av x.
    
    funksjonen vil kalkulere om x har en udefinert verdi, og vil returnere
    'undefined' dersom dette er tilfelle.
    
    args:
        x (float): tolket som radianer.
        
    returns:
        (float) som standard, (str) dersom x er udefinert.
    """
    
    simplified = x * (2 / pi) 
    if simplified % 2 == 1:
        return 'Undefined'
    else:
        return round(tan(x), 15)
    
def calculate_log(x):
    # ser om x kan kalkuleres
    if x <= 0:
        return 'Undefined'
    else:
        return log(x)

def calculate_log10(x):
    # ser om x kan kalkuleres
    if x <= 0:
        return 'Undefined'
    else:
        return log10(x)

def factorial(x):
    """
    utfører utregning for fakultet av x.
    
    funksjonen vil sjekker om x er et helt tall, (int), før den utfører
    utregningen. vil enten be om ny verdi, eller å avslutte utregningen 
    dersom det ikke er et helt tall.
        
    returns:
        int: fakultet av x.
    """
    
    message = '\nGiven number must be a positiv integer greater than 0.\n'
    while x % 1 != 0 or x <= 0:
        if x in break_list:
            print('Canceling current calculation')
            exit()
        if x == 'help':
            help_func()
        
        cancel_func(message)
        x = input().lower()
        x = check_number(x)
    
    x = int(x)
    num[0] = x
    return prod(range(1, x + 1))

def get_result(operator, num):
    """
    tar inn operator og verdiene som skal brukes og returnerer resultatet.
    
    note! kan erstatte if statements med en dictionary som inneholder 
    operator som keys, og utregningen som verdi. fungerer dersom 
    kalkulatoren ikke er for omfattende.
    
    args:
        operator (str): bestemmer den matematiske operatoren som skel brukes
        num (list): liste med 2 elementer.
        
    returns:
        None, resultatet blir printet ut.
    """
    
    x = num[0]
    if operator == 'add':
        result = sum(num)
    elif operator == 'sub':
        result = subtraction(*num)
    elif operator == 'mul':
        result = prod(num)
    elif operator == 'div':
        result = division(*num)
    elif operator == 'sin':
        result = round(sin(x), 15)
    elif operator == 'cos':
        result = round(cos(x), 15)
    elif operator == 'tan':
        result = calculate_tan(x)
    elif operator == 'log':
        result = calculate_log(x)
    elif operator == 'perc':
        result = prod(num) * 1e-2
    elif operator == 'sqrt':
        result = squareroot(x)
    elif operator == 'log10':
        result = calculate_log10(x)
    elif operator == 'fact':
        result = factorial(x)
        
    if operator in advanced_func:
        end_str = '{} of {} ='.format(operator, num[0])  
    else:
        end_str = '{} {} {} ='.format(num[0], operator, num[1])    
    
    output_str = "\n{} {} ".format(end_str, result)
    if operator == 'sqrt':
        output_str += f'V -{result}'
    print(output_str)
    return

if __name__ == '__main__':
    operator = get_valid_operator()
    num = get_numbers(operator)
    get_result(operator, num)
