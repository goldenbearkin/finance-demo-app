from fastapi import APIRouter, Depends
from app.domain.estimation.service import EstimationService
from app.domain.estimation.models import EstimationType
from app.domain.auth.service import get_current_user
from typing import Annotated
from app.domain.estimation.schemas import PrivateEstimatesWrite, PublicEstimatesRead, PrivateEstimatesRead
from app.domain.common.schemas import TableData
from app.domain.user.schemas import UserRead

router = APIRouter(prefix="/estimates", tags=["estimates"])


@router.get("/public", response_model=TableData[PublicEstimatesRead], response_model_exclude_none=True)
async def get_public_estimation(
    symbol: str,
    estimation_type: EstimationType,
    estimation_service: Annotated[EstimationService, Depends()],
):
    # Remark: Protentially can do this in parallel
    # earnings, revenue = await asyncio.gather(
    #     asyncio.to_thread(yf_service.get_earnings_estimates, ticker),
    #     asyncio.to_thread(yf_service.get_revenue_estimates, ticker),
    # )
    match estimation_type:
        case EstimationType.EARNINGS:
            return estimation_service.get_earnings_estimates(symbol)
        case EstimationType.REVENUE:
            return estimation_service.get_revenue_estimates(symbol)


@router.get("/private", response_model=TableData[PrivateEstimatesRead], response_model_exclude_none=True)
async def get_private_estimations(
    symbol: str,
    estimation_type: EstimationType,
    estimation_service: Annotated[EstimationService, Depends()],
    user: Annotated[UserRead, Depends(get_current_user)],
):
    return estimation_service.get_private_estimations(user.email, symbol, estimation_type)


@router.post("/private", status_code=201)
async def save_user_estimation(
    estimation: PrivateEstimatesWrite,
    estimation_service: Annotated[EstimationService, Depends()],
    user: Annotated[UserRead, Depends(get_current_user)],
):
    estimation_service.save_private_estimation(user.email, estimation)
