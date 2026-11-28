# Base image: tag for humans/Dependabot, digest for immutability
ARG PYTHON_IMAGE=python:3.12-slim@sha256:191083cdf6c7bda8c76158983163ead5d5cf7b77cf3033e805bb0f5296f51b4b

# ---- Stage 1: build: install runtime dependencies into a venv ----
FROM ${PYTHON_IMAGE} AS build
WORKDIR /app
COPY requirements.txt .
RUN python -m venv /opt/venv \
 && /opt/venv/bin/pip install --no-cache-dir --require-hashes -r requirements.txt

# ---- Stage 2: runtime: only what the app needs to run ----
FROM ${PYTHON_IMAGE} AS runtime

# Apply Debian security patches newer than the base image
RUN apt-get update \
 && apt-get upgrade -y --no-install-recommends \
 && rm -rf /var/lib/apt/lists/*

# Non-root user (numeric UID so Kubernetes can verify runAsNonRoot)
RUN useradd --create-home --uid 10001 appuser

WORKDIR /app
COPY --from=build /opt/venv /opt/venv
COPY app/ ./app/

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

USER 10001
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]