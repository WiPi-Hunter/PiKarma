
```python

                    ██████╗ ██╗██╗  ██╗ █████╗ ██████╗ ███╗   ███╗ █████╗ 
                    ██╔══██╗██║██║ ██╔╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗
                    ██████╔╝██║█████╔╝ ███████║██████╔╝██╔████╔██║███████║
                    ██╔═══╝ ██║██╔═██╗ ██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║
                    ██║     ██║██║  ██╗██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║
                    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝

                  Detects wireless network attacks performed by KARMA module
```

#### Working Principle

+ Collects all the packets from Wireless Network. (Probe Response) 
+ Analyses all the packets in real time.
+ If PiKarma finds more than one SSID info from unique mac address in Probe Response;
+ Logs the activity with some extra information within defined template and sends deauthentication packets 


#### How works KARMA Module?

+ Sends Probe Response for all Probe Requests

**Example:**

<img src="https://github.com/besimaltnok/pikarma/blob/master/karma.gif">


#### Software and hardware using the KARMA module

+ FruityWifi
+ WiFi Pineapple
+ Mana (improvements to KARMA attacks)
+ ..

