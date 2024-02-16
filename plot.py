import os
from supabase import create_client
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import json


def fetch():
    load_dotenv()
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    supabase = create_client(url, key)
    response = supabase.table("expense").select("date", "amount").execute()
    data_dict = response.data
    return data_dict


def plot(data_list):
    dates = [data["date"] for data in data_list]
    amounts = [data["amount"] for data in data_list]

    plt.figure(figsize=(10, 6))
    plt.scatter(dates, amounts, marker="o", color="b")  # Scatter plot
    plt.title("Amount vs Date")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()


data_list = fetch()
plot(data_list)
