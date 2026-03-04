import os
from colorama import Fore, Style


class DNS:

    def __init__(self):
        print(
            f"""{Fore.MAGENTA} 
:::::  ::    ::   ::::        ::::   :::::  :::::   ::      ::  :::::    :::::                                             
::  :  :: .  ::   ::  .       ::  .  ::___  ::   :  ::     ::   ::___    ::   :                                                  
::  :  ::  . ::  .  ::        . ::   ::     :::::     :: ::     ::       :::::                                                              
:::::  ::   .::   ::::        ::::   :::::  ::   .      :       :::::    ::   . {Style.RESET_ALL}
              """
        )

    def dns_server(self):
        self.hostname = input(
            f"{Fore.BLUE}\n [ + ]  Enter the hostname (e.g: google.com)(q to exit){Style.RESET_ALL}\t"
        )
        try:
            if self.hostname.isdigit():
                print(ValueError("Invalid hostname type!!!"))
            elif self.hostname.lower() == "q":
                print(f"{Fore.GREEN}Exiting{Style.RESET_ALL}")
            else:
                os.chdir("C:\Windows\system32")
                print("Changing directory")
                self.dns = os.system(f"nslookup {self.hostname}")
        except Exception as error2:
            print(error2)
        return self.dns, self.hostname


o = DNS()


def main():
    while True:
        try:
            permission = input(
                f"{Fore.BLUE}\t[ + ]  Do You want to Continue (y/n){Style.RESET_ALL}\t"
            ).lower()
            if permission == "y":
                p = o.dns_server()
                print(p)
            elif permission == "n":
                print(f"{Fore.GREEN}Exiting...{Style.RESET_ALL}")
                break
            else:
                raise f"{Fore.RED}Invalid options inputed!!!"
        except Exception as error:
            print(error)


if __name__ == "__main__":
    main()
