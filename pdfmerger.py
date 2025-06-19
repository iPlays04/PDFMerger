import PyPDF2,os
import tkinter as tk
from tkinter import filedialog

file_paths = []

bgclr = "#819A91"
priclr = "#A7C1A8"
secclr = "#D1D8BE"
hiclr = "#EEEFE0"

def pdfChoice():
    i=0
    
    global file_paths
    
    file_paths.clear()
    file_paths = list(filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF files", "*.pdf")]))
    print(file_paths)
    global boxes
    boxes=[]
    boxes.clear()
    global boxesvars
    boxesvars=[]
    boxesvars.clear()
    global buttons
    buttons = []
    buttons.clear()
   
    for widget in frPDFFrame.winfo_children():
        widget.destroy()

    for file in file_paths:
        boxesvars.append(tk.IntVar(value=0))
        
        button =tk.Button(frPDFFrame,text="up", bg=secclr, command=lambda i=i: up(i))
        buttons.append(button)
        button.grid(column=0,row=i)

        spinbox = tk.Spinbox(frPDFFrame, bg=secclr, width=2,from_=1, to=len(file_paths),textvariable=boxesvars[i])
        boxes.append(spinbox)
        spinbox.grid(column=1,row=i)

        label = tk.Label(frPDFFrame, text=file.split('/')[-1], bg=priclr)
        label.grid(column=2,row=i)

        i=i+1
    #print(boxes)


def merge_pdfs():
    pdf_merger = PyPDF2.PdfMerger()
    newfiles = [None] * len(file_paths)
    i=0
    for file in file_paths:
        newfiles[int(boxes[i].get())-1] = file_paths[i]
        i=i+1
    print(newfiles)

    for pdf in newfiles:
        with open(pdf, 'rb') as file:
            pdf_merger.append(file)

    with open(f"{entDestinationentry.get()}.pdf", 'wb') as output_file:
        pdf_merger.write(output_file)
    print("PDFs merged successfully!")

def up(index):
    hi = 0
    for box in boxes:
        if(int(box.get())>hi):hi=int(box.get())
    if(hi+1 <= len(file_paths)):
        boxesvars[index].set(hi+1)

# UI
root = tk.Tk()
root.title("Simple PDF Merger")
root.geometry('400x620')
root.configure(background=bgclr)
if(os.path.isfile('.\\icon.png')):
    root.iconphoto(False, tk.PhotoImage(file='.\\icon.png'))

btPdfChoice = tk.Button(root, text="PDF-Dateien wählen", bg=priclr,  command=pdfChoice, width=40)
btPdfChoice.pack(pady=10)

#frPDFMaster = tk.Frame(root, bg=priclr, height=400, width=380, highlightthickness=2, highlightbackground=hiclr, highlightcolor="white")
#frPDFMaster.pack(pady=10, expand=False)

frPDFFrame = tk.Frame(root, bg=priclr, height=400, width=380, highlightthickness=2, highlightbackground=hiclr, highlightcolor="white")
frPDFFrame.pack(pady=10, expand=False, fill="x")

#scrollbar=tk.Scrollbar(frPDFMaster,orient="vertical", bg=priclr)
#scrollbar.pack(pady=10,side="right")

labelEntry = tk.Label(root, bg=bgclr, text="Dateinamen für Merged File wählen:")
labelEntry.pack()

frEntry = tk.Frame(root)
frEntry.pack(pady=10)

entDestinationentry = tk.Entry(frEntry, bg=priclr, width=50)
entDestinationentry.pack(side="left")

labelHint = tk.Label(frEntry, bg=priclr, fg=hiclr, text=".pdf")
labelHint.pack(side="right")

btStartMerge = tk.Button(root, text="Zusammenfügen", bg=priclr,  command=merge_pdfs, width=40)
btStartMerge.pack(pady=10)


root.mainloop()