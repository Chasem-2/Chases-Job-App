
# This will import all the widgets and modules from tkinter and tkinter.ttk 
from tkinter import * 
from tkinter.ttk import *
  
# creates a Tk() object 
master = Tk() 
  
# sets the geometry of main root window 
master.geometry("200x200") 
master.title("Chases Job App")

def SaveJobs():
    JobFile = open("CurrentJobs", "a")
    JobFile.write




#Function to open a new window
def openNewWindow(): 
      
    # Toplevel object
    newWindow = Toplevel(master) 
  
    # sets the title of toplevel object
    newWindow.title("New Window") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("200x200") 
  
    # A Label widget to show in toplevel 
    CN = Label(newWindow,
                text = "Add a new Job")
    CN.pack(pady = 2)
    
    AP = Label(newWindow,
                text = "Application Portal")
    AP.pack(pady = 2)
    
    AD = Label(newWindow,
            text = "Apply Date")
    AD.pack(pady = 2)
    
    Label(newWindow,  
          text ="Add a new job",).pack() 

    Button(newWindow,
            text = "Save",
            command = SaveJobs)

AddJob = Button(master,
                text = "Add a new job",
                command = openNewWindow)

ViewJobs = Button(master,
                text = "View Jobs",
                command = "")




label = Label(master,  
              text ="This is the main window") 
  
label.pack(pady = 10) 
AddJob.pack(pady = 10)



mainloop() 