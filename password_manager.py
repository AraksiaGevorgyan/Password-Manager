from tkinter import CENTER, Tk,Label,Button, Entry, Frame, END, Toplevel, messagebox
from tkinter import ttk
from db_operations import DbOperations
import string
import secrets
from encryption import Encryption  # Import the Encryption class


class root_window:

    def __init__(self,root,db):
        self.db = db
        self.root = root
        self.root.resizable(False, False)
        self.root.title('Password Manager')
        self.root.geometry('1000x615+100+100' )
        self.root.configure(bg='steelblue')

        head_title = Label(self.root, text='Password Manager',font=('Arial',20,'bold'), padx=10, pady=10, justify=CENTER, anchor='center',bg='steelblue',fg='midnightblue').grid(padx=140,pady=30)


        self.crud_frame = Frame(self.root,highlightbackground='grey',
                                highlightthickness=2, padx=15,pady=15)
        self.crud_frame.grid()
        self.create_entry_labels()
        self.create_entry_boxes()
        self.create_crud_buttons()
        self.search_entry = Entry(self.crud_frame, width = 30, font=('Arial',12))
        self.search_entry.grid(row = self.row_no, column = self.col_no)
        self.col_no+=1
        Button(self.crud_frame, text = 'Search', bg = 'darkblue', fg = 'white',font = ('Ariel',12), width=25).grid(row = self.row_no, column = self.col_no, padx=5,pady=5)
        self.create_records_tree()



        search_button = Button(self.crud_frame, text='Search', bg='darkblue', fg='white',
                            font=('Ariel', 12), width=25, command=self.search_record)
        search_button.grid(row=self.row_no, column=self.col_no, padx=5, pady=5)


        self.row_no+=1

        #-----password features-------
                # Add a button to check password strength
                # Add an entry field for checking password strength


        self.check_password_entry = Entry(self.crud_frame, width=30, font=('Arial', 12))
        self.check_password_entry.grid(row=5, column=1, padx=5, pady=5)
        self.check_password_button = Button(self.crud_frame, text='Check Password Strength', bg='darkblue', fg='white',
                                            font=('Arial', 12), width=25, command=self.check_password_strength)
        self.check_password_button.grid(row=5, column=2, padx=5, pady=5)

        self.generate_button = Button(self.crud_frame, text='Generate Password', bg='darkblue', fg='white',
                                    font=('Arial', 12), width=20, command=self.generate_password)
        self.generate_button.grid(row=5, column=0, padx=5, pady=5)


        # self.check_password_entry = Entry(self.crud_frame, width=30, font=('Arial', 12))
        # self.check_password_entry.grid(row=self.row_no, column=self.col_no+1, padx=5, pady=5)

        # self.check_password_button = Button(self.crud_frame, text='Check Password Strength', bg='darkblue', fg='white',
        #                                     font=('Arial', 12), width=25, command=self.check_password_strength)
        # self.check_password_button.grid(row=self.row_no, column=self.col_no+2, padx=5, pady=5)

        #  # Add a button to generate a password
        # self.generate_button = Button(self.crud_frame, text='Generate Password', bg='darkblue', fg='white',
        #                             font=('Arial', 12), width=25, command=self.generate_password)
        # self.generate_button.grid(row=self.row_no, column=self.col_no, padx=5, pady=5)
        
        

        

    

    def generate_strong_password(self):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(16))  # Adjust the length as needed
        return password

    def generate_password(self):
        password = self.generate_strong_password()
        self.check_password_entry.delete(0, 'end')
        self.check_password_entry.insert(0, password)

    def is_strong_password(self, password):
        # Check minimum length
        if len(password) < 8:
            return False

        # Check for uppercase letters
        if not any(char.isupper() for char in password):
            return False

        # Check for lowercase letters
        if not any(char.islower() for char in password):
            return False

        # Check for digits
        if not any(char.isdigit() for char in password):
            return False

        # Check for special characters
        special_chars = set(string.punctuation)
        if not any(char in special_chars for char in password):
            return False

        # All criteria passed, password is strong
        return True

    def check_password_strength(self):
        password = self.check_password_entry.get()
        if self.is_strong_password(password):
            messagebox.showinfo('Password Strength', 'Strong Password!')
        else:
            messagebox.showwarning('Password Strength', 'Weak Password. Please use a stronger password.')

            #---------------------------



    def create_entry_labels(self):
        self.col_no , self.row_no = 0, 0
        labels_info = ('ID', 'Website','Username', 'Password')
        for label_info in labels_info:
            Label(self.crud_frame, text = label_info, bg='darkblue',fg='white', 
                font=('Ariel',10), padx=5, pady=5).grid(row=self.row_no, column=self.col_no,padx=2, pady=2)
            self.col_no+=1


    def create_crud_buttons(self):
        self.row_no+=1
        self.col_no=0
        buttons_info = (('Save',"darkblue",self.save_record), ('Update','darkblue',self.update_record), ('Delete','darkblue',self.delete_record),('Copy Password','darkblue',self.copy_password),('Show All Records','darkblue',self.show_records))
        for btn_info in buttons_info:
            if btn_info[0] == 'Show All Records':
                self.row_no+=1
                self.col_no=0
            Button(self.crud_frame, text = btn_info[0], bg=btn_info[1], fg='white',
                font=('Ariel',12), padx=2, pady=1, width=20,command=btn_info[2]).grid(row=self.row_no, column=self.col_no,padx=5, pady=10)
            self.col_no+=1

        
    def create_entry_boxes(self):
        self.row_no+=1
        self.entry_boxes = []
        
        self.col_no = 0
        for i in range(4):
            show = ""
            if i ==3 :
                show = "*"

            entry_box = Entry(self.crud_frame, width=17,font=("Ariel", 15),
                                background='lightgrey', show=show)
            entry_box.grid(row=self.row_no, column = self.col_no, padx = 15,pady=15)
            self.col_no+=1
            self.entry_boxes.append(entry_box)



# Inside your save_record method in root_window class
    def save_record(self):
        website = self.entry_boxes[1].get()
        username = self.entry_boxes[2].get()
        password = self.entry_boxes[3].get()
 
        # Create an instance of Encryption class
        encryptor = Encryption()

        # Encrypt the password
        encrypted_password = encryptor.encrypt_password(password)

        data = {
            'website': website,
            'username': username,
            'password': password,
            'encrypted_password': encrypted_password  # Include encrypted password in data
        }

        self.db.create_record(data)
        self.show_records()


    def update_record(self):
        ID = self.entry_boxes[0].get()
        website = self.entry_boxes[1].get()
        username = self.entry_boxes[2].get()
        password = self.entry_boxes[3].get()

        data = {
            'ID': ID,
            'website': website,
            'username': username,
            'password': password
        }
        self.db.update_record(data)
        self.show_records()

       

    def delete_record(self):
        ID = self.entry_boxes[0].get()

        self.db.delete_record(ID)
        self.show_records()



    def show_records(self):
        for item in self.records_tree.get_children():
            self.records_tree.delete(item)
        records_list = self.db.show_records()
       
        for record in records_list:
            self.records_tree.insert('',END, values=(record[0], record[3],record[4], record[5]))

    def create_records_tree(self):
        columns = ('ID', 'Website', 'Username' , 'Password')
        self.records_tree = ttk.Treeview(self.root, columns = columns,
        show='headings')
        self.records_tree.heading('ID', text='ID')
        self.records_tree.heading('Website', text='Website Name')
        self.records_tree.heading('Username', text='Username')
        self.records_tree.heading('Password', text='Password')
        self.records_tree['displaycolumns'] = ('Website', 'Username')
        

        self.records_tree.grid()

        def item_selected(event):
            for selected_item in self.records_tree.selection():
                item = self.records_tree.item(selected_item)
                record = item['values']
                for entry_box, item in zip(self.entry_boxes, record):
                    entry_box.delete(0, END)
                    entry_box.insert(0, item)
        self.records_tree.bind('<<TreeviewSelect>>', item_selected)


    #Copy to Clipboard
    def copy_password(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.entry_boxes[3].get())
        message = 'Password Copied'
        title = 'Copy'
        if self.entry_boxes[3].get()=='':
            message='Box is empty'
            title= 'Error'
        self.show_message(title,message)

#-----new----
    def search_record(self):
        keyword = self.search_entry.get()
        if keyword:
            records = self.db.search_records(keyword)
            self.display_search_results(records)
        else:
            self.show_message('Error', 'Please enter a keyword to search.')

    def display_search_results(self, records):
        self.records_tree.delete(*self.records_tree.get_children())
        for record in records:
            self.records_tree.insert('', END, values=(record[0], record[3], record[4], record[5]))


#---------------

    def show_message(self, title_box:str=None, message:str=None):
        TIME_TO_WAIT = 900   #in millisec
        root = Toplevel(self.root)
        background = 'lightblue'
        if title_box =='Error':
            background = 'red'
        root.geometry('200x30+600+200')
        root.title(title_box)
        Label(root,text = message, background=background, font=('Ariel',15), fg = 'white').pack(padx=4, pady=2)
        try:
            root.after(TIME_TO_WAIT, root.destroy)
        except Exception as e:
            print("Error occured", e)

 

if __name__ == "__main__":
    #create table if does not exist
    db_class = DbOperations()
    db_class.create_table()

    #create tkinter window
    root = Tk()
    root_class = root_window(root, db_class)
    root.mainloop()