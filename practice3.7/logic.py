def convert_currency(amount, rate):
    """
    Чиста функція: приймає числа, повертає число.
    Ніяких інтерфейсів, тільки математика.
    """
    try:
        amount = float(amount)
        rate = float(rate)
        
        if amount < 0 or rate < 0:
            return None 
            
        return amount * rate
    except ValueError:
        return None 