print("This will help you keep track of your hw!")

print("Do you have Bio hw?")
bio = input("Enter y or n: ")
if bio == "y":
    bio = True
elif bio == "n":
    bio = False

print("Do you have Lit hw?")
lit = input("Enter y or n: ")
if lit == "y":
    lit = True
elif lit == "n":
    lit = False

print("Do you have Calc hw?")
calc = input("Enter y or n: ")
if calc == "y":
    calc = True
elif calc == "n":
    calc = False

print("Do you have Java hw?")
java = input("Enter y or n: ")
if java == "y":
    java = True
elif java == "n":
    java = False

print("Do you have APUSH hw?")
apush = input("Enter y or n: ")
if apush == "y":
    apush = True
elif apush == "n":
    apush = False

print("Do you have Spanish hw?")
spanish = input("Enter y or n: ")
if spanish == "y":
    spanish = True
elif spanish == "n":
    spanish = False

print("Bio? ", end="")
print(bio)
print("Lit? ", end="")
print(lit)
print("Calc? ", end="")
print(calc)
print("Java? ", end="")
print(java)
print("APUSH? ", end="")
print(apush)
print("Spanish? ", end="")
print(spanish)

if bio:
    bioHW = input("Enter bio assignment name: ")
    print()
if lit:
    litHW = input("Enter lit assignment name: ")
    print()
if calc:
    calcHW = input("Enter calc assignment name: ")
    print()
if java:
    javaHW = input("Enter java assignment name: ")
    print()
if apush:
    apushHW = input("Enter APUSH assignment name: ")
    print()
if spanish:
    spanishHW = input("Enter spanish assignment name: ")
    print()

if not bio:
    print("You have nothing to do in bio")
else:
    print("In bio you have to do: " + bioHW)

if not lit:
    print("You have nothing to do in lit")
else:
    print("In lit you have to do: " + litHW)
    
if not calc:
    print("You have nothing to do in calc")
else:
    print("In calc you have to do: " + calcHW)

if not java:
    print("You have nothing to do in java")
else:
    print("In java you have to do: " + javaHW)

if not apush:
    print("You have nothing to do in APUSH")
else:
    print("In APUSH you have to do: " + apushHW)

if not spanish:
    print("You have nothing to do in spanish")
else:
    print("In spanish you have to do: " + spanishHW)
