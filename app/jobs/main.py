from get_data import save_csv
from database import create_db
from create_dataframes import freq_categorias

def main():
    save_csv()
    create_db(freq_categorias)


if __name__ == "__main__":
    main()
