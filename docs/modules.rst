Modules
========

These are currently all of the modules that BYOB supports.
BYOB is open for suggestions of new modules as well.

*Post-exploitation modules that are remotely importable by clients*

1) Keylogger (`byob.modules.keylogger`): logs the user’s keystrokes & the window name entered

2) Screenshot (`byob.modules.screenshot`): take a screenshot of current user’s desktop

3) Webcam (`byob.modules.webcam`): view a live stream or capture image/video from the webcam

4) Ransom (`byob.modules.ransom`): encrypt files & generate random BTC wallet for ransom payment

5) Outlook (`byob.modules.outlook`): read/search/upload emails from the local Outlook client

6) Packet Sniffer (`byob.modules.packetsniffer`): run a packet sniffer on the host network & upload .pcap file

7) Persistence (`byob.modules.persistence`): establish persistence on the host machine using 5 different methods

8) Phone (`byob.modules.phone`): read/search/upload text messages from the client smartphone

9) Escalate Privileges (`byob.modules.escalate`): attempt UAC bypass to gain unauthorized administrator privileges

10) Port Scanner (`byob.modules.portscanner`): scan the local network for other online devices & open ports

11) Process Control (`byob.modules.process`): list/search/kill/monitor currently running processes on the host

12) iCloud (`byob.modules.icloud`): check for logged in iCloud account on macOS

13) Spreader (`byob.modules.spreader`): spread client to other hosts via emails disguised as a plugin update

14) Miner (`byob.modules.miner`): run a cryptocurrency miner in the background (supports Bitcoin & Litecoin)

15) MQTT (`byob.modules.mqtt`): publish data gathered from client to public MQTT brokers to be disseminated by other C&C servers.
