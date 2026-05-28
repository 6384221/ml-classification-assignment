import matplotlib.pyplot as plt

def create_visualization(df):
    '''
    Create simple visualization
    '''
    if 'Finding_Labels' in df.columns:
        label_counts = df['Finding_Labels'].value_counts().head(10)

        plt.figure(figsize=(10, 6))
        label_counts.plot(kind='bar')

        plt.title('Top 10 Finding Labels')
        plt.xlabel('Labels')
        plt.ylabel('Count')

        plt.tight_layout()
        plt.savefig('finding_labels_chart.png')

        print("Visualization saved as 'finding_labels_chart.png'")
    else:
        print("Column 'Finding_Labels' not found in dataset.")