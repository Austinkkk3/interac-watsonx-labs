from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Interac e-Transfer Assistant Tool API",
    description="Helper tool for an Interac e-Transfer support agent: checks sending "
                "limits, calculates fees, and estimates delivery time by account tier.",
    version="1.0.0",
)

# ---------------------------------------------------------------------------
# NOTE: All limits and fees below are ILLUSTRATIVE, FICTIONAL sample values for
# a workshop demo. They do not represent real Interac or financial-institution
# limits, which vary by member institution.
# ---------------------------------------------------------------------------
ACCOUNT_TIERS = {
    "personal basic": {
        "per_transaction_limit": 3000,
        "daily_limit": 3000,
        "weekly_limit": 10000,
        "monthly_limit": 20000,
        "send_fee": 0.00,
        "description": "Standard personal chequing account with everyday e-Transfer access.",
    },
    "personal premium": {
        "per_transaction_limit": 5000,
        "daily_limit": 10000,
        "weekly_limit": 20000,
        "monthly_limit": 40000,
        "send_fee": 0.00,
        "description": "Premium personal account with higher e-Transfer limits.",
    },
    "small business": {
        "per_transaction_limit": 25000,
        "daily_limit": 50000,
        "weekly_limit": 100000,
        "monthly_limit": 250000,
        "send_fee": 1.50,
        "description": "Small business account supporting Interac e-Transfer for Business.",
    },
}

TRANSFER_TYPES = ["send money", "request money", "autodeposit"]


class ETransferRequest(BaseModel):
    transfer_type: str          # "send money", "request money", "autodeposit"
    amount: float               # amount in CAD
    account_tier: str           # "personal basic", "personal premium", "small business"
    recipient_has_autodeposit: Optional[bool] = False


class ETransferResponse(BaseModel):
    transfer_type: str
    amount: float
    account_tier: str
    within_limit: bool
    per_transaction_limit: float
    daily_limit: float
    weekly_limit: float
    monthly_limit: float
    fee: float
    estimated_delivery: str
    status: str
    message: Optional[str] = None


def estimate_delivery(transfer_type: str, recipient_has_autodeposit: bool) -> str:
    """Return an estimated delivery / completion description."""
    if transfer_type == "request money":
        return "The request is sent immediately; funds arrive once the recipient approves it."
    if recipient_has_autodeposit:
        return "Within seconds – funds are deposited automatically via Autodeposit (no security question)."
    return ("Typically within 30 minutes once the recipient accepts the transfer and "
            "answers the security question.")


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Interac e-Transfer Assistant Tool API",
        "version": "1.0.0",
        "endpoints": {"etransfer_tool": "/etransfer_tool", "tiers": "/tiers"},
    }


@app.get("/tiers")
async def get_tiers():
    """Get all available account tiers and their e-Transfer limits/fees."""
    return {"available_tiers": list(ACCOUNT_TIERS.keys()), "tier_details": ACCOUNT_TIERS}


@app.post("/etransfer_tool", response_model=ETransferResponse)
async def etransfer_tool(request: ETransferRequest):
    """
    Check an Interac e-Transfer against account-tier limits, calculate the fee,
    and estimate delivery time.

    Parameters:
    - transfer_type: "send money", "request money", or "autodeposit"
    - amount: transfer amount in CAD
    - account_tier: "personal basic", "personal premium", or "small business"
    - recipient_has_autodeposit: whether the recipient has Autodeposit enabled
    """
    # Validate transfer type
    if request.transfer_type.lower() not in TRANSFER_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid transfer_type. Options: {', '.join(TRANSFER_TYPES)}",
        )

    # Validate account tier
    tier_key = request.account_tier.lower()
    if tier_key not in ACCOUNT_TIERS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid account_tier. Options: {', '.join(ACCOUNT_TIERS.keys())}",
        )

    # Validate amount
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0 CAD.")

    tier = ACCOUNT_TIERS[tier_key]
    within_limit = request.amount <= tier["per_transaction_limit"]

    # Fee applies to sending; requesting money is free
    fee = 0.00 if request.transfer_type.lower() == "request money" else tier["send_fee"]

    if within_limit:
        status = "success"
        message = f"Transfer is within the {tier_key} per-transaction limit."
    else:
        status = "exceeds_limit"
        message = (
            f"Amount ${request.amount:,.2f} CAD exceeds the {tier_key} per-transaction "
            f"limit of ${tier['per_transaction_limit']:,.2f} CAD."
        )

    return ETransferResponse(
        transfer_type=request.transfer_type.lower(),
        amount=request.amount,
        account_tier=tier_key,
        within_limit=within_limit,
        per_transaction_limit=tier["per_transaction_limit"],
        daily_limit=tier["daily_limit"],
        weekly_limit=tier["weekly_limit"],
        monthly_limit=tier["monthly_limit"],
        fee=round(fee, 2),
        estimated_delivery=estimate_delivery(
            request.transfer_type.lower(), bool(request.recipient_has_autodeposit)
        ),
        status=status,
        message=message,
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
