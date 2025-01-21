import matplotlib.pyplot as plt 
from prophet import Prophet 

import pandas as pd

def generate_mock_data():
    """
    Generates mock data for diversity metrics.
    """
    return {
        "Gender": {"Male": 50, "Female": 40, "Non-Binary": 10},
        "Ethnicity": {"White": 60, "Asian": 20, "Black": 15, "Hispanic": 5},
    }

def plot_metrics(data):
    """
    Visualizes diversity metrics using pie charts.
    
    """
    for category, values in data.items():
        labels = values.keys()
        sizes = values.values()
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title(f"{category} Distribution")
        plt.show()

def predict_diversity_trends(data):
    """
    Predicts future diversity trends based on past data using Facebook Prophet.
    """
    df = pd.DataFrame(data)
    df['ds'] = pd.date_range('2021-01-01', periods=len(df), freq='M')
    df['y'] = df['Male']  # Example: predicting Male gender representation

    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(df, periods=6)
    forecast = model.predict(future)
    model.plot(forecast)

def main():
    metrics_data = generate_mock_data()
    plot_metrics(metrics_data)
    predict_diversity_trends(metrics_data['Gender'])

if __name__ == "__main__": 
    main()