import customtkinter as ctk 
import tkinter as tk
from tkinter import *
from PIL import Image 
from tkinter import filedialog
from PIL.Image import open as open_image
import customtkinter as c
import zipfile
import shutil
import os
import random
import pandas as pandasForSortingCSV
import tkinter.messagebox as tmsg
from tkinter import messagebox
import pandas as pd 
import csv


global color


color = "#f2debf"   
drop2  = None

if not os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\" ) :
    
    path = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"
    os.chdir(path)
    Newfolder =  "Data Entry"
    os.makedirs(Newfolder)

class SlidePanel(ctk.CTkFrame):
     
	def __init__(self, parent, start_pos, end_pos):
		super().__init__(master = parent ,  fg_color="#fde8c6"  )

		# general attributes 
		self.start_pos = start_pos + 0.44
		self.end_pos = end_pos +0.19
		self.width = abs(start_pos - end_pos - 0.14 )
       
		# animation logic
		self.pos = self.start_pos
		self.in_start_pos = True

		# layout
		self.place(relx = self.start_pos, rely = 0.15, relwidth = self.width, relheight = 20 )
	
	def animate(self):
		if self.in_start_pos:
			self.animate_forward()
		else:
			self.animate_backwards()

	def animate_forward(self):
     
			
		if self.pos > self.end_pos:
			self.pos -= 0.036
			self.place(relx = self.pos, rely = 0.15, relwidth = self.width, relheight = 20)
			self.after(1, self.animate_forward)
		else:
			self.in_start_pos = False

	def animate_backwards(self):
		if self.pos < self.start_pos:
			self.pos += 0.036
			self.place(relx = self.pos, rely = 0.15, relwidth = self.width, relheight = 20)
			self.after(1, self.animate_backwards)
		else:
			self.in_start_pos = True
def move_btn():
	global button_x
	button_x += 0.001
	button.place(relx = button_x, rely = 0.5, anchor = 'center')
	
	if button_x < 0.9:
		root.after(10, move_btn)
  
  
def infinite_print():
	global button_x
	button_x += 0.5
	if button_x < 10:
		
		root.after(100, infinite_print)
  
global frame1

root = ctk.CTk()
root.geometry("1500x1100+10+30")
root.config(background="papayawhip")

root.resizable( True , True )

f1 = Frame(root, bg = "tan1", borderwidth=10, relief=RIDGE)
f1.pack(side=TOP, fill="x")

frame1 = ctk.CTkFrame(root , width = 1000 , bg_color = "papayawhip" , fg_color = "papayawhip" )
frame1.pack()

frame2 = ctk.CTkFrame(root , width = 1000 , bg_color = "papayawhip" , fg_color = "papayawhip" )
frame2.pack()



#frame1.pack()
my_font = ctk.CTkFont(family="Comicsansms", size=25+5 , weight = "bold")
my_font3 = ctk.CTkFont(family="Comicsansms", size=15 , weight = "bold")

W = ctk.CTkLabel ( f1 , text ="Ascent Investment                                                                      "  , text_color = "white" , fg_color = "tan1" , font = my_font)
W.pack(side = "right" , pady = 20)

Image0 = ctk.CTkImage(Image.open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Icons\\Home_ICON_1.png").resize((40,40) ))
Image1 = ctk.CTkImage(Image.open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Icons\\Register_ICON_1.png").resize((40,40) ))
Image2 = ctk.CTkImage(Image.open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Icons\\Report_ICON_2.png").resize((40,40) ))
Image3 = ctk.CTkImage(Image.open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Icons\\Report_ICON_2.png").resize((40,40) ))
Image4 = ctk.CTkImage(Image.open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Icons\\Delete_ICON_1.png").resize((40,40) ))
Image5 = ctk.CTkImage(Image.open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Icons\\Report_ICON_2.png").resize((40,40) ))
Image6 = ctk.CTkImage(Image.open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Icons\\ShowDetails_ICON_1.png").resize((40,40) ))







def sorting_searching( Tab_Name ,  X , Y ):
    
    global Name_Value
     
    
    NAME= []   
    def get_folder_names(folder_path):
            folder_names = []
            for entry in os.scandir(folder_path):
                if entry.is_dir():
                    folder_names.append(entry.name)
                    
            folder_names.remove("Client Master")
            
            return folder_names

        # Provide the path of the folder you want to read the folder names from
    folder_path = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry"

    folder_names = get_folder_names(folder_path)
    
    for name in folder_names:
        name = name[0:len(name) -1]
        NAME.append(name)
    
    
    def select_option(event):
        selected_index = dropdown_listbox.curselection()
        selected_option = dropdown_listbox.get(selected_index)
        
        
        
        Name_Value.delete(0, tk.END)
        Name_Value.insert(0, selected_option)
        
        if dropdown_frame.winfo_exists():
            dropdown_frame.grid_forget()
    def filter_names(initial):
        dropdown_listbox.delete(0, tk.END)
        for name in names:
            if name.startswith(initial):
                dropdown_listbox.insert(tk.END, name)

    def search_names():
        
        
        if dropdown_frame.winfo_ismapped( ):
            pass
        else:
            
            dropdown_frame.grid(row= 1, column = 0 , columnspan = 2  ,pady = 5 )  
        
        search_query = Name_Value.get().lower()
        dropdown_listbox.delete(0, tk.END)
        
        
    
        
        
        
        def prioritize_list(input_list, input_letter):
            sorted_list = []
            
            # Filter and prioritize words with the input letter
            for word in input_list:
                if input_letter.lower() in word.lower():
                    sorted_list.append(word)
            
            # Sort the filtered list based on letter positions and alphabetical order
            sorted_list.sort(key=lambda x: (x.split()[0].lower(), x.lower().index(input_letter.lower()), x))
            
            return sorted_list

        # List of first names
        first_names = names
        sample_size = len(first_names)
       
        input_list = random.sample(first_names, sample_size)

        input_letter = search_query
        output_list = prioritize_list(input_list, input_letter)
        
        for name in output_list:
            if search_query in name.lower():
                dropdown_listbox.insert(tk.END, name)        

    def toggle_dropdown():
        if dropdown_frame.winfo_ismapped( ):
            dropdown_frame.grid_forget()
        else:
            
            dropdown_frame.grid(row= 1, column = 0 , columnspan = 2  ,pady = 5 )  
            
            for name in names:
                dropdown_listbox.insert(tk.END, name)
   

    
    frame = tk.Frame(tab.tab(Tab_Name), background= "#f2debf"  )
    frame.grid(row  = X +1 , column = Y)
    # Create the dropdown button
    dropdown_button = ctk.CTkButton(frame, text="Select a name", width=10, command=toggle_dropdown , fg_color= "red" ,  bg_color="#f7e7ce" , hover_color= "#ad0303" )
    dropdown_button.grid( padx  = 5 , row = 0 , column = 0)


    # Create the search button
    search_button = ctk.CTkButton(frame, text="Search", command=search_names , width = 10, fg_color= "red" ,  bg_color="#f7e7ce" , hover_color= "#ad0303" )
    search_button.grid(row = 0 , column = 1 , padx  = 5 , pady  = 5)


    # Create the dropdown frame
    dropdown_frame = ctk.CTkFrame(frame , height= 15)

    # Create the scrollbar for the buttons
    buttons_scrollbar = tk.Scrollbar(dropdown_frame, orient="vertical" ,  cursor = "hand2")
    buttons_scrollbar.pack(side="right", fill="y")

    # Create the canvas for the buttons
    buttons_canvas = tk.Canvas(dropdown_frame, yscrollcommand=buttons_scrollbar.set, width=30, height=200)
    buttons_canvas.pack(side="left", fill="both", expand=False)

    # Configure the scrollbar to work with the canvas
    buttons_scrollbar.config(command=buttons_canvas.yview)

    # Create the buttons frame
    buttons_frame = tk.Frame(buttons_canvas)

    # Add the buttons frame to the canvas
    buttons_canvas.create_window((0, 0), window=buttons_frame, anchor="nw" )

    # Configure the canvas to update scroll region
    buttons_frame.bind("<Configure>", lambda e: buttons_canvas.configure(scrollregion=buttons_canvas.bbox("all") , height= 120)  )

    # List of first names
    first_names = ["John", "Alice", "Michael", "Emma", "Daniel", "Olivia", "David", "Sophia", "James", "Isabella", "Ziana" ,"Naitik" , "Ajay" , "Tirthraj", "Brad" ,"LeoNardo","Alan" ,"James" , "Zia"]

    # List of last names
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Miller", "Anderson", "Thomas", "Jackson", "Harris", "Martin" ,"Pit" , "Washington" ,"Donald" ,"Carle"]

    # Generate 100 unique names
    names = NAME
    

    # Sort the names in alphabetical order
    names.sort()

    # Create buttons for each unique initial
    initials = set(name[0] for name in names)

    for initial in sorted(initials):
        button = ctk.CTkButton(buttons_frame, text=initial, width=2, command=lambda i=initial: filter_names(i) , fg_color= "red" , hover_color= "#ad0303" )
        button.pack(side="top", padx=2, pady=2)

    # Add a scrollbar to the listbox
    listbox_scrollbar = tk.Scrollbar(dropdown_frame, orient="vertical" , cursor = "hand2" )
    dropdown_listbox = tk.Listbox(dropdown_frame, yscrollcommand=listbox_scrollbar.set, height=4 , background="papayawhip" , font = "Comicsansms 12" , cursor = "hand2" , width= 15)
    listbox_scrollbar.config(command=dropdown_listbox.yview)

    # Pack the listbox and scrollbar
    dropdown_listbox.pack(side="left", fill="both", expand=False)
    listbox_scrollbar.pack(side="right", fill="y")



    # Create the search entry
    Name_Value = ctk.CTkEntry(tab.tab(Tab_Name), width=150 , placeholder_text_color="black" , placeholder_text= "Select Name of Client" , border_color= "red", bg_color="#f7e7ce" )
    Name_Value.grid(row = X  , column = Y)
    #Name_Value.insert(0,"Select Name of Client")

    
    # Bind the select_option function to the listbox
    dropdown_listbox.bind("<<ListboxSelect>>", select_option)

    # Hide the dropdown frame initially
    dropdown_frame.grid_forget()
    
    dropdown_frame.configure(height = 35)
    
    def forgot():
        if dropdown_frame.winfo_ismapped( ):
            dropdown_frame.grid_forget()
        
        
    #root.bind("<Button-1>", lambda event : forgot())
    root.bind("<Button-3>", lambda event : forgot())
    
def sorting_searching1( Tab_Name ,  X , Y ):
    
    global Name1_Value
     
    
    NAME= []   
    def get_folder_names(folder_path):
            folder_names = []
            for entry in os.scandir(folder_path):
                if entry.is_dir():
                    folder_names.append(entry.name)
                    
            folder_names.remove("Client Master")
            
            return folder_names

        # Provide the path of the folder you want to read the folder names from
    folder_path = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry"

    folder_names = get_folder_names(folder_path)
    
    for name in folder_names:
        name = name[0:len(name) -1]
        NAME.append(name)
    
    
    def select_option(event):
        selected_index = dropdown_listbox.curselection()
        selected_option = dropdown_listbox.get(selected_index)
         
        Name1_Value.delete(0, tk.END)
        Name1_Value.insert(0, selected_option)
        
        if dropdown_frame.winfo_exists():
            dropdown_frame.grid_forget()
    def filter_names(initial):
        dropdown_listbox.delete(0, tk.END)
        for name in names:
            if name.startswith(initial):
                dropdown_listbox.insert(tk.END, name)

    def search_names():
        
        
        if dropdown_frame.winfo_ismapped( ):
            pass
        else:
            dropdown_frame.grid(row= 1, column = 0 , columnspan = 2 , pady = 5 )
        
        search_query = Name1_Value.get().lower()
        dropdown_listbox.delete(0, tk.END)
        
        
    
        
        
        
        def prioritize_list(input_list, input_letter):
            sorted_list = []
            
            # Filter and prioritize words with the input letter
            for word in input_list:
                if input_letter.lower() in word.lower():
                    sorted_list.append(word)
            
            # Sort the filtered list based on letter positions and alphabetical order
            sorted_list.sort(key=lambda x: (x.split()[0].lower(), x.lower().index(input_letter.lower()), x))
            
            return sorted_list

        # List of first names
        first_names = names
        sample_size = len(first_names)
        
        input_list = random.sample(first_names, sample_size)

        input_letter = search_query
        output_list = prioritize_list(input_list, input_letter)
        
        for name in output_list:
            if search_query in name.lower():
                dropdown_listbox.insert(tk.END, name)        

    def toggle_dropdown():
        if dropdown_frame.winfo_ismapped( ):
            dropdown_frame.grid_forget()
        else:
            
            dropdown_frame.grid(row= 1, column = 0 , columnspan = 2  , pady = 5)  
            
            for name in names:
                dropdown_listbox.insert(tk.END, name)
   

    
    frame = tk.Frame(tab.tab(Tab_Name), background= "#f2debf"  )
    frame.grid(row  = X +1 , column = Y)
    # Create the dropdown button
    dropdown_button = ctk.CTkButton(frame, text="Select a name", width=10, command=toggle_dropdown , fg_color= "red" ,  bg_color="#f7e7ce" , hover_color= "#ad0303" )
    dropdown_button.grid( padx  = 5 , row = 0 , column = 0)


    # Create the search button
    search_button = ctk.CTkButton(frame, text="Search", command=search_names , width = 10, fg_color= "red" ,  bg_color="#f7e7ce" , hover_color= "#ad0303" )
    search_button.grid(row = 0 , column = 1 , padx  = 5 , pady  = 5)


    # Create the dropdown frame
    dropdown_frame = ctk.CTkFrame(frame , height= 15)

    # Create the scrollbar for the buttons
    buttons_scrollbar = tk.Scrollbar(dropdown_frame, orient="vertical" ,  cursor = "hand2")
    buttons_scrollbar.pack(side="right", fill="y")

    # Create the canvas for the buttons
    buttons_canvas = tk.Canvas(dropdown_frame, yscrollcommand=buttons_scrollbar.set, width=30, height=200)
    buttons_canvas.pack(side="left", fill="both", expand=False)

    # Configure the scrollbar to work with the canvas
    buttons_scrollbar.config(command=buttons_canvas.yview)

    # Create the buttons frame
    buttons_frame = tk.Frame(buttons_canvas)

    # Add the buttons frame to the canvas
    buttons_canvas.create_window((0, 0), window=buttons_frame, anchor="nw" )

    # Configure the canvas to update scroll region
    buttons_frame.bind("<Configure>", lambda e: buttons_canvas.configure(scrollregion=buttons_canvas.bbox("all") , height= 120)  )

    # List of first names
    first_names = ["John", "Alice", "Michael", "Emma", "Daniel", "Olivia", "David", "Sophia", "James", "Isabella", "Ziana" ,"Naitik" , "Ajay" , "Tirthraj", "Brad" ,"LeoNardo","Alan" ,"James" , "Zia"]

    # List of last names
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Miller", "Anderson", "Thomas", "Jackson", "Harris", "Martin" ,"Pit" , "Washington" ,"Donald" ,"Carle"]

    # Generate 100 unique names
    names = NAME
    

    # Sort the names in alphabetical order
    names.sort()

    # Create buttons for each unique initial
    initials = set(name[0] for name in names)

    for initial in sorted(initials):
        button = ctk.CTkButton(buttons_frame, text=initial, width=2, command=lambda i=initial: filter_names(i) , fg_color= "red" , hover_color= "#ad0303" )
        button.pack(side="top", padx=2, pady=2)

    # Add a scrollbar to the listbox
    listbox_scrollbar = tk.Scrollbar(dropdown_frame, orient="vertical" , cursor = "hand2" )
    dropdown_listbox = tk.Listbox(dropdown_frame, yscrollcommand=listbox_scrollbar.set, height=4 , background="papayawhip" , font = "Comicsansms 12" , cursor = "hand2" , width= 15)
    listbox_scrollbar.config(command=dropdown_listbox.yview)

    # Pack the listbox and scrollbar
    dropdown_listbox.pack(side="left", fill="both", expand=False)
    listbox_scrollbar.pack(side="right", fill="y")



    # Create the search entry
    Name1_Value = ctk.CTkEntry(tab.tab(Tab_Name), width=150 , placeholder_text_color="black" , placeholder_text= "Select Name of Client" , border_color= "red", bg_color="#f7e7ce" )
    Name1_Value.grid(row = X  , column = Y)
    #Name_Value.insert(0,"Select Name of Client")

    
    # Bind the select_option function to the listbox
    dropdown_listbox.bind("<<ListboxSelect>>", select_option)

    # Hide the dropdown frame initially
    dropdown_frame.grid_forget()
    
    dropdown_frame.configure(height = 35)
    
    def forgot():
        if dropdown_frame.winfo_ismapped( ):
            dropdown_frame.grid_forget()
        
        
    #root.bind("<Button-1>", lambda event : forgot())
    root.bind("<Button-3>", lambda event : forgot())
    
    


def Home():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    my_font0 =  ctk.CTkFont(family="Comicsansms", size=30 , weight = "normal")
    my_font1 =  ctk.CTkFont(family="Comicsansms", size=20 , weight = "bold")
    
    
    def extract_group_name(filepath, substrings):
        for substring in substrings:
            if substring in filepath:
                return filepath.split(substring)[0]
        return None
    
    def categorize_files_by_substring(root_folder, substrings):
        categorized_files = {substring: [] for substring in substrings}
        none_files = []

        for foldername, _, filenames in os.walk(root_folder):
            for filename in filenames:
                if filename.lower().endswith(".csv"):
                    filepath = os.path.join(foldername, filename)
                    if "In Flow" in filename:
                        continue
                    
                    found_substring = False
                    for substring in substrings:
                        if substring in filename:
                            categorized_files[substring].append(filepath)
                            found_substring = True
                            break
                    if not found_substring:
                        none_files.append(filepath)

        # Sort the files in each list by their names
        for key in categorized_files:
            categorized_files[key].sort(key=lambda x: os.path.basename(x))

        none_files.sort(key=lambda x: os.path.basename(x))

        return categorized_files, none_files

    # Replace "Data Entry" with the path to your "Data Entry" folder on the desktop
    root_folder = r"C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry"

    substrings = ["TATA", "KOTAK", "NJ", "LIC"]
    categorized_files, none_files = categorize_files_by_substring(root_folder, substrings)

    # Group the files based on the strings that come before the company name and sum the lists
    grouped_files = {}
    for key in categorized_files:
        for file_path in categorized_files[key]:
            group_name = extract_group_name(file_path, substrings)
            if group_name not in grouped_files:
                grouped_files[group_name] = []
            grouped_files[group_name].append(file_path)

    # Sort the groups alphabetically and keep only the paths of CSV files in a flat list
    sorted_csv_files = sorted(file_path for group_files in grouped_files.values() for file_path in group_files if file_path.lower().endswith(".csv"))

    

    TATA = int(str((len(categorized_files['TATA']))))
    KOTAK = int(str((len(categorized_files['KOTAK']))))
    NJ = int(str((len(categorized_files['NJ']))))
    LIC = int(str((len(categorized_files['LIC']))))
    ALL_COMPANIES = TATA + KOTAK + NJ + LIC
    
    
    
    
    
    def Show_TreeView_TATA():
        
        
        
        
        my_tree.delete(*my_tree.get_children())
        
    
        count  = 0 
        

        Paths  = categorized_files["TATA"]

    
 
        my_tree["show"]   = "headings"

            
        for Path in Paths  :
            df  =  pd.read_csv(Path).iloc[:, :4]   

            df_rows = df.to_numpy().tolist()
            for rows in df_rows:
                if count % 2 == 0 :
                    my_tree.insert("" , "end" , values  = rows , tags  = "evenrow" )  
                else:
                    my_tree.insert("" , "end" , values  = rows , tags  = "oddrow" )  
            
                count+=1
        B1.configure(fg_color  = "red", border_color = "red" , border_width=2) 
        B2.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2)
        B3.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2)
        B4.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2)
        B5.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2)  

            
        
    def Show_TreeView_KOTAK():
        
        
        count  = 0 
        
        my_tree.delete(*my_tree.get_children())
        
    
        
        

        Paths  = categorized_files["KOTAK"]

    
        my_tree["show"]   = "headings"

            
            
        for Path in Paths  :
            df  =  pd.read_csv(Path).iloc[:, :4]   

            df_rows = df.to_numpy().tolist()
            for rows in df_rows:
                
                
                if count % 2 == 0 :
                    my_tree.insert("" , "end" , values  = rows , tags  = "evenrow" )  
                else:
                    my_tree.insert("" , "end" , values  = rows , tags  = "oddrow" )  
            
                count+=1
                
        B1.configure(fg_color  = color_treeview, border_color = "Maroon" , border_width=2) 
        B2.configure(fg_color = "red", border_color = "red" , border_width=2)
        B3.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2)
        B4.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2)
        B5.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2) 
    
        
    
    def Show_TreeView_NJ():
        
        
        count  = 0 
        
        my_tree.delete(*my_tree.get_children())
        
    
        
        

        Paths  = categorized_files["NJ"]

    
        my_tree["show"]   = "headings"

            
            
        for Path in Paths  :
            df  =  pd.read_csv(Path).iloc[:, :4]   

            df_rows = df.to_numpy().tolist()
            for rows in df_rows:
                if count % 2 == 0 :
                    my_tree.insert("" , "end" , values  = rows , tags  = "evenrow" )  
                else:
                    my_tree.insert("" , "end" , values  = rows , tags  = "oddrow" )  
            
                count+=1
                
        B1.configure(fg_color  = color_treeview, border_color = "Maroon" , border_width=2) 
        B2.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2)
        B3.configure(fg_color = "red", border_color = "red" , border_width=2)
        B4.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2)
        B5.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2)        
         
    
          
                            
    def Show_TreeView_LIC():
        
        count  = 0 
        
        
        my_tree.delete(*my_tree.get_children())
        
    
        
        

        Paths  = categorized_files["LIC"]

    
      
        my_tree["show"]   = "headings"

            
            
        for Path in Paths  :
            df  =  pd.read_csv(Path).iloc[:, :4]   

            df_rows = df.to_numpy().tolist()
            for rows in df_rows:
                if (count % 2 == 0 ):
                    my_tree.insert("" , "end" , values  = rows  , tags  = "evenrow")   
                else:
                    my_tree.insert("" , "end" , values  = rows  , tags  = "oddrow")   
                count+=1
                
        B1.configure(fg_color  = color_treeview, border_color = "Maroon" , border_width=2) 
        B2.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2)
        B3.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2)
        B4.configure(fg_color = "red", border_color = "red" , border_width=2)
        B5.configure(fg_color = color_treeview, border_color = "Maroon" , border_width=2) 

   
    
    def Show_TreeView_ALL_COMPANIES():
        
        global color_treeview
        
        count  = 0 
        
        my_tree.delete(*my_tree.get_children())
        
    
        
       
        
        
        Paths  = sorted_csv_files

    

        my_tree["show"]   = "headings"

            
            
        for Path in Paths  :
            df  =  pd.read_csv(Path).iloc[:, :4]   

            df_rows = df.to_numpy().tolist()
            for rows in df_rows:
                if count % 2 == 0 :
                    my_tree.insert("" , "end" , values  = rows , tags  = "evenrow" )  
                else:
                    my_tree.insert("" , "end" , values  = rows , tags  = "oddrow" )  
            
                count+=1
            
        color_treeview = "#df4c4c"
        
        B1.configure(fg_color  = color_treeview , border_color = "Maroon" , border_width=2) 
        B2.configure(fg_color =  color_treeview , border_color = "Maroon" , border_width=2)
        B3.configure(fg_color = color_treeview , border_color = "Maroon" , border_width=2)
        B4.configure(fg_color = color_treeview , border_color = "Maroon" , border_width=2)
        B5.configure(fg_color = "red", border_color = "red" , border_width=2) 
        
       
   
    
    L = ctk.CTkLabel(frame1 , text = "Welcome to Ascent Investment and Finicial Services !" , font=my_font0 )
    L.pack(pady  = 40)
    
    
    f = ctk.CTkFrame(frame1 , bg_color= "papayawhip"  , fg_color="papayawhip")
    f.pack(pady  =25)
    
    from tkinter import ttk
    import numpy 
    import pandas as pd 
    

    Frame_Net = ctk.CTkFrame(frame1  , fg_color="papayawhip"  )
    Frame_Net.pack()
    
    tree_Frame1 = ctk.CTkFrame( Frame_Net, border_color="red" , width  = 300 , border_width=6 , bg_color="papayawhip" , fg_color="#f7e7ce" )
    tree_Frame1.pack(side  = "top")

    B_Frame  = ctk.CTkFrame( Frame_Net  , fg_color="papayawhip"  )
    B_Frame.pack(side  = "bottom" , fill = X)
    
    
    tree_Frame  = ctk.CTkFrame(tree_Frame1 , width  = 270  , bg_color="papayawhip"  , fg_color="#f7e1bf" )
    tree_Frame.pack(padx  = 20 , pady  = 20 , side = "left")

    
    
    
    
    
    
    tree_Scroll = Scrollbar(tree_Frame  )
    tree_Scroll.pack(side = "right" , fill = Y , ipadx = 3 )


    my_tree = ttk.Treeview(tree_Frame  , yscrollcommand=tree_Scroll.set , cursor="hand2" , selectmode= "browse" , show  = "tree headings")
    my_tree.pack( )

    my_tree.heading("#0" , text = "\n"    )
    
    W = 180 +40
    A  = "center"
    
    my_tree["columns"] =  ("Name" , "Company" , "Plan" ,"Policy")
    
    my_tree.column("#0" , width  = 0 , stretch = YES)
    my_tree.column("Name",width  = W , anchor= A  )
    my_tree.column("Company",width  = W , anchor= A  )
    my_tree.column("Plan",width  = W , anchor= A  )
    my_tree.column("Policy",width  = W , anchor= A  )
    
    my_tree.heading("Name" , text  = "Name" , anchor  = A)
    my_tree.heading("Company" , text  = "Company" , anchor  = A)
    my_tree.heading("Plan" , text  = "Plan" , anchor  = A)
    my_tree.heading("Policy" , text  = "Policy" , anchor  = A)

    
    #Dark Color = #ccb99b 
    my_tree.tag_configure("evenrow" , background= "#f7e1bf")
    my_tree.tag_configure("oddrow" , background= "#f7e7ce"  )

    style = ttk.Style()
    style.theme_use("default")

    style.configure("Treeview",
                    background= "#f7e1bf" , # Set your desired background color here
                    foreground="black",
                    rowheight=50-20+5,
                    font=("Bold", 15) ,
                    fieldbackground  ="#f7e7ce"  ,
                    bordercolor  = "red"  ,borderwidth  = 1 )      # Set your desired foreground color here

    # Configure Treeview.Heading style (increase the font size)
    style.configure("Treeview.Heading",
                    font=("Bold", 20)  ,
                    rowheight = 30 ,
                    background  = "red" ,
                    foreground="white",
                    bordercolor  = "red",borderwidth  = 1 )  # Adjust the font size (you can change 12 to your desired value)


    style.map("Treeview" , background  = [("selected", "red")] , foreground  = [("selected", "white")] , bordercolor  = [("selected", "white")]  )

    style.map("Treeview.Heading" , background  = [("selected", "red")] , foreground  = [("selected", "white")] , bordercolor  = [("selected", "white")]  )


    tree_Scroll.configure(command=my_tree.yview)
    
    
    
    
    


    B1 = ctk.CTkButton(f , text  = " TATA - ( " + str(TATA) + " ) " , fg_color="red" , hover_color="#790606" , width  =60 , height=40 , text_color="white" , corner_radius=10 , font=my_font1 , command= Show_TreeView_TATA)
    B1.pack(side  = "left" , padx  = 6)
    
    B2 = ctk.CTkButton(f , text  = "KOTAK - ( " + str(KOTAK) + " ) ", fg_color="red" , hover_color="#790606", width  =60 , height=40 , text_color="white" , corner_radius=10 , font=my_font1, command= Show_TreeView_KOTAK)
    B2.pack(side  = "left" , padx  = 6)
    
    B3 = ctk.CTkButton(f , text  = " NJ - ( " + str(NJ) + " ) " , fg_color="red"  , hover_color="#790606" , width  =60 , height=40 , text_color="white" , corner_radius=10 , font=my_font1, command= Show_TreeView_NJ)
    B3.pack(side  = "left" , padx  = 6)
    
    B4 = ctk.CTkButton(f , text  = " LIC - ( " + str(LIC) + " ) " , fg_color="red"  , hover_color="#790606" , width  =60 , height=40 , text_color="white" , corner_radius=10 , font=my_font1, command= Show_TreeView_LIC)
    B4.pack(side  = "left" , padx  = 6)
    
    B5 = ctk.CTkButton(f , text  = " ALL - ( " + str( ALL_COMPANIES ) + " ) "   , fg_color="red"  , hover_color="#790606" , width  =60 , height=40 , text_color="white" , corner_radius=10 , font=my_font1  , command= Show_TreeView_ALL_COMPANIES)
    B5.pack(side  = "left" , padx  = 6)
    
    Show_TreeView_ALL_COMPANIES()
    
    

def setup_entry_widget(placeholder, limit, entry_widget):
        def on_entry_click(event):
            if entry_widget.get() == placeholder:
                entry_widget.delete(0, "end")
                entry_widget.configure(fg_color='white')
                if (limit == 4 ):
                    entry_widget.configure(text_color = "black")
                    entry_widget.insert(0, "20")
        def on_focus_out(event):
            if entry_widget.get() == "":
                entry_widget.insert(0, placeholder)
                entry_widget.configure(fg_color='white')

        def validate_input(new_value):
            return new_value == placeholder or (new_value.isdigit() and len(new_value) <= limit)

        def validate_and_set_color(event):
            value = entry_widget.get()
            if not value.isdigit() or not validate_input(value):
                entry_widget.delete(limit, tk.END)

        entry_widget.configure(fg_color='white')
        entry_widget.insert(0, placeholder)
        entry_widget.bind('<FocusIn>', on_entry_click)
        entry_widget.bind('<FocusOut>', on_focus_out)
        entry_widget.bind('<KeyRelease>', validate_and_set_color)


def Register():
    global tab , clicked2 , clicked1 , Name_Value , Money_Value , Day_Value , Month_Value , Amount_Val , Year_Val , Name_Val , DOB_Val1 , DOB_Value1 , Pan_Val , Name_Val , Name_Val1 ,  Name_Value1 , Year_Val , Year_Value , Adhar_Val , Email_Val , Email_Val1 , Email_Value , Email_Value1 
    global Money_Val , Name1_Value , Amount_Value , B_Year_Value , M_Year_Value , Mobile_Value_1 , Number_Val , Number_Value , Address_Val , Day1_Value , Month1_Value , Year1_Value
    
    
    for widget in frame1.winfo_children():
        widget.destroy()
        
        
    frame2.place_forget()
    
    color = "#f2debf"  
    tab = ctk.CTkTabview(frame1  ,  height=400 , border_color= "red" , border_width= 6  , corner_radius= 18 , bg_color="papayawhip" , fg_color= color , segmented_button_fg_color="red" , segmented_button_selected_color="#e06666", segmented_button_unselected_color="#f54747" , text_color="black" , segmented_button_unselected_hover_color="#f54747" , segmented_button_selected_hover_color="#e06666" )
    tab.pack(side = "left" , pady = 30 , padx = 2 )
    
    
    
    tab.add(" Register Client Master ")
    tab.add(" Register Client Policy " )
    tab.set(" Register Client Policy ")
    #tab.set(" Register Client Master ")
    
    f1 = Frame(tab.tab(" Register Client Policy "), width = 24 ,  bg = "red" ,  borderwidth=10, relief=RIDGE)
    f1.grid( row = 0 , column  = 3 , pady = 25 ,columnspan=2 )
    W = Label ( f1 , text ="  Register Client Policy  "  , width = 17+4   , fg = "White" , bg = "red" , font = ("comicsansms 22 bold"))
    W.pack()
    my_font1 =  ctk.CTkFont(family="Comicsansms", size=15 , weight = "bold")
    W = ctk.CTkLabel ( tab.tab(" Register Client Policy ") , corner_radius=10 , text ="Name of client"  , width = 160  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 1 , column=1 , pady = 15)
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Policy ") , corner_radius=10 ,  text ="Insurance Company"  , width = 160  , text_color = "White" , fg_color = "red" , font = my_font1 )
    W.grid(row = 3 , column=1, pady = 15)
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Policy ") , corner_radius=10 ,text ="Plan Name"   , width = 160  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 4 , column=1, pady = 15)
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Policy ") , corner_radius=10 , text ="Policy Number"  , width = 160  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 5 , column=1 , pady = 15 )
 
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Policy ") , corner_radius=10 , text ="Date"   , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 1 , column=3, pady = 15)
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Policy ") , corner_radius=10 ,  text ="Premium"  , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1 )
    W.grid(row = 2 , column=3, pady = 15)
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Policy ") , corner_radius=10 , text ="Number of Years"   , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 3 , column=3, pady = 15)
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Policy ") , corner_radius=10 , text ="Mode of Payment"   , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 4 , column=3, pady = 15)
    
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Policy ") , corner_radius=10 , text ="Year In Flow"   , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 1 , column=5, pady = 15  , padx = 15)
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Policy ") , corner_radius=10 , text ="Mony In Flow"   , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 2 , column=5, pady = 15 , padx = 15)
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Policy ") , corner_radius=10 , text ="Number of Years"   , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 3 , column=5, pady = 15 , padx = 15)
   
    
    Email_Value = ctk.CTkEntry( tab.tab(" Register Client Policy ") , border_color= "red" , border_width=2 , height=30 , width = 130, corner_radius= 15 , placeholder_text_color="black" , placeholder_text= " Plan Name")
    Email_Value.grid(row  = 4 , column = 2 , padx  = 5)
    
    Number_Value = ctk.CTkEntry( tab.tab(" Register Client Policy ") , border_color= "red" , border_width=2 , height=30 , width = 130, corner_radius= 15 , placeholder_text_color="black" , placeholder_text= " Policy Number")
    Number_Value.grid(row  = 5 , column = 2 , padx  = 5)
    
    
    
    

    
    Amount_Value = ctk.CTkEntry( tab.tab(" Register Client Policy ") , border_color= "red" , border_width=2 , height=30 , width = 130, corner_radius= 15 , placeholder_text_color="black" , placeholder_text= " Premium")
    Amount_Value.grid(row  = 2 , column = 4 )
    
    Number1_Value = ctk.CTkEntry( tab.tab(" Register Client Policy ") , border_color= "red" , border_width=2 , height=30 , width = 130, corner_radius= 15 , placeholder_text_color="black" , placeholder_text= " Number of Years ")
    Number1_Value.grid(row  = 3 , column = 4 )
    
    
    M_Year_Value = ctk.CTkEntry( tab.tab(" Register Client Policy ") , border_color= "red" , border_width=2 , height=30 , width = 130, corner_radius= 15 , placeholder_text_color="black" , placeholder_text= " Year (In Flow) ")
    M_Year_Value.grid(row  = 1 , column = 6 )
    
    Money_Value = ctk.CTkEntry( tab.tab(" Register Client Policy ") , border_color= "red" , border_width=2 , height=30 , width = 130, corner_radius= 15 , placeholder_text_color="black" , placeholder_text= " Money (In Flow) ")
    Money_Value.grid(row  = 2 , column = 6 )
    
    B_Year_Value = ctk.CTkEntry( tab.tab(" Register Client Policy ") , border_color= "red" , border_width=2 , height=30 , width = 130, corner_radius= 15 , placeholder_text_color="black" , placeholder_text= " Number of Years ")
    B_Year_Value.grid(row  = 3 , column = 6 )
    
    Button5 = ctk.CTkSwitch( tab.tab(" Register Client Policy ") , text = "Check it is Existing client",
                        bg_color=color,
                        progress_color= "red" ,
                        button_color= "black" ,
                        button_hover_color= "#444444" ,
                        fg_color= "white" ,
                        
                        onvalue = 1,
                        offvalue = 0,
                        height = 1,
                        width = 25 , border_color= "black" ,border_width=0  )
    
    Button5.grid(row = 5 , column=5 , columnspan = 2)
    
    
    
    
    options1 = ["TATA","KOTAK" ,"NJ" ,"LIC"]
  
    # datatype of menu text
    clicked1 = ctk.StringVar()
    
    # initial menu text
    clicked1.set( "  Select Company  " )
    
    # Create Dropdown menu
    drop1 = ctk.CTkOptionMenu(tab.tab(" Register Client Policy ")   , dynamic_resizing=False , variable = clicked1 , values= options1 , bg_color= color , fg_color= "white" , text_color= "black" , button_color= "red" , button_hover_color = "#ad0303" , dropdown_fg_color="white" , dropdown_hover_color="#f7e7ce" )
    drop1.grid(row = 3, column = 2)
    
    
    options2 = ["Yearly","Quarterly" ,"Monthly" ,"Half Yearly"]
  
    # datatype of menu text
    clicked2 = ctk.StringVar()
    
    # initial menu text
    clicked2.set( "  Select Mode  " )
    
   
    
    # Create Dropdown menu
    drop2 = ctk.CTkOptionMenu(tab.tab(" Register Client Policy "), dynamic_resizing=False , variable = clicked2 , values= options2 , bg_color= color , fg_color= "white" , text_color= "black" , button_color= "red" , button_hover_color = "#ad0303" , dropdown_fg_color="white" , dropdown_hover_color="#f7e7ce" )
    drop2.grid(row = 4, column = 4)

    
    

    H  = 15 + 5
    
    frame = ctk.CTkFrame( tab.tab(" Register Client Policy ") ,height = H  , bg_color = color , border_color="RED" , border_width=2 , corner_radius=10 , fg_color= "white" )
    frame.grid(row  = 1 , column = 4 , padx  = 0 , pady  = 0)

    Day_Value = ctk.CTkEntry(frame , border_color="white"  , placeholder_text_color="black" ,height = H   , width  = 35 , fg_color="WHITE" , corner_radius=5 )
    Month_Value = ctk.CTkEntry(frame, border_color="white" , placeholder_text_color="black" ,height = H  , fg_color="WHITE" , width  = 35 , corner_radius=5)
    Year_Value = ctk.CTkEntry(frame, border_color="white" , placeholder_text_color="black" ,height = H  ,fg_color="WHITE" , width  = 45  , corner_radius=5)


    label = ctk.CTkLabel(frame, text="" , fg_color="white"  ,height = H , bg_color="white")
    label1 = ctk.CTkLabel(frame, text="-" , fg_color="white" ,height = H  , bg_color="white")
    label2 = ctk.CTkLabel(frame, text="-" , fg_color="white" ,height = H  , bg_color="white")
    label3 = ctk.CTkLabel(frame, text="" , fg_color="white" ,height = H  , bg_color="white")

    setup_entry_widget("YYYY", 4, Year_Value)

    # Setup the second entry widget with placeholder "DD" and limit 2 digits
    setup_entry_widget("DD", 2, Day_Value)

    setup_entry_widget("MM", 2, Month_Value)
    
    setup_entry_widget(" Number of Years", 2, Number1_Value)

    # Setup the second entry widget with placeholder "DD" and limit 2 digits
    setup_entry_widget(" Year (In Flow)", 4, M_Year_Value)

    setup_entry_widget(" Number of Years", 2, B_Year_Value)


    label.pack(side = "left" , padx  = 3 , pady  =5)
    Day_Value.pack(side=tk.LEFT)
    label1.pack(side=tk.LEFT)
    Month_Value.pack(side=tk.LEFT)
    label2.pack(side=tk.LEFT)
    Year_Value.pack(side=tk.LEFT)
    label3.pack(side = tk.LEFT ,  padx  = 3 , pady  =5)
    
    def deselect_all():
    
        
        
        Name_Value.delete(0,END)
        Email_Value.delete(0, END)
        Number_Value.delete(0, END)
        Amount_Value.delete(0, END)
        Year_Value.delete(0, END)
        Number1_Value.delete(0, END)
        Money_Value.delete(0, END)
        B_Year_Value.delete(0,END)
        M_Year_Value.delete(0,END)
        Day_Value.delete(0, END)
        Month_Value.delete(0,END)
        Button5.deselect()
        
        clicked1.set("  Select Company  ")
        clicked2.set("  Select Mode  ")
        
        Email_Value.configure(placeholder_text= " Plan Name")
        Number_Value.configure(placeholder_text= " Policy Number ")
        Day_Value.configure(placeholder_text = "DD")
        Month_Value.configure(placeholder_text = "MM")
        Year_Value.configure(placeholder_text= "YYYY")
        
        Amount_Value.configure(placeholder_text= " Premium ")
        Number1_Value.configure(placeholder_text= " Number of Years ")
        M_Year_Value.configure(placeholder_text= " Years (In Flow) ")
        Money_Value.configure(placeholder_text= " Money (In Flow) ")
        B_Year_Value.configure(placeholder_text= " Number of Years ")
   
   
   
         
    #FOR TRIMMING VALUES   
    def Trim_Values():
        global Email_Val , Number_Val , Amount_Val , Day_Val , Month_Val , Year_Val , Number1_Val , Money_Val , M_Years_Val , B_Years_Val , Name_Val
        
        Name_Val = ' '.join((str(Name_Value.get())).split()).title()
        Email_Val  = ' '.join((str(Email_Value.get())).split()) 
        Number_Val = ' '.join((str(Number_Value.get())).split()) 
        Amount_Val = ' '.join((str(Amount_Value.get())).split()) 
        
        Year_Val = ' '.join((str(Year_Value.get())).split()) 
        Number1_Val = ' '.join((str(Number1_Value.get())).split()) 
        Money_Val = ' '.join((str(Money_Value.get())).split()) 
        M_Years_Val = ' '.join((str(M_Year_Value.get())).split()) 
        B_Years_Val = ' '.join((str(B_Year_Value.get())).split()) 
    
    #FOR CHECKING VALUES
    def Check1():
        global ERROR
        global Email_Val , Number_Val , Amount_Val , Day_Val , Month_Val , Year_Val , Number1_Val , Money_Val , M_Years_Val , B_Years_Val , Day_Value , Month_Value
        
        
        ERROR = 0 
        
        
        if ( int(len(Day_Value.get()) < 2)):
            tmsg.showinfo("ERROR" , "Please Enter Numerical 2 digits in Day" ,parent = root)
            ERROR = 1
            return
        
        if ( int(len(Month_Value.get()) < 2)):
            tmsg.showinfo("ERROR" , "Please Enter Numerical 2 digits in Month" ,parent = root)
            ERROR = 1
            return
        
        if ( int(len( Year_Value.get()) < 4)):
            tmsg.showinfo("ERROR" , "Please Enter Numerical 4 digits in Year ( Out Flow )" ,parent = root)
            ERROR = 1
            return
        
      
        
        
        
        if ( (Day_Value.get()).isdigit() == False):
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Day" ,parent = root)
            ERROR = 1
            return
        
        if ( (Month_Value.get()).isdigit() == False  ):
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Month" ,parent = root)
            ERROR = 1
            return
           
        if (Amount_Val.isdigit() == False):
            ERROR = 1
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Premium" ,parent = root)
            return
        if (Year_Val.isdigit() == False  ):
            ERROR = 1
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Year" ,parent = root)
            return
        if (Number1_Val.isdigit() == False  ):
            ERROR = 1
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Number of Years ( Out Flow )" ,parent = root)
            return
        
        
        
        if clicked1.get() == "  Select Company Name  ":
            tmsg.showinfo("ERROR" , " Select Company Name ." , parent = root )
            ERROR = 1
            return
        if clicked2.get() == "  Select Mode of Payment  ":
            tmsg.showinfo("ERROR" , " Select Mode of Payment " , parent = root )
            ERROR = 1
            return
        
        
        if (Number_Val == "" ):
            tmsg.showinfo("ERROR" , "Please Enter Policy Number ." , parent = root )
            ERROR = 1
            return
       
        if (Email_Val == ""):
            tmsg.showinfo("ERROR" , "Please Enter Plan Name ." , parent = root )
            ERROR = 1
            return
        
        
            
        if (Name_Value.get() == ""   ):
            tmsg.showinfo("ERROR" , "Please Select Name of Client ." , parent  = root)
            ERROR = 1
            return
        
    
    # FOR CHECKING VALUES
    def Check2():
        
        global ERROR
        global Email_Val , Number_Val , Amount_Val , Day_Val , Month_Val , Year_Val , Number1_Val , Money_Val , M_Years_Val , B_Years_Val , Day_Value , Month_Value
        
        
        ERROR = 0 
        
        
       
        
        if ( int(len(Day_Value.get()) < 2)):
            tmsg.showinfo("ERROR" , "Please Enter Numerical 2 digits in Day" ,parent = root)
            ERROR = 1
            return
        
        if ( int(len(Month_Value.get()) < 2)):
            tmsg.showinfo("ERROR" , "Please Enter Numerical 2 digits in Month" ,parent = root)
            ERROR = 1
            return
        
        if ( int(len( Year_Value.get()) < 4)):
            tmsg.showinfo("ERROR" , "Please Enter Numerical 4 digits in Year ( Out Flow )" ,parent = root)
            ERROR = 1
            return
        
        if ( int(len( M_Year_Value.get()) < 4)):
            tmsg.showinfo("ERROR" , "Please Enter Numerical 4 digits in Year ( In Flow )" ,parent = root)
            ERROR = 1
            return
        
        if ( (Day_Value.get()).isdigit() == False):
            ERROR = 1
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Day" ,parent = root)
            return
        if ( (Month_Value.get()).isdigit() == False  ):
            ERROR = 1
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Month" ,parent = root)
            return
           
        if (Amount_Val.isdigit() == False):
            ERROR = 1
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Premium" ,parent = root)
            return
        if (Year_Val.isdigit() == False  ):
            ERROR = 1
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Year" ,parent = root)
            return
        if (Number1_Val.isdigit() == False  ):
            ERROR = 1
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Number of Years ( Out Flow )" ,parent = root)
            return
        
        
        
        if clicked1.get() == "  Select Company  ":
            tmsg.showinfo("ERROR" , " Select Company Name ." , parent = root )
            ERROR = 1
            return
        if clicked2.get() == "  Select Mode  ":
            tmsg.showinfo("ERROR" , " Select Mode of Payment " , parent = root )
            ERROR = 1
            return
        
        
        if (Number_Val == "" ):
            tmsg.showinfo("ERROR" , "Please Enter Policy Number ." , parent = root )
            ERROR = 1
            return
       
        if (Email_Val == ""):
            tmsg.showinfo("ERROR" , "Please Enter Plan Name ." , parent = root )
            ERROR = 1
            return
        
        
            
        if (Name_Value.get() == ""   ):
            tmsg.showinfo("ERROR" , "Please Select Name of Client ." , parent  = root)
            ERROR = 1
            return
        
        
      
        
        
        if (Money_Val.isdigit() == False  ):
            
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Money ( In Flow )" ,parent = root)
            ERROR = 1
            return
        if (M_Years_Val.isdigit() == False  ):
            ERROR = 1    
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Year ( In Flow)" ,parent = root)
            return
        if (B_Years_Val.isdigit() == False  ):
            ERROR = 1        
            tmsg.showinfo("ERROR" , "Please Enter Numerical Data in Number of Year ( In Flow)" ,parent = root)
            return
    

        
    def Submit():
        
        global YEAR , MONEY , Money_Value , B_Year_Value , M_Year_Value  , Manually , Name_Val , Exist , ERROR 
        global Email_Val , Number_Val , Amount_Val ,  Year_Val , Number1_Val , Money_Val , M_Years_Val , B_Years_Val
        ERROR = 0 
        
        
        Date_Val  = Day_Value.get() + "-" + Month_Value.get() + "-" +Year_Value.get()
       
        
        Trim_Values()
        
        Check2()
        
        
        
        
        N6 = 0
        
        #TO check , if the client name entered through String Var , then the client is new or existing .
        if ( str(Button5.get()) == "1" ):
            if  os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_"   ) :
                M = messagebox.askokcancel("Existing Client" , "It is Existing Client .\nDo you want to register as \"Existing Client\" ? ", parent = root)
                if M == True:
                    Name_Val = ' '.join((str(Name_Value.get())).split()).title()
                    pass
                else:
                    Name_Val = ' '.join((str(Name_Value.get())).split()).title()
                    Name_Val = Name_Val + "_(1)"
                    N8 = 1
                
        else:
            Name_Val = ' '.join((str(Name_Value.get())).split()).title()
        
     
        
        
            
        if( clicked2.get() == "Yearly"):
            Mode = 1
        if( clicked2.get() == "Quarterly"):
            Mode = 4   
        if( clicked2.get() == "Monthly"):
            Mode = 12
        if( clicked2.get() == "Half Yearly"):
            Mode = 2
        
        #For Counting Spaces 
        count_spaces = 0
        count_words = 0
        words = Name_Val.split()
        for i in range(len(words)-1):
            if words[i] and words[i+1]:
                count_spaces += 1
        count_words = len(words)
        
        
        DASH = count_words - count_spaces
        n1 =1 
        
        if( 1 != DASH and N6 == 0 and ERROR == 0 ):
          
            tmsg.showinfo("ERROR", " You have entered Name of Client in Incorrect manner \n It should be in format \'First_Name Surname\' \n There should only one place between first name and surname  ",parent=root)
        
        
        if(1 == Button5.get() and N6 == 0 and ERROR == 0 ):
            if not os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_" ) :
                messagebox1 =  messagebox.askokcancel("ERROR"," " + Name_Val+ " is not an existing Client . \n There might be a spelling mistake . \n On Pressing \' OK \' the details will be registered as New Client . \n On Pressing \'Cancel\' the details will not be registered . ",parent=root)
                if( messagebox1 == True):
                    pass
                else:
                    n1+=1 
            else:
                messagebox.askokcancel("Existing Client", Name_Val + " is an Existing  client . " , parent  = root)
            pass
        else:
            
            pass
       
        n3 = 0      
        if not os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_" ) :
            
            if( n1 == 1 and DASH == 1):
           
                path = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"
                os.chdir(path)
                Newfolder = Name_Val + "_"
                os.makedirs(Newfolder)
                n3+=1
        else:
            pass
        
        
        if( DASH == 1 and n1 ==1 and N6 == 0 and ERROR == 0  ):
            #For Out Flow sheet of csv
            if not os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_" + "\\" + Name_Val + " " + clicked1.get() + " Out Flow" + '.csv') :
            
                f=open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_" + "\\" + Name_Val + " " + clicked1.get() + " Out Flow" + '.csv','w',newline='')
                writer = csv.writer(f)
                writer.writerow(["Name","Insurance company","Plan name", "Policy_number" , "Premium" , "Mode of payment" , "Date"])
                f.close()
            else :
                pass
            
            f=open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_" + "\\" + Name_Val + " " + clicked1.get() + " Out Flow" + '.csv','a',newline='')
            writer = csv.writer(f)
            writer.writerow([])
        
            f.close()
            
            
            path = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_" + "\\" + Name_Val + " " + clicked1.get() + " Out Flow" +  ".csv"
            df = pd.read_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_" + "\\" + Name_Val + " " + clicked1.get() + " Out Flow" +  ".csv")
            # Drop first column of dataframe
            
            reader = csv.reader(open(path))
            n= len(list(reader))
            
            details =  ['Name','Insurance company','Plan name' , 'Policy_number','Premium','Mode of payment',"Date"]
            
            
            details_1 = [Name_Val , clicked1.get() ,  Email_Val   , Number_Val , Amount_Val   , clicked2.get() , Date_Val ]
            
            
            
            for i in range (0,7):
                df.loc[int(n) -1,  details[i]] = details_1[i]

            for i in range (0,int(Number1_Val)):
                
                n2 = int(Year_Val) + int(i)
                n1 = str(n2)
                df.loc[int(n)-1, "Years Out flow (" + n1 + ")"] = (int(Amount_Val))*(int(Mode))
    

            df.to_csv(path , index = False)
            
            
            
            
            
            
            if not os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_" + "\\" + Name_Val + " " + clicked1.get() + " In Flow" + '.csv') :
                f=open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_" + "\\" + Name_Val + " " + clicked1.get()+ " In Flow" + '.csv','a',newline='')
                writer = csv.writer(f)
                writer.writerow(["Name","Insurance company","Plan name", "Policy_number" , "Premium" , "Mode of payment","Date"])
                f.close()
            else :
                pass
            
            
            #For In Flow csv sheet
            f=open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_" + "\\" + Name_Val + " " + clicked1.get() + " In Flow" + '.csv','a',newline='')
            writer = csv.writer(f)
            writer.writerow([ ])
        
            f.close()
            
            
            path = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_" + "\\" + Name_Val + " " + clicked1.get() + " In Flow" +  ".csv"
            df = pd.read_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val + "_" + "\\" + Name_Val + " " + clicked1.get() + " In Flow" +  ".csv")
            # Drop first column of dataframe
            
            reader = csv.reader(open(path))
            n= len(list(reader))
            
            details =  ['Name','Insurance company','Plan name' , 'Policy_number','Premium','Mode of payment',"Date"]
            
            details_1 = [Name_Val , clicked1.get() ,  Email_Val   , Number_Val , Amount_Val   , clicked2.get() , Date_Val]
            
            for i in range (0,7):
                df.loc[int(n) -1,  details[i]] = details_1[i]
            
            if (Money_Val == "0" and Manually == 1):
                if (M_Years_Val == "0" and Manually == 1):
                    if (B_Years_Val == "0" and Manually == 1):
                        pass
            else:
                
                YEAR = []
                MONEY = []
                    
                for i in range (0,int(B_Years_Val)):
                    n2 = int(M_Years_Val) + int(i)
                    n1 = str(n2)
                    YEAR.append(n1 )
                    
                    MONEY.append(Money_Val)
                

            for i in range (0,len(YEAR)):
                
                n2 = int(M_Years_Val) + int(i)
                n1 = str(n2)
                
                df.loc[int(n)-1, "Years In Flow ("+YEAR[i]+")"] = MONEY[i]
                

            df.to_csv(path, index = False) 
            
            
            if ( n3 == 1 ):
                N2 ="New Client"
            if( n3 == 0):
                N2 = "Existing Client" 
            
            messagebox.askokcancel("Details are recorded","The Detalis of Client " + Name_Val + " are recorded as \'"+N2+"\' and are saved in folder named " + Name_Val + "_ which is in folder Data Entry . " , parent = root)
            
            deselect_all()  
        
        
        

    
    def Manual():
        
    
        global YEAR , MONEY , Money_Value , B_Year_Value , M_Year_Value  , Manually , Name_Val , Exist , ERROR 
        global Email_Val , Number_Val , Amount_Val ,  Year_Val , Number1_Val , Money_Val , M_Years_Val , B_Years_Val
        ERROR = 0 

        Trim_Values()
     
        Check1()
        
        if (ERROR == 0 ):
            global entry_widgets_col1, entry_widgets_col2 , MAX_ENTRIES
            
       
            
            def deselect_all1():
                entry.delete(0,"0")
                
                # Destroy previously created entry widgets and labels (if any)
                for widget in frame.winfo_children():
                    widget.destroy()
                    
                for widget in button.winfo_children():
                    widget.destroy()    
            
            def retrieve_values(entry_widgets_col1, entry_widgets_col2):
                
                global YEAR , MONEY , Money_Value , B_Years_Value , M_Years_Value ,Manually
                
                
                
                Money_Value.delete(0 , END)
                B_Year_Value.delete(0 , END)
                M_Year_Value.delete(0 , END)
                
                Val = "0"
                Val1 = "0000"
                
                
                Money_Value.insert(0 , Val)
                B_Year_Value.insert(0 , Val)
                M_Year_Value.insert(0 , Val1)
                            
                # Retrieve the values from entry widgets
                YEAR = [entry_widget.get() for entry_widget in entry_widgets_col1]
                MONEY = [entry_widget.get() for entry_widget in entry_widgets_col2]

                Manually = 1
                
                
                window.destroy()
                
       
                
                Submit()
                
                Manually = 0

            def Escape1():
                window.destroy()
               
                
            
            def move_focus(event):
                
                global num_entries ,MAX_ENTRIES
                
                if (num_entries > 15 ):
                    ROWS1 = 15
                    if (num_entries%MAX_ENTRIES == 0 ):
                        COLS1 = (num_entries//MAX_ENTRIES)*2
                    else:
                        COLS1 = ((num_entries//MAX_ENTRIES) + 1)*2
                else:
                    ROWS1 = num_entries
                    COLS1 = 2
                
                current_entry = window.focus_get()

                if current_entry in entry_widgets_col1:
                    current_index = entry_widgets_col1.index(current_entry)
                    entry_widgets = entry_widgets_col1
                elif current_entry in entry_widgets_col2:
                    current_index = entry_widgets_col2.index(current_entry)
                    entry_widgets = entry_widgets_col2
                else:
                    return

                num_entries = len(entry_widgets)
                num_columns = (num_entries + MAX_ENTRIES - 1) // MAX_ENTRIES

                if event.keysym == "Up":
                    if current_index - num_columns >= 0:
                        entry_widgets[current_index - num_columns].focus()
                elif event.keysym == "Down":
                    if current_index + num_columns < num_entries:
                        entry_widgets[current_index + num_columns].focus()
                elif event.keysym == "Left":
                    if current_index % num_columns != 0:
                        entry_widgets[current_index - 1].focus()
                elif event.keysym == "Right":
                    if (current_index + 1) % num_columns != 0:
                        entry_widgets[current_index + 1].focus()
            
            def create_entry_widgets():
                
                global entry_widgets_col1, entry_widgets_col2 , num_entries , entry_widget
                
                
                
                
                color = "#f7e7ce"
                
                n1 = 0
        
                
                try:
                    num_entries = int(entry.get())
                except ValueError:
                    # Handle the case when the entry is empty or contains a non-integer value
                    num_entries = 0
                    
                if ( num_entries > 40):
                    tmsg.showinfo("ERROR" , "Please Enter Value Less than 40" , parent = window)
                    n1 = 1
                    
                    
                
                
                
                if (n1 == 0 ):
                    
                    
                    
                    
                    # Destroy previously created entry widgets and labels (if any)
                    for widget in frame.winfo_children():
                        widget.destroy()
                        
                    for widget in button.winfo_children():
                        widget.destroy()

                    # Calculate the number of columns required
                    num_columns = (num_entries + MAX_ENTRIES - 1) // MAX_ENTRIES
                    
                    
                    entry_frame = ctk.CTkFrame(frame , fg_color="#f7e7ce" ,   bg_color="PAPAYAWHIP"  , border_color = "red" ,  border_width= 7 ,width= 350 ,height= 600  ,corner_radius= 20)
                    entry_frame.pack(fill= "both" , padx = 100 , pady =10 + 5  )
                    
                
                    # Create labels for numbering, "Year", and "Money In Flow"
                    number_label = tk.Label(entry_frame, text="Number", background=color  , font = ("comicsans 15 bold"))
                    number_label.grid(row=0, column=0, padx=10, pady=20)
                    year_label = tk.Label(entry_frame, text="Year", background=color , font = ("comicsans 15 bold"))
                    year_label.grid(row=0, column=1, padx=5, pady=10)
                    money_label = tk.Label(entry_frame, text="Money In Flow", background=color , font = ("comicsans 15 bold"))
                    money_label.grid(row=0, column=2, padx=20, pady=10)

                    # Create additional labels for new columns
                    for i in range(num_columns-1):
                        col_label = tk.Label(entry_frame, text="Year" , background=color , font = ("comicsans 15 bold") )
                        col_label.grid(row=0, column=(i*3)+4, padx=10)
                        
                        
                        
                        if (i == num_columns -2):
                            col_label = tk.Label(entry_frame, text="Money In Flow" , background=color , font = ("comicsans 15 bold") )
                            col_label.grid(row=0, column=(i*3)+5, padx=20 + 5)

                        else:
                            col_label = tk.Label(entry_frame, text="Money In Flow" , background=color , font = ("comicsans 15 bold") )
                            col_label.grid(row=0, column=(i*3)+5, padx=10)

                    # Create entry widgets in each column
                    entry_widgets_col1 = []
                    entry_widgets_col2 = []
                    for i in range(num_entries):
                        row = (i % MAX_ENTRIES) + 1 + (num_entries > MAX_ENTRIES)  # Adjust row index if num_entries > MAX_ENTRIES
                        column = i // MAX_ENTRIES * 3  # Calculate the column based on MAX_ENTRIES

                        number_label = ctk.CTkLabel(entry_frame, text=str(i+1), fg_color  =  color )
                        number_label.grid(row=row, column=column, padx=10, pady=3)
                        
                        entry_widget = ctk.CTkEntry(entry_frame , border_color= "#990000" , width= 120 , bg_color= color)
                        entry_widget.grid(row=row, column=column+1, padx=5, pady=3)
                        setup_entry_widget("Year", 4, entry_widget)
                        entry_widgets_col1.append(entry_widget)
                        
                        entry_widget1 = ctk.CTkEntry(entry_frame , placeholder_text= "Money In flow" , placeholder_text_color = "#1f1f1f" , border_color="#990000"  , width= 120 , bg_color= color)
                        entry_widget1.grid(row=row, column=column+2, padx=15, pady=3)
                        entry_widgets_col2.append(entry_widget1)
                    
                    
                    
                        
                        
                        if ( num_entries <= MAX_ENTRIES):
                            
                            if ( row%(num_entries) == 0 ):
                                number_label = ctk.CTkLabel(entry_frame, height=5, text=str(" "), fg_color  =  color)
                                number_label.grid(row=row+1, column=column, padx=20, pady=10)
                        
                        else:
                            
                            if ( row%(MAX_ENTRIES) == 1 ):
                                number_label = ctk.CTkLabel(entry_frame , height=5, text=str(" "), fg_color  = color)
                                number_label.grid(row=row+1, column=column, padx=20, pady=10)
                            else:
                                pass
                            
                    entry_widgets_col1[0].focus() 
                    entry_widgets_col2[0].focus()    
                    
                    my_font3 = ctk.CTkFont(family="Comicsansms", size=20 , weight = "bold")   
                            
                    retrieve_button = ctk.CTkButton(button, fg_color= "white" ,  text_color = "red" , hover_color = "lightgray"  , border_color= "red" , border_width= 5 , corner_radius = 0 , text = "Clear All" , font = my_font3 , command= deselect_all1)
                    retrieve_button.pack(side = "left" ,padx = 5)
                            
                    retrieve_button = ctk.CTkButton(button, fg_color= "white" ,  text_color = "red" , hover_color = "lightgray"  , border_color= "red" , border_width= 5 , corner_radius = 0 , text = "Submit details" , font = my_font3)
                    retrieve_button.pack(side = "right" ,padx = 5)

                    # Update the retrieve_values function with the current entry_widgets lists
                    retrieve_button.configure(command=lambda: retrieve_values(entry_widgets_col1, entry_widgets_col2))
                    
                    
                    if num_entries <=20 and num_entries >=0 :
                        width = 0
                    if num_entries <=30 and num_entries >=21 :
                        width = 1
                    if num_entries <=40 and num_entries >=31 :
                        width = 2

                   
                    window_width = 900 + width * 320  # Adjust the width based on the number of widgets
                    
                    if (width == 1 or width == 2 ):
                        padx  = 400 - (width)*(90 + (width-1)*60)
                    else:
                        padx = 400
                        
                    window_height = 670
                    
                    window_height =670 
                    window.geometry(f"{window_width}x{window_height}+{padx}+180")
                    window.resizable(False , False)

            # Create the main window
            window=ctk.CTk()#Creating new root
            window.attributes("-topmost", True)#To keep tkinter window on top
            window.title("Enter In Flow Manually")
            window.resizable(False , False)
            window.geometry("800x670+400+180")
            window.config(background="papayawhip")

            f1 = Frame(window, bg= "Red", borderwidth=10, relief=RIDGE)
            f1.pack(side=TOP, fill="x")
            
            
            W = ctk.CTkLabel ( f1 , text ="Enter In Flow Manually"  , text_color = "White" , fg_color = "red" , font = my_font)
            W.pack()


            # Create a label and an entry for user input
            frame1 = ctk.CTkFrame(window , bg_color=  "papayawhip" , fg_color=  "papayawhip")
            frame1.pack(pady = 20)

            label = ctk.CTkLabel(frame1,text_color = "white" , fg_color = "red" , text="Number of Years:" ,width = 180 , font = my_font1)
            label.pack(side="left" , padx = 10)

            entry = ctk.CTkEntry(frame1 , border_color= "#990000" )
            entry.pack(side="left"  , padx = 10 )
            
            # Create a button to generate entry widgets
            button = ctk.CTkButton(window, text_color = "white" , fg_color = "red" , bg_color = "#f7e7ce" ,  text="Generate" ,width = 20 , hover_color= "#990000"  , corner_radius= 5+5 , font = my_font1, command=create_entry_widgets)
            button.pack(pady = 3)

            # Create a frame to hold the entry widgets
            frame = Frame(window , background="papayawhip")
            frame.pack()
            
            button = Frame(window , background="papayawhip")
            button.pack()
            
            window.bind("<Return>", lambda event: retrieve_values(entry_widgets_col1, entry_widgets_col2))
            window.bind("<Delete>", lambda event: deselect_all1())
            window.bind("<Control-M>", lambda event: create_entry_widgets())
            window.bind("<Control-m>", lambda event: create_entry_widgets())
            window.bind("<Escape>", lambda event: Escape1())
            
    
            
        

            # Create a button to retrieve the values
            

            # Maximum number of entry widgets in each column
            MAX_ENTRIES = 10

            # Start the Tkinter event loop
            window.mainloop()
    

    B1 = ctk.CTkButton (tab.tab(" Register Client Policy ")  ,  fg_color = "white"  , text_color = "red" , hover_color= "lightgray" , cursor= "hand2" , text = "  Submit Details  ", corner_radius=0 , border_width=3 ,border_color="red" ,height=40 , font = my_font3 , command = Submit)
    B1.grid(row = 6 , column = 4 , columnspan = 2 , pady = 20)
    
    deselect_button = ctk.CTkButton( tab.tab(" Register Client Policy ") ,  fg_color = "white"  , text_color = "red",  hover_color= "lightgray" , cursor= "hand2" , text="Clear All", corner_radius=0 , border_width=3 ,border_color="red" , height=40 , font = my_font3 , command=deselect_all)
    deselect_button.grid(row = 6 , column = 2, columnspan = 2, pady = 20)
    
    B2 = ctk.CTkButton ( tab.tab(" Register Client Policy ") , fg_color = "red" ,  text_color = "white" ,  hover_color= "brown" , cursor= "hand2" , text = "Enter Manually" , font = my_font3 , command = Manual)
    B2.grid(row = 4 , column = 5)
    
    
    f1 = Frame(tab.tab(" Register Client Master "), width = 30 ,  bg = "red", borderwidth=10, relief=RIDGE)
    f1.grid(row = 0 ,column = 0  , columnspan=6 , pady = 20)
    
    W = Label ( f1 , text ="Register Client Master "  , width = 20  , fg = "White" , bg = "red" , font = ("comicsansms 22 bold"))
    W.pack()
    
    global Upload1 , Upload2
    
    Upload1 = 0
    Upload2 = 0 
    
    
    def upload_file():
        global file_path , Upload1
        
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg; *.jpeg; *.png")])
        
        if file_path:
            # Load the selected image
            image = open_image(file_path)
            
            # Display the image in a label
            photo = c.CTkImage(image)
            
                
            # Enable the deselect button
            deselect_button.configure(state=tk.NORMAL)
            # Update the selected file Entry
            selected_file_Entry.delete(0 , END)
            selected_file_Entry.insert(0, file_path)
            Upload1  = 1
        elif file_path.lower().endswith('.zip'):
            # Process the selected zip file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Extract the contents of the zip file
                zip_ref.extractall()
            
            
    def upload_file1():
        global file_path1 , Upload2 
        
        file_path1 = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg; *.jpeg; *.png")])
        
        if file_path:
            # Load the selected image
            image = open_image(file_path1)
            
            # Display the image in a label
            photo = c.CTkImage(image)
            
                
            # Enable the deselect button
            deselect_button.configure(state=tk.NORMAL)
            # Update the selected file Entry
            selected_file_Entry1.delete(0 , END)
            selected_file_Entry1.insert(0, file_path1)
            Upload2 = 1
            
        elif file_path.lower().endswith('.zip'):
            # Process the selected zip file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Extract the contents of the zip file
                zip_ref.extractall()
            
        
                


    def submit():
        client_name = Name_Val1
        
        # Create the folder with the client's name
        folder_path = "./Data Entry/Client Master/Adhar Card Copy" 
        

        # Copy the selected photo to the client's folder
        if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_name = client_name + ".jpg"  # Save the photo with the client's name
            target_path = folder_path + "/" + file_name
            shutil.copy(file_path, target_path)
            
        tmsg.showinfo("Adhar Card Copy Uploaded" , " The Adhar Card Copy of Client : " + Name_Val1 + " is Uploaded . ")
            
        selected_file_Entry.delete(0, END)
        
        
        
    def submit1():
        client_name = Name_Val1
        
        # Create the folder with the client's name
        folder_path = "./Data Entry/Client Master/Pan Card Copy" 
        

        # Copy the selected photo to the client's folder
        if file_path1.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_name = client_name + ".jpg"  # Save the photo with the client's name
            target_path = folder_path + "/" + file_name
            shutil.copy(file_path1, target_path)
            
        tmsg.showinfo("Pan Card Copy Uploaded" , " The Pan Card Copy of Client : " + Name_Val1 + " is Uploaded . ")
         
        selected_file_Entry1.delete(0, END)   
        
    def Clear01():
        
        global Upload1 
        
        
        selected_file_Entry.delete(0,END)
        Upload1 = 0
        
    def Clear02():
        global Upload2
        
        selected_file_Entry1.delete(0,END)   
        Upload2 = 0 
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Master ") , corner_radius=10 , text ="Name of client"  , width = 160  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 1 , column=0 , pady = 15)
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Master ") , corner_radius=10 ,text ="Email ID"   , width = 160  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 2 , column=0, pady = 15)
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Master ") , corner_radius=10 ,  text ="Address"  , width = 160  , text_color = "White" , fg_color = "red" , font = my_font1 )
    W.grid(row = 3 , column=0, pady = 15)
    
    
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Master ") , corner_radius=10 , text ="Mobile Number"   , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 1 , column=2, pady = 15, padx  =13)
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Master ") , corner_radius=10 , text ="Date of Birth"   , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 2 , column=2, pady = 15)

    W = ctk.CTkLabel ( tab.tab(" Register Client Master ") , corner_radius=10 , text ="Adhar Card Copy"   , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 3 , column=2, pady = 15)
    
    W = ctk.CTkLabel ( tab.tab(" Register Client Master ") , corner_radius=10 , text ="Pan Card Copy"   , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 5 , column=2, pady = 15)
    
    Address = ctk.CTkTextbox(tab.tab(" Register Client Master ") , height = 70 , width = 180 , border_color="red" , border_width=2 , scrollbar_button_color="red" , scrollbar_button_hover_color="brown")
    Address.grid(row = 3 , column = 1  , rowspan = 2  ,padx = 25 )
    
    Name_Value1 = ctk.CTkEntry( tab.tab(" Register Client Master ") , placeholder_text_color="black" , placeholder_text="Name of Client" , border_color="red" , border_width=2 , width =170 )
    Name_Value1.grid(row =1 , column = 1)
    
    Email_Value1 = ctk.CTkEntry( tab.tab(" Register Client Master ") , placeholder_text_color="black" , placeholder_text="Email ID" , border_color="red" , border_width=2 , width =170 )
    Email_Value1.grid(row = 2 , column = 1)
    
    Mobile_Value_1 = ctk.CTkEntry( tab.tab(" Register Client Master ") , placeholder_text_color="black" , placeholder_text="Mobile Number" , border_color="red" , border_width=2 , width =170 )
    Mobile_Value_1.grid(row = 1 , column = 3)

    
    
    Frame_Adhar = ctk.CTkFrame(tab.tab(" Register Client Master ") , bg_color = color , fg_color = color )
    Frame_Adhar.grid(row = 3 , column = 3)
    
    Frame_Pan = ctk.CTkFrame(tab.tab(" Register Client Master ") , bg_color = color , fg_color = color)
    Frame_Pan.grid(row = 5 , column = 3)
    
    
    Adhar_Entry = ctk.CTkEntry( Frame_Adhar, placeholder_text_color="black" , placeholder_text="Adhar Card Number" , border_color="red" , border_width=2 , width =130 )
    Adhar_Entry.pack(side = "left" , padx  = 5 )
    
    Pan_Entry = ctk.CTkEntry( Frame_Pan, placeholder_text_color="black" , placeholder_text="Pan Card Number" , border_color="red" , border_width=2 , width =130 )
    Pan_Entry.pack(side = "left" , padx  = 5 )
    
    
    
    Adhar = ctk.CTkButton( Frame_Adhar, text = "Upload" , width  =15 , fg_color="#e06666" , command = upload_file  , hover="red")
    Adhar.pack(side = "right" , padx  = 5 )
    
    Pan = ctk.CTkButton( Frame_Pan , text = "Upload", width  =15 , fg_color="#e06666", command = upload_file1 , hover_color="red")
    Pan.pack(side = "right" , padx  = 5 )
    
    
    Frame_Deselection = c.CTkFrame( tab.tab(" Register Client Master " ) , fg_color=color , bg_color=color)
    Frame_Deselection.grid(row = 4 , column = 3 , columnspan = 10 )

    # Create an entry for the client's name
    client_name_label = c.CTkLabel(Frame_Deselection, text="Selected File:", fg_color=color, bg_color=color)
    client_name_label.pack(side="left")

    selected_file_Entry = c.CTkEntry(Frame_Deselection , width=180, border_color=color , fg_color=color, bg_color=color)
    selected_file_Entry.pack(side="right" , expand = False)
    
    
    
    Frame_Deselection1 = c.CTkFrame( tab.tab(" Register Client Master " ), fg_color=color, bg_color=color)
    Frame_Deselection1.grid(row = 6 , column = 3 , columnspan = 3)

    # Create an entry for the client's name
    client_name_label = c.CTkLabel(Frame_Deselection1, text="Selected File:", fg_color=color, bg_color=color)
    client_name_label.pack(side="left")

    selected_file_Entry1 = c.CTkEntry(Frame_Deselection1, width=180 , border_color=color , fg_color=color, bg_color=color)
    selected_file_Entry1.pack(side="right" , expand = False)
    
    frame = ctk.CTkFrame( tab.tab(" Register Client Master ") ,height = H  , bg_color = color , border_color="RED" , border_width=2 , fg_color= "white" )
    frame.grid(row  = 2 , column = 3 , padx  = 0 , pady  = 0)

    Day1_Value = ctk.CTkEntry(frame , border_color="white" , placeholder_text_color="black" ,height = H   , width  = 35 , fg_color="WHITE" , corner_radius=5 )
    Month1_Value = ctk.CTkEntry(frame, border_color="white" , placeholder_text_color="black" ,height = H  , fg_color="WHITE" , width  = 35 , corner_radius=5)
    Year1_Value = ctk.CTkEntry(frame, border_color="white" , placeholder_text_color="black" ,height = H  ,fg_color="WHITE" , width  = 45  , corner_radius=5)

    label1 = ctk.CTkLabel(frame, text="-" , fg_color="white" ,height = H  , bg_color="white")
    label2 = ctk.CTkLabel(frame, text="-" , fg_color="white" ,height = H  , bg_color="white")
    
    Clear1 = ctk.CTkButton( Frame_Deselection, text = "Clear" , width  =10 , text_color="black" ,  border_color=color , fg_color=color, bg_color=color , command = Clear01  , hover =False)
    Clear1.pack(side = "right" , padx  = 5 )
    
    Clear2 = ctk.CTkButton( Frame_Deselection1 , text = "Clear", width  =10 ,  text_color="black"  , border_color=color , fg_color=color, bg_color=color, command = Clear02 , hover =False)
    Clear2.pack(side = "right" , padx  = 5 )

    setup_entry_widget("YYYY", 4, Year1_Value)

    # Setup the second entry widget with placeholder "DD" and limit 2 digits
    setup_entry_widget("DD", 2, Day1_Value)

    setup_entry_widget("MM", 2, Month1_Value)
    



    
    Day1_Value.pack(side=tk.LEFT , padx  = 10)
    label1.pack(side=tk.LEFT , pady = 5)
    Month1_Value.pack(side=tk.LEFT)
    label2.pack(side=tk.LEFT)
    Year1_Value.pack(side=tk.LEFT  , padx  = 10)
   
    
    
    def Trim_Values_Master():
        
        global Name_Val1 , Email_Val1 , Mobile_Val1 ,  Address_Val , Adhar_Val , Pan_Val , Month1_Value , Year1_Value , ERROR1 
        ERROR1  = 0 
        

        
        if( int(len(Day1_Value.get())) <  2):
            tmsg.showerror("ERROR" , "Please enter 2 digits in Day")
            ERROR1  = 1
            return
        
        if( int(len(Month1_Value.get())) <  2):
            tmsg.showerror("ERROR" , "Please enter 2 digits in Month")
            ERROR1  = 1
            return
        
        if( int(len(Year1_Value.get())) <  4):
            tmsg.showerror("ERROR" , "Please enter 4 digits in Years")
            ERROR1  = 1
            return
        
        if( Day1_Value.get().isdigit() == False ):
            tmsg.showerror("ERROR" , "Please enter numerical value in Day")
            ERROR1  = 1
            return
        
        if( Month1_Value.get().isdigit() == False ):
            tmsg.showerror("ERROR" , "Please enter numerical value in Month")
            ERROR1  = 1
            return
        
        if( Year1_Value.get().isdigit() == False ) :
            tmsg.showerror("ERROR" , "Please enter numerical value in Years")
            ERROR1  = 1
            return
            
        
        
        Name_Val1 = ' '.join((str(Name_Value1.get())).split()).title()
        Email_Val1  = ' '.join((str(Email_Value1.get())).split()) 
        Mobile_Val1 = ' '.join((str(Mobile_Value_1.get())).split()) 
        
        
        Address_Val = ' '.join((str(Address.get("0.0", "end"))).split()) 
        Adhar_Val = ' '.join((str(Adhar_Entry.get())).split()) 
        Pan_Val = ' '.join((str(Pan_Entry.get())).split()) 
        
        if( Name_Val1 == "" ) :
            tmsg.showerror("ERROR" , "Please Enter Name of Client .")
            ERROR1  = 1
            return
        
    
    def deselect_All1():
    
        Name_Value1.delete(0, END)   
        Email_Value1.delete(0, END)
        Mobile_Value_1.delete(0, END)   
        Address.delete("0.0", "end" ) 
        Adhar_Entry.delete(0, END)   
        Pan_Entry.delete(0, END)
        Day1_Value.delete(0, END)   
        Month1_Value.delete(0, END)
        Year1_Value.delete(0, END)
        
          
        setup_entry_widget("YYYY", 4, Year1_Value)

        setup_entry_widget("DD", 2, Day1_Value)

        setup_entry_widget("MM", 2, Month1_Value)
        
        Pan_Entry.configure(placeholder_text  = "Pan Number")
        Adhar_Entry.configure(placeholder_text  = "Adhar Number")
        Mobile_Value_1.configure(placeholder_text  = "Mobile Number")
        Email_Value1.configure(placeholder_text  = "Email Id")
        Name_Value1.configure(placeholder_text  = "Name of Client")
        
        
    
    def Submit_Client_Master():
        
        Trim_Values_Master()
     
        if( ERROR1 == 1):
            return
        
        Date_Val1 = Day1_Value.get() + "-" + Month1_Value.get() + "-" + Year1_Value.get()
        
        
        
        deselect_All1()
        
        
            
        f=open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\Client Master\\Client Master .csv",'a',newline='')
        writer = csv.writer(f)
        writer.writerow([Name_Val1 , Email_Val1 , Mobile_Val1 , Date_Val1 , Adhar_Val , Pan_Val , Address_Val ])
        f.close()
        
        if Upload1 == 1 :
            submit()
        
        if Upload2 == 1 :
            submit1()
        
        
        tmsg.showinfo( "Recorded" , "The Details of Client "+ Name_Val1 + " are Recorded .")
    
    B1 = ctk.CTkButton ( tab.tab(" Register Client Master " ) ,  fg_color = "white"  , text_color = "red" , hover_color= "lightgray" , cursor= "hand2" , text = "  Submit Details  ", corner_radius=0 , border_width=3 ,border_color="red" ,height=40 , font = my_font3, command = Submit_Client_Master)
    B1.grid(row  = 7 , column = 1 , columnspan = 4)
    
    sorting_searching(" Register Client Policy " , 1 , 2 )
def replace_empty_cells_with_zero(csv_path):
    
    
    df_1 = pd.read_csv(csv_path)

    t_r_1=len(df_1.axes[0]) 

    t_c_1=len(df_1.axes[1])
    # Input 2: Number of rows and columns

        
    
    Empty_cell_Position_Row = []
    Empty_cell_Position_Col = []
    f = open(csv_path ,"r")
    r = 0  
    
    Empty_Cell = 0 
                 
    reader=csv.reader(f)
    for row in reader:
        c=0
        
        for col in row:
            
            if ( col == "" or col  == " "):
                Empty_Cell = 1
                Empty_cell_Position_Row.append(r)
                Empty_cell_Position_Col.append(c)
            c+=1    
        r+=1 
        
    
    
    
    if Empty_Cell == 0 :  
        return
    
    df = pd.read_csv(csv_path, header=None)  # Assuming CSV has no header

    # Get the maximum row and column positions provided
    max_row = max(Empty_cell_Position_Row)
    max_column = max(Empty_cell_Position_Col)

    # Adjust the DataFrame size if needed
    t_r_1, t_c_1 = df.shape
    if max_row >= t_r_1:
        df = pd.concat([df, pd.DataFrame([[float('nan') for _ in range(t_c_1)] for _ in range(max_row - t_r_1 + 1)])], ignore_index=True)
    if max_column >= t_c_1:
        df = pd.concat([df, pd.DataFrame([[float('nan') for _ in range(max_column - t_c_1 + 1)] for _ in range(df.shape[0])], axis=1)], ignore_index=True)

    # Replace cells with 0 at the specified positions
    for row, col in zip(Empty_cell_Position_Row, Empty_cell_Position_Col):
        df.iat[row, col] = 0

    # Save the modified DataFrame back to the CSV file
    df.to_csv(csv_path, index=False, header=False)
    
def Report():
    global tab
    
    for widget in frame1.winfo_children():
        widget.destroy()
        
    frame2.place_forget()
        
    
    tab = ctk.CTkTabview(frame1  ,  height=300 , border_color= "red" , border_width= 6+1  , corner_radius= 25 , bg_color="papayawhip" , fg_color= color , segmented_button_fg_color="red" , segmented_button_selected_color="#e06666", segmented_button_unselected_color="#f54747" , text_color="black" , segmented_button_unselected_hover_color="#f54747" , segmented_button_selected_hover_color="#e06666" )
    tab.pack(side = "left" , pady = 30 , padx = 20 )
    
    
    
    tab.add(" Report 1 ")
    
    tab.set(" Report 1 ")
        
    f1 = Frame(tab.tab(" Report 1 "), width = 30 , bg = "red", borderwidth=10, relief=RIDGE)
    f1.grid(row = 0 , column = 0 , columnspan=2 )
    W = Label ( f1 , text ="Enter details" ,width = 20  , fg = "White" , bg = "red" , font = ("comicsansms 22 bold"))
    W.pack()
    
    my_font1 =  ctk.CTkFont(family="Comicsansms", size=15 , weight = "bold")
    
    W = ctk.CTkLabel ( tab.tab(" Report 1 ") , corner_radius=10 , text ="Name of client"  , width = 160  , text_color = "White" , fg_color = "red" , font = my_font1)
    W.grid(row = 1 , column=0 , padx = 10 , pady = 40)
    
    
    def Sumbit_Report():
        n4 = 0 
        
        if  os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"  + "Data Entry\\" + Name1_Value.get() + "_" ) :
            
            
            pass
        
        
        else:
            tmsg.showerror("ERROR" , "The Client Name Doesn't Exists")
            Name1_Value.configure(placeholder_text  = "Name of Client")
            n4 = 1
            
        
        
        def delete_folder_and_files(folder_path):
            if not os.path.exists(folder_path):
             
                return
            else:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if file.endswith(".csv") or file.endswith(".pdf"):
                            os.remove(file_path)
                           
                os.rmdir(folder_path)
          
     
        from datetime import datetime
        
        
        

        present_time=datetime.now()
        current_date=present_time.strftime("%d-%m-%Y")
        
        
        
        if (Name1_Value.get() == "Select Name Of Client" ):
            n4 = n4 + 1
            tmsg.showinfo("Select Name Of Client", "Please Select Name Of Client ",parent=root)
        
        
        if  os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\" + current_date +Name1_Value.get() + "_" ) :
            
            
            delete_folder_and_files("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\" + current_date +Name1_Value.get() + "_")
            
            
            
        
        if(  n4 == 0 ):
            
            
            path4 = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"
            os.chdir(path4)
            Newfolder =current_date+ Name1_Value.get() + "_"
            os.makedirs(Newfolder)
            f = open('C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\'+ current_date + Name1_Value.get() +"_\\" +  current_date +" " +  Name1_Value.get() +  ' .csv',"w")
            writer = csv.writer(f)
            writer.writerow(['Year'])
            f.close()



                

            df_1= pd.read_csv('C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\'+ current_date + Name1_Value.get() +"_\\"+  current_date + " "  + Name1_Value.get() +  ' .csv')
            path1 = 'C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\'+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  ' .csv'


            List11 = ['KOTAK','LIC','TATA',"NJ"]
            List2 = []
            List4 = [ "Net Out flow"]
            List7 = ['Year']
            N =0  
            for i in range (0, len(List11))   :
                if not os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' Out Flow.csv') :
                    N+=1
            
                    pass
                else :
                    
                    csv_file_path = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' Out Flow.csv'



                    # Replace empty cells with 0 in the CSV file
                    replace_empty_cells_with_zero(csv_file_path)
                                        
                    
                    f = open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' Out Flow.csv',"r")
                    df= pd.read_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' Out Flow.csv')
                    
                    df.fillna(0, inplace = True)
                    
                    
                    df.to_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' Out Flow.csv', index = False)
                    
                    Path6 = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' Out Flow.csv' 
                    
                    df_s1 = pd.read_csv(Path6)
                    df = pd.read_csv(Path6)
                    t_r1=len(df.axes[0]) 

                    t_c1=len(df.axes[1]) 

                    
                    
                    list56 = []
                    for i1 in range ( 0 , t_c1):
                        list56.append ("0")
                        
                        
                    with open (Path6 , 'a') as csvfile : 
                        csvwriter = csv.writer(csvfile) 
                        csvwriter.writerow(list56)   
                        
                            
                    df = pd.read_csv(Path6)
                    
                    
                    
                    path = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' Out Flow.csv'
                    reader=csv.reader(f)

                    t_r=len(df.axes[0]) 

                    t_c=len(df.axes[1]) 

                    t_r_1=len(df_1.axes[0]) 

                    t_c_1=len(df_1.axes[1]) 

                    df_1.loc[int(t_r_1),"Year"] = List11[i]  + " (Out Flow) "
                    List7.append(List11[i]  + " (Out Flow) ")
                    r =5
                    
                    
                
                    for row in reader:
                        c=0
                    
                    
                        for col in row:
                            c+=1
                            
                            
                            
                            
                            if (c <  8):
                                continue
                         
                            
                            
                            math_sum = df[col].sum()
                        
                            col1 = col[16: 20]
                            
                            List2.append(col1)
                                
                            
                            df_1.loc[t_r_1, str(col1)] = math_sum
                            
                            
                        
                            df_1.to_csv(path1 , index  =False)
                            if ( c== t_c):
                                break
                    
                    
                        if (r > 2)  :
                            break 
                        
                        r+=1
                        
                        
            #MiN = int(min(List2))
            #Max = int(max(List2))

            t_r_1=len(df_1.axes[0]) 

            t_c_1=len(df_1.axes[1])

            
            Path5 = 'C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\'+ current_date + Name1_Value.get() +"_\\"+  current_date + " " + Name1_Value.get() +  ' .csv'
            df = pd.read_csv(path1)
            df.fillna(0, inplace = True)
            df.to_csv(path1, index = False)
            
            for i1 in range (1, t_c_1) :
                i=0 
                #i1 = 2
            
                with open('C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\'+ current_date + Name1_Value.get() +"_\\"+  current_date + " " + Name1_Value.get() +  ' .csv', 'r') as f:
                    csv_reader = csv.reader(f)
                    for line in csv_reader:
                        # process each line
                        i+=1
                        #i1+=1
                        
                        
                        if( N == 3):
                        
                            if (i !=2):
                                
                                
                                continue
                                    
                        

                            if(line[i1]==''):
                                line[i1] = 0
                            if (i == 2):
                                sum_12 = (line[i1])
                            
                        
                    
                        if( N == 2):
                        
                            if (i !=2):
                                
                                if( i != 3):
                                    continue
                    
                        
                            if(line[i1]==''):
                                line[i1] = 0
                            if (i == 2):
                            
                                sum_12 = (line[i1])
                            if (i == 3):
                            
                                sum1 = (line[i1])
                        
                        
                        if( N == 1):
                        
                            if (i !=2):
                                
                                if( i != 3):
                                    if( i != 4):
                                        continue
                                    
                                    
                        
                            if(line[i1]==''):
                                line[i1] = 0
                            if (i == 2):
                            
                                sum_12 = (line[i1])
                            if (i == 3):
                        
                                sum1 = (line[i1])
                            if (i == 4):
                        
                                sum2 = (line[i1])
                        
                        
                        
                        if( N == 0):
                        
                            if (i !=2):
                            
                                if( i != 3):
                                    if(i != 4):
                                        if( i != 5):
                                            continue
                                    
                                    
                            
                  
                            if(line[i1]==''):
                                line[i1] = 0
                            if (i == 2):
                        
                                sum_12 = (line[i1])
                            if (i == 3):
                            
                                sum_1 = (line[i1])
                            if (i == 4):
                            
                                sum_2 = (line[i1])   
                            if (i == 5):
                            
                                sum_3 = (line[i1])  
                    
                    if ( N == 3):
                                
                        s = float(sum_12)    
                    
                     
                        sum3 = int(s)
                        List4.append(sum3)
                                
                                
                    if ( N == 2):
                                
                        s = float(sum_12)    
                        s1 = float(sum1)    
                       
                        sum3 = int(s1) + int(s)
                        List4.append(sum3)
                        
                    
                        
                    if ( N == 1):
                                
                        s = float(sum_12)    
                        s1 = float(sum1)  
                        s2 = float(sum2)  
                            
                        sum3 = int(s1) + int(s) + int(s2)
                        List4.append(sum3)    
                    
                    
                    if(N == 0 ):
                        s = float(sum_12)
                        s1 = float(sum_1)
                        s2 = float(sum_2)
                        s3 = float(sum_3)
                        sum3 = int(s) + int(s3) + int(s1) + int(s2)
                        List4.append(sum3)
                    
            
          


            List11 = ['KOTAK','LIC','TATA',"NJ"]
            List2 = []
            List5 = ["Net In flow"]
            N =0  
            for i in range (0, len(List11))   :
                if not os.path.exists( "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' In Flow.csv') :
                    N+=1
                
            
                    pass
                else :
                    Path7 = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' In Flow.csv'
                    
                    csv_file_path = Path7
                    
                    # Replace empty cells with 0 in the CSV file
                    replace_empty_cells_with_zero(csv_file_path)
                    
                    
                    f = open( "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' In Flow.csv',"r")
                    
                    df= pd.read_csv( "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' In Flow.csv')
                    
                    t_r1=len(df.axes[0]) 

                    t_c1=len(df.axes[1])
                    
                    df.fillna(0, inplace = True)
                    df.to_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' In Flow.csv', index = False)                  
                    
                  
                    list55 = []
                    for i4 in range ( 0 , t_c1):
                        list55.append ("0")
                        
                        
                    with open (Path7 , 'a') as csvfile : 
                        csvwriter = csv.writer(csvfile) 
                        csvwriter.writerow(list55)   
                        
                    df = pd.read_csv(Path7)     
                      
                    df_1= pd.read_csv('C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\'+ current_date + Name1_Value.get() +"_\\"+  current_date + " "  + Name1_Value.get() +  ' .csv')
                    path =  "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List11[i] + ' In Flow.csv'
                    reader=csv.reader(f)

                    t_r=len(df.axes[0]) 

                    t_c=len(df.axes[1]) 

                    t_r_1=len(df_1.axes[0]) 

                    t_c_1=len(df_1.axes[1]) 

                    df_1.loc[int(t_r_1),"Year"] = List11[i]  + " (In Flow) "
                    List7.append(List11[i]  + " (In Flow) ")
                    r =5
                    
                    i6 = 20
                    for row in reader:
                        c=0
                    
                    
                        for col in row:
                            c+=1
                            
                            
                            
                            
                            if (c <  8):
                                continue
                            math_sum = df[col].sum()
                            
                            col1 = col[15: 19]
                            
                            List2.append(col1)
                                
                            
                            df_1.loc[t_r_1, str(col1)] = math_sum
                            
                        
                            df_1.to_csv(path1, index  =False)
                            if ( c== t_c):
                                break
                    
                   
                        if (r > 2)  :
                            break 
                        
                        r+=1
                        
                        
            #MiN = int(min(List2))
            #Max = int(max(List2))

            t_r_1=len(df_1.axes[0]) 

            t_c_1=len(df_1.axes[1])
            
            df = pd.read_csv(path1)
            df.fillna(0, inplace = True)
            df.to_csv(path1, index = False)                  
                    

            for i1 in range (1, t_c_1) :
                i=0 
                
                with open(path1, 'r') as f:
                    csv_reader = csv.reader(f)
                    for line in csv_reader:
                        # process each line
                        i+=1
                        #i1+=1
                        
                        
                        if (N == 3):
                        
                            if (i != 3 ):
                                    continue
                                
                        
                            if(line[i1]==''):
                                line[i1] = 0
                            if (i == 3):
                                sum_12 = (line[i1])
                        
                        if (N == 2):
                        
                            if (i != 4 ):
                                if( i != 5):
                                    continue
                            
                        
                        
                            if(line[i1]==''):
                                line[i1] = 0
                            if (i == 2+N):
                                sum_12 = (line[i1])
                            
                            if (i == 3+N):
                                sum_1 = (line[i1])
                        
                        
                        
                        if (N == 1):
                        
                            if (i != 4+N ):
                                if( i != 5+N):
                                    if( i != 6+N):
                                        continue
                            
                        
                    
                            if(line[i1]==''):
                                line[i1] = 0
                            if (i == 5):
                                sum_12 = (line[i1])
                            
                            if (i == 6):
                                sum_1 = (line[i1])
                                
                            if (i == 7):
                                sum_3 = (line[i1])
                        
                        
                        
                        
                        if (N == 0):
                        
                            if (i != 6+N ):
                                if( i != 7+N):
                                    if( i != 8+N):
                                        if( i != 9+N):
                                            continue
                            
                        
                        
                            if(line[i1]==''):
                                line[i1] = 0
                            if (i == 6):
                                sum_12 = (line[i1])
                            
                            if (i == 7):
                                sum_1 = (line[i1])
                                
                            if (i == 8):
                                sum_3 = (line[i1])
                                
                            if (i == 9):
                                sum_4 = (line[i1])
                    
                    if( N == 3):
                        s = float(sum_12)    
                        sum3 = int(s)
                        List5.append(sum3)
                    
                    
                    if( N == 2):
                        s = float(sum_12) 
                        s1 = float(sum_1)  
                    
                        sum3 = int(s) + int(s1)
                        List5.append(sum3)
                        
                    if( N == 1 ):
                        s = float(sum_12) 
                        s1 = float(sum_1)
                        s2 = float(sum_3)  
                    
                        sum3 = int(s) + int(s1) + int(s2)
                        List5.append(sum3)
                
                    
                                
                    if(  N  == 0 ):    
                        s = float(sum_12) 
                        s1 = float(sum_1)
                        s2 = float(sum_3)  
                        s3 = float(sum_4)
                        sum3 = int(s) + int(s1) + int(s2) + int(s3)
                        List5.append(sum3)
             
            
            for i in range( 0 ,len(List5)- len(List4)):
                List4.append(0)
            
        
                
            with open (path1 , 'a') as csvfile : 
                csvwriter = csv.writer(csvfile) 
                csvwriter.writerow(List4)     
                
            with open (path1 , 'a') as csvfile : 
                csvwriter = csv.writer(csvfile) 
                csvwriter.writerow(List5)
        
                            
                
        
            t_r_1=len(df_1.axes[0]) 

            t_c_1=len(df_1.axes[1])
        
        

            
            t_r_1=len(df_1.axes[0]) 

            t_c_1=len(df_1.axes[1]) 
            List6 = [ 'Total Cash Flow']

        
            N1 = (4-N)*2
            i =0
        
            List11 = [ 'Total In Flow']
            #N1 = (4-N)*2
            i7 = 0
            for i1 in range (1, t_c_1  ) :
                
                i=0 
                with open(path1, 'r') as f:
                    csv_reader = csv.reader(f)
                    for line in csv_reader:
                        # process each line
                        i+=1
                        
                        #i1+=1
                        if( i != 2+N1):
                            if( i != 4+N1 ):
                                continue
                    
                 
                            
                        if (i == 2+N1):
                            sum2 = (line[i1])
                        if (i == 4+N1):
                            sum1 = (line[i1])
                            
                    s = float(sum2)    
                    s1 = float(sum1)    
            
                    sum3 = int(s1) - int(s)
                    sum4 = int(s1) - int(s)
                    List6.append(sum3)
                
                    i4 = str(2005 + i1)
                
           
                
            with open (path1 , 'a') as csvfile : 
                csvwriter = csv.writer(csvfile) 
                csvwriter.writerow(List6)
                
            from datetime import datetime
            
            present_time=datetime.now()
            current_date=present_time.strftime("%d-%m-%Y")
            
            df_1= pd.read_csv('C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\'+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  ' .csv')
            path1 = 'C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\'+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  ' .csv'
         
            df1 = pd.DataFrame(data=df_1)
            df1_transposed = df1.T # or df1.transpose()

            #df1_transposed.sort_index(['Year'],axis=0, ascending=True, inplace = True)
       
            df1_transposed.to_csv(path1)
            #df1_transposed.sort_index(['Year'],axis=0, ascending=True, inplace = True)
          
            
            List7.append(" Net Out Flow")
            List7.append("Net In flow")
            List7.append("Total Cash Flow")
            
           
            
            
            f2 = open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " Format 1 .csv","w") 
            writer = csv.writer(f2)
            writer.writerow(List7)
            f2.close()
            
            
            df2 = pd.read_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " Format 1 .csv")

            path2 = 'C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\'+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  ' Format 1 .csv'
            df2 = pd.read_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " Format 1 .csv")
            
            
            
                    
            list11 = ['Year', 'TATA (Out Flow)', 'TATA (In Flow)',  'Net Out flow', 'Net In flow', 'Total Cash Flow' ] 
            
            r = 0 
            f = open(path1,"r")
            reader=csv.reader(f)

            for row in reader:
                c=0
                r+=1
                if(r<2):
                    continue
                List4 = [ ]
                for col in row:

                    List4.append(col)
                    c+=1
                    
                #if(r == 2):
                    #with open (path2 , 'a') as csvfile : 
                    #        csvwriter = csv.writer(csvfile) 
                    #        csvwriter.writerow(List7)
                            
                            
                if( r> 2):    
                    for i1 in range(0,len(List7)):
                        df2.loc[r-2,List7[i1]] = List4[i1]
                    df2.to_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " Format 1 .csv", index = False)
                
                
             
                
            df2.to_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " Format 1 .csv", index = False)
            
            csvData = pandasForSortingCSV.read_csv(path2)

            csvData.sort_values(['Year'],axis=0, ascending =[True] , inplace = True ) 

          

            csvData.to_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " Format 1 .csv", index  =False)
            
            
            
            
            
            
            f3 = open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " Format 2 .csv","w") 
            writer = csv.writer(f3)
            writer.writerow([""])
            f3.close()



            path3 ="C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " Format 2 .csv"
            df3 = pd.read_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " Format 2 .csv")
                    
            list11 = ['Year', 'TATA (Out Flow)', 'TATA (In Flow)',  'Net Out flow', 'Net In flow', 'Total Cash Flow' ] 
            
            r = 0 
            f = open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " Format 1 .csv","r")
            reader=csv.reader(f)

            for row in reader:
                c=0
                r+=1
                
                List11 = [ ]
                for col in row:
                    c+=1
                 
                    List11.append(col)
                    
                    
                
                
                
                f2 = open(path3,"a") 
                writer = csv.writer(f2)
                writer.writerow(List11)

                f2.close()            
                            
            
            List13 = ['KOTAK','LIC','TATA',"NJ"]
            
            
            
            for i4 in range ( 0 , len(List13)):
                
                
                
                if not os.path.exists( "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List13[i4] + ' In Flow.csv') :
                    pass
                else :
                
                    def delete_rows_with_keyword(csv_file, keyword, csv_file1):
                        # Read the CSV file into a DataFrame
                        df = pd.read_csv(csv_file)

                        # Convert the column to string if it contains non-string values
                        df['Policy_number'] = df['Policy_number'].astype(str)

                        # Filter the rows based on the keyword condition
                        filtered_df = df[df['Policy_number'] != keyword]

                        # Save the modified DataFrame back to the CSV file
                        filtered_df.to_csv(csv_file, index=False)
                       
                        df = pd.read_csv(csv_file1)

                        # Convert the column to string if it contains non-string values
                        df['Policy_number'] = df['Policy_number'].astype(str)

                        # Filter the rows based on the keyword condition
                        filtered_df = df[df['Policy_number'] != keyword]

                        # Save the modified DataFrame back to the CSV file
                        filtered_df.to_csv(csv_file1, index=False)
                      

                    # Example usage
                    csv_file = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\" + Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + List13[i4] + " Out Flow.csv"
                    
                    csv_file1 = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\" + Name1_Value.get() + "_\\" + Name1_Value.get() + " " + List13[i4] + " In Flow.csv"
                    
                    keyword = "0"
        
                    delete_rows_with_keyword(csv_file, keyword , csv_file1 )
            
            def delete_csv_file(file_path):
                if not os.path.exists(file_path):
    
                    return

                if not file_path.endswith(".csv"):
               
                    return

                os.remove(file_path)
            
            # Example usage
            file_path = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " .csv"
            delete_csv_file(file_path)

                        
                        
                            
            tmsg.showinfo("Report Generated ", "The Report of Client " + Name1_Value.get() + " is generated and saved on Destop .  ",parent=root)
            
            
            ctk.set_appearance_mode("light")
            root2=ctk.CTk()
            root2.geometry("450x120+660+450")
            root2.attributes("-topmost", True)
            root2.title("Generate Pdf")
            root2.config(background="white")
            root2.resizable(False, False)
            
            
            
            def convert_Pdf(C , C1 , C2 , C3 ):
                
                
                import webcolors
                
                
                from reportlab.lib import colors
                from tkinter import colorchooser
                
                from reportlab.lib.pagesizes import inch
                from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
            
                
                
                csv_file = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " Format 1 .csv"
                pdf_file = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\"+ current_date + Name1_Value.get() +"_\\"+  current_date  + " " + Name1_Value.get() +  " Format 1 .pdf"

                # Read the CSV file using pandas
                df = pd.read_csv(csv_file)
                
                df = df.astype(int)
                
                # Create a PDF document with custom page size
                
                if (N == 3):
                    doc = SimpleDocTemplate(pdf_file, pagesize=(12 * inch, 10   * inch), title="CSV to PDF")
                
                if (N == 2):
                    doc = SimpleDocTemplate(pdf_file, pagesize=(15 * inch, 10   * inch), title="CSV to PDF")
                
                if (N == 1):
                    doc = SimpleDocTemplate(pdf_file, pagesize=(18 * inch, 10   * inch), title="CSV to PDF")
                
                if (N == 0):
                    doc = SimpleDocTemplate(pdf_file, pagesize=(21 * inch, 10   * inch), title="CSV to PDF")
                    
                elements = []

                # Convert the dataframe to a 2D list for the table
                data = [list(df.columns)] + df.values.tolist()

                # Set a fixed width for the first column
                column_widths = [100] + [None] * (len(df.columns) - 1)

                # Define table style with the selected font color
                table_style = TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), C),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, 0), 12),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                    ("BACKGROUND", (0, 1), (-1, -1), C1),
                    ("GRID", (0, 0), (-1, -1), 1, C2),  # Add grid lines
                    ("TEXTCOLOR", (0, 1), (-1, -1), C3)  # Set font color
                ])

                # Create a table and apply the style
                table = Table(data, colWidths=column_widths)
                table.setStyle(table_style)

                # Add the table to the document
                elements.append(table)

                # Build the PDF document
                doc.build(elements)            
                
            
            def button_action(option):
                
                import webcolors


                from reportlab.lib import colors
                from tkinter import colorchooser
                
                from reportlab.lib.pagesizes import inch
                from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
                
                if (option == "Default Pdf"):
                    root2.destroy()
                                    
                    convert_Pdf(colors.black , colors.white ,colors.black , colors.black )
                    tmsg.showinfo("PDF Generated" , "The PDF report of client " + Name1_Value.get() + " generated and saved in folder " + current_date + Name1_Value.get() + "_ ." ,parent = root)
                    
                    
                if (option == "Formatting of Pdf"):
                
                   
                    root2.destroy()
                    root3=ctk.CTk()
                    root3.attributes("-topmost", True)#To keep tkinter window on top
                    root3.title("Formatting PDF")

                    root3.geometry("750x660+500+180")
                    root3.config(background="papayawhip")

                    frame = ctk.CTkFrame(root3 , width  =800 , bg_color=  "papayawhip" , fg_color=color , border_color="red" , corner_radius=20 , border_width=7 )
                    frame.pack(pady = 40)
                    
                    
                    f1 = Frame(frame, bg = "red", borderwidth=10, relief=RIDGE)
                    f1.grid(row  = 0 , column = 0  , columnspan = 3 ,  pady = 40)
                    W = ctk.CTkLabel ( f1 , text ="Formatting of PDF"  , text_color = "White" , fg_color = "red" , bg_color = "red" , font = my_font)
                    W.pack()  


                    
                        
                    def hex_to_color_name(hex_color):
                        try:
                            color_name = webcolors.hex_to_name(hex_color)
                            return color_name
                        except ValueError:
                            return "Unknown"


                    def select_color():
                        
                        color = colorchooser.askcolor(title="Select Header color" , parent = root3)
                        if color[1] is not None:
                           
                            color_name = hex_to_color_name(color[1])
                          
                            global selected_color
                            selected_color = color[1]
                            color_label.config(background =selected_color)
                        
                        else:
                            pass
                            
                    def select_color1():
                        
                        color = colorchooser.askcolor(title="Select Background color" , parent = root3)
                        if color[1] is not None:
                          
                            color_name = hex_to_color_name(color[1])
                            global selected_color1
                            selected_color1 = color[1]
                            color_label1.config(background = selected_color1)
                        else:
                            pass


                    def select_color2():
                        
                        color = colorchooser.askcolor(title="Select Font color" , parent = root3)
                        if color[1] is not None:
                          
                            color_name = hex_to_color_name(color[1])
                           
                            global selected_color2
                            selected_color2 = color[1]
                            color_label2.config(background=selected_color2)
                        else:
                           pass

                    def select_color3():
                        
                        color = colorchooser.askcolor(title="Select Border color" , parent = root3)
                        if color[1] is not None:
                           
                            color_name = hex_to_color_name(color[1])
                           
                            global selected_color3
                            selected_color3 = color[1]
                            color_label3.config(background=selected_color3)   
                        else:                 
                            pass
                            
                  
                    color_Frame = frame
                    
                    color_label = tk.Label(color_Frame, width=8 , text="", height=3 )
                    color_label.grid(row =  1 , column = 1 , padx  = 50 , pady = 20)
                    
                    color_label1 = tk.Label(color_Frame , width=8 , text = "", height=3)
                    color_label1.grid(row = 2 , column = 1 , pady = 20)
                    
                    color_label2 = tk.Label(color_Frame , width=8, text = "", height=3)
                    color_label2.grid(row =  3 , column = 1, pady = 20)
                    
                    
                    color_label3 = tk.Label(color_Frame , width=10-2, text = "", height=3)
                    color_label3.grid(row =  4 , column = 1, pady = 20)
                    
                    
                    def submit123():
                        
                        if "selected_color" in globals():
                            pass
                        else:
                            tmsg.showerror("ERROR" , "Please Select Header Color" , parent  = root3)
                            return
                        
                        
                        if "selected_color1" in globals():
                            pass
                        else:
                            tmsg.showerror("ERROR" , "Please Select Background Color" , parent  =root3)
                            return
                        
                        
                        if "selected_color2" in globals():
                            pass
                        else:
                            tmsg.showerror("ERROR" , "Please Select Font Color" , parent = root3  )
                            return
                        
                        
                        
                        if "selected_color3" in globals():
                            pass
                        
                        else:
                            tmsg.showerror("ERROR" , "Please Select Border Color" ,parent  = root3)
                            return
                            
                      
                        convert_Pdf(colors.HexColor(selected_color) , colors.HexColor(selected_color1) ,colors.HexColor(selected_color3), colors.HexColor(selected_color2) )
                        tmsg.showinfo("PDF Generated" , "The PDF report of client " + Name1_Value.get() + " generated and saved in folder " + current_date + Name1_Value.get() + "_ ." ,parent = root3)
                        root3.destroy()
                        
                    B1 = ctk.CTkButton ( frame  , bg_color="papayawhip" ,  fg_color = "white"  , text_color = "red" , hover_color= "lightgray" , cursor= "hand2" , text = " Submit ", corner_radius=0 , border_width=3 ,border_color="red" ,height=40 , font = my_font3 , command=submit123 )
                    B1.grid(row =  5 , column = 0 , columnspan = 3, pady = 20)


                    B2 = ctk.CTkButton ( frame , width=200 , bg_color="papayawhip" , text_color = "White" , fg_color="Red" , corner_radius= 10 , hover_color="Brown" , text = "Select Header Color" , font = my_font1 , command = select_color)
                    B2.grid(row =  1 , column = 0, padx  = 50)

                    B2 = ctk.CTkButton ( frame , width=200 , bg_color="papayawhip" , text_color = "White" , fg_color="Red" , corner_radius= 10  , hover_color="Brown" , text = "Select Background Color" , font = my_font1 , command = select_color1)
                    B2.grid(row =  2 , column = 0)

                    B3 = ctk.CTkButton ( frame , width =  200 , bg_color="papayawhip" , text_color = "White" , fg_color="Red" , corner_radius= 10  , hover_color="Brown" , text = "Select Font Color" , font = my_font1 , command = select_color2)
                    B3.grid(row =  3 , column = 0)

                    B4 = ctk.CTkButton ( frame , width =  200 , bg_color="papayawhip" , text_color = "White" , fg_color="Red" , corner_radius= 10  , hover_color="Brown" , text = "Select Border Color" , font = my_font1 , command = select_color3)
                    B4.grid(row =  4 , column = 0)
                    
                    root3.mainloop()
            
                if (option == "Cancel"):
                    root2.destroy()
                   
                    
                    
            
            # Create the custom dialog box on root
            dialog_frame = tk.Frame(root2, padx=20, pady=10 , bg = "white")
            dialog_frame.pack(pady = 15)

            message_label = tk.Label(dialog_frame, text="Do you want to Generate Pdf ?" , font = "comicsansms 15 normal" , bg = "white")
            message_label.pack()

            button_frame = tk.Frame(dialog_frame , bg = "white")
            button_frame.pack(pady=20)

            # Create three custom buttons
            button1 = ctk.CTkButton(button_frame, text="Formatting of Pdf", width=15 , fg_color="white" , border_color="#56adca" , border_width=2, bg_color="white"  , text_color= "black" , hover_color="#56adca"  , command=lambda: button_action("Formatting of Pdf"))
            button1.pack(side=tk.LEFT, padx=10)
            
            button2 = ctk.CTkButton(button_frame, text="Default Pdf", width=10 , fg_color="white" , border_color="#56adca" , border_width=2, bg_color="white" , text_color= "black" , hover_color="#56adca"  , command=lambda: button_action("Default Pdf"))
            button2.pack(side=tk.LEFT, padx=5)
            
            button3 = ctk.CTkButton(button_frame, text="Cancel", width=10 , fg_color="white" , border_color="#56adca" , border_width=2, bg_color="white" , text_color= "black" , hover_color="#56adca"  , command=lambda: button_action("Cancel"))
            button3.pack(side=tk.LEFT, padx=5)
                    
            root2.mainloop()
            
       
        
    
    
    

    
    
    
    B1 = ctk.CTkButton (tab.tab(" Report 1 ")  ,  fg_color = "white"  , text_color = "red" , hover_color= "lightgray" , cursor= "hand2" , text = "  Genrate Report  ", corner_radius=0 , border_width=3 ,border_color="red" ,height=40 , font = my_font3 , command=Sumbit_Report  )
    B1.grid(row = 3 , column = 0  , pady = 20 , columnspan = 2 )
    
    sorting_searching1( " Report 1 ", 1 , 1 )
    
def Policy_Number(Tab_Name1):
    global my_font1 , clicked1 , clicked2 , drop2
    
    
    my_font1 =  ctk.CTkFont(family="Comicsansms", size=15 , weight = "bold")
    

    Name = ctk.CTkLabel ( tab.tab(Tab_Name1) , corner_radius=10 ,  text ="Name of Client"  , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1 )
    Name.grid(row = 1 , column=0, pady = 25)
    
    Company = ctk.CTkLabel ( tab.tab(Tab_Name1) , corner_radius=10 ,  text ="Company Name"  , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1 )
    Company.grid(row = 1 , column=2, pady = 15)
    
    
    
    
    options1 = ["TATA","KOTAK" ,"NJ" ,"LIC"]
  
    # datatype of menu text
    clicked1 = ctk.StringVar()
    
    # initial menu text
    clicked1.set( " Select Company " )
    
    # Create Dropdown menu
    drop1 = ctk.CTkOptionMenu(tab.tab(Tab_Name1)   , dynamic_resizing=True , variable = clicked1 , values= options1 , bg_color= color , fg_color= "white" , text_color= "black" , button_color= "red" , button_hover_color = "#ad0303" , dropdown_fg_color="white" , dropdown_hover_color="#f7e7ce" )
    drop1.grid(row = 1, column = 3)
    
    
    def Find_Policy_Number():
        if not os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\" + Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + clicked1.get() + " Out Flow.csv" ) :
                tmsg.showerror("Doesn't Exists " , "The client " + Name1_Value.get() + " has no Policy in Company " + clicked1.get() , parent = root)
     
                clicked1.set(" Select Comany ")
        else:
            global clicked2,drop2
            if drop2:
                drop2.destroy()  # Remove the drop1 OptionMenu widget
            Path = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\" + Name1_Value.get() + "_\\"+ Name1_Value.get() + " " + clicked1.get() + " Out Flow.csv"
            df = pd.read_csv(Path)
            POLICY = []
            f = open(Path,"r")
            reader=csv.reader(f)
            r = 0 
            for row in reader:
                c=0
                r+=1
                
                for col in row:
                    c+=1
                    if ( r == 1):
                        continue
                    
                    if (c <= 4-1):
                        continue
                    
                    col1 = col + " (" + Name1_Value.get() + " , " + clicked1.get() + ")"
                    POLICY.append(col1)
                    
                    if (c >= 5-1):
                        break
            
            
            
            if len(POLICY) == 0:
                tmsg.showerror("No Polices found" , "There is no policy of client " + Name1_Value.get() + " in the company " + clicked1.get())
          
                return
            else:
                    
                options2 = POLICY
                
                # datatype of menu text
                clicked2 = ctk.StringVar()
                
                # initial menu text
                clicked2.set( " Select Policy ")
                
                
                
            
                
                # Create Dropdown menu
                drop2 = ctk.CTkOptionMenu(tab.tab(Tab_Name1), dynamic_resizing=False , variable = clicked2 , values= options2 , bg_color= color , fg_color= "white" , text_color= "black" , button_color= "red" , button_hover_color = "#ad0303" , dropdown_fg_color="white" , dropdown_hover_color="#f7e7ce" )
                drop2.grid(row = 1, column = 5 , columnspan  =2 , padx  =15 )
                
                
    
    Policy = ctk.CTkButton ( tab.tab(Tab_Name1) , corner_radius=10 ,  text ="Policy Number"  , width = 140  , text_color = "White" , fg_color = "red" , hover_color="Brown" , font = my_font1  , command = Find_Policy_Number)
    Policy.grid(row = 1 , column=4, pady = 15)
    
    
    sorting_searching1( Tab_Name1, 1 , 1 )
    
def Surrender():
    global tab , Name1_Value
    my_font1 =  ctk.CTkFont(family="Comicsansms", size=15 , weight = "bold")
    

    for widget in frame1.winfo_children():
        widget.destroy()
        
    frame2.place_forget()
        
        
    
    tab = ctk.CTkTabview(frame1  ,  height=400 , border_color= "red" , border_width= 6+1  , corner_radius= 25 , bg_color="papayawhip" , fg_color= color , segmented_button_fg_color="red" , segmented_button_selected_color="#e06666", segmented_button_unselected_color="#f54747" , text_color="black" , segmented_button_unselected_hover_color="#f54747" , segmented_button_selected_hover_color="#e06666" )
    tab.pack(side = "left" , pady = 30 , padx = 2 )
    

    
    
    
    tab.add(" Surrender Policy ")
    
    
    f1 = Frame(tab.tab(" Surrender Policy "), width = 24 ,  bg = "red" ,  borderwidth=10, relief=RIDGE)
    f1.grid( row = 0 , column  = 2 , pady = 5 ,columnspan=2 )
    W = Label ( f1 , text ="  Surrender Policy  "  , width = 17+4   , fg = "White" , bg = "red" , font = ("comicsansms 22 bold"))
    W.pack()
    
    
    Year_Out = ctk.CTkLabel ( tab.tab(" Surrender Policy ") , corner_radius=10 ,  text ="Year Out Flow"  , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1 )
    Year_Out.grid(row = 3 , column=0, padx = 5 , pady  =15)
    
    Year_In = ctk.CTkLabel ( tab.tab(" Surrender Policy ") , corner_radius=10 ,  text ="Years In Flow"  , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1 )
    Year_In.grid(row = 3 , column=2, pady = 15)
    
    Money_In = ctk.CTkLabel ( tab.tab(" Surrender Policy ") , corner_radius=10 ,  text ="Money In Flow"  , width = 140  , text_color = "White" , fg_color = "red" , font = my_font1 )
    Money_In.grid(row = 3 , column=4, pady = 15)
    
    
    Year_Out_Value = ctk.CTkEntry( tab.tab(" Surrender Policy ") , corner_radius=10 ,  placeholder_text = "Year Out Flow"  , width = 140 , placeholder_text_color="black" , text_color="black"  , border_color = "red"  , border_width=2)
    Year_Out_Value.grid(row = 3 , column=1, padx = 5 , pady  =15)
    
    Year_In_Value = ctk.CTkEntry ( tab.tab(" Surrender Policy ") , corner_radius=10  ,  placeholder_text = "Year In Flow"   , width = 140 , placeholder_text_color="black" , text_color="black"     , border_color = "red" , border_width=2 )
    Year_In_Value.grid(row = 3 , column=3, pady = 15)
    
    Money_In_Value = ctk.CTkEntry ( tab.tab(" Surrender Policy ") , corner_radius=10  ,  placeholder_text = "Money In Flow"  , width = 140 , placeholder_text_color="black" , text_color="black"     , border_color = "red" , border_width=2 )
    Money_In_Value.grid(row = 3 , column=5, pady = 15*2 , padx  =5*2)
    
    setup_entry_widget("Year Out Flow", 4 , Year_Out_Value)
    setup_entry_widget("Year In Flow" , 4 , Year_In_Value)
    
    Button_F = ctk.CTkFrame(tab.tab(" Surrender Policy ") , fg_color=  color)
    Button_F.grid(row  = 4 , column  = 2 , columnspan  = 2 , pady = 15)
    
    def Trim_Values_1():
        global ERROR2 , Money_In_Val , Name_Val2
        
        ERROR2 = 0 
        
        
        
        Money_In_Val  =  ' '.join((str(Money_In_Value.get())).split())
        Name_Val2 = ' '.join((str(Name1_Value.get())).split()).title()
        
        
        if drop2 is None :
            tmsg.showerror("ERROR" , " Please select Policy Number . ")
            ERROR2 = 1
            return
        
        
        if not os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val2 + "_" ) :
            tmsg.showerror("ERROR" , " Please enter valid \' Name of Client \' . ")
            ERROR2 = 1
            return
        
        if not os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val2 + "_" + "\\" + Name_Val2 + " " + clicked1.get() + " Out Flow" + '.csv') :
            tmsg.showerror("ERROR" , " The Client " + Name_Val2 + " has no Policy in Company " + clicked1.get())
            ERROR2 = 1
            return
        
        
        if ( len(Year_In_Value.get()) != 4 ):
            tmsg.showerror("ERROR", "Please Enter 4 Digits in \"Years In Flow\" ." )
            ERROR2  = 1
            return
        if ( len(Year_Out_Value.get()) != 4 ):
            tmsg.showerror("ERROR", "Please Enter 4 Digits in \"Years Out Flow\" ." )
            ERROR2  = 1
            return
        if ( Year_In_Value.get().isdigit() == False):
            tmsg.showerror("ERROR", "Please Enter Numerical Values in \"Years In Flow\" ." )
            ERROR2  = 1
            return
        if ( Year_Out_Value.get().isdigit() == False):
            tmsg.showerror("ERROR", "Please Enter Numerical Values in \"Years Out Flow\" ." )
            ERROR2  = 1
            return
        if ( Money_In_Val.isdigit() == False):
            tmsg.showerror("ERROR", "Please Enter Numerical Values in \"Money In Flow\" ." )
            ERROR2  = 1
            return
        
        
    
    def desellect_ALL2():
        
        Name1_Value.delete(0,END)
        clicked1.set("Select Company")
        if drop2 is not None:
            drop2.destroy()
        Year_In_Value.delete(0 ,END)
        Year_Out_Value.delete(0 ,END)
        Money_In_Value.delete(0,END)
        
        
        
        Year_In_Value.configure(placeholder_text = "Year In Flow")
        Year_Out_Value.configure(placeholder_text = "Year Out Flow")
        Money_In_Value.configure(placeholder_text = "Money In Flow")
        
        
    def Surrender_Policy():
        Trim_Values_1()
        
        if ERROR2  == 1 :
            return
        
        #For Out Flow 
        Path3 = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val2 + "_" + "\\" + Name_Val2 + " " + clicked1.get() + " Out Flow" + '.csv'
    
        Policy = str(clicked2.get())
       
        
        Policy = Policy[0:int(len(clicked2.get())) - (int(len(Name_Val2)) + int(len(clicked1.get()) + int(6)))]
        
        yEAR = int(Year_Out_Value.get())
        Year = "Years Out flow (" + str(yEAR)+")"
        df = pd.read_csv(Path3)
        t_r=len(df.axes[0]) 

        t_c=len(df.axes[1]) 
        r=0
        
        r1 = 0 
        N1 = 0 
        f = open(Path3,"r")
        reader=csv.reader(f)

        for row in reader:
            c=0
            r+=1
            
            for col in row:
                c+=1
                col1 = col[16: 20]
                
                if ( col == Policy):
                    rr = r
                    
                    
        r=0
        r1 = 0 
        N1 = 0 
        f = open(Path3,"r")
        reader=csv.reader(f)
        Cell_Value = []
        for row in reader:
            c=0
            r+=1
            
            for col in row:
                c+=1
                col1 = col[16: 20]
                if ( col1 > str(yEAR) and str(col1) != "y" ):
                    #print( "io")
                    df.loc[t_r+5,t_c-1] = " "
                    
                    
                    df= pd.read_csv(Path3)
                    df.loc[r-1, "Years Out flow ("+str(col1)+")"] = " "
                    df.to_csv(Path3 , index = False)
        
        df = pd.read_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name_Val2 + "_\\"+ Name_Val2 + " " + clicked1.get() + ' Out Flow.csv') 
                    
        df.fillna(0, inplace = True)

        df.to_csv("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+ Name_Val2 + "_\\"+ Name_Val2 + " " + clicked1.get() + ' Out Flow.csv', index = False)                  
                    
                    
        #For In Flow 
        
        Path4 = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\" + Name_Val2 +"_\\"+Name_Val2+" "+clicked1.get() +" In Flow.csv"
        Year ='Years In Flow ('+ Year_In_Value.get() + ')'
        r=0
        f = open(Path4,"r")
        reader=csv.reader(f)
        n = 0 
        for row in reader:
            c=0
            r+=1
            
            for col in row:
                c+=1
                
                if( col  == Policy):
                    rr = r
                    
                if( col  == Year):
                    cc = c
                    n+=1
           
        list2 = []

        r=0
        f = open(Path4,"r")
        reader=csv.reader(f)

        for row in reader:
            c=0
            r+=1
            
            for col in row:
                c+=1
                if( c == 7):
                    break
                if( r== rr):
                    list2.append(col)
                    
                    

            
        df = pd.read_csv(Path4)   
        
            
        
        path = Path4


        t_r1=len(df.axes[0]) 

        t_c1=len(df.axes[1]) 
        
        if( n != 0 ):
            for i in range ( 0 , cc - 7 ):
                list2.append(" ") 
        else:
            for i in range ( 0 , t_c1-6 ):
                list2.append(" ")
        
        list2.append(Money_In_Val) 
        
        
        
        def delete_rows_with_keyword(csv_file, keyword):
                # Read the CSV file into a DataFrame
                df = pd.read_csv(csv_file)

                # Convert the column to string if it contains non-string values
                df['Policy_number'] = df['Policy_number'].astype(str)

                # Filter the rows based on the keyword condition
                filtered_df = df[df['Policy_number'] != keyword]
                
                
                if( n == 0 ):
                    filtered_df.loc[1,str(Year)]  = " "
                else:
                    pass
                

                # Save the modified DataFrame back to the CSV file
                filtered_df.to_csv(csv_file, index=False)
               



            # Example usage
            
            
        csv_file = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\" + Name_Val2 + "_\\"+  Name_Val2 + " " + clicked1.get() + " In Flow.csv"
            
            
        keyword = Policy

        delete_rows_with_keyword(csv_file, keyword )
        


    
    
        
        df= pd.read_csv(Path4)    
            
        f2 = open(Path4,"a") 
        writer = csv.writer(f2)
        writer.writerow(list2)
        f2.close()
        
        
        df = pd.read_csv(Path4)
        
        
        
        df.fillna(0, inplace = True)
        df.to_csv(Path4, index = False)
        
        
        def delete_rows_with_keyword(csv_file, keyword, csv_file1):
        # Read the CSV file into a DataFrame
            df = pd.read_csv(csv_file)

            # Convert the column to string if it contains non-string values
            df['Policy_number'] = df['Policy_number'].astype(str)

            # Filter the rows based on the keyword condition
            mask = df['Policy_number'].str.contains(keyword)
            filtered_df = df[~mask]  # Use ~ to negate the mask and get non-matching rows

            # Save the modified DataFrame back to the CSV file
            filtered_df.to_csv(csv_file, index=False)            
            
            df = pd.read_csv(csv_file1)

            # Convert the column to string if it contains non-string values
            df['Policy_number'] = df['Policy_number'].astype(str)

            # Filter the rows based on the keyword condition
            mask = df['Policy_number'].str.contains(keyword)
            filtered_df = df[~mask]  # Use ~ to negate the mask and get non-matching rows

            # Save the modified DataFrame back to the CSV file
            filtered_df.to_csv(csv_file1, index=False)
            

        # Example usage
        csv_file = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\" + Name_Val2 + "_\\"+ Name_Val2 + " " + clicked1.get() + " Out Flow.csv"
        csv_file1 = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\" + Name_Val2 + "_\\"+ Name_Val2 + " " + clicked1.get() + " In Flow.csv"
        keyword = "0"

        delete_rows_with_keyword(csv_file, keyword,csv_file1)
        
        
        df = pd.read_csv(Path3)
        df.fillna(0, inplace = True)
        df.to_csv(Path3, index = False)
        
        
        
        df = pd.read_csv(Path4)
        df.fillna(0, inplace = True)
        df.to_csv(Path4, index = False)
    
        tmsg.showinfo("The policy of client " + Name_Val2 +  " is surrendered " , " Client Name = " + Name_Val2 + " \n Company Name " + clicked1.get() +  "\n Policy Number =  "+ clicked2.get() +"\n Year Out Flow (Last year  )  = " + Year_Out_Value.get() + " \n Year In flow = "  + Year_In_Value.get() + " \n Money Recived  in year "+Year_In_Value.get() +  "= " + Money_In_Val ,parent=root)
        
        
        global drop2
        Year_Out_Value.delete(0, END)
        Year_In_Value.delete(0, END)
        Money_In_Value.delete(0, END)
        clicked1.set("Select Company ")
        if drop2 is not None:
            drop2.destroy()
        
        
        
        
        
        
        
        
   
    B1 = ctk.CTkButton (Button_F ,  fg_color = "white"  , text_color = "red" , hover_color= "lightgray" , cursor= "hand2" , text = "  Surrender  ", corner_radius=0 , border_width=3 ,border_color="red" ,height=40 , font = my_font3  , command = Surrender_Policy)
    B1.pack(side  = "right" , padx  = 13)
    
    deselect_button = ctk.CTkButton( Button_F ,  fg_color = "white"  , text_color = "red",  hover_color= "lightgray" , cursor= "hand2" , text="Clear All", corner_radius=0 , border_width=3 ,border_color="red" , height=40 , font = my_font3 , command= desellect_ALL2 )
    deselect_button.pack(side  = "left" , padx  = 13)
    
    
    
    Policy_Number(" Surrender Policy ")
 
 
def Delete():
    global tab , Name1_Value
    my_font1 =  ctk.CTkFont(family="Comicsansms", size=15 , weight = "bold")
    

    for widget in frame1.winfo_children():
        widget.destroy()
    
    frame2.place_forget()
        
        
    
    tab = ctk.CTkTabview(frame1  ,  height=200 , border_color= "red" , border_width= 6+1  , corner_radius= 25 , bg_color="papayawhip" , fg_color= color , segmented_button_fg_color="red" , segmented_button_selected_color="#e06666", segmented_button_unselected_color="#f54747" , text_color="black" , segmented_button_unselected_hover_color="#f54747" , segmented_button_selected_hover_color="#e06666" )
    tab.pack(side = "left" , pady = 30 , padx = 2 )
    

    
    
    
    tab.add(" Delete Policy ")
    
    
    
    f1 = Frame(tab.tab(" Delete Policy "), width = 24 ,  bg = "red" ,  borderwidth=10, relief=RIDGE)
    f1.grid( row = 0 , column  = 2 , pady = 5 ,columnspan=2 )
    W = Label ( f1 , text ="Delete Policy"  , width = 17+4   , fg = "White" , bg = "red" , font = ("comicsansms 22 bold"))
    W.pack()
    
    Invisible  = ctk.CTkLabel(tab.tab(" Delete Policy ") ,  text = " " , width  =160 , fg_color= color , corner_radius=0)
    Invisible.grid(row = 4 , column  = 6 )

    Policy_Number(" Delete Policy ")
    
    Button_F = ctk.CTkFrame(tab.tab(" Delete Policy ") , fg_color=  color)
    Button_F.grid(row  = 4 , column  = 2 , columnspan  = 2 , pady = 15)
    
    def deselect_All3():
        Name1_Value.delete( 0, END )
        clicked1.set(" Select Company ")
        if drop2 is not None:
            drop2.destroy()  
            
    def Check3():
        global ERROR3 , Name_Val3 , drop2 , Policy
        
        ERROR3  = 0 
        
        Name_Val3 = ' '.join((str(Name1_Value.get())).split()).title()
        
        if not os.path.exists("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\"+Name_Val3 + "_" ) :
            tmsg.showerror("ERROR" , " Please enter valid \' Name of Client \' . ")
            ERROR3  = 1
            return
        
        if clicked1.get() == " Select Company ":
            tmsg.showerror("ERROR" , " Please Select Company Name . ")
            ERROR3  = 1
            return
    
        
        if clicked2.get() == " Select Policy ":
            
            tmsg.showerror("ERROR" , " Please Select Policy Number . ")
            ERROR3  = 1
            return
        
        Policy = clicked2.get()
        
        Policy = Policy[0:int(len(clicked2.get())) - (int(len(Name_Val3)) + int(len(clicked1.get()) + int(6)))]
        
            
        Warning = messagebox.askokcancel("Deleting Policy","Are you sure to delete the Policy of \nClient : \"" + Name_Val3 + "\" ,   Company : \"" + clicked1.get()  + "\" , Policy Number : \"" + Policy + "\"  " , icon  = messagebox.WARNING )
        if ( Warning == False ):
            deselect_All3()
            ERROR3 = 1
            return
        
        
    def Delete_Policy():
        global drop2 , Plan
        
        ERROR3 = 0 
        
        
        
        Check3()
        
        if ERROR3 == 1:
            return
        
        
      
        #Policy = Policy[0:int(len(clicked2.get())) - (int(len(Name_Val3)) + int(len(clicked1.get()) + int(6)))]
        
        
        Path = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\" + Name_Val3 + "_\\"+ Name_Val3 + " " + clicked1.get() + " Out Flow.csv"
    
        def delete_rows_with_keyword(csv_file, keyword ,csv_file1):
                # Read the CSV file into a DataFrame
                df = pd.read_csv(csv_file)

                # Convert the column to string if it contains non-string values
                df['Policy_number'] = df['Policy_number'].astype(str)

                # Filter the rows based on the keyword condition
                filtered_df = df[df['Policy_number'] != keyword]
                
                # Save the modified DataFrame back to the CSV file
                filtered_df.to_csv(csv_file, index=False)
               
                
                
                
                df = pd.read_csv(csv_file1)

                # Convert the column to string if it contains non-string values
                df['Policy_number'] = df['Policy_number'].astype(str)

                # Filter the rows based on the keyword condition
                filtered_df = df[df['Policy_number'] != keyword]
                
                # Save the modified DataFrame back to the CSV file
                filtered_df.to_csv(csv_file1, index=False)
               



                # Example usage
                
                
        csv_file = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\" + Name_Val3 + "_\\"+  Name_Val3 + " " + clicked1.get() + " In Flow.csv"
        csv_file1 = "C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Data Entry\\" + Name_Val3 + "_\\"+  Name_Val3 + " " + clicked1.get() + " Out Flow.csv"
        keyword = Policy
        delete_rows_with_keyword(csv_file, keyword , csv_file1 )
        
        
        
        
        tmsg.showinfo("Policy Deleted" , "Policy is Deleted \nClient Name = " + Name_Val3 + "\nCompany Name = " + clicked1.get() +"\nPolicy Number = " + Policy)

        deselect_All3()
    
    
    B1 = ctk.CTkButton (Button_F ,  fg_color = "white"  , text_color = "red" , hover_color= "lightgray" , cursor= "hand2" , text = "  Delete  ", corner_radius=0 , border_width=3 ,border_color="red" ,height=40 , font = my_font3  , command = Delete_Policy)
    B1.pack(side  = "right" , padx  = 13)
    
    deselect_button = ctk.CTkButton( Button_F ,  fg_color = "white"  , text_color = "red",  hover_color= "lightgray" , cursor= "hand2" , text="Clear All", corner_radius=0 , border_width=3 ,border_color="red" , height=40 , font = my_font3 , command= deselect_All3 )
    #deselect_button.pack(side  = "left" , padx  = 13)
    
    
    
    
    
    
# animated widgets

animated_panel = SlidePanel(root, -0.43, -0.72)
ctk.CTkLabel(animated_panel, text = '' , height=40 , bg_color="#fde8c6").pack(expand = False, fill = 'both')
my_font2 = ctk.CTkFont(family="Comicsansms", size=15, weight = "normal")

ctk.CTkButton(animated_panel ,text = "Home                " , image= Image0 , corner_radius=80 , font = my_font2 , height= 50 , bg_color="#fde8c6" , fg_color="#e2ceaf" , text_color= "black" , hover_color="#d2c2b2" , command= Home).pack(fill = "both", padx = 8)
ctk.CTkLabel(animated_panel, text = '' , height=30 , bg_color="#fde8c6").pack(expand = False, fill = 'both' )
ctk.CTkButton(animated_panel ,text = "Register Client" , image= Image1 , corner_radius=80 , font = my_font2 , height= 50 , bg_color="#fde8c6" , fg_color="#e2ceaf" , text_color= "black" , hover_color="#d2c2b2" , command= Register).pack(fill = "both", padx = 8, pady  =15)
ctk.CTkLabel(animated_panel, text = '' , height=30 , bg_color="#fde8c6").pack(expand = False, fill = 'both')
ctk.CTkButton(animated_panel ,text = "Generate Report" , image= Image2 , corner_radius=80 , font = my_font2 , height= 50 , bg_color="#fde8c6" , fg_color="#e2ceaf" , text_color= "black" , hover_color="#d2c2b2" , command= Report).pack(fill = "both", padx = 6)
ctk.CTkLabel(animated_panel, text = '' , height=30 , bg_color="#fde8c6").pack(expand = False, fill = 'both')
ctk.CTkButton(animated_panel ,text = "Surrender Policy" , image= Image3 , corner_radius=80 ,  font = my_font2 , height= 50 , bg_color="#fde8c6" , fg_color="#e2ceaf" , text_color= "black" , hover_color="#d2c2b2" , command  = Surrender ).pack(fill = "both", padx = 8, pady  =15)
ctk.CTkLabel(animated_panel, text = '' , height=30 , bg_color="#fde8c6").pack(expand = False, fill = 'both')
ctk.CTkButton(animated_panel ,text = "Delete Policy      " , image= Image4 , corner_radius=80 , font = my_font2 , height= 50 , bg_color="#fde8c6" , fg_color="#e2ceaf" , text_color= "black" , hover_color="#d2c2b2" , command  = Delete ).pack(fill = "both", padx = 8)
ctk.CTkLabel(animated_panel, text = '' , height=30 , bg_color="#fde8c6").pack(expand = False, fill = 'both')

#Image
Image = ctk.CTkImage(Image.open("C:\\Users\\NAITIK SHAH\\OneDrive\\Desktop\\Icons\\image-removebg-preview.png").resize((50,20) ))
# button
button_x = 0.5
button = ctk.CTkButton(f1 , image = Image  , text = '' , width = 20 , corner_radius=10 , hover_color="#cf8806" , height=25 , fg_color="#cf8806" , bg_color= "#cf8806", command = animated_panel.animate ,border_width=10 , border_color="#cf8806" )
button.pack(side = "left" , padx  = 10 , ipadx  = 5)

Home()

# run
root.mainloop()
