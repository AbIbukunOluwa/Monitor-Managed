# Monitor-Managed
Python script to help you change your wireless mode back and forth

                           _                      
            _             (_ )                    
 _   _   _ (_) _ __   __   | |    __    ___   ___ 
( ) ( ) ( )| |( '__)/'__`\ | |  /'__`\/',__)/',__)
| \_/ \_/ || || |  (  ___/ | | (  ___/\__, \\__, \
`\___x___/'(_)(_)  `\____)(___)`\____)(____/(____/
                                                  
                                                  

This script will help in your wifi penetration tasks. Move swiftly back and forth between monitor mode and managed as you test.

Note that this script is best run using python2 as python3 will have issues with running the code


usage:
  For help
  python2 wireless.py --help
  
  
-i is for your interface
-m is for the mode you want to be in
  
  
use case:
python2 wireless.py -i eth0 -m monitor
