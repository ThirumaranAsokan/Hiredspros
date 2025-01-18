import matplotlib.pyplot as plt # type: ignore

def generate_mock_data():
    """
    Generates mock data for diversity metrics.

    Returns:
    - dict: A dictionary containing diversity metrics.
    """
    return {
        "Gender": {"Male": 50, "Female": 40, "Non-Binary": 10},
        "Ethnicity": {"White": 60, "Asian": 20, "Black": 15, "Hispanic": 5},
    }

def plot_metrics(data):
    """
    Visualizes diversity metrics using pie charts.

    Args:
    - data (dict): A dictionary containing diversity metrics.
    """
    for category, values in data.items():
        labels = values.keys()
        sizes = values.values()
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title(f"{category} Distribution")
        plt.show()

def main():
    metrics_data = generate_mock_data()
    plot_metrics(metrics_data)

if __name__ == "__main__":
    main()
