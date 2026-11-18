import tkinter as tk
from math import comb
# muốn xác suất là 1 phân số
from fractions import Fraction


# hàm chính
def calculate():
    p = Fraction(entry_p.get())
    n = int(entry_n.get())
    i = int(entry_i.get())
    # định nghĩa lambda
    pmf = lambda k: comb(n, k) * p**k * (1 - p)**(n - k)
    r1.config(text=f"Probability (Number of Successes = {i}) =  {pmf(i).numerator}/{pmf(i).denominator} = {pmf(i):.8f}")
    result = sum(pmf(k) for k in range(i + 1))
    r2.config(text=f"Probability (Number of Successes <= {i}) = {result.numerator}/{result.denominator} = {result:.8f}")
    
# hàm bổ sung
def calculate_all():
    p = Fraction(entry_p.get())
    n = int(entry_n.get())
    text.delete("1.0", tk.END)
    # định nghĩa lambda
    pmf = lambda k: comb(n, k) * p**k * (1 - p)**(n - k)            
    for i in range(n+1):
        text.insert(tk.END, f"Probability (Number of Successes = {i}) =  {pmf(i).numerator}/{pmf(i).denominator} = {pmf(i):.8f} \n")
        result = sum(pmf(k) for k in range(i + 1))
        text.insert(tk.END, f"Probability (Number of Successes <= {i}) = {result.numerator}/{result.denominator} = {result:.8f} \n")

# tạo cửa sổ
root = tk.Tk()
# tiêu đề cửa sổ
root.title("Binominal Distribution")
# kích thước cửa sổ
root.geometry("900x600")

# hiện thị label_p
label_p = tk.Label(root, text="Enter Value For p: ")
label_p.grid(row=0,column=0)
# nhập xác suất p
entry_p = tk.Entry(root, width = 10)
entry_p.grid(row=0,column=1) 

# hiện thị label_n
label_n = tk.Label(root, text="Enter Value For n: ")
label_n.grid(row=1,column=0)
# nhập n
entry_n = tk.Entry(root, width = 10)
entry_n.grid(row=1,column=1)

# label i
label_i = tk.Label(root, text="Enter Value For i: ", height = 2)
label_i.grid(row=2,column=0)
# nhập i
entry_i = tk.Entry(root, width = 10)
entry_i.grid(row=2,column=1)

# space 
label_space = tk.Label(root, text="", width = 5)
label_space.grid(row=0,column=2)
# button start
btn_start = tk.Button(root, text = "Start", width = 10, height = 2, command = calculate)
btn_start.grid(row=0,column=3)
# button start
btn_quit = tk.Button(root, text = "Quit", width = 10, height = 2, command = root.destroy)
btn_quit.grid(row=2,column=3)
# space 
label_space_01 = tk.Label(root, text="", width = 5)
label_space_01.grid(row=0,column=4)
# button All
btn_all = tk.Button(root, text = "All", width = 10, height = 2, command = calculate_all)
btn_all.grid(row=0,column=5,sticky="w")

# hiện kết quả
r1 = tk.Label(root, text="?", height = 2)
r1.grid(row=3, columnspan = 5)
r2 = tk.Label(root, text="?", height = 2)
r2.grid(row=4, columnspan = 5)
r3 = tk.Label(root, text="All case:")
r3.grid(row=5, columnspan = 5)

# tạo 1 listbox
text = tk.Text(root, width=80, height=15)
scroll = tk.Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scroll.set)

text.grid(row=6, column=0, columnspan=5)
scroll.grid(row=6, column=5, sticky="ns")

# hiện cửa sổ lên
root.mainloop()