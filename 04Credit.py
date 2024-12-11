import tkinter

window = tkinter.Tk()
window.geometry("900x700")
window.title("Credit Approval/Denial")

# Initial settings
x = 0
y = 0
z = 0

#title for GUI
title_label = tkinter.Label(window, text="Credit Approval/Denial Check", fg="Black", width=50, height=2, font=("Oswald", 14, "bold"), anchor="w")
title_label.grid(row=0, column=1)

# Name Variable part
def name():
    fullname = entry_fullname.get()
    if fullname == "":
        message = "Name Cannot Be Empty!"
    else:
        message = "The Entered Name is: " + fullname
    message_result.configure(text=message)

# Name title
name_title_label = tkinter.Label(window, text="Please Enter Your Name: ", bg="#a0d8c7", fg="black", width=20, height=1, font=("Arial", 12, "bold"))
name_title_label.grid(row=11, column=1)

# Name Part
entry_fullname = tkinter.Entry(window, bg="#e7f7d3", fg="black", width=50)
entry_fullname.grid(row=12, column=1)

buttonname = tkinter.Button(window, text="Verify Name", command=name, width = 10, bg = "#377663", fg = "White")
buttonname.grid(row=14, column=1)

message_result = tkinter.Label(window, width=40, bg="#9ebab2", fg="black")
message_result.grid(row=13, column=1)

# Age Variable part
def age():
    Userage = entry_Userage.get()
    if Userage.isdigit():
        Userage = int(Userage)
        message2 = "The Entered Age is: " + str(Userage)
        if Userage > 110:
            message2 = "Invalid Age. Please enter a new number."
    else:
        message2 = "Invalid age! Please enter a valid number."
    message_result2.configure(text=message2)

# Age Title
Age_title_label = tkinter.Label(window, text="Please Enter Your Age: ", bg="#a0d8c7", fg="black", font=("Arial", 12, "bold"))
Age_title_label.grid(row=16, column=1)

# Age Part
entry_Userage = tkinter.Entry(window, bg="#e7f7d3", fg="Black", width=25)
entry_Userage.grid(row=17, column=1)

buttonage = tkinter.Button(window, text="Verify Age", command=age, bg = "#377663", fg = "White")
buttonage.grid(row=19, column=1)

message_result2 = tkinter.Label(window, width=30, bg="#9ebab2", fg="Black")
message_result2.grid(row=18, column=1)

# To Store Radio Button Values
group_selected = tkinter.StringVar()

# Education Variable part
def education_level():
    global y
    group = group_selected.get()

    if group == "No_Formal_Education":
        y = 0
        education_level_text = "Education Level: No Formal Education."
    elif group == "High_School_or_Equivalent":
        y = 1
        education_level_text = "Education Level: High School or Equivalent."
    elif group == "Undergraduate_or_Associates_degree":
        y = 2
        education_level_text = "Education Level: Undergraduate or Associate's degree."
    elif group == "Graduate_degree":
        y = 3
        education_level_text = "Education Level: Graduate degree (Master's, Doctorate, PhD, etc.)."

    message_result3.configure(text=education_level_text)

# Education Title
Education_title_label = tkinter.Label(window, text="Please Enter Your Level Of Education: ", bg="#a0d8c7", width = 35, fg="Black", font=("Arial", 12, "bold"))
Education_title_label.grid(row=11, column=0)

# Education Radio Buttons part
group_No_Formal_Education = tkinter.Radiobutton(window, text="No Formal Education", relief="raised", width=35, anchor='center',
                                                variable=group_selected, value="No_Formal_Education", command=education_level)
group_No_Formal_Education.grid(row=12, column=0)

group_High_School_or_Equivalent = tkinter.Radiobutton(window, text="High School or Equivalent", relief="raised", width=35, anchor='center',
                                                      variable=group_selected, value="High_School_or_Equivalent", command=education_level)
group_High_School_or_Equivalent.grid(row=13, column=0)

group_Undergraduate_or_Associates_degree = tkinter.Radiobutton(window, text="Undergraduate or Associate's degree", relief="raised", width=35, anchor='center',
                                                               variable=group_selected, value="Undergraduate_or_Associates_degree", command=education_level)
group_Undergraduate_or_Associates_degree.grid(row=14, column=0)

group_Graduate_degree = tkinter.Radiobutton(window, text="Graduate degree", relief="raised", width=35, anchor='center',
                                            variable=group_selected, value="Graduate_degree", command=education_level)
group_Graduate_degree.grid(row=15, column=0)

message_result3 = tkinter.Label(window, width=50, bg="grey", fg="White")
message_result3.grid(row=16, column=0)

# Annual Income Variable part
def annual_income():
    global x
    group = group_selected.get()

    if group == "Low_Income":
        x = 0
        annual_income_text = "Annual Income range: $0 to $15,000."
    elif group == "Lower_Middle_Income":
        x = 1
        annual_income_text = "Annual Income range: $15,001 to $30,000."
    elif group == "Middle_Income":
        x = 2
        annual_income_text = "Annual Income range: $30,001 to $50,000."
    elif group == "High_Income":
        x = 3
        annual_income_text = "Annual Income range: $50,001 and Above."

    message_result4.configure(text=annual_income_text)

# Annual Income Title
Annual_Income_title_label = tkinter.Label(window, text="Please Enter The Value Of Your Annual Income: ", bg="#a0d8c7", fg="Black", font=("Arial", 12, "bold"))
Annual_Income_title_label.grid(row=18, column=0)

# Annual Income Radio Buttons part
group_Low_Income = tkinter.Radiobutton(window, text="$0 to $15,000 (Low Income)", relief="raised", width=35, anchor='center',
                                                variable=group_selected, value="Low_Income", command=annual_income)
group_Low_Income.grid(row=19, column=0)

group_Lower_Middle_Income = tkinter.Radiobutton(window, text="$15,001 to $30,000 (Lower-Middle Income)", relief="raised", width=35, anchor='center',
                                                variable=group_selected, value="Lower_Middle_Income", command=annual_income)
group_Lower_Middle_Income.grid(row=20, column=0)

group_Middle_Income = tkinter.Radiobutton(window, text="$30,001 to $50,000 (Middle Income)", relief="raised", width=35, anchor='center',
                                                variable=group_selected, value="Middle_Income", command=annual_income)
group_Middle_Income.grid(row=21, column=0)

group_High_Income = tkinter.Radiobutton(window, text="$50,001 and Above (High Income)", relief="raised", width=35, anchor='center',
                                                variable=group_selected, value="High_Income", command=annual_income)
group_High_Income.grid(row=22, column=0)

message_result4 = tkinter.Label(window, width=50, bg="grey", fg="white")
message_result4.grid(row=23, column=0)

# Savings Amount Variable part
def savings_amount():
    global z
    group = group_selected.get()

    if group == "Minimal_Savings":
        z = 0
        savings_amount_text = "Savings Amount is: Minimal."
    elif group == "Low_Savings":
        z = 1
        savings_amount_text = "Savings Amount is: Low."
    elif group == "Moderate_Savings":
        z = 2
        savings_amount_text = "Savings Amount is: Moderate."
    elif group == "High_Savings":
        z = 3
        savings_amount_text = "Savings Amount is: High."

    message_result5.configure(text=savings_amount_text)

# Savings Amount Title
Savings_Amount_title_label = tkinter.Label(window, text="Please Enter The Value Of Your Savings: ", bg="#a0d8c7", fg="Black", font=("Arial", 12, "bold"))
Savings_Amount_title_label.grid(row=25, column=0)

# Savings Amount Radio Buttons part
group_Minimal_Savings = tkinter.Radiobutton(window, text="$0 to $5,000 (Minimal Savings)", relief="raised", width=35, anchor='center',
                                                variable=group_selected, value="Minimal_Savings", command=savings_amount)
group_Minimal_Savings.grid(row=26, column=0)

group_Low_Savings = tkinter.Radiobutton(window, text="$5,001 to $10,000 (Low Savings)", relief="raised", width=35, anchor='center',
                                                variable=group_selected, value="Low_Savings", command=savings_amount)
group_Low_Savings.grid(row=27, column=0)

group_Moderate_Savings = tkinter.Radiobutton(window, text="$10,001 to $20,000 (Moderate Savings)", relief="raised", width=35, anchor='center',
                                                variable=group_selected, value="Moderate_Savings", command=savings_amount)
group_Moderate_Savings.grid(row=28, column=0)

group_High_Savings = tkinter.Radiobutton(window, text="$20,001 and Above (High Savings)", relief="raised", width=35, anchor='center',
                                                variable=group_selected, value="High_Savings", command=savings_amount)
group_High_Savings.grid(row=29, column=0)

message_result5 = tkinter.Label(window, width=50, bg="grey", fg="White")
message_result5.grid(row=30, column=0)

# Approval Check
def check_credit():
    score = 2 * x + 3 * y + z
    if stable_job.get():
        score += 1
    if no_debt.get():
        score += 1
    if score >= 8:
        message_result6.configure(text="Credit APPROVED!")
        approval_label.configure(text="✅", fg="green", font=("Arial", 30))
    else:
        message_result6.configure(text="Credit DENIED!")
        approval_label.configure(text="❌", fg="red", font=("Arial", 30))
        
# Stable Job Checkbox
stable_job = tkinter.BooleanVar()

stable_job_checkbox = tkinter.Checkbutton(window, text="Do you have a stable job?", variable=stable_job)
stable_job_checkbox.grid(row=24, column=1)

# No Debt Checkbox
no_debt = tkinter.BooleanVar()

no_debt_checkbox = tkinter.Checkbutton(window, text="Are you debt free?", variable=no_debt)
no_debt_checkbox.grid(row=23, column=1)

# Button to check credit
check_credit_button = tkinter.Button(window, width = 30, height = 1, bg = "#377663", fg = "White", text="Check Credit", command=check_credit)
check_credit_button.grid(row=27, column=1)

message_result6 = tkinter.Label(window, width=20, fg="Black", font =("Arial", 12, "bold"))
message_result6.grid(row=34, column=0)

#Label to show the approval/denial graphic
approval_label = tkinter.Label(window, width=10, font=("Arial", 15))
approval_label.grid(row=45, column=0)

# Exit Variable part
def exit_program():
    window.destroy()

# Exit Button
exit_button = tkinter.Button(window, text="Exit", width = 20, command=exit_program, bg = "#ad3131", fg = "white", font = ("arial", 9, "bold"))
exit_button.grid(row=43, column=1)

window.mainloop()
