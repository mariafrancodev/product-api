# Run instructions

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv\Scripts\activate     # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the server (development):

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Open interactive docs: http://localhost:8000/docs

5. Run tests:

```bash
pytest -q
```

## 🐳 Run with Docker

### 1. Build Docker image
```bash
docker build -t product-api .

### 2. Run the container
```bash
docker run -p 8000:8000 product-api