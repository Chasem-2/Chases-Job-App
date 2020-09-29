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
        #Function to set application date
        def SetAppDate():
            AppDateText.insert(INSERT, cal.selection_get())
            top.destroy()
        #Creates top level window to load calendar into
        top = Toplevel(master)
        #Creates Calendar
        cal = Calendar(top,
                    font="Arial 14", selectmode='day',
                    cursor="hand1")
        cal.pack(fill="both", expand=True)
        #Creates an Ok button at the bottom of the screen to set the application date
        Button(top, text="Ok", command=SetAppDate).pack()

    #Save Job File Input
    def SaveJob():
        #Create text string retrieving text from entry boxes
        PNT = PosNameText.get()
        APT = AppPortText.get()
        ADT = AppDateText.get()
        LLT = LinkListText.get()
        
        #Open Job File in Append Mode
        JobFile = open("CurrentJobs", "a")
        #Saves text from entry files and creates a new line
        JobFile.write("1 " + PNT + "\n" + "2 " + APT + "\n" + "3 " + ADT + "\n" + "4 " + LLT + "\n")
        #Closes Job File
        JobFile.close


    # Toplevel object
    newWindow = Toplevel(master) 
  
    # sets the title of toplevel object
    newWindow.title("New Application") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("450x200") 
    
    #Creates Label for the job name
    PosName = Label(newWindow,
                text = "Position Name")
    
    #Places Label in row 1, column 0 
    PosName.grid(row = 1, column = 0, sticky = W, pady = 2)
    
    #Creates Entry box for job name
    PosNameText = Entry(newWindow)
    
    #Places Entry box on row 1, column 1 beside the job name Label
    PosNameText.grid(row = 1, column = 1, pady = 2)

    #Creates Label for the application portal link
    AppPort = Label(newWindow,
                text = "Application Portal")
    
    #Places Label on row 2, column 0
    AppPort.grid(row = 2, column = 0, sticky = W, pady = 2)
    
    #Creates Entry widget to intake Application Portal Link
    AppPortText = Entry(newWindow)
    
    #Places Entry widget beside the Label Widget on row 2, coumn 1
    AppPortText.grid(row = 2, column = 1, sticky = W, pady = 2)

    AppDate = Label(newWindow,
            text = "Application Date")
    AppDate.grid(row = 3, column = 0, sticky = W, pady = 2)

    AppDateText = Entry(newWindow)

    AppDateText.grid(row = 3, column = 1, sticky = W, pady = 2)

    LinkList = Label(newWindow,
            text = "Link to job listing")
    LinkList.grid(row = 4, column = 0, sticky = W, pady = 2)
    
    LinkListText = Entry(newWindow)
    LinkListText.grid(row = 4, column = 1, sticky = W, pady = 2)













    #Saves input to CurrentJobs file
    Save = Button(newWindow,
                text = "Save",
                command = SaveJob)
    Save.grid(row = 5, column = 1, sticky = W, pady =2)
    
    SD = Button(newWindow,
                text = "Set Application Date",
                command = example1)
    SD.grid(row = 3, column = 2, sticky = W, pady = 2)

def ViewJobs():
    #Create view jobs window
    ViewJobsWindow = Toplevel(master)

    #Set the title for the window
    ViewJobsWindow.title("Current Jobs")

    #Set the size of the window
    ViewJobsWindow.geometry("450x200") 


    #Opens file as f, then creates a dictionary d
    with open('CurrentJobs') as f:
        d = dict(x.rstrip().split(None, 1) for x in f)




    #Creates first job name entry
    JobNameEntry = Entry(ViewJobsWindow)
    #Places Entry widget beside the Label Widget on row 2, coumn 1
    JobNameEntry.grid(row = 0, column = 0, sticky = W, pady = 2)
    #Inserts position name for the first position in the file
    JobNameEntry.insert(INSERT, d.get("1"))




AddJob = Button(master,
                text = "Add a new job",
                command = openNewWindow)

ViewJobs = Button(master,
                text = "View Jobs",
                command = ViewJobs)




label = Label(master,  
              text ="Welcome!") 
  
label.pack(pady = 10) 
AddJob.pack(pady = 10)
ViewJobs.pack(pady = 10)


mainloop() 