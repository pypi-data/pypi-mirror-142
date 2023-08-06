from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionTable:
	"""CorrectionTable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correctionTable", core, parent)

	def set(self, file: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:MCGD:CTABle \n
		Snippet: driver.applications.k17Mcgd.massMemory.store.mcgd.correctionTable.set(file = '1', store = repcap.Store.Default) \n
		Stores the carrier table to a .csv file.
			INTRO_CMD_HELP: The .csv file has the following structure: \n
			- Column 1: Carrier position index
			- Column 2: Carrier frequency
			- Column 3: Carrier state (0|1|on|off)
			- Column 4: Carrier Threshold (in dBm)  \n
			:param file: 1..n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = Conversions.value_to_quoted_str(file)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:MCGD:CTABle {param}')
