#!/usr/bin/env python
# Terminal tool for looking up information on domains
import whois as search


# Main function
def main():
    """Checks domain inputted by user and get information from WHOIS library."""
    try:
        # Domain input
        DOMAIN = input("\033[96m" + "Domain 💪: " + "\033[00m").lower()
        # Domain searched in whois database
        DATA = search.whois(DOMAIN, timeout=15)
        if DOMAIN is not str:
            # Struture information returned neatly
            for data, values in DATA.items():
                print("\033[95m" + f"\n{data.title()}: {values} 📢" + "\033[00m") # Purple color

            print("\033[94m" + "\nTo find more information on searched domain, visit ➤ https://www.whois.com/" + "\033[00m") # Light Purple color
            
    except search.WhoisError:
        # Display error message to user in colored text
        # + ANSI coloring used
        print("\033[93m" + "🗳 Make sure you have entered a valid domain (e.g., google.com)." + "\033[00m")
    except KeyboardInterrupt:
        # Catch CTRL+C interruption
        print("\033[92m" + "\nThank you for using this script! Sad to see you go! 🥺" + "\033[00m")

main()    
