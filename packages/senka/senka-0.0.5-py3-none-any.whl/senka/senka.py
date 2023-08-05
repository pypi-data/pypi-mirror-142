from typing import List, Tuple
from senka.unknown_transaction import UnknownTransaction
from senkalib.senka_lib import SenkaLib
from senkalib.senka_setting import SenkaSetting
from senkalib.caaj_journal import CaajJournal
from senka.plugin_manager import PluginManager
import pandas as pd

pd.set_option("display.max_columns", 50)

class Senka:
  def __init__(self, setting_dict, setting_toml_path:str):
    self.setting = SenkaSetting(setting_dict)
    self.setting_toml_path = setting_toml_path
    pass
 
  def get_caaj_csv(self, chain:str, address:str) -> str:
    caaj_list, unknown_transactions_list = self.get_caaj(chain, address)
    caaj_dict_list = SenkaLib.get_caaj_jounal_dicts(caaj_list)
    df = pd.DataFrame(caaj_dict_list)
    df = df.sort_values('time')
    caaj_csv = df.to_csv(None, index=False)
    return caaj_csv

  def get_caaj(self, chain:str, address:str) -> Tuple[List[CaajJournal], List[UnknownTransaction]]:
    token_original_ids = SenkaLib.get_token_original_ids()
    available_chains = self.get_available_chains()
    if chain.lower() not in available_chains:
      raise ValueError('this chain is not supported.')

    caaj = []
    unknown_transactions = []
    transaction_generator = list(filter(lambda x:x.chain.lower() == chain.lower(),SenkaLib.get_available_chain()))[0]
    transactions = transaction_generator.get_transactions(self.setting, address)
    plugins = PluginManager.get_plugins(chain, self.setting_toml_path)

    for transaction in transactions:
      for plugin in plugins:
        if plugin.can_handle(transaction):
          caaj_peace = plugin.get_caajs(address, transaction, token_original_ids)
          caaj.extend(caaj_peace)
          break
      else:
        unknown_transactions.append(UnknownTransaction(chain, address, 
          transaction.transaction_id, 'there is no applicable plugin'))

    return caaj, unknown_transactions



  def get_available_chains(self) -> List[str]:
    chains = SenkaLib.get_available_chain()
    chains = list(map(lambda x:x.chain,chains))
    return chains
