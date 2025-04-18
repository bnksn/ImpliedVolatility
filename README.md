# Python Packages

```bash
pip install flask flask_cors yfinance scipy
```

# Launching the Back End server

1.  Open a new terminal or command prompt.
2.  Navigate to the directory containing your `main.py` file.
3.  Run the back end server with the Python interpreter:

    ```bash
    python3 main.py
    ```

# Launching the Front End server

1.  Navigate to the downloaded `ui` directory:
    ```bash
    cd ImpliedVolatility/ui
    ```
2.  ```bash
    npm install
    ```
3.  ```bash
    npm run build
    ```
4.  Navigate to the `dist` directory:
    ```bash
    cd dist
    ```
4.  Start a Python HTTP server on port 8000:

    ```bash
    python3 -m http.server 8000
    ```
5.  Open your browser and go to the following URL:

    ```
    http://localhost:8000
