# File Sorter

This application is to clean up your Downloads folder/directory.  

I built this application as I was tired of looking through a cluttered Downloads directory, spending lots of time looking for files. Let's face it, who normally cleans their downloads :P.  

This application currently works on Linux and Windows, MacOS functionality to coming soon.  

What this app does when it is ran...  
It will dynamically get the username of the current logged in user.  
It will then navigate to the Downloads Folder, and begin scanning the directory.  
Several new folders will be created in this process:  
- Image Files
- Video Files
- Audio Files
- Text Files
- CSV Files
- PDF Files
- Shell Scripts
- presentation (powerpoint) Files
- Drivers and Executables
  - This last one is for Windows systems
 
Based on the extensions of the files, they will then be moved into their respective folders.  

## How to use the application
There are currently two ways to use this application.   
1. Easy way (Windows) - Clone the repo on a Windows computer to a directory of your choice, double click of the ".exe" file and watch your files organize like magic!  
2. (Any OS with Python installed) - Clone the repo to a directory of your choice.  
   Then open the "fileSorter.py" file in your favorite text editor/IDE, and  
   a) press the run button or use one of the below commands in the IDE terminal.  
   b) navigate to the file in a command line tool.  
   Once you are in the same Folder/Directory simply run:  
   - Windows - `py .\fileSorter.py` or `py .\path\to\file\fileSorter.py`
   - Linux - `python3 fileSorter.py` or `python3 path/to/file/fileSorter.py`
   - MacOS - `python3 fileSorter.py` or `python3 path/to/file/fileSorter.py`

## Screenshots
Before the program is run:  
![Screenshot from 2024-06-17 00-05-15](https://github.com/j-bloom/file-sorter/assets/36741471/b2045bf9-274b-479f-bacf-02f4ba739a4e)

After the program is run:
![Screenshot from 2024-06-17 00-08-02](https://github.com/j-bloom/file-sorter/assets/36741471/b2cc5b0c-be60-4b67-a523-08d6a4398668)


## Approach to the application
I first thought of creating this application as an automated tool, which would allow the files to be moved into the correct folders at the time they are downloaded.  

I decided against this as I thought of times that I was in class (while I was still in school), and would need to download several files and need to interact with each of them. I thought in a situation like this 
it would become a nuisance and cumbersome to continually have to change directories to interact with all the files I need should I find myself in a situation like this in the future.  


