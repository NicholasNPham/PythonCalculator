import tkinter as tk

# Window Properties
root = tk.Tk()
root.geometry("600x700")
root.title("Calculator")

for r in range(5):
    root.rowconfigure(r, weight=1)

for c in range(4):
    root.columnconfigure(c, weight=1)

# Screen Displaying/Updating
screenDisplay = tk.StringVar()

# Check to see if expression was evaluated
justEvaluated = False

# Function to Display Button Press
def buttonPressed(value):
    # Check to See what ScreenDisplay Currently Have
    current = screenDisplay.get()
    global justEvaluated

    if justEvaluated == True and value != "=":
        screenDisplay.set("")
        justEvaluated = False
        current = screenDisplay.get()

    if current == "":
        if value.isdigit():
            screenDisplay.set(value)
        elif value == "C":
            screenDisplay.set("")
        else:
            return

    if value == "=":
        expression = current
        if expression and expression[-1] in calculatorOperators:
            return
        try:
            justEvaluated = True
            result = eval(expression)
            screenDisplay.set(str(result))
        except:
            screenDisplay.set("Error")

    else:
        if value == "C":
            screenDisplay.set("")
        elif value in calculatorOperators and current[-1] in calculatorOperators:
            screenDisplay.set(current[:-1] + value)
        else:
            screenDisplay.set(current + value)

# Label for Number Display
label = tk.Label(root, textvariable=screenDisplay, bg="black",fg="white",anchor="e",font=("Arial", 40))
label.grid(column=0, row=0, sticky="nsew", columnspan=4)

# Buttons for Grid List
calculatorLayout = ["7", "8", "9", "+",
                    "4", "5", "6", "-",
                    "1", "2", "3", "*",
                    "C", "0", "=", "/"]

calculatorOperators = ["+", "-", "*", "/"]

# Position Array for Buttons
for index, displayLabel in enumerate(calculatorLayout):
    # Conditions for Which Label Represents Which Color
    if displayLabel in calculatorOperators:
        backgroundColor = "darkgrey"
    elif displayLabel == "C":
        backgroundColor = "red"
    elif displayLabel == "=":
        backgroundColor = "lightblue"
    else:
        backgroundColor = "white"

    # Math to Determine Row and Column
    r = index // 4 + 1
    c = index % 4
    b = tk.Button(root,
                  text=displayLabel,
                  bg=backgroundColor,
                  fg="black",
                  anchor="center",
                  font=("Arial", 40),
                  command=lambda val=displayLabel: buttonPressed(val))
    b.grid(column=c, row=r, sticky="nsew")

# Start Program
root.mainloop()
