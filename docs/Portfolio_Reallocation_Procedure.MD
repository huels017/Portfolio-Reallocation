# Portfolio Reallocation Procedure



## Step 1: Fund Accounts
	
   Accounts to be funded will be funded with cash from ‘Cash on Hand’ accounts. The accounts will be funded until cash in ‘Cash on Hand’ + Minimum cash in other accounts (‘HSA’ Cash min, 3% of CRIA, etc)  reaches the desirable Cash allocation. This many mean not all accounts are funded, in which a message should be added to the report stating that there was not enough cash on hand to fund all accounts. 
	
   There will be an option to fund ‘excess cash’ into the brokerage account. ‘Excess cash’ is the difference between the desired allocation of cash and what is still in the ‘Cash on Hand’ account + Minimum cash in other accounts. All other sources of ‘Cash/MMKT’ will later be reallocated into other categories. 

The order of funding each account is based on user input. 

Rules: 
-If funding +$25k into a brokerage account, it will go into a CRIA account(Active Managed Accts).
-Active Managed Accts: If a Qualified account is above $25k and is with MMLIS or transferring to MMLIS it will be assumed it goes into a CRIA account


These are the account types that can be funded: 

H.S.A
Roth IRA
Roth 401(k)
401(k)
Trad IRA
Non-Ded IRA
SIMPLE IRA
Cash Value
Var. Life
Var. Annuity
Fix Annuity
Brokerage





## Step 2: Reallocate Accounts

   Accounts will be reallocated in order of their tax statues. First Exempt & Deffered(Exp&Def) accounts, then Deffered Only(Def) accounts, and last Non-Qualified accounts. Fixed accounts will not be changed. 

### Rules Types: 
#### Minimum Category Value:
-HSA minimum cash value. Default is $5,000. (Don’t sell assets if not at cash min, only buy assets if about cash min)
-Active Managed Accts/CRIA(institution) has a minimum of 3% cash

#### Category Grouping:
-Crypto Currency counts as a commodity
-Balanced category counts as 50% taxable bonds and 50% large cap blend

#### Category limitations: 
-No Municipal bonds in qualified accounts.
-Crypto Currency category can’t be bought or sold

#### Sales Restrictions:
-Option to cap taxed sales in non-qualified accounts. Default is infinity. Moving cash (and Muni Bonds) in a NQ account does not count against taxed sales.  
-Balanced category is sold first, until Max Taxed Sales value is hit or no more balanced category.




### Reallocate a tax group:
1) Use the ‘Reallocate a Single Account’ procedure to reallocate accounts one at a time.
2) Iterate through the tax group list, reallocating each account. Once every account has been reallocated, start over from the top of the list. 
3) Repeat the iteration process until there are no more sales for a full iteration in a tax group. 
4) Repeat for each tax group. 


### Reallocate a Single Account:
1) Determine which categories should be bought or sold and by how much to reach desired allocation. Assign these values to a buy/sell variable.

2) Determine what rules to apply for the account type, and incorporate them into the buy/sell variable. This includes a reallocation dampening factor. The dampening factor will prevent the account from fully reallocating in one step and must be iteratively reallocated. This will prevent a tax group from concentrating funds in particular categories across the tax group.

3) For all categories that need to be sold, sell the lower of the 'account value for the category' and 'the value needed to be sold to reach desired allocation' from the buy/sell variable. The order of account selling doesn't matter -NQ account may have a max taxed sales variable in play.

4) Add up all sales. This amount will need to be bought in the next steps.	

5) Follow the "Ranking starting with best in tax exempt" category list order to determine which categories to buy first. This will concentrate high growth categories in tax exempt and tax deferred account which gives a better tax benefit. (for NQ accounts, reverse this ranking list) 

6) For a buy category, buy the lower of the 'amount needed to reach desired allocation' and 'the amount needed to be bought to reach the total of all sales'.

7) Iterate through the buy categories using the "Ranking starting with best in tax exempt" list until the total amount sold equals the total amount bought.



	
### Additional Functionality:
   It is yet to be determined if there is a need to implement a desired allocation for each tax group, instead of a single overall allocation. This would also necessitate the creation of an allocation calculator in order to input allocations for each rule group and get the overall allocation as an output. This will help in the determination of the desired allocations per individual group. 











## Step 3: Future Portfolio Projections

   The future state of the portfolio needs to be estimated. This will be done by taking in a estimated yearly return for the overall portfolio, the clients savings rate, and information of financial products that client owns (annuities, life insurance, ext.) 

   The output should be flexible enough to enter in a few different time ranges and scenarios. For example, if 10 year, 20 year, and 20 year end of life were entered. The output should be the predicted portfolio for 10 years into the future, 20 years into the future, and 20 years into the future with the event of the client’s death. 

   The portfolio overall desired allocation should be variable through time. As, the client ages the portfolio allocation should be able to be more conservative per the users input. (not predetermined by the software)
