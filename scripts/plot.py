import matplotlib.pyplot as plt 
import seaborn as sns

def plot_sentiment_data(df):
    plt.figure(figsize=(12, 6)) 
    sns.histplot(df, bins=30, kde=True) 
    plt.title('Sentiment Distribution of Headlines') 
    plt.xlabel('Sentiment Score') 
    plt.ylabel('Frequency')
    plt.show()