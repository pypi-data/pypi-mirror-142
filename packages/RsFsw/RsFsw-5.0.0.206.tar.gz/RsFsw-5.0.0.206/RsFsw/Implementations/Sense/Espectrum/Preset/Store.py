from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Store:
	"""Store commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("store", core, parent)

	def set(self, standard: str, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:PRESet:STORe \n
		Snippet: driver.sense.espectrum.preset.store.set(standard = '1', subBlock = repcap.SubBlock.Default) \n
		This command saves the current SEM measurement configuration. Standard definitions are stored in an xml file. The default
		directory for SEM standards is C:/R_S/INSTR/sem_std. \n
			:param standard: String containing the file name. You can save the file in a subdirectory of the directory mentioned above. In that case, you have to include the relative path to the file.
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.value_to_quoted_str(standard)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:PRESet:STORe {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> str:
		"""SCPI: [SENSe]:ESPectrum<sb>:PRESet:STORe \n
		Snippet: value: str = driver.sense.espectrum.preset.store.get(subBlock = repcap.SubBlock.Default) \n
		This command saves the current SEM measurement configuration. Standard definitions are stored in an xml file. The default
		directory for SEM standards is C:/R_S/INSTR/sem_std. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: standard: String containing the file name. You can save the file in a subdirectory of the directory mentioned above. In that case, you have to include the relative path to the file."""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:PRESet:STORe?')
		return trim_str_response(response)
