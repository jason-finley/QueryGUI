from tkinter import DISABLED, END, INSERT, Radiobutton, OptionMenu, StringVar, scrolledtext, IntVar
from tkinter.font import NORMAL
from graphics import *
from processing import search

# Function to create the main window with GUI elements
def Window():
    win = GraphWin("GUI", 800, 500)  # Create a window with title "GUI" and dimensions 800x500
    win.setBackground("white")  # Set the background color to white

    # Create and draw the title text
    Title = Text(Point(400, 30), "BICCN - 3D Brain Mapping")
    Title.setSize(24)
    Title.setFill("black")
    Title.draw(win)

    # Create and draw the header text
    Header = Text(Point(400, 70), "Select a Search Term")
    Header.setSize(24)
    Header.setFill("black")
    Header.draw(win)

    # Create and draw the button for "Molecules"
    Molecules = Rectangle(Point(80, 105), Point(250, 180))
    Molecules.setFill("light blue")
    Molecules.draw(win)
    mol_label = Text(Point(165, 142.5), "Molecules")
    mol_label.setStyle("bold")
    mol_label.setSize(24)
    mol_label.setFill("black")
    mol_label.draw(win)

    # Create and draw the button for "Lipids"
    Lipids = Rectangle(Point(315, 105), Point(485, 180))
    Lipids.setFill("light blue")
    Lipids.draw(win)
    lip_label = Text(Point(400, 142.5), "Lipids")
    lip_label.setStyle("bold")
    lip_label.setSize(24)
    lip_label.setFill("black")
    lip_label.draw(win)

    # Create and draw the button for "Metabolites"
    Meta = Rectangle(Point(550, 105), Point(720, 180))
    Meta.setFill("light blue")
    Meta.draw(win)
    met_label = Text(Point(635, 142.5), "Metabolites")
    met_label.setStyle("bold")
    met_label.setSize(24)
    met_label.setFill("black")
    met_label.draw(win)

    # Create and draw the button for "Proteins"
    Proteins = Rectangle(Point(80, 240), Point(250, 315))
    Proteins.setFill("light blue")
    Proteins.draw(win)
    pro_label = Text(Point(165, 277.5), "Proteins")
    pro_label.setStyle("bold")
    pro_label.setSize(24)
    pro_label.setFill("black")
    pro_label.draw(win)

    # Create and draw the button for "Cells"
    Cells = Rectangle(Point(315, 240), Point(480, 315))
    Cells.setFill("light blue")
    Cells.draw(win)
    cel_label = Text(Point(400, 277.5), "Cells")
    cel_label.setStyle("bold")
    cel_label.setSize(24)
    cel_label.setFill("black")
    cel_label.draw(win)

    # Create and draw the button for "Regions"
    Regions = Rectangle(Point(550, 240), Point(720, 315))
    Regions.setFill("light blue")
    Regions.draw(win)
    reg_label = Text(Point(635, 277.5), "Regions")
    reg_label.setStyle("bold")
    reg_label.setSize(24)
    reg_label.setFill("black")
    reg_label.draw(win)

    # Create and draw the button for "Edit"
    Edit = Rectangle(Point(80, 375), Point(250, 450))
    Edit.setFill("#FF3131")
    Edit.draw(win)
    edi_label = Text(Point(165, 412.5), "Edit")
    edi_label.setStyle("bold")
    edi_label.setSize(24)
    edi_label.setFill("black")
    edi_label.draw(win)

    # Create and draw the button for "Help"
    Help = Rectangle(Point(315, 375), Point(480, 450))
    Help.setFill("yellow")
    Help.draw(win)
    hel_label = Text(Point(400, 412.5), "??? Help")
    hel_label.setStyle("bold")
    hel_label.setSize(24)
    hel_label.setFill("black")
    hel_label.draw(win)

    # Create and draw the button for "Query"
    Query = Rectangle(Point(550, 375), Point(720, 450))
    Query.setFill("#7CFC00")
    Query.draw(win)
    que_label = Text(Point(635, 412.5), "Query")
    que_label.setStyle("bold")
    que_label.setSize(24)
    que_label.setFill("black")
    que_label.draw(win)

    # Store all graphics elements in a list and return the window and graphics list
    graphics = [Molecules, Lipids, Proteins, Cells, Meta, Regions, Edit, Help, Query, Header, 
                mol_label, lip_label, pro_label, cel_label, met_label, reg_label, edi_label, hel_label, que_label]

    return win, graphics

# Function to check if a click is within a specified rectangle
def clicked(click, rect):
    if not click:
        return False
    mx, my = click.getX(), click.getY()
    x1, y1 = rect.getP1().getX(), rect.getP1().getY()
    x2, y2 = rect.getP2().getX(), rect.getP2().getY()

    return (x1 < mx < x2) and (y1 < my < y2)

# Function to handle the search page and form for input
def search_page(form, win, graphics, query_list):
    inputs = {
        'Molecules': ('Name', 'SMILES', 'InChi Key', 'LopP'),
        'Lipids': ('Name', 'Category', 'LM ID', 'Mass'),
        'Proteins': ('ID', 'Family', 'Domain', 'Disease', 'Mass'),
        'Cells': ('Type', 'Size'),
        'Metabolites': ('SMILES', 'Biospecimen', 'Mass'),
        'Regions': ('Cerebellum', 'Contrical Subplate', 'Fiber Tracts', 'Hindbrain', 'Hipocampal Region')
    }

    click = win.checkMouse()
    for graphic in graphics:
        graphic.undraw()

    form_label = Text(Point(400, 70), form)
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

    Add = Rectangle(Point(550, 375), Point(720, 450))
    Add.setFill("cyan")
    Add.draw(win)
    Add_label = Text(Point(635, 412.5), "Add")
    Add_label.setStyle("bold")
    Add_label.setSize(24)
    Add_label.setFill("black")
    Add_label.draw(win)

    Submit = Rectangle(Point(315, 375), Point(480, 450))
    Submit.setFill("#7CFC00")
    Submit.draw(win)
    sub_label = Text(Point(400, 412.5), "Submit")
    sub_label.setStyle("bold")
    sub_label.setSize(24)
    sub_label.setFill("black")
    sub_label.draw(win)

    selection = StringVar()
    selection.set("Select Seach Term")
    drop = OptionMenu(win, selection, *inputs[form])
    drop.config(width=16, direction='right')
    drop.place(x=75, y=80)

    if form != "Regions":
        mainBox = Entry(Point(400, 250), 46)
        mainBox.setSize(24)
        mainBox.draw(win)
        
        or_label = Text(Point(400, 285), "or")
        or_label.setSize(24)
        or_label.setFill("black")
        or_label.draw(win)

        and_label = Text(Point(495, 320), "and")
        and_label.setSize(24)
        and_label.setFill("black")
        and_label.draw(win)

        leftBox = Entry(Point(355, 320), 12)
        leftBox.setSize(24)
        leftBox.draw(win)

        rightBox = Entry(Point(635, 320), 12)
        rightBox.setSize(24)
        rightBox.draw(win)

        push = IntVar()
        push.set('1')
        Equal = Radiobutton(win, text="Equal To", variable = push, value=1, font=(None, 20))
        Equal.place(x=80, y=200)
        Less = Radiobutton(win, text="Less Than", variable = push, value=2, font=(None, 20))
        Less.place(x=330, y=200)
        Greater = Radiobutton(win, text="Greater Than", variable = push, value=3, font=(None, 20))
        Greater.place(x=580, y=200)
        Between = Radiobutton(win, text="Between", variable = push, value=4, font=(None, 20))
        Between.place(x=830, y=200)

        while True:
            click = win.checkMouse()
            if clicked(click, Add):
                query_list.append(f"{selection.get()} = {mainBox.getText()}")
                print(f"{selection.get()} = {mainBox.getText()}")
            elif clicked(click, Back):
                for graphic in graphics:
                    graphic.draw(win)
                break
            elif clicked(click, Submit):
                query_list.append(f"{selection.get()} = {mainBox.getText()}")
                print(f"{selection.get()} = {mainBox.getText()}")
                query_list.append("")
                search(query_list)
    else:
        drop.place(x=260, y=100)
        description = scrolledtext.ScrolledText(win, wrap='word', height=7, width=65, font=(None, 24))
        description.insert(INSERT, "Please enter a description")
        description.place(x=200, y=175)

        while True:
            click = win.checkMouse()
            if clicked(click, Back):
                for graphic in graphics:
                    graphic.draw(win)
                break
            elif clicked(click, Submit):
                query_list.append(f"{selection.get()} = {description.get('1.0', END)}")
                query_list.append("")
                search(query_list)
