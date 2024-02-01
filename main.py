from textblob import TextBlob
import tkinter as tk
from tkinter import ttk


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive sentiment!"
    elif sentiment_score < 0:
        return "Negative sentiment!"
    else:
        return "Neutral sentiment!"


def on_analyze_button_click():
    user_input = entry.get()

    # Perform sentiment analysis
    sentiment_result = analyze_sentiment(user_input)

    # Display the result
    result_label.config(text=f"Sentiment: {sentiment_result}")


# Create the main window
root = tk.Tk()
root.title("Fancy Sentiment Analysis")
root.geometry("500x250")  # Set window dimensions

# Create and place widgets with some fancy styling
frame = ttk.Frame(root, padding=10, style="My.TFrame")  # Use a custom style
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Enter a sentence:", font=("Arial", 14),
                  style="My.TLabel")  # Change font and use a custom style
label.grid(column=0, row=0, sticky=tk.W, pady=10)

entry = ttk.Entry(frame, width=30, font=("Arial", 12), style="My.TEntry")  # Change font and use a custom style
entry.grid(column=0, row=1, sticky=tk.W, pady=10)

analyze_button = ttk.Button(frame, text="Analyze", command=on_analyze_button_click,
                            style="My.TButton")  # Use a custom style
analyze_button.grid(column=1, row=1, sticky=tk.W, pady=10)

result_label = ttk.Label(frame, text="", font=("Arial", 16, "bold"), foreground="blue",
                         style="My.TLabel")  # Change font and use a custom style
result_label.grid(column=0, row=2, columnspan=2, pady=10)

# Apply custom styles
style = ttk.Style()
style.configure("My.TFrame", background="#f0f0f0")  # Set background color
style.configure("My.TLabel", font=("Arial", 12), background="#f0f0f0")  # Set background color
style.configure("My.TEntry", font=("Arial", 12), background="#e0e0e0")  # Set background color
style.configure("My.TButton", font=("Arial", 12, "bold"), background="#4caf50",
                foreground="white")  # Set background and text color

# Start the GUI
root.mainloop()
