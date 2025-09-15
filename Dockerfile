# Uses Python 3.13 slim image
FROM python:3.13-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="/opt/poetry/bin:/app/.venv/bin:$PATH"

# System dependencies (keep minimal)
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry (official installer)
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set working directory
WORKDIR /app

# Copy only dependency manifests first for better build caching
COPY pyproject.toml poetry.lock* poetry.toml* /app/

# Install project dependencies (only main group; no dev)
RUN poetry install --only main --no-interaction --no-ansi

# Copy project files
COPY . /app

# Copy entrypoint script
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose app port
EXPOSE 8000

# Default environment variables for superuser (override in runtime)
# DJANGO_SUPERUSER_USERNAME=
# DJANGO_SUPERUSER_EMAIL=
# DJANGO_SUPERUSER_PASSWORD=
# DJANGO_SETTINGS_MODULE=your_project.settings

# Run the entrypoint (migrations, superuser, server)
ENTRYPOINT ["/entrypoint.sh"]