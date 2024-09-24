# README

Teste para saber como funciona o netCDF4 e Twisted.

## Execute

- `make start-server`
- `make start-client`

## Funcionamento

- Quando um client se conecta ao server, o server envia dados climáticos aleatórios em json a cada 5 segundo.
- O client recebe os dados e:
  - Armazena em um arquivo usando netCDF4 e NumPy
  - Busca todos os dados do arquivo
  - Cria gráfico de temperatura, umidade e pressão no Matplotlib
