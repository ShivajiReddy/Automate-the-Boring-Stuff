def div42by(x):
    try:
        return 42/x
    except:
        print('Error: You tried to divide by zero')
        
print(div42by(2))
print(div42by(0))
