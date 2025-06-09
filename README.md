# App de Reserva de Hotel

Este projeto é um aplicativo de reserva de hotel desenvolvido em Python, utilizando Streamlit e SQLite. Ele segue a arquitetura Model-View-Controller (MVC), separando a lógica da aplicação em componentes distintos para melhor organização e manutenção.

## Estrutura do Projeto

```
AppReservaHotel
├── controller
│   ├── main.py
│   └── reserva_controller.py
├── models
│   ├── hospede.py
│   ├── quarto.py
│   ├── reserva.py
│   └── database.py
├── services
│   └── reserva_service.py
├── view
│   ├── app.py
│   ├── telaInicio.py
│   ├── telaUsuario.py
│   ├── telaQuarto.py
│   ├── telaReserva.py
│   ├── telaEditarReserva.py
│   ├── telaHistoricoReserva.py
│   └── ... (demais telas)
├── app.py
├── hotel.db
├── requirements.txt
└── README.md
```

## Funcionalidades

- Cadastro e gerenciamento de hóspedes.
- Cadastro e gerenciamento de quartos.
- Criação, edição, cancelamento e histórico de reservas.
- Interface amigável desenvolvida com Streamlit.

## Como Executar

1. **Clone o repositório:**
   ```
   git clone <url-do-repositorio>
   cd AppReservaHotel
   ```

2. **Instale as dependências:**
   ```
   pip install -r requirements.txt
   ```

3. **Execute a aplicação:**
   ```
   streamlit run app.py
   ```

## Como Usar

- Abra o aplicativo no navegador.
- Utilize a interface para cadastrar hóspedes, quartos e reservas.
- Todos os dados são armazenados no banco SQLite `hotel.db`.

## Dependências

- Streamlit
- SQLite3
- Outras bibliotecas listadas em `requirements.txt`.

## Autores 

Luciano Franzoi Filho 
Leonardo de Lima Póss
Raffael Guideti Miello
Filipe Pimenta de Souza


