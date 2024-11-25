# BCF2000plus
Behringer BCF2000 Remote Script for Ableton Live.

## Thank you

This is a fork of [BCR2000plus](https://github.com/widdly/BCR2000plus) from [widdly](https://github.com/widdly), which is based on the [Generic-Python-Remote-Script](https://github.com/j74/Generic-Python-Remote-Script) from [j74](https://github.com/j74).

A big thank you for the great work to all contributors!

## What is this?

This script adds a new remote capabilities for the Behringer BCF2000 to Ableton Live.

The default BCF2000 settings in Live only works for the first 8 channels.  This script gives a moveable box so that you can control all the channels.

## Layout

The faders control the track volumes.

The rows of buttons control Mute and Record.

The top row of encoders have 4 groups of functions.  The different functions are selected by the 4 encoder group buttons.

Group 1 has encoders controlling pans, and pushbutton sets Solo.

Group 2 has device control (the blue hand) encoders and the pushbuttons select between of 8 banks device controls.  The "Edit" and "Exit" buttons also scroll through the device control banks.  The "Store" and "Learn" buttons scroll through plugins.

Group 3 has Crossfader on encoder 6, Headphones on 7 and Master Volume on 8.  The push buttons select tracks.

Group 4 has Send 1 levels and the pushbuttons stop the clips for that track.

The buttons on the lower right move the rectangle left and right, selecting a different set of 8 channels.  It is possible to control the return channels as well as the normal channels.  The two buttons above operate the Play and Stop transport.

## How to install

You will need to copy the entire BCF2000plus folder to the Ableton Live remote scripts directory...

### User Library folder 
Create a "MIDI Remote Scripts" folder in your User Library folder. This is the preffered method.

### Windows
\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts\
This folder is hidden by default.

### Mac
The Remote Script folder is inside the Ableton Live application bundle. Locate the Live application in Finder, right click on it and select "Show Package Content". Then navigate to: /Contents/App-Resources/MIDI Remote Scripts/.

After you restart Live, you should see the BCF2000plus in Preferences/Link Midi/Control Surfaces.

There is file called preset.syx you need to send to your BCF2000.  Ideally you could press the "dump" button in the Live GUI but I've found it cannot transfer the whole file properly so I recommend you use the Elektron C6 utility from here.. https://www.elektron.se/support/?connection=analog-four    You will need to add a delay in the configure page of about 10ms for it to work properly with the BCF2000
