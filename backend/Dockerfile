FROM python:3.14-slim

#uv install
COPY --from=ghcr.io/astral-sh/uv:0.11.31 /uv /uvx /bin/

WORKDIR /video-streaming-backend

COPY pyproject.toml uv.lock .

RUN uv sync --frozen

COPY . .

EXPOSE 8080

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
