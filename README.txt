----------------------------------------------------------------------------------
	   ECOR 1051 W2020 TEAM 51 Image Filtering Tool v1.0 01/04/2020
----------------------------------------------------------------------------------
This project may be refered to as the ITF throughout this document for simplicity

The project can be reached at:
Voice: 613 415 3093
Email: huugiabaongo@cmail.carleton.ca

----------------------------------------------
                 User Info
----------------------------------------------

Description
-------------------------------------
    This project's purpose is to filter images with various common filters effectively and save the filtered image. 
The selection of what image file to filter and what filter to apply is facilitated through a simple CLI user interface.
Filters can be stacked on top of each other cumulatively once already filtered since the program keeps the original image 
and any other filtered images in local memory for quick reuse within the same session. This also enables the program to be 
able to handle multiple images being loaded during the same session. The user is prompted to select the photo they would like 
to filter from a list of all filtered and original images in local memory. Although there are a limited number of preset filters 
to be used, more filter functions can be easily added to the program and UI as described under Developer Notes.
    The project also contains a seperate script to mass filter photos in a batch with the existing filters designed with
the program. The batch filter commands are located in a text file which the program reads and follows instructions.

    The project is made up of the following files:
	T51_interactive_ui.py		Main Script
	T51_image_filters.py		Pre-Defined Filters
	batch.txt			File containing sample batch commands
	Cimpl.py			Carleton Image Manipulation Python Library
	miss_sullivan.jpg		Sample Image
	

Installation
-------------------------------------
DEPENDENCIES:
The tool runs in a Python environment has been tested for Python v3.7+      		(04/01/2020) 
**IMPORTANT: THIS PROGRAM HAS NOT BEEN TESTED FOR MAC OSX NOR LINUX/UNIX BASED OS’**

To install Python, visit https://www.python.org/downloads/ and download a compatible version. 
Launch the downloaded installer and check the checkbox "Add Python to PATH"

This tool depends on functions from the Carleton Image Manipulation Python Library (Cimpl) which depends on Pillow 
*Note: Cimpl is included with the tool’s package*.
To install the Pillow module, open command line and enter "pip install Pillow"
The "pip" installer should come with Python. If not found, the user may have to install it manually.

INSTALLATION:
Download and extract the ITF’s compressed file and ensure all files are present in the same directory.

ALTERNATIVE INSTALLATION:
The GitHub repository for this program is available at:
https://github.com/ahm23/ECOR1051-T51-Image-Filtering-Tool

Usage & Execution
-------------------------------------
USER INTERFACE:
To launch the program, launch the python script T51_interactive_ui.py with a valid Python version.
> python T51_interactive_ui.py

The user interface is very interactive and very straightforward to use. Simply follow the instructions
on the interface. After running the program, the launching window need to be minimized because the file selection is showing up under 
the launching window.  

BATCH INTERFACE:

To launch the program, launch the python script T51_batch_ui.py with a valid python version.

The batch user interface requires the user to create and edit their own text document. Once the user runs the
program, they will be prompted to enter a file name. The user must enter the name of the text document they 
created which contains the instructions for the batch interface, followed by .txt. For example, if the user 
created a text file titled "instructions", they would enter "instructions.txt" when prompted to enter a file.
Each line of the text document created by the user contains the specific instructions on how to filter a desired image. It is 
important that the user knows that each line contains a filter job for a single image. The user cannot enter
the image filter instructions for one photo over multiple lines, or enter the instructions for two photos in
one line.

 

The instructions must follow a specific format, modelled by the following line of text:

O S F1 F2 F3... Fn

"O" represents the name of the original image that the user wants to be filtered. This file location must be in
the same file directory as the "T51_batch_ui.py" file. The user must also be aware that the name of the file must
include the file type as well. For example, if the user wishes to filter a .jpg file with the title "photo", the 
user must enter "photo.jpg" as the first word of the line in their text file. As mentioned earlier, "photo.jpg" 
must be in the same file directory as "T51_batch_ui.py".

S represents the name of the file which the user wishes to save the new, filtered image to. The name must contain
the file type. The file will be saved to the same file directory as the "T51_batch_ui.py" file. For example, if the
user wishes to save their filtered image as a .PNG file with the title "my_filtered_photo", they must enter 
"my_filtered_photo.PNG" as the second word of the line in their text file.

"F1 F2 F3... Fn" represents the filters that the user wishes to apply to their image. The user may apply as many 
filters to their image as they wish. Each filter is represented by a code name, as follows:

"2" represents the two-tone filter. 

"X" represents the extreme contrast filter.

"P" represents the posterize filter.

"V" represents the vertical flip filter.

"H" represents the horizontal flip filter.

"R" represents the red channel filter.

"G" represents the green channel filter.

"B" represents the blue channel filter.

"C" represents the combine filter. (The combine filter will not work unless the red, blue and green channel filters
have been applied to the photo before the combine filter is applied.)

"3" represents the three-tone filter.

"S" represents the sepia filter.

"D" represents the detect edges filter.

"DB" represents the detect edges better filter.

It is important that the user understands that each filter is applied to the image in succession, not at the same time.
For example, if the user enters "H D 3", image would first be passed through the horizontal flip filter. The flipped 
image would then be passed through the detect edges filter. Finally, the flipped image with the detect edges filter 
applied would then be passed through the three-tone filter, resulting in the image that would be saved with the
pre-entered file name.

Format examples:

my_fun_image.jpg cool_filter.png 2 S R H 
cool_photo.png edge_detected.jpg DB
carleton.png carleton1.png S V D

If the user were to run a text document with the above instructions through the T51_batch_ui.py script, they would 
filter three images. The first, being titled "my_fun_image" with a .jpg file format, would be run through the two-tone
filter, then the sepia filter, then the red channel filter, then the horizontal flip filter. The final image would be
saved as a .png file forma with the title "cool_filter".


Pre-Defined Filters
-------------------------------------
2-Tone (Hardcoded colors cyan and yellow due to course requirements)
3-Tone (Hardcoded colors cyan, magenta, and yellow due to course requirements)
Xtreme Contrast
Sepia Tone
Posterize 
Edge Detect
Improved Edge Detection
Vertical Flip
Horizontal Flip

----------------------------------------------
      Developer Notes (for interactive UI)
----------------------------------------------

Custom Colour for 2 and 3 Tone
-------------------------------------
Due to unfortunate circumstances, the course in which this program has been developed set a requirement 
for the 2 and 3 tone filters to have hardcoded colour values. This can be unlocked.

To do so, within the file T51_interactive_ui.py, you may find a large list called mainMenu. Within the list, 
all of the possible filter options can be found. Find the 2 or 3 tone filter and replace
["static", "cyan"], ["static", "yellow"]	
with:
["input", "colour 1"], ["input", "colour 2"]
for the 2-tone filter and:
["static", "cyan"], ["static", "magenta"], ["static", "yellow"]
with:
["input ", "colour 1"], ["input ", "colour 2"], ["input ", "colour 3"]
for the 3-tone filter.
This will enable a prompt for the colours to be used for the filters.

Adding Custom Filters
-------------------------------------
As mentioned above, the program is extremely dynamic to the point where you can add your own custom filters very easily. 
The first step to that is to import any extra modules that you may need. Then the used should add their filter function 
into T51_image_filters.py or import their own custom module.
**ENSURE THAT NONE OF YOUR CUSTOM FUNCTIONS ARE ALREADY DEFINED BY THE SAME NAME**
Locate the large 4-dimensional list named mainMenu. Every grouping of list rows is a row of selections in the UI. 
Every row in the groups is a selection. The structure of these selections in the groups is as follows:

["Selection Name ", "Selection Type", Function, Arguments[Argument["Argument Type", "Argument Description"]]]

PARAMETER DESCRIPTIONS:
Selection Name: Display name on the UI for the selection. (string)
Selection Type: There are 4 types of selections: load, save, filter, quit. (string) 
Function: Simply type in the function name (function)
Arguments: List of arguments that the function takes (list)
	Argument: List of singular argument details (list)
		Argument Type: There are 3 types of arguments: image, input, static. (string)
			Image: this will prompt the user to select an image to be used as argument.
			Input: this will prompt the user to input data as an argument.
			Static: this is used for a hardcoded argument
		Argument Description: Description of argument (will vary by type). (string)
			Image: the program will prompt “Select image {description}”
				Ex. description = “to apply sepia tone”
			Input: the program will prompt “Please enter {description}”
				Ex. description = “threshold”
			Static: the program will use the description field as input for the hardcoded arg

Adding a row like this within a group of list rows will add a selection to the UI with your function.
Not that if your new entry is not at the end of a group you will need to add a comma after the list entry.
This feature would be implemented as another feature for the general user on the interface; however the requirements
of this program insisted that no new features are to be added thus the developer must add filters manually if wanted.

Modifying Load Image & Save As
-------------------------------------
Highly not recommended but if ever needed it is possible. The functions are located in T51_user_interface.py


Credits
-------------------------------------
Ngo Huu Gia Bao (Team Lead) - 2 & 3 Tone Filter, Detect Edges
Ahmed Moussa - Interactive UI - Sepia Filter, Vertical Flip
Alexander Szabo - Batch UI - Posterize, Improved Edge Detection
Jaden Paget - Extreme Contrast, Horizontal Flip


Copyright 2020 Ngo Huu Gia Bao, Ahmed Moussa, Alexander Szabo, Jaden Paget

