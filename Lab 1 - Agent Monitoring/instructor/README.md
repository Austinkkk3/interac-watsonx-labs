# Interac e-Transfer Assistant Tool API

A FastAPI application that backs the e-Transfer Support Agent. It checks Interac e-Transfer sending limits, calculates fees, and estimates delivery time by account tier.

> All limits and fees are **illustrative sample values** for a workshop demo. They do not represent real Interac or financial-institution limits.

## Endpoints

- `GET /` — API information.
- `GET /tiers` — all account tiers with their limits and fees.
- `POST /etransfer_tool` — main endpoint: checks a transfer against account-tier limits, calculates the fee, and estimates delivery time.

### Account tiers (sample)

| Account tier | Per transaction | Daily | Weekly | Monthly | Send fee |
|---|---|---|---|---|---|
| personal basic | $3,000 | $3,000 | $10,000 | $20,000 | $0.00 |
| personal premium | $5,000 | $10,000 | $20,000 | $40,000 | $0.00 |
| small business | $25,000 | $50,000 | $100,000 | $250,000 | $1.50 |

### `POST /etransfer_tool`

**Request body:**
```json
{
  "transfer_type": "send money",
  "amount": 2500,
  "account_tier": "personal basic",
  "recipient_has_autodeposit": true
}
```

**Parameters:**
- `transfer_type` (string, required): `"send money"`, `"request money"`, or `"autodeposit"`
- `amount` (number, required): transfer amount in CAD (> 0)
- `account_tier` (string, required): `"personal basic"`, `"personal premium"`, or `"small business"`
- `recipient_has_autodeposit` (boolean, optional): whether the recipient has Autodeposit enabled (default `false`)

**Response:** whether the transfer is within the per-transaction limit, the tier's limits, the fee, an estimated delivery description, and a status/message.

## Installation

### Option 1: Local

```bash
pip install -r requirements.txt
python main.py
# or: uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API is available at `http://localhost:8000`. Interactive docs: `http://localhost:8000/docs`.

### Option 2: Docker

```bash
docker build -t interac-etransfer-tool .
docker run -d -p 8000:8000 --name etransfer-tool interac-etransfer-tool
docker logs etransfer-tool
```

### Option 2b: Docker Compose

```bash
docker-compose up -d
docker-compose logs -f
docker-compose down
```

## Usage examples

```bash
# List tiers
curl http://localhost:8000/tiers

# Check a transfer
curl -X POST http://localhost:8000/etransfer_tool \
  -H "Content-Type: application/json" \
  -d '{"transfer_type":"send money","amount":2500,"account_tier":"personal basic","recipient_has_autodeposit":true}'
```

## Uploading to watsonx Orchestrate

The OpenAPI spec `etransfer_tool.json` is uploaded to watsonx Orchestrate as a tool.

1. **Make the API reachable.** watsonx Orchestrate must be able to reach the running service. If running locally, expose it with a tunnel (e.g. ngrok) or deploy it to a public host.
2. **Set the server URL.** Open `etransfer_tool.json` and set `servers[0].url` to your public base URL (e.g. `"https://your-ngrok-url.ngrok.io"` or your cloud URL). It currently reads `https://REPLACE-WITH-YOUR-TOOL-URL`.
3. **Import.** In watsonx Orchestrate, add a tool → Import → OpenAPI → upload `etransfer_tool.json`. Select the **Etransfer Tool** operation (`POST /etransfer_tool`) and add it to the agent.

## Files

- `main.py` — FastAPI application
- `etransfer_tool.json` — OpenAPI spec for the tool
- `requirements.txt` — Python dependencies
- `Dockerfile`, `docker-compose.yml` — container setup

## License

Demonstration API for educational purposes.
