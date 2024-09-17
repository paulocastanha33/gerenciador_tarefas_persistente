# Gerenciador de Tarefas Persistente

Este é um aplicativo de terminal para gerenciar tarefas, desenvolvido em Python. Ele permite que os usuários adicionem, visualizem, concluam e removam tarefas, e as tarefas são salvas em um banco de dados SQLite3. O programa pode ser compilado em um executável para distribuição.

## Funcionalidades

- Adicionar tarefas
- Listar tarefas
- Marcar tarefas como concluídas
- Remover tarefas
- Salvar tarefas em um banco de dados SQLite
- Exportar como executável

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/paulocastanha33/gerenciador_de_tarefas_persistente.git
    cd gerenciador-de-tarefas
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    .\venv\Scripts\activate    # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Como usar

1. Para iniciar o programa, execute:
    ```bash
    python main.py
    ```

2. Siga as instruções no terminal para gerenciar suas tarefas.

## Compilar para executável

Se você deseja compilar o programa para um executável (ex.: para Windows), use o `PyInstaller`:

```bash
pip install pyinstaller
pyinstaller --onefile main.py

O executável será gerado na pasta dist/.

Tecnologias utilizadas
Python
SQLite3
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
