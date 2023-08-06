from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpd:
	"""Dpd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpd", core, parent)

	def set(self, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:DPD \n
		Snippet: driver.applications.k18AmplifierEt.massMemory.store.dpd.set(filename = '1', store = repcap.Store.Default) \n
		This command generates and stores a waveform containing the DPD in a file you have specified.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- DPD method 'Generate Predistorted Waveform File' has to be selected (method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.Method.set = WFILe)
			- The DPD calculation has been initiated with method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.File.Generate.set. \n
			:param filename: String containing the file name.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = Conversions.value_to_quoted_str(filename)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:DPD {param}')
