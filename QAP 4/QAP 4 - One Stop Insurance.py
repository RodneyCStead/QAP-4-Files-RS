# Program for the One Stop Insurance Company to enter and calculate
# new insurance policy information for its customers.
# Written on: Nov. 17, 2023.
# Written by: Rodney Stead

# Imported libraries
import datetime
from dateutil.relativedelta import relativedelta 
import FormatValues as FV

# Program constants
POLICY_NUMBER            = '1944'   # This is the default policy number
BASIC_PREMIUM_RATE       = 869.00 # This is the basic premium rate
DISC_ADD_CARS            = .25    # There is a 25% discount for additional cars
EXTRA_LIABILITY_RATE     = 130.00 # This is the extra liability coverage rate
GLASS_COVERAGE_RATE      = 86.00  # This is the glass coverage rate
LOAN_CAR_COVERAGE_RATE   = 58.00  # This is the coverage rate for a loaner car
HST_RATE                 = .15    # This is the HST rate, 15%
MONTHLY_PROCESS_FEE_RATE = 39.99  # Monthly processing fee for payments.

# Character sets
NameAllowedChar          = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ,'. abcdefghijklmnopqrstuvwxyz")

# Program functions
def InsurancePremium (NumCars):
    if NumCars == 1:
        return BASIC_PREMIUM_RATE
    if NumCars > 1:
        return BASIC_PREMIUM_RATE + ((BASIC_PREMIUM_RATE - BASIC_PREMIUM_RATE * DISC_ADD_CARS) * (NumCars - 1))

def TotExtraCost (ExtraLiability, GlassCover, LoanCar,):
    ExtraCost = 0
    if ExtraLiability == 'Y':
        ExtraCost += EXTRA_LIABILITY_RATE * NumCars
    else: ExtraLiability == 'N'
    ExtraCost += 0  
    if GlassCover == 'Y':
        ExtraCost +=GLASS_COVERAGE_RATE * NumCars
    else: GlassCover == 'N'
    ExtraCost += 0
    if LoanCar == 'Y':
        ExtraCost += LOAN_CAR_COVERAGE_RATE * NumCars
    else: LoanCar == 'N'
    ExtraCost += 0
    return ExtraCost

def MonthlyPayments (TotCost, DownPay):
# Monthly payments for a 8 month term with or without a down payment.
    MonthlyPay = 0.00
    MonthlyPay = (TotCost - DownPay + MONTHLY_PROCESS_FEE_RATE) / 8
    return MonthlyPay
    


# Program Inputs

while True:

    # Customer name validation
    while True:
        First = input ("Enter customer's first name: ").title()
        if First == "":
                print("First name can't be blank, please re-enter.")
        elif set(First).issubset(NameAllowedChar) == False:
                print("Invalid charcters, please re-enter.")
        else:
            break
    while True:
        Last  = input ("Enter customer's last name: ").title()
        if Last == "":
            print("Last name can't be blank, please re-enter.")
        elif set(Last).issubset(NameAllowedChar) == False:
            print("Invalid charcters, please re-enter.")
        else:
            break
    
    # Street number and name validation
    while True:
        CustStNum = input("Customer Street number: ")
        if CustStNum == "":
            print("Customers street number can't be blank, please re-enter.")
        elif CustStNum.isdigit() == False:
            print("Customer street number must contain numbers only, please re-enter.") 
        else:
            break
    
    while True:
        CustStName = input("Enter Customers street name: ").title()
        if CustStName == "":
            print("Customer Street name can't be blank, please re-enter.")
        elif set(CustStName).issubset(NameAllowedChar) == False:
            print("Customer Street contains invalid charcters, please re-enter.")
        else:
            break
    
    # City validation
    while True:
        City  = input ("Enter customer's city: ").title()
        if City == "":
            print("Last name can't be blank, please re-enter.")
        elif set(City).issubset(NameAllowedChar) == False:
            print("Invalid charcters, please re-enter.")
        else:
            break

    # Province validation
    ValidProvLst = ["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"]
    while True:
        province = input("Enter customer's province: ").upper()
        if province in ValidProvLst:
            break
        else:
            print("Invalid province. Please re-enter.")

    # Postal code validation
    while True:
        CustPost = input("Enter customer postal code (X9X9X9): ").upper()
        if CustPost == "":
            print("Postal code can't be blank, please re-enter.")
        elif len(CustPost) != 6:
            print("Postal code must contain 6 charcters only, please re-enter.")    
        elif CustPost[0].isalpha() == False:
            print("Postal Code must be  entered as: X9X9X9, please re-enter.") 
        elif CustPost[1].isdigit() == False:
            print("Postal Code must be  entered as: X9X9X9, please re-enter.")
        elif CustPost[2].isalpha() == False:
            print("Postal Code must be  entered as: X9X9X9, please re-enter.")
        elif CustPost[3].isdigit() == False:
            print("Postal Code must be  entered as: X9X9X9, please re-enter.")   
        elif CustPost[4].isalpha() == False:
            print("Postal Code must be  entered as: X9X9X9, please re-enter.")
        elif CustPost[5].isdigit() == False:
            print("Postal Code must be  entered as: X9X9X9, please re-enter.")
        else:
            break
    
    # Phone number validation
    while True:
        PhoneNum = input("Enter customer's phone number (1112223333): ")
        if len(PhoneNum) != 10:
            print("Invalid phone number. Please re-enter.")
        elif PhoneNum.isdigit() == False:
            print("Invalid phone number. Please re-enter.")
        else:
            break
    
    # Validate number of cars
    while True:
        try:
            NumCars  = int(input("Enter number of cars being insured no more than 100: "))
        except:
            print("Invalid input. Please enter a number.")
        else:    
            if NumCars > 100:
                print("Invalid input. Must be less than 100, please-re-enter.")
            elif NumCars < 1:
                print("Invalid input. Number of cars must be at least 1, please-re-enter.")    
            else:
                break
    # Validate extra liability
    while True:
        ExtraLiability = input("Extra liability up to $1,000,000 (Y for Yes or N for No): ").upper()
        if ExtraLiability != 'Y' and ExtraLiability != 'N':
            print("Invalid input. Please re-enter Y for yes or N for no.")
        else:
            break
    
    # Validate glass coverage
    while True:
        GlassCover = input("Optional glass coverage (Y for Yes or N for No): ").upper()
        if GlassCover != 'Y' and GlassCover != 'N':
            print("Invalid input. Please re-enter Y for yes or N for no.")
        else:
            break
            
    
    # Validate loaner car option
    while True:
        LoanCar = input("Optional loaner car (Y for Yes or N for No): ").upper()
        if LoanCar != 'Y' and LoanCar != 'N':
            print("Invalid input. Please re-enter Y for yes or N for no.")
        else:
            break
    
    # Validate payment method
    ValidPayMethLst = ["Full", "Monthly", "Down Pay"]
    while True:
        PayMeth = input("Enter payment method (Full, Monthly, Down Pay): ").title()
        if PayMeth in ValidPayMethLst:
            break
        else:
            print("Invalid payment method. Please enter Full, Monthly, or Down Pay.")
    
    DownPay = 0
    if PayMeth == "Down Pay":
        DownPay = float(input("Enter the amount of the down payment: "))
    
    # Previous claim Dates and Costs for list of claims
    ClaimDateLst = []
    ClaimCostLst = []
    
    while True:
        ClaimDate = input("Enter the date of a previous claim (YYYY-MM-DD)(press  Enter (Return key on Mac) to finish): ")
        if ClaimDate == "":
            break
        try:
            ClaimDate = datetime.datetime.strptime(ClaimDate, "%Y-%m-%d")
            if ClaimDate > datetime.datetime.now():
                print("Claim date cannot be greater than todays date, please re-enter.")
                continue
        except ValueError:
            print("Invalid date. Please re-enter.")
            continue
        while True:
            try:
                ClaimCost = float(input("Enter the cost of the claim: "))
                if ClaimCost < 0:
                    print("Claim cost cannot be less than 0. Please re-enter.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        ClaimDateLst.append(ClaimDate)
        ClaimCostLst.append(ClaimCost)
                
    Continue = input("Do you want to enter another customer (Y for Yes or N for No)? ").upper()
    if  Continue == 'N':
        break

# Program calculations

# Extra Charges
Liability = 0
if ExtraLiability == 'Y':
    Liability = EXTRA_LIABILITY_RATE * NumCars
Glass = 0
if GlassCover == 'Y':
    Glass = GLASS_COVERAGE_RATE * NumCars
Loaner = 0
if LoanCar == 'Y':
    Loaner = LOAN_CAR_COVERAGE_RATE * NumCars

ExtraCost = TotExtraCost(ExtraLiability, GlassCover, LoanCar)

# Insurance Premium and Subtotal + Total
InsurPrem = InsurancePremium(NumCars)
TotInsurPrem = InsurPrem + ExtraCost
Hst = TotInsurPrem * HST_RATE
TotCost = TotInsurPrem + Hst

# Monthly Payments
MonthlyPay = MonthlyPayments(TotCost, DownPay)

# Full Payment
FullPay = TotCost - DownPay

# Customer Name & Street Address
FullName = First + " " + Last
StreetAdd = CustStNum + " " + CustStName 

# Current Date and First Payment Date
CurDate = datetime.date.today()
if CurDate.month == 12:
    FirstPayDate = CurDate.replace(year=CurDate.year+1, month=1, day=1)
else:
    FirstPayDate = CurDate.replace(month=CurDate.month+1, day=1)
InvDate = CurDate.strftime("%Y-%m-%d")
FirstPayDateDsp = FirstPayDate.strftime("%Y-%m-%d")

# Bonus expected last payment date, 8 months from first payment date
# Something extra I looked up and wanted to try.
EightMonths = CurDate + relativedelta(months=+8)
LastPayDate = EightMonths.replace(day=1)


# Program print out

print (u'\u2500' * 62)
print (f" One Stop Insurance Company")
print (f" ")
print (f" Customer Invoice ")
print (f"")
print (f" Policy Number: {POLICY_NUMBER:<4s}  # of Cars: {FV.Paddeing3(NumCars):<3}  Invoice Date: {FV.FDateS(CurDate):>10s}")
print ("-" * 62)
print (f" Customer Information")
print (f"")
print (f" Full Name: {FullName:<40s}")
print (f" City: {City:<20s}           Payment method: {PayMeth:<8s}")
print (f" Province: {province:<2s}                         Phone Number: {PhoneNum:<10s}")
print (f" Street Address: {StreetAdd:<25s} Postal Code: {CustPost:<6s}")
print ("-" * 62)
print (f" Extra Charges                                      | Cost |")
print ("-" * 62)
print (f" Extra Liability:                                   {FV.FDollar2(Liability):>10s}")
print (f" Glass Coverage:                                    {FV.FDollar2(Glass):>10s}")
print (f" Loaner Car:                                        {FV.FDollar2(Loaner):>10s}")
print (f" Total Extra Charges:                               {FV.FDollar2(ExtraCost):>10s}")
print ("-" * 62)
print (f" List of Charges                                    | Cost |")
print ("-" * 62)
print (f" Insurance Premium:                                 {FV.FDollar2(InsurPrem):>10s}")
print (f" Total Insurance Premium:                           {FV.FDollar2(TotInsurPrem):>10s}")
print (f" Tax:                                               {FV.FDollar2(Hst):>10s}")
print (f" Total Cost:                                        {FV.FDollar2(TotCost):>10s}")
print (f"")
print (f" *** Full AND Monthly Payments Have Any Down ***")
print (f" *** Payment Made subtracted If Applicable   ***")
print ("-" * 62)
print (f" Cost If Paid in Full:                              {FV.FDollar2(FullPay):>10s}")
print (f" Monthly Payments (8 Month Term):                   {FV.FDollar2(MonthlyPay):>10s}")
print ("-" * 62)
print (f" ***      Payments for monthly Customers Are Due      ***")
print (f" ***           On the First of Each Month.            ***")
print (f" *** Customers Who Pay In full have till the Due Date ***")
print (f"")
print (f"  First Payment Due Date:                           {FirstPayDateDsp:>10s}")
print (f"  Expected Last Payment Date (If Paying Monthly):   {FV.FDateS(LastPayDate):>10s}")
print ("-" * 62)
print (f" List of Previous Claims")
print (f" Claim #  Claim Date        Amount")
print (f" ---------------------------------")
for i in range(3):
    try:
        ClaimDateLstDsp = FV.FDateS(ClaimDateLst[i])
        ClaimCostLstDsp = FV.FDollar2(ClaimCostLst[i])
    except IndexError:
        ClaimDateLstDsp = "N/A"
        ClaimCostLstDsp = "N/A"
        
    print (f"   {i+1}.      {ClaimDateLstDsp:<10s}   {ClaimCostLstDsp:>10s}")
print (f" ---------------------------------")
print (u'\u2500' * 62)
print (f"")