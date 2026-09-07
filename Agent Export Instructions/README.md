## Before You Begin

- Install Python 3.11 or newer (3.13 recommended).
- Ensure `pip` is available.
- (Optional) Create and activate a virtual environment with `python -m venv .venv && source .venv/bin/activate`.

## Install the ADK

```bash
pip install ibm-watsonx-orchestrate
orchestrate --version
# Get help for any command:
# orchestrate --help
```

## Connect to Your Orchestrate Environment

You need your IBM Cloud API key and your watsonx Orchestrate instance URL.

1. **Create and download an API key**
   - IBM Cloud console: https://cloud.ibm.com/resources  
   - Ensure you are in the bootcamp-provided account.
   - Navigate: Manage → Access (IAM) → API keys → Create. Save the key.
2. **Copy the Orchestrate instance URL**
   - IBM Cloud console: https://cloud.ibm.com/resources  
   - Under Resources → AI / Machine Learning → your Watson Orchestrate instance → Launch watsonx Orchestrate.
   - Profile (top right) → Settings → API details → copy Instance URL.
3. **Add and activate the environment (replace placeholders):**

```bash
orchestrate env add -n agentic-bootcamp -u ORCHESTRATE_INSTANCE_URL
orchestrate env activate agentic-bootcamp --api-key API_KEY
orchestrate env list   # verify it is active
```

## Command to list agents
```bash
orchestrate agents list -v
```

## Command to export agents
```bash
orchestrate agents export -n <agent-name> -k <agent-type> -o <output-path>.zip
```

### Example of an export command:
```bash
orchestrate agents export -k native -n HR_Agent_6161by -o hr_agent.zip
```

Here agent-name (-n) is HR_Agent_6161b, and agent kind (-k) is native and output path (-o) is the hr_agent.zip folder in the current dierctory

More information on export commands and each parameter can be found [here](https://developer.watson-orchestrate.ibm.com/agents/manage_agent#exporting-agents)
