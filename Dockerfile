# ---- Stage 1: build: install dependencies into a venv ----
FROM python:3.12-slim:sha256:191083cdf6c7bda8c76158983163ead5d5cf7b77cf3033e805bb0f5296f51b4b AS build
WORKDIR /app
COPY requirements.txt .
RUN python -m venv /opt/venv \
 && /opt/venv/bin/pip install --no-cache-dir --require-hashes -r requirements.txt

# ---- Stage 2: runtime: only what the app needs to run ----
FROM python:3.12-slim:sha256:191083cdf6c7bda8c76158983163ead5d5cf7b77cf3033e805bb0f5296f51b4b AS runtime
RUN useradd --create-home --uid 10001 appuser
WORKDIR /app
COPY --from=build /opt/venv /opt/venv
COPY app/ ./app/
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
USER appuser
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]