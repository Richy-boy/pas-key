#!/bin/bash
# =============================================================================
# PAS-K (Pas-key) - Password Generator Tool
# Version: 1.4 (2026)
# Author: Richard J fute
# Company: EgoClavis Labs
# Description: Simple yet secure readable password generator for Linux
# Website: egoclavislabs.github.io 
# License: MIT
# =============================================================================

VERSION="1.0 (2026)"

# ASCII Art Header


echo "#########                ##@@@@                       $$$$$$$                                     ****           #@*#"
echo "###    $$$              ##   \{\                     $$$     $$$                                  ####          $$$$"
echo "###    $$$            ##      \{\                  $$$$                                           ###3        ##$"
echo "###    $$            ##$$$$$$$ \{\                  $$$$                                          ###3     %$$$"
echo "########           ##  $$$$$$$$ \}\                   $$$$4            *%63&5&###*****            $$$$####%$^"
echo "### $$$           ##             \{\                      $$$$           **^67%*&0&&###*          $$$%#$$$&$#"
echo "###              ##               \{\                          ###                                $$$$      %^&*"
echo "###             ##                 \{\              ####      #3##                                $4$$       ###"
echo "###            ##                   \}\              ####      ###)                               $###         ####"
echo "###           ##                     \{\                #########                                 #&&#            #$%&"
echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo
echo " PAS-K (Pas-key) : version $VERSION"
echo " Password generator tool by EgoClavis Labs"
echo "Press enter to continue :"
read -r

# Menu
echo "****************************************************"
echo "-h     help"
echo "--help help (similar long-form)"
echo "-g     get new password"
echo "--generate get new password (similar long-form)"
echo " man    manual guide information about the tool"
echo "**************************************************"
echo
echo "************************"
echo "Try the above commands"
echo "************************"

# Function to generate password
generate_password() {
    # Simple readable password: Capital + symbol + lowercase + number pattern
    # You can improve this later with /dev/urandom or pwgen if installed
    words=("M" "y" "N" "y" "e" "k" "a" "B" "r" "o" "T" "h" "e" "r" "S" "i" "s")
    symbols=("!" "@" "#" "$" "%" "^" "&" "*")
    
    pass=""
    for i in {1..8}; do
        case $((i % 4)) in
            0) pass+="${words[$RANDOM % ${#words[@]}]}" ;;
            1) pass+="${symbols[$RANDOM % ${#symbols[@]}]}" ;;
            2) pass+="$(tr '[:upper:]' '[:lower:]' <<< ${words[$RANDOM % ${#words[@]}]})" ;;
            3) pass+="$((RANDOM % 10))" ;;
        esac
    done
    
    echo "-----------------"
    echo " $pass"
    echo " ----------------"
    echo " If you don't like this password, you can repeat the process again"
}

# Main loop
while true; do
    read -p "$ " cmd
    case $cmd in
        -h|--help|"help")
            echo "PAS-K Help:"
            echo "  -g or --generate : Generate new password"
            echo "  man              : Show manual"
            echo "  exit or quit     : Exit tool"
            ;;
        -g|--generate|"g")
            echo " Already Created below !!!! (copy it)"
            generate_password
            ;;
        man|"man")
            echo "PAS-K Manual:"
            echo "This tool generates readable but secure passwords."
            echo "Made with ❤️ by EgoClavis Labs"
            ;;
        exit|quit|"")
            echo "Goodbye from EgoClavis Labs!"
            exit 0
            ;;
        *)
            echo "Unknown command. Type -h for help."
            ;;
    esac
    echo
done
