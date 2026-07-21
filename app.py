# imports
import csv
import customtkinter as ctk
import os
from tkinter import filedialog, ttk

# GUI class
class AttendanceTrendsApp(ctk.CTk):
    def __init__(self):
        
        # inherit from CTK
        super().__init__()
        
        # app title
        self.title("Attendance Trends")
        
        # set initial width and height
        self.geometry("1000x600")

        # container for buttons
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10, padx=5)

        # new report button
        self.open_btn = ctk.CTkButton(self.button_frame, text="New Report", command=self.new_report)
        self.open_btn.pack(side="left", padx=5)

        # clear the tree; this button is hidden until tree is loaded with csv data
        self.clear_btn = ctk.CTkButton(self.button_frame, text="Clear", command=self.clear_data)

        # list saved reports button
        self.list_btn = ctk.CTkButton(self.button_frame, text="Saved Reports", command=self.list_saved_reports)
        self.list_btn.pack(side="left", padx=5)

        # close the app button
        self.exit_btn = ctk.CTkButton(self.button_frame, text="Exit", command=self.destroy)
        self.exit_btn.pack(side="left", padx=5)

    # new report button
    def new_report(self):
        # step 1: show the grade level text entry
        self.grade_level_text_box = ctk.CTkEntry(self, placeholder_text="Enter Grade Level: ")
        self.grade_level_text_box.pack(pady=5)

        # show the create report button
        self.open_csv_btn = ctk.CTkButton(self, text="Open CSV File", command=self.create_report)
        self.open_csv_btn.pack(pady=5)

        # text label to display user entry 
        self.output_label = ctk.CTkLabel(self, text="")
        self.output_label.pack(pady=5)

    # create the report
    def create_report(self):

        # error if no grade level entered

        # set initial directory as Desktop
        # file_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # temp direct file path
        file_path = '/Desktop'

        # to do: handle errors if user does not make a selection

        # show only csv file types
        file_types = [
            ("CSV", "*.csv"),
        ]

        # dialog for selecting file
        selected_file = filedialog.askopenfilename(
            initialdir=file_path,
            title="Select CSV File",
            filetypes=file_types
        )

        # exit method if can't find Desktop
        if not file_path: 
            return
        
        # create a window / frame / "tree" view below the buttons
        self.tree = ttk.Treeview(self, show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # remove anything in the window / frame below
        self.tree.delete(*self.tree.get_children())

        # open the file and display data in the "tree" container
        with open(selected_file, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader)
            self.tree["columns"] = headers
            for h in headers: self.tree.heading(h, text=h)
            for row in reader: self.tree.insert("", "end", values=row)

        user_text = self.grade_level_text_box.get() 
        # print(f"User typed: {user_text}")
        
        # 2. Update the label to display it
        self.output_label.configure(text=f"Importing data for grade level: {user_text}")

        # show the clear button
        self.clear_btn.pack(side="left", padx=5)

        # hide the open csv file button
        self.open_csv_btn.destroy()

        # hide the text entry box
        self.grade_level_text_box.destroy()

    # save imported csv

    # clear imported data
    def clear_data(self):
        # remove anything in the window / frame / tree below the buttons
        self.tree["columns"] = ()
        self.tree.delete(*self.tree.get_children())
        self.tree.destroy()
        self.output_label.destroy()
        self.open_csv_btn.destroy();
        self.grade_level_text_box.destroy()

        # hide clear button
        self.clear_btn.pack_forget()

        # to do: remove the tree, remove the grade level text box, remove the create report button

    # process the csv

    # list stored reports
    def list_saved_reports(self):
        pass

# 
if __name__ == "__main__":
    app = AttendanceTrendsApp()
    app.mainloop()