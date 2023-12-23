# Comment like a pro.
# programming  for Policies company to calculate the Policies premium 
# Start Date:2023-12-23; End Date:2023-12-23;
# Author: Shiva(Danny) Biera



# Import required libraries.
import datetime
from datetime import datetime
import FormatValues as FV
import math

# Declare variables.


def read_value(file):
    line = file.readline().strip()
    if not line:
        raise ValueError("Unexpected empty line in defaults.dat")
    return line

try:
    defaults = open("defaults.dat", "r")
except FileNotFoundError:
    print("'defaults.dat' not found")
    exit()

try:
    POLICY_NUM = int(read_value(defaults))
    BAS_PREM = float(read_value(defaults))
    DISC_ADD_CARS = float(read_value(defaults))
    EXLBTY_CRG = float(read_value(defaults))
    GLS_CRG = float(read_value(defaults))
    LNR_CAR = float(read_value(defaults))
    HST = float(read_value(defaults))
    PROS_FEE = float(read_value(defaults))
except ValueError as e:
    print(f"Error reading defaults.dat: {e}")
    exit()

defaults.close()

# Calculate the current date.
Today = datetime.now()
TodayDsp = Today.strftime("%d-%m-%y")



# Open the file with the "r" mode for read.
f = open("Policies.dat", "r")

# Print the header
print ("1234567890123456789012345678901234567890123456789012345678901234567890123")
print()
print("ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTING AS OF {TodayDsp:>10s}")
print()
print()
print("POLICY CUSTOMER               TOTAL                 TOTAL      DOWN       MONTHLY")
print("NUMBER NAME                  PREMIUM       HST      COST      PAYMENT     PAYMENT")
print("=================================================================================")

TotPolCtr = 0
InsPremAcc = 0
HstAcc = 0
TotCostAcc = 0
DownPayAcc = 0
MonthlyAcc = 0

# Set up the loop to process all the records in the file
for PoliciesRecord in f:
    
    # Input - read the first record and split into a list.    
    PoliciesLst = PoliciesRecord.split(",")
    
    
    CutFstName = PoliciesLst[2].strip()
    CutLstName = PoliciesLst[3].strip()
    PolNumber = PoliciesLst[0].strip()
    PolDate = PoliciesLst[1].strip()
    NumCars = PoliciesLst[9].strip()
    NumCars = int(NumCars)
    Liabty = PoliciesLst[10].strip()
    GlscCr = PoliciesLst[11].strip()
    LnrcCr = PoliciesLst[12].strip()
    PmtOpt = PoliciesLst[13].strip()
    DownP = float(PoliciesLst[14])
    CustName = CutFstName + " " + CutLstName
    
    # Calculate required results.
    BasRate = BAS_PREM
    NewDisc = 0
    FnRate = 0
    
    
    if NumCars >1 :
        BasRate = BAS_PREM * NumCars
        NewDisc = BAS_PREM * DISC_ADD_CARS * (NumCars - 1)
        InsPrem =  BasRate - NewDisc    
    else:
        InsPrem = BasRate
    
   
    if Liabty == "Y":
        LiabtyAmt =EXLBTY_CRG
    else:
        LiabtyAmt = 0
        
    if GlscCr == "Y":
        GlscCrAmt = GLS_CRG   
    else:
        GlscCrAmt = 0

    if LnrcCr == "Y":
        LnrcCrAmt = LNR_CAR    
    else:
        LnrcCrAmt = 0
        
    TotExCost = (LiabtyAmt + GlscCrAmt + LnrcCrAmt) * NumCars
    
    

    TotCst = InsPrem + TotExCost
    Hst = TotCst * HST
    Total = TotCst + Hst
    Monthly = (Total - DownP)/ 12

    # Assign variables to each item in the list that are required in the report.
    if PmtOpt == "Monthly" or PmtOpt == "Down Pay":
        print(f"{PolNumber:>5}  {CustName:<20s}{FV.FDollar2(TotCst):>10s} {FV.FDollar2(Hst):>10s} {FV.FDollar2(Total):>10s} {FV.FDollar2(DownP):>10s} {FV.FDollar2(Monthly):>10s}")

        TotPolCtr += 1
        InsPremAcc += InsPrem
        HstAcc += Hst
        TotCostAcc += Total
        DownPayAcc += DownP
        MonthlyAcc += Monthly
        
        
        
        
         
    
f.close()

# Print the footer.
print("=================================================================================")
print(f"TOTAL POLICIES :{TotPolCtr:>2d}         {FV.FDollar2(InsPremAcc):>10s} {FV.FDollar2(HstAcc):>10s} {FV.FDollar2(TotCostAcc):>10s} {FV.FDollar2(DownPayAcc):>10s} {FV.FDollar2(MonthlyAcc):>10s}")
print()
print()

