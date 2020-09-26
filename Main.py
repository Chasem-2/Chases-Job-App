# This will import all the widgets and modules from tkinter and tkinter.ttk 
from tkinter import * 
from tkinter.ttk import *
#Imports date entry wiget from tkcalendar
from tkcalendar import Calendar, DateEntry


# creates a Tk() object 
master = Tk() 
  
# sets the geometry of main root window 
master.geometry("200x200") 
#Sets Title
master.title("Chases Job App")


#Function to open a new window
def openNewWindow(): 

    #Function for the calendar
    def example1():
        def SetAppDate():
            AppDateText.insert(INSERT, cal.selection_get())
            top.destroy()

        top = Toplevel(master)

        cal = Calendar(top,
                    font="Arial 14", selectmode='day',
                    cursor="hand1")
        cal.pack(fill="both", expand=True)
        Button(top, text="Ok", command=SetAppDate).pack()

    #Save Job File Input
    def SaveJob():
        #Open Job File in Append Mode
        JobFile = open("CurrentJobs", "a")
        #Create text string retrieving text from entry boxes
        CNT = CompNameText.get()
        APT = AppPortText.get()
        ADT = AppDateText.get()
        LLT = LinkListText.get()
        #Saves text from entry files and creates a new line
        JobFile.write(CNT + ";" + APT + ";" + ADT + ";" + LLT + ";\n")
        #Closes Job File
        JobFile.close

    #View Saved Jobs

    # Toplevel object
    newWindow = Toplevel(master) 
  
    # sets the title of toplevel object
    newWindow.title("New Application") 
  
    # sets the geometry of toplevel 

    newWindow.geometry("450x200") 
    
    #Creates First Label
    CompName = Label(newWindow,

                text = "Position Name")
    CompName.grid(row = 1, column = 0, sticky = W, pady = 2)
    
    CompNameText = Entry(newWindow)
    CompNameText.grid(row = 1, column = 1, pady = 2)

    AppPort = Label(newWindow,
                text = "Application Portal")
    AppPort.grid(row = 2, column = 0, sticky = W, pady = 2)
    
    AppPortText = Entry(newWindow)
    AppPortText.grid(row = 2, column = 1, sticky = W, pady = 2)

    AppDate = Label(newWindow,
            text = "Application Date")
    AppDate.grid(row = 3, column = 0, sticky = W, pady = 2)

    AppDateText = Entry(newWindow)
    #Insert Text here

    AppDateText.grid(row = 3, column = 1, sticky = W, pady = 2)

    LinkList = Label(newWindow,
            text = "Link to job listing")
    LinkList.grid(row = 4, column = 0, sticky = W, pady = 2)
    
    LinkListText = Entry(newWindow)
    LinkListText.grid(row = 4, column = 1, sticky = W, pady = 2)

    Save = Button(newWindow,
                text = "Save",
                command = SaveJob)
    Save.grid(row = 5, column = 1, sticky = W, pady =2)
    
    SD = Button(newWindow,
                text = "Set Application Date",
                command = example1)
    SD.grid(row = 3, column = 2, sticky = W, pady = 2)

AddJob = Button(master,
                text = "Add a new job",
                command = openNewWindow)

ViewJobs = Button(master,
                text = "View Jobs",
                command = "ViewJobs")




label = Label(master,  
              text ="Welcome!") 
  
label.pack(pady = 10) 
AddJob.pack(pady = 10)
ViewJobs.pack(pady = 10)


mainloop() 