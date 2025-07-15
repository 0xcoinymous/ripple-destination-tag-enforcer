# simple script to force require destination tag on deposits to your ripple wallet

## steps to setup the project

* install python
sudo apt install python3 

* create virtual environment
python3 -m venv venv

* activate the created virtual environment
source venv/bin/activate

* install the dependencies
pip install -r requirements.txt

* run the main app
python main.py 

## example output

signed_tx =>  AccountSet(account='rssBhrTwf7XxW8UJkN9cpiJWE8WkXRD4HR', transaction_type=<TransactionType.ACCOUNT_SET: 'AccountSet'>, fee='10', sequence=92061477, account_txn_id=None, flags=0, last_ledger_sequence=97467202, memos=None, signers=None, source_tag=None, signing_pub_key='02648e3a695cb059b04f3098e729251e0d6eb9965cf13ee7da89e827afa2f6b9b0', ticket_sequence=None, txn_signature='3044022061C6A43C46062423182F2021258A5398EF18E51DECE8B75D428FFE9E125071BF02203EC3679A9FA3708F7CE1D110A2B39991FAF2079433596126BBB894A193B19B61', network_id=None, clear_flag=None, domain=None, email_hash=None, message_key=None, set_flag=1, transfer_rate=None, tick_size=None, nftoken_minter=None)

tx_response =>  Response(status=<ResponseStatus.SUCCESS: 'success'>, result={'tx_json': {'Account': 'rssBhrTwf7XxW8UJkN9cpiJWE8WkXRD4HR', 'Fee': '10', 'Flags': 0, 'LastLedgerSequence': 97467202, 'Sequence': 92061477, 'SetFlag': 1, 'SigningPubKey': '02648E3A695CB059B04F3098E729251E0D6EB9965CF13EE7DA89E827AFA2F6B9B0', 'TransactionType': 'AccountSet', 'TxnSignature': '3044022061C6A43C46062423182F2021258A5398EF18E51DECE8B75D428FFE9E125071BF02203EC3679A9FA3708F7CE1D110A2B39991FAF2079433596126BBB894A193B19B61', 'date': 805810612, 'ledger_index': 97467184}, 'ctid': 'C5CF3B30005A0000', 'hash': '4C2690FC713567BD1A438B7C1A1F7A1C09371BB5D27F924E5821342EBE93FA5A', 'meta': {'AffectedNodes': [{'ModifiedNode': {'FinalFields': {'Account': 'rssBhrTwf7XxW8UJkN9cpiJWE8WkXRD4HR', 'Balance': '46898281', 'Flags': 131072, 'OwnerCount': 0, 'Sequence': 92061478}, 'LedgerEntryType': 'AccountRoot', 'LedgerIndex': '4A94C0FCD8C6391607E91064C9C09DD6BA4E683860F3E1EF6852FB64122E51A8', 'PreviousFields': {'Balance': '46898291', 'Flags': 0, 'Sequence': 92061477}, 'PreviousTxnID': 'A1EA60D432D923BCCF45FB1DC589096ADCEC5539581E468BF59982FDE0B5BD26', 'PreviousTxnLgrSeq': 97465683}}], 'TransactionIndex': 90, 'TransactionResult': 'tesSUCCESS'}, 'validated': True, 'ledger_index': 97467184, 'ledger_hash': '32015144CFE2F9719593F907AE283F84B3818B0C3EA69310109E1DA8175254E2', 'close_time_iso': '2025-07-14T12:16:52Z'}, id=None, type=<ResponseType.RESPONSE: 'response'>)

