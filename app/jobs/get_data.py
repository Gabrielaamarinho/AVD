import requests

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

if __name__ == "__main__":
    download_file_from_google_drive('1gicuzoA80zCR2DgtXqPY87HcMP4fDxJE', 'app/data/fornecedores.csv')
    download_file_from_google_drive('1KVNl6YiZeRlMelvgQjTXSO1T68vS6OuF', 'app/data/avaliacoes.csv')
    download_file_from_google_drive('19ShHKn88_zBmf2x9lfc4aCn3-bkubhl4', 'app/data/relatorio_recife.csv')
    download_file_from_google_drive('1zXznw_vqngsnf9mvXjUKQi3o0ZUHSmvr', 'app/data/relatorio_norte.csv')
    download_file_from_google_drive('1MmZ2ayBWinT516p6JGc9Xpz3tb99wXn_', 'app/data/relatorio_curitiba.csv')
    download_file_from_google_drive('104XwNDfqcAQsL50xrp-Sqg5FP-e4e7Sl', 'app/data/relatorio_sorocaba.csv')