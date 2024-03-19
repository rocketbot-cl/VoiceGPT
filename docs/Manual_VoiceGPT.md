



# VoiceGPT
  
Send an audio and receive the data according to the template created in VoiceGPT.  
  
![banner](imgs/Banner_VoiceGPT.png o jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Get audio template
  
Obtains the data indicated in the VoiceGPT template from an audio
|Parameters|Description|example|
| --- | --- | --- |
|API Key|Key generated in the Profile section of VoiceGPT.|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey...|
|Template ID|The ID of the template to occupy. It can be taken from the url https//voicegpt.rocketbot.com/#/template/{template}|83540b69bb195851896cd3881555c222|
|Select audio|URL of the location and name of the audio to send|C:/Users/user/Downloads/file.mp3|
|Assign result to variable|Variable where the result will be stored.|Variable|
