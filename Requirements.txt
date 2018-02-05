Requirements


Create User Profile: Users should be able to create a username and password. 

Login: Users should be able to use their username and password to access the web app.

Payment: As part of creating a user profile the user is required to pay for their license.

Template Download: The template excel file for client portofilo account information should be available for download.

File Upload: Users should be able to upload their modified excel template file to their profile. 

Run 'Portfolio-Reallocation': Users can initiate the portfolio reallocation program using any of their uploaded excel template 
  files.

Access Reallocation: Users can access the output of the portfolio reallocation program in a report. 
  They can view it through their profile or download the file.
  

####################
Reallocation Program

The reallocation program imports data from the excel template. It will create a instance of an account class for each account in
  the excel template. 
  
The account class will store a $ value for every category, the tax statues/rules of the account, and any special rules TBD...

Tax Statues/rules:
  -Fixed, Taxed, Cash, Exempt & Deffered(Exp&Def), Deffered Only(Def)

Special Rules: 
  -HSA have an cash minimun. $5000 default with option to change minimun.
  -Option to cap the amount of taxed sales. (Max Taxed Sales)
  -Option to fund IRA if yearly minimum has not yet been met. (IRA Funding)
  -Cash - No or minimal cash in Exp&Def, and Def accounts (execpt HSA)
  -Cash in taxed accounts is in it's own rule group.
  
Reallocating Process:  
  -Determine categories that are overweighted or underweighted compared to desired allocation.
  
  -Iterate through each rule group
    -Iterate through each account in the rule group, 
      -Subtract funds in overweighted categories and move subtracted value into underweighted categories. 
       -Use 'Category Priority List' to determine which categories are filled first.
  -Don't move $s between accounts unless special rules require it. 
  
  -Follow this rule group order when reallocating (filling categories): Start with --> Exp&Def, Def, Cash, Taxed <-- End with
  -(Fixed accounts cann't be modified)
  
  -Us a 'Category Priority List' to determine order to fill in underweighted categories. 
      Results in overweight of high growth categories in Exp&Def and Def accounts. 
      Results in low growth categories being overweighted in taxed accounts. 
  -Default 'Category Priority List': High Growth to Low Growth
    ['International', 'Sm/Mid Value', 'Commodities', 'LC Blend', 'Emg Mkts', 'Sm/Mid Blend', 'Sm/Mid Growth', 'LC Value', 
    'Muni Bonds', 'LC Growth', 'REIT', 'Cash/MMKT', 'Tax Bonds', 'Accounts']
  -'Category Priority List' can be modified by user.
  

  
  
  
  
  
  
