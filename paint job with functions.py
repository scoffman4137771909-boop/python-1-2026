#functions Paint output
import math

def getFloatInput(sPrompt):
    while True:
        try:
            sInput = input(sPrompt +": ")
            fValue = float(sInput)
            if fValue <=0:
                print(" enter a value above 0.")
                
            else:
                return fValue
        except ValueError:
            print("error : numeric values only!")

            
#calculation functions

def getGallonsofPaint(fSquare_Feet_Wall,fFeet_P_Gallon_Paint):
    #return an interger

    iGallons = math.ceil(fSquare_Feet_Wall / fFeet_P_Gallon_Paint)
    return iGallons

def getLaborHours(fLabors_Hours_P_Gallons, iGallons):

    fTotalHours =fLabors_Hours_P_Gallons * iGallons
    return fTotalHours

def getLaborCost(fTotal_Labor_Hours, fPainting_Hourly_Charge):
    fLaborCost =fTotal_Labor_Hours * fPainting_Hourly_Charge
    return fLaborCost

def getPaintCost(iGallons, fPaint_price):

    fPaintCost = iGallons * fPaint_price
    return fPaintCost

def getSalesTax(sState_of_job):

    sState = sState_of_job.strip().upper()
    if sState == "MA":
        return 0.0625
    elif sState == "CT":
        return 0.06
    elif sState == "ME":
        return 0.085
    elif sState == "NH":
        return 0.0
    elif sState == "RI":
        return 0.07
    elif sState == "VT":
        return 0.06
    else:
        return 0.0


def showCostEstimate(iGallons, fTotal_Labor_Hours, fPaintCost, fLaborCost, fTaxRate, sCustomer_LastName):
    fSubtotal = fPaintCost + fLaborCost
    fTaxAmount = fSubtotal * fTaxRate
    fTotalCost = fSubtotal + fTaxAmount
     
     
    print("Gallons of Paint:")
    print(iGallons)
    print("Hours of Labor")
    print(f"{fTotal_Labor_Hours:,.1f}")
    print(f"Paint Charges: ${fPaintCost:,.2f}")
    print(f"Labor Charges: ${fLaborCost:,.2f}")
    print(f"Tax: ${fTaxAmount:,.2f}")
    print(f"Total Cost: $ {fTotalCost:,.2f}")

    #file output
    sFileName = f"{sCustomer_LastName}_PaintJobOutput.txt"

    with open(sFileName,"w", encoding="utf-8")as file:
        file.write("gallons of paint:\n")
        file.write(f"{iGallons}\n")
        file.write(f"Hours of Labor:\n")
        file.write(f"Paint Charges: ${fPaintCost:,.2f}\n")
        file.write(f"Labor Charges: ${fLaborCost:,.2f}\n")
        file.write(f"Tax: ${fTaxAmount:,.2f}\n")
        file.write(f"Total Cost: ${fTotalCost:,.2f}\n")

    print(f"File {sFileName} was created.")

    
def main():

    fSquare_Feet_Wall = getFloatInput(" enter wall space in sqaree feet")
    fPaint_Price = getFloatInput(" enter paint price per gallon")
    fFeet_P_Gallon_Paint = getFloatInput(" enter feet per gallon")
    fLabor_Hours_P_Gallon= getFloatInput(" how many labor hours per gallon")
    fPainting_Hourly_Charge = getFloatInput(" labor charge per hour")
    
    
    sState_of_job = input("state of job: List all states").strip()
    sCustomer_LastName = input("customer Last Name").strip()
#call fununctions for below
    iGallons = getGallonsofPaint(fSquare_Feet_Wall,fFeet_P_Gallon_Paint)
    fTotal_Labor_Hours = getLaborHours(fLabor_Hours_P_Gallon,iGallons)
    fPaintCost = getPaintCost(iGallons, fPaint_Price)
    fLaborCost = getLaborCost(fTotal_Labor_Hours,fPainting_Hourly_Charge)
    fTaxRate = getSalesTax(sState_of_job)

    showCostEstimate(iGallons,
            fTotal_Labor_Hours,
            fPaintCost,
            fLaborCost,
            fTaxRate,
            sCustomer_LastName)

if __name__ == "__main__":

    main()
        
    
    
    

    
    
    

            
            
                
            
            
