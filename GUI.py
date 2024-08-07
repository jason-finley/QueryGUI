# Import necessary modules and classes from tkinter and graphics packages
from tkinter import DISABLED, END, INSERT, Radiobutton, OptionMenu, StringVar, scrolledtext, IntVar
from tkinter.font import NORMAL
from graphics import *


# Function to create and configure the main window
def Window():
    # Create a graphical window with title "GUI" and size 800x500
    win = GraphWin("GUI", 800, 500)
    win.setBackground("white")

    # Add title text to the window
    Title = Text(Point(400, 30), "BICCN - 3D Brain Mapping")
    Title.setSize(24)
    Title.setFill("black")
    Title.draw(win)

    # Add header text to the window
    Header = Text(Point(400, 70), "Select a Search Term")
    Header.setSize(24)
    Header.setFill("black")
    Header.draw(win)

    # Create and draw rectangles with labels for each search term
    Molecules = Rectangle(Point(80, 105), Point(250, 180))
    Molecules.setFill("light blue")
    Molecules.draw(win)
    mol_label = Text(Point(165, 142.5), "Molecules")
    mol_label.setStyle("bold")
    mol_label.setSize(24)
    mol_label.setFill("black")
    mol_label.draw(win)

    Lipids = Rectangle(Point(315, 105), Point(485, 180))
    Lipids.setFill("light blue")
    Lipids.draw(win)
    lip_label = Text(Point(400, 142.5), "Lipids")
    lip_label.setStyle("bold")
    lip_label.setSize(24)
    lip_label.setFill("black")
    lip_label.draw(win)

    Meta = Rectangle(Point(550, 105), Point(720, 180))
    Meta.setFill("light blue")
    Meta.draw(win)
    met_label = Text(Point(635, 142.5), "Metabolites")
    met_label.setStyle("bold")
    met_label.setSize(24)
    met_label.setFill("black")
    met_label.draw(win)

    Proteins = Rectangle(Point(80, 240), Point(250, 315))
    Proteins.setFill("light blue")
    Proteins.draw(win)
    pro_label = Text(Point(165, 277.5), "Proteins")
    pro_label.setStyle("bold")
    pro_label.setSize(24)
    pro_label.setFill("black")
    pro_label.draw(win)

    Cells = Rectangle(Point(315, 240), Point(480, 315))
    Cells.setFill("light blue")
    Cells.draw(win)
    cel_label = Text(Point(400, 277.5), "Cells")
    cel_label.setStyle("bold")
    cel_label.setSize(24)
    cel_label.setFill("black")
    cel_label.draw(win)

    Regions = Rectangle(Point(550, 240), Point(720, 315))
    Regions.setFill("light blue")
    Regions.draw(win)
    reg_label = Text(Point(635, 277.5), "Regions")
    reg_label.setStyle("bold")
    reg_label.setSize(24)
    reg_label.setFill("black")
    reg_label.draw(win)

    # Create and draw buttons for Edit, Help, and Query functionalities
    Edit = Rectangle(Point(80, 375), Point(250, 450))
    Edit.setFill("#FF3131")
    Edit.draw(win)
    edi_label = Text(Point(165, 412.5), "Edit")
    edi_label.setStyle("bold")
    edi_label.setSize(24)
    edi_label.setFill("black")
    edi_label.draw(win)

    Help = Rectangle(Point(315, 375), Point(480, 450))
    Help.setFill("yellow")
    Help.draw(win)
    hel_label = Text(Point(400, 412.5), "??? Help")
    hel_label.setStyle("bold")
    hel_label.setSize(24)
    hel_label.setFill("black")
    hel_label.draw(win)

    Query = Rectangle(Point(550, 375), Point(720, 450))
    Query.setFill("#7CFC00")
    Query.draw(win)
    que_label = Text(Point(635, 412.5), "Query")
    que_label.setStyle("bold")
    que_label.setSize(24)
    que_label.setFill("black")
    que_label.draw(win)

    # Store all graphical elements in a list
    graphics = [Molecules, Lipids, Proteins, Cells, Meta, Regions, Edit, Help, Query, Header, 
                mol_label, lip_label, pro_label, cel_label, met_label, reg_label, edi_label, hel_label, que_label]

    # Return the window object and the list of graphical elements
    return win, graphics

# Function to check if a rectangle was clicked
def clicked(click, rect):
    # If there is no click event, return False
    if not click:
        return False
    # Get the coordinates of the click event
    mx, my = click.getX(), click.getY()
    # Get the coordinates of the rectangle's corners
    x1, y1 = rect.getP1().getX(), rect.getP1().getY()
    x2, y2 = rect.getP2().getX(), rect.getP2().getY()

    # Return True if the click is inside the rectangle, otherwise False
    return (x1 < mx < x2) and (y1 < my < y2)


# Function to handle search page interactions
def search_page(form, win, graphics, query_list):
    # Dictionary to map form types to their input fields
    inputs = {
        'Molecules': ('Name', 'SMILES', 'InChi Key', 'LopP'),
        'Lipids': ('Name', 'Category', 'LM ID', 'Mass'),
        'Proteins': ('ID', 'Family', 'Domain', 'Disease', 'Mass'),
        'Cells': ('Type', 'Size'),
        'Metabolites': ('SMILES', 'Biospecimen', 'Mass'),
        'Regions': ('Cerebellum', 'Contrical Subplate', 'Fiber Tracts', 'Hindbrain', 'Hipocampal Region')
    }

    # Remove all previous graphical elements from the window
    click = win.checkMouse()
    for graphic in graphics:
        graphic.undraw()

    # Create form label
    form_label = Text(Point(400, 70), form)
    form_label.setStyle("bold italic")
    form_label.setSize(35)
    form_label.setFill("black")
    form_label.draw(win)

    # Create Back button
    Back = Rectangle(Point(80, 375), Point(250, 450))
    Back.setFill("#FF3131")
    Back.draw(win)
    back_label = Text(Point(165, 412.5), "Back")
    back_label.setStyle("bold")
    back_label.setSize(24)
    back_label.setFill("black")
    back_label.draw(win)
    
    # Create Submit button
    Submit = Rectangle(Point(315, 375), Point(480, 450))
    Submit.setFill("#7CFC00")
    Submit.draw(win)
    sub_label = Text(Point(400, 412.5), "Submit")
    sub_label.setStyle("bold")
    sub_label.setSize(24)
    sub_label.setFill("black")
    sub_label.draw(win)

    # Create Add button
    Add = Rectangle(Point(550, 375), Point(720, 450))
    Add.setFill("cyan")
    Add.draw(win)
    Add_label = Text(Point(635, 412.5), "Add")
    Add_label.setStyle("bold")
    Add_label.setSize(24)
    Add_label.setFill("black")
    Add_label.draw(win)

    # Create dropdown menu for selection
    selection = StringVar()
    selection.set("Select Search Term")
    drop = OptionMenu(win, selection, *inputs[form])
    drop.config(width=16, direction='right')
    drop.place(x=75, y=80)

    # Create input boxes and radio buttons based on form type
    if form != "Regions":
        # Main input box
        mainBox = Entry(Point(400, 250), 38)
        mainBox.setSize(24)
        mainBox.draw(win)
        
        # Labels for 'or' and 'and'
        or_label = Text(Point(400, 285), "or")
        or_label.setSize(24)
        or_label.setFill("black")
        or_label.draw(win)

        and_label = Text(Point(495, 320), "and")
        and_label.setSize(24)
        and_label.setFill("black")
        and_label.draw(win)

        # Additional input boxes for 'and' condition
        leftBox = Entry(Point(355, 320), 12)
        leftBox.setSize(24)
        leftBox.draw(win)

        rightBox = Entry(Point(635, 320), 12)
        rightBox.setSize(24)
        rightBox.draw(win)

        # Radio buttons for selecting conditions
        push = IntVar()
        push.set('1')
        Equal = Radiobutton(win, text="Equal To", variable = push, value=1, font=(None, 20))
        Equal.place(x=80, y=170)
        Less = Radiobutton(win, text="Less Than", variable = push, value=2, font=(None, 20))
        Less.place(x=315, y=170)
        Greater = Radiobutton(win, text="Greater Than", variable = push, value=3, font=(None, 20))
        Greater.place(x=545, y=170)
        Between = Radiobutton(win, text="Between", variable = push, value=4, font=(None, 20))
        Between.place(x=90, y=298)

    # Handle click events
    while not clicked(click, Back) and not clicked(click, Add):
        click = win.checkMouse()

        if clicked(click, Add):
            if selection.get() != "Select Seach Term":
                if form == "Regions":
                    query_list.append(str(form + ": " + selection.get()))
                elif push.get() == 1:
                    if mainBox.getText() != "":
                        query_list.append(str(form + ": " + selection.get() +  " = " + mainBox.getText()))
                    else:
                        click = False
                elif push.get() == 2:
                    if mainBox.getText() != "":
                        query_list.append(str(form + ": " + selection.get() + " < " + mainBox.getText()))
                    else:
                        click = False
                elif push.get() == 3:
                    if mainBox.getText() != "":
                        query_list.append(str(form + ": " + selection.get() + " > " + mainBox.getText()))
                    else:
                        click = False
                else:
                    if leftBox.getText() != "" and rightBox.getText() != "":
                        query_list.append(str(form + ": " + leftBox.getText() + " < " + selection.get() + " < " + rightBox.getText()))
                    else:
                        click = False
            else:
                click = False
        if clicked(click, Submit):
            search(query_list)

    form_label.undraw()
    Back.undraw()
    back_label.undraw()
    Add.undraw()
    Add_label.undraw()
    Submit.undraw()
    sub_label.undraw()
    drop.place_forget()
    
    if form != "Regions":
        mainBox.undraw()
        or_label.undraw()
        and_label.undraw()
        leftBox.undraw()
        rightBox.undraw()
        Equal.place_forget()
        Less.place_forget()
        Greater.place_forget()
        Between.place_forget()
    
    for graphic in graphics:
        graphic.draw(win)

    return query_list


# Display all entered queries with Back, Clear, and Submit buttons
def query_display(win, graphics, query_list):
    click = win.checkMouse()
    for graphic in graphics:
        graphic.undraw()

    form_label = Text(Point(400, 70), "Current Search Query")
    form_label.setStyle("bold italic")
    form_label.setSize(35)
    form_label.setFill("black")
    form_label.draw(win)

    Back = Rectangle(Point(80, 375), Point(250, 450))
    Back.setFill("#FF3131")
    Back.draw(win)
    back_label = Text(Point(165, 412.5), "Back")
    back_label.setStyle("bold")
    back_label.setSize(24)
    back_label.setFill("black")
    back_label.draw(win)

    Clear = Rectangle(Point(315, 375), Point(480, 450))
    Clear.setFill("#FF3131")
    Clear.draw(win)
    cle_label = Text(Point(400, 412.5), "Clear")
    cle_label.setStyle("bold")
    cle_label.setSize(24)
    cle_label.setFill("black")
    cle_label.draw(win)

    Submit = Rectangle(Point(550, 375), Point(720, 450))
    Submit.setFill("#7CFC00")
    Submit.draw(win)
    sub_label = Text(Point(635, 412.5), "Submit")
    sub_label.setStyle("bold")
    sub_label.setSize(24)
    sub_label.setFill("black")
    sub_label.draw(win)

    text_display = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=62, height=9, font=("Times New Roman", 20))
    text_display.place(x=80, y=110)
    for query in query_list:
        text_display.insert(INSERT, str(query))
        text_display.insert(INSERT, "\n")
    text_display.config(state=DISABLED, highlightbackground="gray")
    

    while not clicked(click, Back):
        click = win.checkMouse()
        if clicked(click, Submit):
            search(query_list)
        if clicked(click, Clear):
            query_list = []
            text_display.config(state=NORMAL)
            text_display.delete(1.0,END)
            for query in query_list:
                text_display.insert(INSERT, str(query))
                text_display.insert(INSERT, "\n")
            text_display.config(state=DISABLED)

    form_label.undraw()
    Back.undraw()
    back_label.undraw()
    Submit.undraw()
    sub_label.undraw()
    Clear.undraw()
    cle_label.undraw()
    text_display.place_forget()

    for graphic in graphics:
        graphic.draw(win)

    return query_list


# Allow user to delete inputted queries or clear all
def edit_page(win, graphics, query_list):
    click = win.checkMouse()
    for graphic in graphics:
        graphic.undraw()

    Back = Rectangle(Point(80, 375), Point(250, 450))
    Back.setFill("#FF3131")
    Back.draw(win)
    back_label = Text(Point(165, 412.5), "Back")
    back_label.setStyle("bold")
    back_label.setSize(24)
    back_label.setFill("black")
    back_label.draw(win)

    Clear = Rectangle(Point(315, 375), Point(480, 450))
    Clear.setFill("#FF3131")
    Clear.draw(win)
    cle_label = Text(Point(400, 412.5), "Clear")
    cle_label.setStyle("bold")
    cle_label.setSize(24)
    cle_label.setFill("black")
    cle_label.draw(win)

    Delete = Rectangle(Point(550, 375), Point(720, 450))
    Delete.setFill("#FF3131")
    Delete.draw(win)
    del_label = Text(Point(635, 412.5), "Delete")
    del_label.setStyle("bold")
    del_label.setSize(24)
    del_label.setFill("black")
    del_label.draw(win)

    selection = StringVar()
    selection.set("Select query to delete")
    if query_list == []:
        drop = OptionMenu(win, selection, "Add query to list before editing")
    else:
        drop = OptionMenu(win, selection, *query_list)
    drop.place(x=75, y=80)

    edit_label = Text(Point(400, 220), "")
    edit_label.setSize(25)
    edit_label.setFill("black")
    edit_label.draw(win)

    while not clicked(click, Back) and not clicked(click, Delete) and not clicked(click, Clear):
        click = win.checkMouse()
        edit_label.setText("Delete: \n\n" + selection.get())
        if clicked(click, Delete):
            if selection.get() in query_list:
                query_list.remove(selection.get())
            else:
                click = False
        if clicked(click, Clear):
            query_list = []
    
    Back.undraw()
    back_label.undraw()
    Clear.undraw()
    cle_label.undraw()
    Delete.undraw()
    del_label.undraw()
    edit_label.undraw()
    drop.place_forget()
    
    for graphic in graphics:
        graphic.draw(win)

    return query_list


# Display helpful instructions of program
def help_display(win, graphics):
    click = win.checkMouse()
    for graphic in graphics:
        graphic.undraw()

    help_label = Text(Point(400, 200), "This is the help instruction page\nThis is the help instruction")
    help_label.setSize(25)
    help_label.setFill("black")
    help_label.draw(win)

    Back = Rectangle(Point(80, 375), Point(250, 450))
    Back.setFill("#FF3131")
    Back.draw(win)
    back_label = Text(Point(165, 412.5), "Back")
    back_label.setStyle("bold")
    back_label.setSize(24)
    back_label.setFill("black")
    back_label.draw(win)


    while not clicked(click, Back):
        click = win.checkMouse()
    
    help_label.undraw()
    Back.undraw()
    back_label.undraw()
    
    for graphic in graphics:
        graphic.draw(win)


# Submit inputted queries into search
def search(query):
    print(query)


def main():
    win, graphics = Window()
    query_list = []
    boxes = graphics[:9]
    print(boxes)

    while True:
        click = win.checkMouse()
        for i in range(len(boxes)):
            if clicked(click, boxes[i]):
                if i < 6:
                    query_list = search_page(graphics[i+10].getText(), win, graphics, query_list)
                elif i == 6:
                    query_list = edit_page(win, graphics, query_list)
                elif i == 7:
                    help_display(win, graphics)
                else:
                    query_list = query_display(win, graphics, query_list)


main()
