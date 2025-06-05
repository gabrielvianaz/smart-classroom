# Smart Classroom Monorepo

Este repositório contém a aplicação Smart Classroom, organizada em um monorepo com dois diretórios principais:

- `back`: Backend em Python (Flask)
- `front`: Frontend em JavaScript (Vite/React)

---

## Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js 16+ e npm](https://nodejs.org/)

---

## Executando o Backend (`back`)

1. **Acesse o diretório do backend:**
   ```bash
   cd back
   ```
   

2. **(Opcional, mas recomendado) Crie e ative um ambiente virtual:**

    `No Windows`:
    ```bash
    python -m venv venv
    venv\Scripts\activate
   ```
   
    `No Linux/Mac`:
    ```bash
    python -m venv venv
    source venv/bin/activate
   ```

3. **Instale as dependências:**

    ```bash
    python -m pip install -r requirements.txt
    ```

4. **Inicie o servidor Flask:**
    ```bash
   python main.py
   ```
   
O backend estará acessível em `http://localhost:5000`

___

## Executando o Frontend (`front`)

1. **Acesse o diretório do frontend:**
    ```bash
    cd front
    ```

2. **Instale as dependências:**
    ```bash
    npm install
   ```

3. **Inicie o servidor de desenvolvimento:**
   ```bash
   npm run dev
   ```

O frontend estará acessível em `http://localhost:5173`
