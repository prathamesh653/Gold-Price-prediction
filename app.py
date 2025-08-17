import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("gold_price_prediction.pkl", "rb"))   # <-- change filename here

# Prediction function
def predict_price():
    try:
        # Get input values from entry fields
        feature1 = float(entry1.get())
        feature2 = float(entry2.get())
        feature3 = float(entry3.get())
        feature4 = float(entry4.get())
        feature5 = float(entry5.get())

        # Arrange into numpy array for prediction
        features = np.array([[feature1, feature2, feature3, feature4, feature5]])

        # Predict
        prediction = model.predict(features)

        # Show result
        messagebox.showinfo("Prediction", f"Predicted Gold Price: {prediction[0]:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create Tkinter window
root = tk.Tk()
root.title("Gold Price Prediction")
root.geometry("400x300")

# Labels and Entry fields
tk.Label(root, text="SPX :").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="GLD :").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="USO :").pack()
entry3 = tk.Entry(root)
entry3.pack()

tk.Label(root, text="SLV :").pack()
entry4 = tk.Entry(root)
entry4.pack()

tk.Label(root, text="EUR/USD :").pack()
entry5 = tk.Entry(root)
entry5.pack()

# Predict button
predict_btn = tk.Button(root, text="Predict Price", command=predict_price, bg="gold")
predict_btn.pack(pady=10)

# Run the GUI
root.mainloop()
