from fastapi import APIRouter

router = APIRouter(
    prefix="/api/threats",
    tags=["Threat Intelligence"],
)


@router.get("")
def get_threats() -> dict:
    return {
        "items": [],
        "total": 0,
    }


@router.get("/blacklist")
def get_blacklist() -> dict:
    return {
        "items": [],
        "total": 0,
    }


@router.get("/whitelist")
def get_whitelist() -> dict:
    return {
        "items": [],
        "total": 0,
    }