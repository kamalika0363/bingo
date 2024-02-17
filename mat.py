import os
from supabase import create_client
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import json


def fetch_dt():
    load_dotenv()
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    supabase = create_client(url, key)
    response = supabase.table("expense").select("date", "amount").execute()
    data_dict = response.data
    return data_dict


def fetch_cat():
    load_dotenv()
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    supabase = create_client(url, key)
    response = supabase.table("expense").select("amount", "category").execute()
    data_cat = response.data
    return data_cat


def plot_dt(data_list):
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


def plot_cat(data_pie):
    category_amounts = {}

    for entry in data_pie:
        category = entry["category"]
        amount = entry["amount"]
        category_amounts[category] = category_amounts.get(category, 0) + amount

    # Prepare data for pie plot
    categories = list(category_amounts.keys())
    amounts = list(category_amounts.values())

    # Plotting the pie plot
    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Distribution of Expenses by Category")
    plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


data_list = fetch_dt()
plot_dt(data_list)

data_pie = fetch_cat()
plot_cat(data_pie)
