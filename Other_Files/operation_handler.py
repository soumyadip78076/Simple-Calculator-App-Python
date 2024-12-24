from operations.addition import add
def operation_handle(operation,a,b):
    try:
        a=float(a)
        b=float(b)
    except:
        print("Invalid Input Entered")
    if operation=="+":
        return add(a,b)
    else:
        return "Invalid operation. Please try again."