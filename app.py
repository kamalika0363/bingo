from flask import Flask, jsonify, render_template
import os
from supabase import create_client
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import json

app = Flask(__name__)
print("sdsdgds")

def fetch_dt():
    load_dotenv()
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    supabase = create_client(url, key)
    response = supabase.table("expense").select("date", "amount").execute()
    data_dict = response.data
    return data_dict

def plot_dt(data_list):
    dates = [data["date"] for data in data_list]
    amounts = [data["amount"] for data in data_list]
    return json.dumps({"dates": dates, "amounts": amounts})
    
    # plt.figure(figsize=(10, 6))
    # plt.scatter(dates, amounts, marker="o", color="b")  # Scatter plot
    # plt.title("Amount vs Date")
    # plt.xlabel("Date")
    # plt.ylabel("Amount")
    # plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    # plt.tight_layout()
    # plt.show()

def plot_dt(data_list):
    dates = [data["date"] for data in data_list]
    amounts = [data["amount"] for data in data_list]

    data_json = json.dumps({"dates": dates, "amounts": amounts})

    return data_json


@app.route('/api/data')
def some_function():
    data_list = fetch_dt()
    plot_dt(data_list)

    


@app.route('/')
def index_page():
    print("yolo yolo toloo")
    data = plot_dt(fetch_dt())
    print(data)
    return render_template('index.html',data=data)

if __name__ == '__main__':
    print("aaaaaa")
    app.run(debug=True)
