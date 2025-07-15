from hdwallet import HDWallet
from hdwallet.const import PUBLIC_KEY_TYPES
from hdwallet.cryptocurrencies import Ripple as Cryptocurrency
from hdwallet.hds import BIP32HD
from xrpl.account import get_balance, does_account_exist
from xrpl.clients import JsonRpcClient
from xrpl.models.transactions import Payment
from xrpl.transaction import autofill_and_sign
from xrpl.transaction import submit_and_wait
from xrpl.utils import xrp_to_drops
from xrpl.wallet import Wallet
from xrpl.models.transactions import (
    AccountSet,
    AccountSetAsfFlag,
)

XRP_PRIVATE_KEY = "SafePalPrivateKey"

class XRP:
    def __init__(self):
        self.rpc_url = "https://s2.ripple.com:51234/"

        hdwallet: HDWallet = HDWallet(
            cryptocurrency=Cryptocurrency,
            hd=BIP32HD,
            network=Cryptocurrency.NETWORKS.MAINNET,
            public_key_type=PUBLIC_KEY_TYPES.COMPRESSED
        ).from_private_key(private_key=XRP_PRIVATE_KEY)
        self.private_key = XRP_PRIVATE_KEY
        self.public_key = hdwallet.public_key()


    def send_require_destination_tag(self):
        wallet = Wallet(self.public_key, XRP_PRIVATE_KEY)
        print()
        tx = AccountSet(
            account=wallet.address,
            set_flag=AccountSetAsfFlag.ASF_REQUIRE_DEST,
        )

        client = JsonRpcClient(self.rpc_url)
        signed_tx = None

        try:
            signed_tx = autofill_and_sign(tx, client, wallet)
            print("signed_tx => ", signed_tx)
        except Exception as e:
            print(f"error in transaction sign ---> {e}")
            raise e

        try:
            tx_response = submit_and_wait(signed_tx, client)
            print("tx_response => ", tx_response)
            return tx_response.to_dict()["result"]["hash"]
        except Exception as e:
            print(f"Error transaction broadcast ---> {e}")
            raise e

