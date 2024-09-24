# README

Teste para saber como funciona o netCDF4 e Twisted.

## Como executar?

- `make up`
- `make start-server`
- `make start-client`

## Funcionamento

- Quando um client se conecta ao server, o server envia dados climáticos aleatórios em json a cada 5 segundo.
- O client recebe os dados e:
  - Armazena em um arquivo usando netCDF4 e NumPy
  - Busca todos os dados do arquivo
  - Cria gráfico de temperatura, umidade e pressão no Matplotlib

## Enunciado

Enunciado gerado pelo chatgpt para testar de forma simples as ferramentas.

- Coleta de Dados via Twisted:

  - Use o Twisted para criar um servidor simples que simula o envio de dados climáticos (temperatura, umidade, pressão) a cada 5 segundos de forma assíncrona.
  - O servidor pode gerar dados aleatórios (ex: temperatura entre 20°C e 30°C, umidade entre 40% e 70%, pressão entre 1000 hPa e 1050 hPa) e enviá-los para o cliente via TCP.

- Processamento com NumPy:

  - O cliente, ao receber os dados, deve usar NumPy para armazenar e processar as informações recebidas. Por exemplo, calcular a média, variância ou aplicar alguma transformação (como normalização) nos dados coletados.

- Armazenamento com netCDF4:

  - Após processar uma quantidade de dados (por exemplo, 100 medições), o programa deve armazenar os dados em um arquivo netCDF4, organizando-os em variáveis de tempo, temperatura, umidade e pressão.

- Visualização com Matplotlib:
  - Ao fim do processo, o programa deve gerar gráficos com Matplotlib para visualizar as informações armazenadas no arquivo netCDF4. O gráfico pode incluir a variação da temperatura, umidade e pressão ao longo do tempo.
