#Create a net worth calculator, based on a free net worth worksheet from Charles Schwab
#https://www.schwabmoneywise.com/public/file/P-4038856/Net-Worth-Worksheet.pdf

#import sys for sys.exit, and re for regular expressions
import sys, re

#Create classes for assets
#Cash and cash equivalents
class CashAndCashEquivalents:
    totalCash = 0.0

    def __init__(self, checkingAccounts, savingsAccounts, moneyMarketAccounts, savingsBonds, CDs, cashValueOfLifeInsurance):
        self.checkingAccounts = checkingAccounts
        self.savingsAccounts = savingsAccounts
        self.moneyMarketAccounts = moneyMarketAccounts
        self.savingsBonds = savingsBonds
        self.CDs = CDs
        self.cashValueOfLifeInsurance = cashValueOfLifeInsurance
        CashAndCashEquivalents.totalCash += checkingAccounts + savingsAccounts + moneyMarketAccounts + savingsBonds + CDs \
                                            + cashValueOfLifeInsurance

    def displayTotal(self):
        print('\nYour total cash and cash equivalent assets amount to', '${:,.2f}'.format(CashAndCashEquivalents.totalCash))

#Invested Assets
class InvestedAssets:
    totalInvestedAssets = 0.0

    def __init__(self, brokerage, other1, IRA, Roth_IRA, fourOhOneK_fourOhThreeB, SEP_IRA, keogh, pension, annuity, \
                realEstate, soleProprietorship, partnership, cCorp, sCorp, limitLiabilityComp, other2):
        self.brokerage = brokerage
        self.other1 = other1
        self.IRA = IRA
        self.Roth_IRA = Roth_IRA
        self.fourOhOneK_fourOhThreeB = fourOhOneK_fourOhThreeB
        self.SEP_IRA = SEP_IRA
        self.keogh = keogh
        self.pension = pension
        self.annuity = annuity
        self.realEstate = realEstate
        self.soleProprietorship = soleProprietorship
        self.partnership = partnership
        self.cCorp = cCorp
        self.sCorp = sCorp
        self.limitLiabilityComp = limitLiabilityComp
        self.other2 = other2
        InvestedAssets.totalInvestedAssets += brokerage + other1 + IRA + Roth_IRA + fourOhOneK_fourOhThreeB + SEP_IRA + keogh + \
                                pension + annuity + realEstate + soleProprietorship + partnership + cCorp + sCorp + \
                                limitLiabilityComp + other2

    def displayTotal(self):
        print('\nYour total invested assets amount to', '${:,.2f}'.format(InvestedAssets.totalInvestedAssets))

#Last assets class will be for 'Use Assets'
class UseAssets:
    totalUseAssets = 0.0

    def __init__(self, principalHome, vacayHome, carsTrucksBoats, homeFurnishings, artAntiquesCoinsCollectibles, \
                jewelryFurs, other3):
        self.principalHome = principalHome
        self.vacayHome = vacayHome
        self.carsTrucksBoats = carsTrucksBoats
        self.homeFurnishings = homeFurnishings
        self.artAntiquesCoinsCollectibles = artAntiquesCoinsCollectibles
        self.jewelryFurs = jewelryFurs
        self.other3 = other3
        UseAssets.totalUseAssets += principalHome + vacayHome + carsTrucksBoats + homeFurnishings + artAntiquesCoinsCollectibles + \
                                jewelryFurs + other3

    def displayTotal(self):
        print('\nYour total use assets amount to', '${:,.2f}'.format(UseAssets.totalUseAssets))

#Define class for current liabilities
class CurrentLiabilities:
    totalCurrentLiabilities = 0.0

    def __init__(self, creditCardBalances, estimatedIncomeTaxOwed, otherBills):
        self.creditCardBalances = creditCardBalances
        self.estimatedIncomeTaxOwed = estimatedIncomeTaxOwed
        self.otherBills = otherBills
        CurrentLiabilities.totalCurrentLiabilities += creditCardBalances + estimatedIncomeTaxOwed + otherBills

    def displayTotal(self):
        print('\nYour total current liabilities amount to', '${:,.2f}'.format(CurrentLiabilities.totalCurrentLiabilities))

#Define class for long-term liabilities
class LongTermLiabilities:
    totalLongTermLiabilities = 0.0

    def __init__(self, homeMortgage, homeEquityLoan, mortgageOnRentalProperty, carLoans, studentLoans, \
                    lifeInsurancePolicyLoans, otherLongTermDebt):
        self.homeMortgage = homeMortgage
        self.homeEquityLoan = homeEquityLoan
        self.mortgageOnRentalProperty = mortgageOnRentalProperty
        self.carLoans = carLoans
        self.studentLoans = studentLoans
        self.lifeInsurancePolicyLoans = lifeInsurancePolicyLoans
        self.otherLongTermDebt = otherLongTermDebt
        LongTermLiabilities.totalLongTermLiabilities += homeMortgage + homeEquityLoan + mortgageOnRentalProperty + carLoans + \
                                        studentLoans + lifeInsurancePolicyLoans + otherLongTermDebt

    def displayTotal(self):
        print('\nYour total long-term liabilities amount to', '${:,.2f}'.format(LongTermLiabilities.totalLongTermLiabilities))

#-----------------------------------------------------------------------------------------------------------------#
def calcAssetsAndLiabilities():
    try:
        #Input cash & cash equivalents amounts and then create cash assets object
        print("\nOkay, here we go!  First, please input the cash and cash equivalent assets you have in each category.\n")
        print("-" * 101 + "\n")
        checkingAccountsInput = float(input("Checking account: $"))
        savingsAccountInput = float(input("Savings account: $"))
        moneyMarketAccountsInput = float(input("Money market accounts: $"))
        savingsBondsInput = float(input("Savings bonds: $"))
        cdsInput = float(input("CDs: $"))
        cashValueOfLifeInsuranceInput = float(input("Life insurance: $"))

        #Create checking assets object
        cashAssetsObject = CashAndCashEquivalents(checkingAccountsInput, savingsAccountInput, moneyMarketAccountsInput, \
                            savingsBondsInput, cdsInput, cashValueOfLifeInsuranceInput)
        cashAssetsObject.displayTotal()

        print("\n" + "-" * 101 + "\n")

        #Next, input totals for invested assets
        print("Great!  Now we'll start accounting for your invested assets.")
        print("The first sub-category is taxable accounts.  This includes brokerage assets as well as any other assets you might have under taxable accounts.\n")
        brokerageInput = float(input("Brokerage: $"))
        other1Input = float(input("Other: $"))
        print("\nThe second sub-category is retirement accounts.  These include things like IRA and Roth IRA accounts.")
        iraInput = float(input("IRA: $"))
        rothIRAInput = float(input("Roth IRA: $"))
        fourOhOneK_fourOhThreeBInput = float(input("401(k) or 403(b): $"))
        sepIRAInput = float(input("SEP-IRA: $"))
        keoghEtAlInput = float(input("Keogh or other qualified plan: $"))
        pensionInput = float(input("Pension (vested benefit): $"))
        annuityInput = float(input("Annuity (accumulated value): $"))
        print("\nAlmost done with assets!  The third and last sub-category is business ownership interests.\n")
        realEstateInput = float(input("Real estate (rental property or land): $"))
        soleProprietorshipInput = float(input("Sole proprietorship: $"))
        partnershipInput = float(input("Partnership: $"))
        cCorpInput = float(input("C-Corporation: $"))
        sCorpInput = float(input("S-Corporation: $"))
        limitLiabilityCompInput = float(input("Limited Liability Company: $"))
        other2Input = float(input("Other: $"))

        #Create invested assets object
        investedAssetsObject = InvestedAssets(brokerageInput, other1Input, iraInput, rothIRAInput, fourOhOneK_fourOhThreeBInput, \
                                sepIRAInput, keoghEtAlInput, pensionInput, annuityInput, realEstateInput, soleProprietorshipInput, \
                                partnershipInput, cCorpInput, sCorpInput, limitLiabilityCompInput, other2Input)
        investedAssetsObject.displayTotal()

        print("\n" + "-" * 101 + "\n")

        #Last category for assets -> 'Use Assets'
        print("Okey dokey, smokey!  Now it's time to tabulate your use assets.")
        print("These are things like your home, a vacation home (if you have one), cars, trucks, boats, home furnishings, jewelry, furs, etc.\n")
        principalHomeInput = float(input("Principal Home: $"))
        vacayHomeInput = float(input("Vacation Home: $"))
        carsTrucksBoatsInput = float(input("Cars, trucks, boats: $"))
        homeFurnishingsInput = float(input("Home furnishings: $"))
        artAntiquesCoinsCollectiblesInput = float(input("Art, antiques, coins, collectibles: $"))
        jewelryFursInput = float(input("Jewelry, furs: $"))
        other3Input = float(input("Other: $"))

        #Create use assets object
        useAssetsObject = UseAssets(principalHomeInput, vacayHomeInput, carsTrucksBoatsInput, homeFurnishingsInput, \
                                    artAntiquesCoinsCollectiblesInput, jewelryFursInput, other3Input)
        useAssetsObject.displayTotal()
        print("\n" + ("-" * 101) + "\n")
        totalAssets = '${:,.2f}'.format(CashAndCashEquivalents.totalCash + InvestedAssets.totalInvestedAssets + UseAssets.totalUseAssets)
        print("Your total assets (sum of cash, invested assets, and use assets) are: $", totalAssets)
        print("\n" + ("-" * 101) + "\n")

        #Okay, now we're done tabulating assets - time to move on to liabilities
        print("Now we'll calculate your liabilities, starting with current liabilities.")
        print("\n" + ("-" * 101) + "\n")
        creditCardBalancesInput = float(input("Credit card balances: $"))
        estimatedIncomeTaxOwedInput = float(input("Estimated income tax owed: $"))
        otherBillsInput = float(input("Other outstanding bills: $"))

        #Create current liabilities object
        currentLiabilitiesObject = CurrentLiabilities(creditCardBalancesInput, estimatedIncomeTaxOwedInput, otherBillsInput)
        currentLiabilitiesObject.displayTotal()

        print("\nLast bit!  Now we'll ask you about your long-term liabilities.")
        print("\n" + ("-" * 101) + "\n")
        homeMortgageInput = float(input("Home mortgage: $"))
        homeEquityLoanInput = float(input("Home equity loan: $"))
        mortgageOnRentalPropertyInput = float(input("Mortgage on rental property: $"))
        carLoansInput = float(input("Car loans: $"))
        studentLoansInput = float(input("Student loans: $"))
        lifeInsurancePolicyLoansInput = float(input("Life insurance policy loans: $"))
        otherLongTermDebtInput = float(input("Other long-term debt: $"))

        #Create long-term liabilities object
        longTermLiabilitiesObject = LongTermLiabilities(homeMortgageInput, homeEquityLoanInput, mortgageOnRentalPropertyInput, \
                                    carLoansInput, studentLoansInput, lifeInsurancePolicyLoansInput, otherLongTermDebtInput)
        longTermLiabilitiesObject.displayTotal()

        print("\n" + ("-" * 101) + "\n")
        totalLiabilities = '${:,.2f}'.format(CurrentLiabilities.totalCurrentLiabilities + LongTermLiabilities.totalLongTermLiabilities)
        print("Your total liabilities (current and long-term) are: ", totalLiabilities)
        print("\n" + ("-" * 101) + "\n")

        #Define a final variable: net worth -> assets - liabilities = net worth
        netWorth = (CashAndCashEquivalents.totalCash + InvestedAssets.totalInvestedAssets + UseAssets.totalUseAssets) - \
                    (CurrentLiabilities.totalCurrentLiabilities + LongTermLiabilities.totalLongTermLiabilities)
        print("Taadah!  Your current net worth is", '${:,.2f}'.format(netWorth), "\n\n")

        #Now give the option to go again
        goAgain = input("Would you like to go again? ")
        while True:
            if goAgain.isalpha() and goAgain.lower() == 'y':
                main()
            elif goAgain.isalpha() and goAgain.lower() == 'n':
                print("Thanks for using my program!")
                sys.exit()
            elif not goAgain.isalpha():
                print("No cheating now!  Enter either 'y' for yes or 'n' for no.")
                continue
            elif goAgain.lower() != r'[yn]':
                print("Aha! Think you can get past my regex, do you?")
                print("Please enter either 'y' for yes or 'n' for no.")
                continue
    except Exception as ex:
        print(ex)

def main():
    try:
        #Title card!
        print("-" * 101)
        print((" " * 40) + "NET WORTH CALCULATOR" + (" " * 25))
        print("-" * 101 + "\n")
        calcAssetsAndLiabilities()
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()
