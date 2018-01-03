# Portfolio-Reallocation
A tool for financial advisers to streamline portfolio analysis and reallocation recommendations for their clients. 

Minimun Viable Product:
The financial advisers will copy their client accounts and category value data from eMoney and paste it into an excel template. 
They will then navigate to this 'Portfolio_Reallocation' web app and upload their excel file. 
The web app will then run a python program/script which pulls data from the excel file, runs the calculations, and ouputs the results into a new excel file. 
The new excel file will then be sent back to the financial advisor for download. 

Will also need user accounts, login, payment mechanism, and a way to track how many times a user runs the application.
We want to prevent a user from creating and paying for 1 account and letting other users from using their account. 
Possibly put a cap on the number of times per year an advisor can run the application. 
Also would be nice to prevent the user from logining in on more than one computer at once. 

For privacy and security reasons the excel template will not have client identification.  







Teir 2 product:
Later versions will be intergrated with MorningStar, eMoney, and/or other finical applications(possibly banking institutions) in order to stream line the flow of client data and have access to more data. This will allow the program to make better reallocation recommendations. The intergration with financial institutions will nessesitate adaquate security measures to insure client data protection and privacy. 
