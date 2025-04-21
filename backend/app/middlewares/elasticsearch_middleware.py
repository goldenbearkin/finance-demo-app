import json
import time
import uuid
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from elasticsearch import Elasticsearch
from typing import Any, Dict, List, Union, Callable, Awaitable, cast
from starlette.types import ASGIApp
from app.domain.auth.service import get_current_user_from_token

SENSITIVE_KEYS = {"password", "token", "access_token", "secret"}


def mask_sensitive(data: Union[Dict[str, Any], List[Any], Any]) -> Union[Dict[str, Any], List[Any], Any]:
    if isinstance(data, dict):
        return {key: "***" if key.lower() in SENSITIVE_KEYS else mask_sensitive(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [mask_sensitive(item) for item in data]
    else:
        return data


class ElasticsearchLoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, es_host: str, index_name: str):
        super().__init__(app)
        self.es = Elasticsearch(es_host)
        self.index_name = index_name

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        auth_header = request.headers.get("Authorization")
        user = None

        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header[7:]
            user = get_current_user_from_token(token)

        correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
        request.state.correlation_id = correlation_id  # Save in request context

        start_time = time.time()

        try:
            body_bytes = await request.body()
            body_data = json.loads(body_bytes.decode())
        except Exception:
            body_data = {}

        masked_body = mask_sensitive(cast(dict[str, str], body_data))
        masked_query = mask_sensitive(dict(request.query_params))

        response = await call_next(request)  # type: ignore[return-value]

        response.headers["X-Correlation-ID"] = correlation_id

        duration = round((time.time() - start_time) * 1000)

        log_doc_response = {
            "correlation_id": correlation_id,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "sub": user.email if user else None,
            "method": request.method,
            "path": request.url.path,
            "query": masked_query,
            "body": masked_body,
            "status_code": response.status_code,
            "duration_ms": duration,
        }

        self.es.index(index="fastapi-logs", document=log_doc_response)

        return response
