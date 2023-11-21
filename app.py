import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import json
import easyocr
import threading
from textblob import TextBlob
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Function to read text from an image using EasyOCR
def read_text(file_path):
    results = reader.readtext(file_path)
    return ' '.join([result[1] for result in results])

# Function to describe the image using Azure Computer Vision
def describe_image(file_path):
    with open(file_path, "rb") as image_stream:
        analysis = client.analyze_image_in_stream(image_stream, visual_features=[VisualFeatureTypes.description])
    description = ''
    if analysis.description:
        description = ' '.join([caption.text for caption in analysis.description.captions])
    return description

# Function to analyze sentiment using TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}"

# Load Azure credentials from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

# Initialize Azure Computer Vision Client
cv_key = config['AZURE_COMPUTER_VISION_KEY']
cv_endpoint = config['AZURE_COMPUTER_VISION_ENDPOINT']
client = ComputerVisionClient(cv_endpoint, CognitiveServicesCredentials(cv_key))

# Function to update the GUI after processing is complete
def update_gui_after_processing(file_path, text, description, sentiment):
    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, f"File: {os.path.basename(file_path)}\n{text}\n")
    description_output.delete('1.0', tk.END)
    description_output.insert(tk.END, f"File: {os.path.basename(file_path)}\n{description}\n")
    sentiment_output.delete('1.0', tk.END)
    sentiment_output.insert(tk.END, sentiment)
    progress_bar.stop()

# Function to handle image processing in a separate thread
def process_image(file_path):
    try:
        text = read_text(file_path)
        description = describe_image(file_path)
        sentiment = analyze_sentiment(text)
        root.after(0, update_gui_after_processing, file_path, text, description, sentiment)
    except Exception as e:
        messagebox.showerror("Processing Error", str(e))
        progress_bar.stop()

# Modified upload_and_process_image function to use threading
def upload_and_process_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        progress_bar.start(10)
        threading.Thread(target=process_image, args=(file_path,), daemon=True).start()

# Set up the Tkinter window with enhanced layout and design
root = tk.Tk()
root.title("Image Analysis Tool")

# Layout using frames
main_frame = ttk.Frame(root)
main_frame.pack(padx=10, pady=10)

upload_button = ttk.Button(main_frame, text="Upload and Analyze Image", command=upload_and_process_image)
upload_button.pack()

progress_bar = ttk.Progressbar(main_frame, mode='indeterminate')
progress_bar.pack()

text_output = tk.Text(main_frame, height=10, width=60)
text_output.pack()

description_output = tk.Text(main_frame, height=10, width=60)
description_output.pack()

sentiment_output = tk.Text(main_frame, height=5, width=60)
sentiment_output.pack()

root.mainloop()
