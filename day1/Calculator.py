while True:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        if b==0:
            return "invalid "
        return a/b
    print("Operations\n1.Additon\n2.Subtraction\n3.Multiplication\n4.Divition")
    n1=int(input("ENter the number 1: "))
    opt =int(input("Choose on operation: "))
    n2=int(input("ENter the number 2: "))
    if opt==1:
          print("The addition is",add(n1,n2))
          break
    elif opt==2:
        print("The Subtaction is",sub(n1,n2))
        break
    elif opt==3:
        print("The Multiplication is",mul(n1,n2))
        break
    elif opt==4:
        print("The Division is",div(n1,n2))
        break
    else:
        print("Invalid number")
        
