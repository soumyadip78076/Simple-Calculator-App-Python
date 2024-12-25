def devide(a, b):
    try:
        return float(a) / float(b)
    except ValueError:
        return "Invalid input. Please enter numbers only."
