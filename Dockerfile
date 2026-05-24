FROM ghcr.io/astral-sh/uv:python3.13-alpine

LABEL org.opencontainers.image.source="https://github.com/cssnr/inaturalist-mcp"
LABEL org.opencontainers.image.description="iNaturalist MCP"
LABEL org.opencontainers.image.authors="cssnr"

ENV TZ=UTC

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Ensure installed tools can be executed out of the box
ENV UV_TOOL_BIN_DIR=/usr/local/bin

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
        uv sync --locked --no-install-project

COPY src/ .

RUN addgroup -S app && adduser -S app -G app && chown -R app:app /app

ARG VERSION="Dockerfile"
#ENV APP_VERSION="${VERSION}"
LABEL org.opencontainers.image.version="${VERSION}"

USER app

CMD ["uvicorn", "inaturalist_mcp.server:app", "--host", "0.0.0.0"]
