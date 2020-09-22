
# This will import all the widgets and modules from tkinter and tkinter.ttk 
from tkinter import * 
from tkinter.ttk import *
#Imports date entry wiget from tkcalendar
from tkcalendar import Calendar, DateEntry


# creates a Tk() object 
master = Tk() 
  
# sets the geometry of main root window 
master.geometry("200x200") 
master.title("Chases Job App")

#def SaveJobs():
#    JobFile = open("CurrentJobs", "a")
#    JobFile.write

def example1():
    def print_sel():
        print(cal.selection_get())

    top = Toplevel(master)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    Button(top, text="ok", command=print_sel).pack()


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
    CN.grid(row = 1, column = 0, sticky = W, pady = 2)
    
    CNText = Entry(newWindow)
    CNText.grid(row = 1, column = 1, pady = 2)

    AP = Label(newWindow,
                text = "Application Portal")
    AP.grid(row = 2, column = 0, sticky = W, pady = 2)
    
    APText = Entry(newWindow)
    APText.grid(row = 2, column = 1, sticky = W, pady = 2)

    AD = Label(newWindow,
            text = "Apply Date")
    AD.grid(row = 3, column = 0, sticky = W, pady = 2)
    
    ADText = Entry(newWindow)
    ADText.grid(row = 3, column = 1, sticky = W, pady = 2)

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
                command = example1)




label = Label(master,  
              text ="This is the main window") 
  
label.pack(pady = 10) 
AddJob.pack(pady = 10)
ViewJobs.pack(pady = 10)


mainloop() 