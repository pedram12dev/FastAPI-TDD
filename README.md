# FastAPI TDD Project

This project demonstrates Test-Driven Development (TDD) with FastAPI.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Environment Setup](#environment-setup)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fastAPI-TDD.git
    ```
2. Change to the project directory:
    ```bash
    cd fastAPI-TDD
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```
2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Environment Setup

1. Create a `.env` file in the project root with the following content:
    ```env
    POSTGRES_USER=yourusername
    POSTGRES_PASSWORD=yourpassword
    ```
      

