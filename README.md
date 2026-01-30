# AtmoTrack
# Coleta de Dados Climáticos – Web Scraping e API
Automatiza a coleta de dados climáticos coletados por Web Scraping e API pública, formata e salva em CSV, seguindo a mesma estrutura, facilitando análise e comparação.

## Requisitos
- Python 3.9+
- pip

## Instalação do Python (no Windows):
1. Acesse o site oficial: https://www.python.org/downloads/
2. Clique em Download Python 3.12.x (qualquer 3.9+ serve).
3. Ao abrir o instalador, marque a opção `☑ Add Python to PATH` e finalize a instalação.
4. Após a instalação, você pode verificar a versão do Python no terminal usando os comandos:

   ```
   python --version
   pip --version
   ```

## Dependências
Você precisará usar o seguinte comando para instalar as dependências do projeto:
```
pip install requests beautifulsoup4
```

Obter sua chave no OpenWeatherMap:

1. Crie uma conta: https://openweathermap.org/
2. Vá em API Keys → Gere uma nova chave.
3. Copie para .env como mostrado acima.
4. Altere a constante na classe `main_api`

Para executar os scripts use os seguintes comandos:

## Web Scraping
```
python main_scraping.py
```
## API
```
python main_api.py
```


Ao final da execução, o arquivo `weather_data.csv` deverá ser criado com as informações das cidades de São Paulo, Rio de Janeiro, Belo Horizonte, Curitiba e Porto Alegre.
