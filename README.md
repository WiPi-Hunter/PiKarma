
```python

                    ██████╗ ██╗██╗  ██╗ █████╗ ██████╗ ███╗   ███╗ █████╗ 
                    ██╔══██╗██║██║ ██╔╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗
                    ██████╔╝██║█████╔╝ ███████║██████╔╝██╔████╔██║███████║
                    ██╔═══╝ ██║██╔═██╗ ██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║
                    ██║     ██║██║  ██╗██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║
                    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝

                  Detects wireless network attacks performed by KARMA module
```

<p align="center">
<img src="https://img.shields.io/badge/Python-2-yellow.svg"></a>
</p>

#### Working Principle for PiKarma

+ Collects all the packets from Wireless Network. (Probe Response) 
+ Analyses all the packets in real time.
+ If PiKarma finds more than one SSID info from unique mac address in Probe Response;
+ Logs the activity with some extra information within defined template and sends deauthentication packets 


#### How works KARMA Attack?

+ Sends Probe Response for all Probe Requests

**Example:**

<img src="https://github.com/besimaltnok/pikarma/blob/master/karma.gif">


#### Softwares and hardwares that uses KARMA module

+ FruityWifi
+ WiFi Pineapple
+ Mana (improvements to KARMA attacks)
+ ..


#### Screenshots
<img src="karma_detect.png" width="45%"></img>

#### DEMO

+ https://www.youtube.com/playlist?list=PLwHi7Vsh6TpNrCX87KRzO9WVtHmqqC2aB
