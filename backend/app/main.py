from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.db import create_db_and_tables
from app.domain.estimation.routes import router as estimations_router
from app.domain.user.routes import router as users_router
from app.domain.auth.routes import router as token_router
from app.domain.charts.routes import router as charts_router
from app.domain.tickers.routes import router as tickers_router
from app.middlewares.elasticsearch_middleware import ElasticsearchLoggingMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    ElasticsearchLoggingMiddleware,
    es_host="http://elasticsearch:9200",
    index_name="fastapi-logs",
)

app.include_router(estimations_router)
app.include_router(users_router)
app.include_router(token_router)
app.include_router(charts_router)
app.include_router(tickers_router)
