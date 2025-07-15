## Ripple Destination Tag Enforcer

A simple Python script to enforce the requirement of a destination tag (memo) for deposits to your Ripple (XRP) wallet.
Useful for exchanges and custodial wallets to prevent user error and lost funds.

### Setup Instructions

1. **Install Python (if not already installed):**

   ```bash
   sudo apt install python3
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Add your SafePal XRP private key:**
Open the xrp_req_tag.py file and set your SafePal private key in the SafePalPrivateKey field:

   ```bash
   SafePalPrivateKey = "your_xrp_private_key_here"
   ```

6. **Run the script:**

   ```bash
   python main.py
   ```

### Example Output
```python
signed_tx => AccountSet(
    account='rssBhrTwf7XxW8UJkN9cpiJWE8WkXRD4HR',
    transaction_type=<TransactionType.ACCOUNT_SET: 'AccountSet'>,
    fee='10',
    sequence=92061477,
    ...
    set_flag=1,
    ...
)

tx_response => Response(
    status=<ResponseStatus.SUCCESS: 'success'>,
    result={
        'tx_json': {
            'Account': 'rssBhrTwf7XxW8UJkN9cpiJWE8WkXRD4HR',
            'TransactionType': 'AccountSet',
            'SetFlag': 1,
            ...
        },
        'validated': True,
        'ledger_index': 97467184,
        ...
    }
)
```
