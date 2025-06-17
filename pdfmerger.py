import PyPDF2
import tkinter as tk
from tkinter import filedialog

file_paths = []

def pdfChoice():
    i=0
    global file_paths
    file_paths.clear()
    file_paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF files", "*.pdf")])
    global boxes
    boxes=[]
    global boxesvars
    boxesvars=[]
    global buttons
    buttons = []
   

    for file in file_paths:
        boxesvars.append(tk.IntVar(value=0))
        
        button =tk.Button(frPDFFrame,text="up", bg="grey", fg="white", command=lambda i=i: up(i))
        buttons.append(button)
        button.grid(column=0,row=i)

        spinbox = tk.Spinbox(frPDFFrame, bg="grey", fg="white", width=2,from_=1, to=len(file_paths),textvariable=boxesvars[i])
        boxes.append(spinbox)
        spinbox.grid(column=1,row=i)

        label = tk.Label(frPDFFrame, text=file.split('/')[-1], bg="grey", fg="white")
        label.grid(column=2,row=i)

        i=i+1
    print(boxes)


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

    with open("merged.pdf", 'wb') as output_file:
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

btPdfChoice = tk.Button(root, text="PDF-Dateien wählen", command=pdfChoice)
btPdfChoice.pack(pady=10)

frPDFFrame = tk.Frame(root, bg="grey")
frPDFFrame.pack(pady=10)

btStartMerge = tk.Button(root, text="Zusammenfügen", command=merge_pdfs)
btStartMerge.pack(pady=10)


root.mainloop()