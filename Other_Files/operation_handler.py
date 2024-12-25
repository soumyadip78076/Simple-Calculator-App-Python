from operations.addition import add
from operations.substruction import sub
from operations.multiplication import multiply
from operations.division import devide
def operation_handle(operation,a,b):
    try:
        a=float(a)
        b=float(b)
    except:
        print("Invalid Input Entered")
    if operation=="+":
        return add(a,b)
    elif operation=="-":
        return sub(a,b)
    elif operation=="*":
        return multiply(a,b)
    elif operation=="/":
        return devide(a,b)
    else:
        return "Invalid operation. Please try again."