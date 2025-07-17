FROM python:3.13

WORKDIR /app
COPY pyproject.toml .

RUN pip install .

COPY app/ .

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENV APP_PORT=8000
ENV INSTANCE_ID="API_X"

ENTRYPOINT ["entrypoint.sh"]
CMD ["fastapi", "run"]
