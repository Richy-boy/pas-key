# importing the "random module" 
import random

# container for tool description
tool_Description = """

 #########            ##@@@@                  $$$$$$$$                             ****          #@*#
###      $$$         ##    \{\              $$$      $$$                           ####        $$$$
###      $$$        ##      \{\            $$$$                                    ###3      ##$
###      $$        ##$$$$$$$ \{\            $$$$                                   ###3    %$$$
########          ## $$$$$$$$$\}\              $$$$4           *%63&5&###*****     $$$$####%$^
### $$$          ##            \{\                   $$$$      **^67%*&0&&###*     $$$%#$$$&$#
###             ##              \{\                    ###                         $$$$      %^&*
###            ##                \{\        ####       #3##                        $4$$        ###
###           ##                  \}\        ####      ###)                        $###          ####
###          ##                    \{\         #########                           #&&#             #$%&

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
 PAS-K  (Pas-key ) :                version 1.0  (2025)
 Password generator tool \n \n """

 
# menu section container
menu =""" 
****************************************************
-h            help  
--help        help (similar long-form)
-g            get new password 
--generate    get new password(similar long-form )
 man          manual guide  information about the tool 
 **************************************************
  \n"""

#container for instructs
instruct=""" 
************************
Try the above commands
************************ """





 # container for all manual information 
info = """
   General commands manual      PAS-K  (Pas-key )      version 1.0 
Description \n
Is a simple tool that will help you  to create new unique password .
Also combines  , It enables to get strong password with combination of all characters, numeric, alpha-numeric,letters 
      
      
             Commands \n
-h              help  
--help          help (similar long-form)
- g             get new password 
--generate      get new password(similar long-form )
man             manual guide  information about the tool \n\n

AUTHOR \n
Richard J Fute \n
Email(richyrjrj@gmail.com)

            This manual page was written by Richard Fute   (it can be used by others)

                    23/06/2025                        Pas-k   version 1.0
"""

# container for help commands

info2 = """ 
              
              Commands  \n

-h            help  
--help        help (similar long-form)
-g            get new password 
--generate    get new password(similar long-form )
man           manual guide  information about the tool \n
"""

print (tool_Description)                            # display description
input(("Press enter to continue :"))     #prompt input to continue
print( menu,instruct)                               #display for menu and instruct contents

enter2 = (input(""))            # input  prompt for used commands 



# password generating code snippet
 # defining 
early = "0123456789"                          # defining the numbers
list1= "abcdefghijklmnopqrstuvxyz"            # defining the alphabets & small letters
list2= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"           
list3=  "#$%&*+@=!/>-#$&!"                          # defining  characters 

#concenating  them in collect variable
collect = list1 + list2 + list3 + early
out = random.choices(collect,k=8)            # using "random.choices" function , using collect variable and k password size is 8
 
#decision methods for commands
if "-h"  in enter2:
       print(info2)
elif "--help" in enter2:
       print(info2)
elif  "-g" in enter2 :
       print("\n Already  Created below !!!!    (copy it) \n-----------------\n",*out,"\n ----------------")   # Display for the results    
       print ("\n If you don't like this password , you can repeat the process again ")          
elif  "--Generate" in  enter2:
       print("\n Already  Created  below !!!!!  (copy it) \n*******************\n",*out,"\n******************")
       print ("\n If you don't like this password , you can repeat the process again ") 
elif "man " in enter2:
       print(info)
else:
       print("\n unknown command , try something like:   | -h |--help | -g  |--Generate | " )

  






 


















