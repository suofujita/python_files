import tkinter as tk
from fractions import Fraction
import math

# các hàm chính
def BasicCase():
    lamda = Fraction(entry_lamda.get())
    i = int(entry_i.get())
    result = (math.exp(-lamda)*pow(lamda,i))/math.factorial(i)
    basic_result_01.config(text = f"P(X={i}) = {result}")
    op = 0
    for k in range(i+1):
        op += (math.exp(-lamda)*pow(lamda,k))/math.factorial(k)
    basic_result_02.config(text = f"P(X>{i}) = {1-op}")
    basic_result_03.config(text = f"P(X<={i}) = {op}")

def AdvancedCase():
    lamda = Fraction(ad_entry_lamda.get())
    t = Fraction(ad_entry_t.get())
    k = int(ad_entry_k.get())
    lamda_t = lamda*t
    result = (math.exp(-lamda_t)*pow(lamda_t,k))/(math.factorial(k))
    op = 0
    for i in range(k+1):
        op += (math.exp(-lamda_t)*pow(lamda_t,i))/(math.factorial(i))
    ad_result_01.config(text = f"P(N({t})={k}) = {result}")
    ad_result_02.config(text = f"P(N({t})<={k}) = {op}")
    ad_result_03.config(text = f"P(N({t})>={k}) = {1-op+result}")

# thiết lập cửa sổ
root = tk.Tk()
root.title("Poisson Distribution")
root.geometry("560x500")

# trường hợp cơ bản
header_01 = tk.Label(root, text = "1. Basic Case: given lamda & i")
header_01.grid(row = 0, column = 0)
label_lamda = tk.Label(root, text = "Enter Value For Lamda: ")
label_lamda.grid(row=1, column=0)
entry_lamda = tk.Entry(root, width = 10)
entry_lamda.grid(row=1, column=1)

label_i = tk.Label(root, text = "Enter Value For i: ")
label_i.grid(row=2, column=0)
entry_i = tk.Entry(root, width = 10)
entry_i.grid(row=2, column=1)

#space
space_01 = tk.Label(root, text="", width = 5)
space_01.grid(row=2, column=2)
btn_cal = tk.Button(root, text = "Calculate", width = 10, height = 1, command = BasicCase)
btn_cal.grid(row=1, column=3)

basic_result_01 = tk.Label(root, text ="?", height = 1)
basic_result_01.grid(row=3, columnspan = 5)
basic_result_02 = tk.Label(root, text ="?", height = 1)
basic_result_02.grid(row=4, columnspan = 5)
basic_result_03 = tk.Label(root, text ="?", height = 1)
basic_result_03.grid(row=5, columnspan = 5)

header_02 = tk.Label(root, text = "2. Advanced Case: given lamda & t & i")
header_02.grid(row=6, column=0)
ad_label_lamda = tk.Label(root, text = "Enter Value For lamda: ").grid(row=7,column=0)
ad_entry_lamda = tk.Entry(root, width = 10)
ad_entry_lamda.grid(row=7,column=1)
ad_label_t = tk.Label(root, text = "Enter Value For t: ").grid(row=8,column=0)
ad_entry_t = tk.Entry(root, width = 10)
ad_entry_t.grid(row=8,column=1)
ad_label_k = tk.Label(root, text = "Enter Value For k: ").grid(row=9,column=0)
ad_entry_k = tk.Entry(root, width = 10)
ad_entry_k.grid(row=9,column=1)

btn_ad_cal = tk.Button(root, text = "Calculate", width = 10, height = 1, command = AdvancedCase)
btn_ad_cal.grid(row=7, column=3)
ad_result_01 = tk.Label(root, text="?")
ad_result_01.grid(row=11, columnspan = 5)
ad_result_02 = tk.Label(root, text="?")
ad_result_02.grid(row=12, columnspan = 5)
ad_result_03 = tk.Label(root, text="?")
ad_result_03.grid(row=13, columnspan = 5)

quit = tk.Button(root, text = "Quit", width = 10, command = root.destroy).grid(row=14,column=5)
root.mainloop()