from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coefficient:
	"""Coefficient commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coefficient", core, parent)

	def set(self, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:EQUalizer:FILTer:COEFficient \n
		Snippet: driver.applications.k18AmplifierEt.massMemory.store.equalizer.filterPy.coefficient.set(filename = '1', store = repcap.Store.Default) \n
		This command stores the equalizer filter that has been calculated.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Train an equalizer filter (method RsFsw.Applications.K18_AmplifierEt.Configure.Equalizer.Train.set) . \n
			:param filename: String containing the file name and location of the filter (csv file format) .
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = Conversions.value_to_quoted_str(filename)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:EQUalizer:FILTer:COEFficient {param}')
