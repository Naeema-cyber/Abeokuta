class Student:
    def __init__(self, name, course, level):
        print("Creating a new student...")
        self.name = name
        self.course = course
        self.level = level
        print(f"Student {name} has been created!")


kemi = Student("Kemi Adebayo", "Computer Science", 300)
print(kemi.level)


class NigerianStudent:
    def __init__(self, name, state, course):
        print(f"Step 1: Creating student object...")
        self.name = name
        self.state_of_origin = state
        self.course = course
        self.student_id = self.generate_id()
        print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")


    def generate_id(self):
        import random
        return f"UNISAIL{random.randint(1000, 9999)}"
    


ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statisitcs")

print(ayo.name)
print(ayo.student_id)


class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")

    def buy_airtime(self, amount):
        self.airtime+=amount
        return f"{self.name} now has ₦{self.airtime} airtime"
    


#Creating multple users
abeeb = PhoneUser("Abeeb Bakare", "MTN")
onisemo = PhoneUser("Onisemo Williams", "Airtel")


# Each person's actions affect only their own account
print(abeeb.buy_airtime(500))
print(onisemo.buy_airtime(1000))
print(abeeb.airtime)
print(onisemo.airtime)


class Student:
    def __init__(self, name, course, level, state_of_origin):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0


# Creating a student object
Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State")


# Accessing attributes
print(Fathia.name)
print(Fathia.course)
print(Fathia.state_of_origin)


# 1. Instance Attributes

student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

print(student1.name)
print(student2.name)

# 2. Class Attribute - Shared by all objects of the class.

class Student:
    university = "Federal University of Technology Akure"

    def __init__(self, name, course):
        self.name = name
        self.course = course
print(Student.university)
print(student1.course)
print(student2.level)                            
    

#Methods
class Students:
    def __init__(self, name, course, level):
        #Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False

 
    # Method: Action the student can do
    def pay_school_fees(self):
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"
    
    # Method: another action
    def register_courses(self):
        if self.fees_paid:
            return f"{self.name} has registered  courses for {self.course}"
        else:
            return f"{self.name} must pay school fees first"
    # Method calculates CPGA
    def calculate_cgpa(self, grades):
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        return "No grades provided" 
    

# Using methods
Abiodun = Students("Abiodun Akinola", "Gistologyy", 600)
print(Abiodun.pay_school_fees())
print(Abiodun.register_courses())
print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))


# Types of Methods

#1. Instance methods

# "self" refers to the specific student

def pay_school_fees(self):
    return f"{self.name} has paid school fees"



#2. Class methods- works with class level data

@classmethod
def get_university(cls):
    return cls.university

#3. Static methods - don't need object or class data

@staticmethod
def academic_calender():
    return "Academic session runs from september to July"




class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        #Attributes - what the account has
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()


    # Methods - What the account can do
    def deposit(self, amount):
        """ Add money to the account"""
        if amount > 0:
            self.balance += amount 
            return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
        return "Insufficient funds or Invalid amount"
    
    def transfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
        return "Transfer failed: Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    

    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"01{random.randint(10000000, 99999999)}"
    
    # Creating and using the account
adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 50000)

# Attributes (characteristics)
print(f"Owner: {adunni_account.owner}")
print(f"Bank: {adunni_account.bank_name}")
print(f"Account Number: {adunni_account.account_number}")

# Methods (actions)
print(adunni_account.deposit(25000))
print(adunni_account.withdraw(10000))
print(adunni_account.transfer(15000, "Sunday James"))
print(adunni_account.check_balance())

# Attributes vs Methods

class NaijaPhone:
    def __init__(self,brand,model,network_provider):
        self.brand = brand
        self.model = model
        self.network_provider = network_provider
        self.airtime_balance = 0
        self.data_balance =0
        self.is_on = False


    def power_on(self):
        self.is_on = True
        return f"{self.brand} phone is now on. Network: {self.network_provider}"
    
    def buy_airtime(self, amount):
        self.airtime_balance += amount
        return f"{amount} airtime purchased. Balance: ₦{self.airtime_balance}"
    
    def make_call(self, number):
        if self.is_on and self.airtime_balance > 0:
            self.airtime_balance -= 10
            return f"Calling {number}... Remaining airtime: ₦{self.airtime_balance}"
        return "Cannot make call. Check phone and airtimr balance"
    
    def send_sms(self, message, number):
        if self.airtime_balance >= 4:
            self.airtime_balance -= 4
            return f"SMS sent to {number}: '{message}. Remaining airtime: ₦{self.airtime_balance}"
        return "Insufficient airtime to send SMS"
    

class BRTBus:
    def __init__(self, route, bus_number):

        self.route = route
        self.bus_number = bus_number
        self.current_stop = "Ikorodu"
        self.passenger_count = 0
        self.fare = 300

    def announce_stop(self):
        return f"Next stop: {self.current_stop}. Fare is ₦{self.fare}"
    
    def board_passengers(self, count):
        self.passenger_count += count
        return f"{count} passengers boarded. Total: {self.passenger_count}"
    


class MarketTrader:
    def __init__(self, name, market_name, goods):

        self.name = name
        self.market_name = market_name
        self.goods = goods
        self.daily_sales = 0


    def advertise_goods(self):
        return f"{self.name} at {self.market_name}: Fresh  {', '.join(self.goods)} available!"
    
    def make_sale(self, amount):
        self.daily_sales += amount
        return f"Sale made! Today's total: ₦{self.daily_sales:,}"
    

class NigerianBankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self._balance = initial_balance
        self._pin = "1234"
        self._transaction_history = []


    # Public methods - anyone can use these
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transaction_history.append(f"Depoisited ₦{amount:,}")
            return f"₦{amount:,} deposited successfully"
        return "Invalid deposit amount"
    

    def withdraw(self, amount, pin):
        if self.__verify_pin(pin):
            if amount <= self._balance:
                self._balance -= amount
                self._transaction_history.append(f"Withdrew ₦{amount:,}")
                return f"₦{amount:,} withdrawn successfully"
            return "Insufficient funds"
        return "Invalid PIN"
    

    def check_balance(self, pin):
        if self
    