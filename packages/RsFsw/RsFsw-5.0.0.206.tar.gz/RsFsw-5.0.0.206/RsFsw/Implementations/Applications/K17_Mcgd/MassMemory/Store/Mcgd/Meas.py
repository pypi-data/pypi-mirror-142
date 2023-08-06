from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Meas:
	"""Meas commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("meas", core, parent)

	def set(self, file: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:MCGD:MEAS \n
		Snippet: driver.applications.k17Mcgd.massMemory.store.mcgd.meas.set(file = '1', store = repcap.Store.Default) \n
		This command stores the current measurement results (all active traces in all windows, including calibration traces) to
		the selected file. \n
			:param file: path and file name of the .csv file that contains the measured data
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = Conversions.value_to_quoted_str(file)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:MCGD:MEAS {param}')
