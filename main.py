def multi_converter():
    print("Welcome to Multi Converter: ")
    while True:
        print("\n1.Lenght Converter. \n2.Currency Converter. \n3.Temprature Converter. \n4.Exit.")
        choice = int(input("Enter your choice: "))

        if choice == 1:
           Lenght_conevrter()
        elif choice == 2:
            Currency_Converter()
        elif choice == 3:
            Temprature_Converter()
        elif choice == 4:
             print("Exiting the Multi Converter!")
             break
        else:
            print("Invaild Choice!")

def Lenght_conevrter():
            print("\nLenght Converter.")
            print("\n1.meter to feet. \n2.feet to meter")
            choice = int(input("Enter your choice:"))

            if choice == 1:
                 print("Conversion for meter to feet.")
                 #here a is the value that user want to conv to feet. 
                 meter = float(input("Enter the Value: "))
                 feet = meter * 3.28
                 print(f"{meter} meters is equale to {feet} feets.")

            elif choice == 2:
                 print("feet to meter.")
                 feet = float(input("Enter the value:"))
                 meter = feet / 3.28
                 print(f"{feet} feets is equal to {meter} meters.")


def Currency_Converter():
        print("\nCurrency Converter.")
        print("\n1.IND to USD. \n2.USD to IND.")
        choice = int(input("Enter your Choice: "))
            
        if choice == 1:
             print("conversion IND to USD.")
             IND = float(input("Enter the Amount: "))
             USD = IND / 88
             print(f"{IND} IND is equal to {USD} USD.")

        elif choice == 2:
             print("Conversion USD to IND.")
             USD = float(input("Enter Amount: "))
             IND = USD * 88
             print(f"{USD} USD is equal to {IND} IND.")

             
def Temprature_Converter():
     print("\nTemprature_converter.")
     print("\n1 Celcuis to Fehrenheit. \n2.Fehrenheit to Celcius.")
     choice = int(input("Enter your Choice: "))

     if choice == 1:
        print("Conversion C to Fe")  
        C = float(input("Enter the temp: "))
        Fe = (C * 1.8 )+32
        print(f"{C} C is equal to {Fe} Fe.")    

     elif choice == 2:
          print("Conversion Fe to C.")
          Fe = float(input("Enter the temp: "))
          C = (Fe - 32) / 1.8
          print(f"{Fe} Fe is equal to {C} C.")        

        

multi_converter()