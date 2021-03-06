# Computer guide for resource model study


#### Before participant gets there

1. Turn on the iMac, and make sure the external desktop is connected to it. All of the USB's behind the iMac should be plugged into it. If not, try to remove anything extraneous (mouse, flash drives, etc.) to fit the cables that are there. 

2. Go into the other room and turn on the monitor. Come back and turn on the extra monitor next to the iMac. You should see the generic mac background. 

3. Open NeuLog (Command-Space and then type neulog to find it). Once you have opened NeuLog, a small window will appear and tell you whether or not the grip strength meter is connected.   

	- If there's a picture of a USB with a green checkmark, then it's good. Otherwise, go into the other room and unplug and then replug the grip. 
	- Another good way to check if the Grip isn't working is once Neulog is open, if it's stuck on some weird number like 7.3, something broke. Just unlpug and replug. 

4. Open Psychopy (Command-Space and then type psychopy). Once you have opened Psychopy, click File-Open and then find "run.py" (it will be in Desktop in the "resource_model-master" folder that you downloaded. Within that folder it is in the "gui" folder).
	- If the code doesn't open, but a smaller blank pyschopy window opens, just repeat step 4 again. 

5. In Pyschopy, below where it says "ENTER SUBJECT INFO HERE", update the subject id. 
	- **NOTE** Don't edit any other code besides the number after `subjectID =` 
	- After you update the subjectID, Command-S to save, so you keep track of what IDs you are upto. 
	

#### Running the Experiment with the GUI  
Once the participant is in the other room, consent forms signed, watching the computer and ready to go.

1. In Neulog, hit the "New Experiment" button to start a new experiment. The settings should already be at `30` and `minutes`, but if not, click those to make sure we're recording for 30 minutes. You should see a grid with a moving colored line moving to indicate the grip strength is working. 

2. Go back to the pyschopy window and click "Run" (the little green button with a runing person). As quickly as you can, drag the window over to the other monitor. 
	- If it froze/moved too slowly and by the time it's on the other monitor (where the participant can see it), the directions are gone, go back to the PsychoPy window and click the red stop sign and do this step again. We want to make sure they see the directions!

3. Bring NeuLog to the front of the screen and ait for the first GO/STOP cycle to begin. Once it does, you should see a spike in the window that is tracking the grip. 
	- If you don't, click and drag the grid to the left. Keep going until you see the spike. 

4. On the second GO/STOP cycle, zoom in on the grid to see what the highest peak output (in N) was. Take 35% of this number and take note of it somewhere, this is the threshold for the participant. Zoom back out so you can see all the spikes
	- You may periodically need to click and drag the window to keep up with the moving readout. It won't automatically do this (unfortunately). 

5. On the first GO iteration that the participant **doesn't** hit their threshsold, move your mouse into the black screen that says "GO" (the psychopy window), and press the spacebar **once**. 
	- Nothing will happen immediately. Resist the urge to press it again to make something happen. 
	- The "GO" should finish, and then "STOP" should appear. Once STOP is over, you should see a "+" come on the screen. If at this point you don't, and you see a "GO" again instead, you can press the spacebar again. 

6. Once the "+" is over, there will be another set of directions (just a reminder to keep gripping as hard as possible). Click back over into the NeuLog screen. And click and drag to keep up with the readout. 

7. After the directions, there will be another trial of gripping. Repeat steps 4 - 6. 
8. After the directions, there will be a third, and final set of gripping. Repeat steps 4 and 5. 
	- This time, after the "+", you should see "END" and then the program will close automatically. 

9. Go back to neuLog and click the stop button (right next to the pause button). Then, in the upper right hand side of the toolbar click on the "Export" button. Title the file in the following format: [DATE]\_[INITIALS]_[ID] and save as ."CSV".
	- Example filename: `01032017_CL_0.csv`
	- Make sure that there are no special characters (!, ?, ; , \ ) except for the underscores in the filename. Also no spaces

10. The file will download and show up in the bottom of the neulog screen. Open finder and navigate to the "resource_model-master" folder on your desktop. Open it and go into the "exportedData" folder. Drag the file from the bottom of the neulog screen and plop it into the exportedData folder. 
	- If you accidentally mistyped the filename and downloaded it, just go back and correct the filename and then redownload it and place the correct one in the exportedData folder.


#### At the end of a session/day   
Once you've run all the participants in a given day or aren't going to be running any for a while, it's best to close completely out of NeuLog and PsychoPy as both tend to freeze if left open. 

Make sure they're closed completely (Command-Q) out of both of them. If PsychoPy asks you if you want to save, click yes. 

Also make sure you've closed Chromium (A blue-ish google chrome logo on the bottom dock). 

#### Basic troubleshooting

 - If NeuLog crashes or freezes, Command-Q out of it and also Command-Q out of Chromium (blue-ish chrome icon). Try reopening. 
 - If psychopy crashes (which it will eventually; it is super finicky and likes to crash), just click ignore and try again. 
 - If you're not getting any output from the grip strength meter, just unplug it and try again. 
 - If the external monitors are not showing up, or are flashing on and off, make sure that the connections are good. Make sure that they are plugged into the outlets as well as the main iMac. 
 - If somehow the PsychoPy code gets messed up, deleted, or otherwise lost, you can always download a fresh working copy from: github.com/caitlynlee/resource_model
 	- in the middle of the screen there's a green button that says clone or download. just download the zip and all the contents should be inside. 
  