from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Store:
	"""Store commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("store", core, parent)

	def set(self, standard: str) -> None:
		"""SCPI: [SENSe]:ADEMod:PRESet:STORe \n
		Snippet: driver.sense.ademod.preset.store.set(standard = '1') \n
		This command saves the current Analog Modulation Analysis measurement configuration. Standard definitions are stored in
		an xml file.
		The default directory for Analog Modulation Analysis standards is C:/R_S/INSTR/USER/predefined/AdemodPredefined. \n
			:param standard: String containing the file name. You can save the file in a subdirectory of the directory mentioned above. In that case, you have to include the relative path to the file.
		"""
		param = Conversions.value_to_quoted_str(standard)
		self._core.io.write(f'SENSe:ADEMod:PRESet:STORe {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:ADEMod:PRESet:STORe \n
		Snippet: value: str = driver.sense.ademod.preset.store.get() \n
		This command saves the current Analog Modulation Analysis measurement configuration. Standard definitions are stored in
		an xml file.
		The default directory for Analog Modulation Analysis standards is C:/R_S/INSTR/USER/predefined/AdemodPredefined. \n
			:return: standard: String containing the file name. You can save the file in a subdirectory of the directory mentioned above. In that case, you have to include the relative path to the file."""
		response = self._core.io.query_str(f'SENSe:ADEMod:PRESet:STORe?')
		return trim_str_response(response)
