import tkinter as tk
import joblib 
import statsmodels.api as sm

loaded_model = joblib.load('./model/apt_price.pkl')

root = tk.Tk()
root.geometry("300x250")

def on_submit(event = None):
  year = year_entry.get()
  square = square_entry.get()
  floor = floor_entry.get()

  pred = loaded_model.predict([[1, int(year), int(square), int(floor)]])
  pred_label.configure(text="예측금액은 {:,.0f}만원입니다.".format(pred[0]))


year_label = tk.Label(root, text="Year:")
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack(pady=5)

square_label = tk.Label(root, text="Square:")
square_label.pack()
square_entry = tk.Entry(root)
square_entry.pack(pady=5)

floor_label = tk.Label(root, text="Floor:")
floor_label.pack()
floor_entry = tk.Entry(root)
floor_entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

pred_label = tk.Label(root, text="")
pred_label.pack(pady=10)

root.bind('<Return>', on_submit)
year_entry.focus_set()
root.mainloop()
