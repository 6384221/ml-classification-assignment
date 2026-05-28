from data_loader import load_data
from preprocess import preprocess_data
from database import save_to_database
from visualization import create_visualization

def main():
    file_path = 'sample_labels.csv'

    print("Loading dataset...")
    df = load_data(file_path)

    print("Preprocessing dataset...")
    df_clean = preprocess_data(df)

    print("Saving data into SQLite database...")
    save_to_database(df_clean)

    print("Generating visualization...")
    create_visualization(df_clean)

    print("Project completed successfully!")

if __name__ == "__main__":
    main()