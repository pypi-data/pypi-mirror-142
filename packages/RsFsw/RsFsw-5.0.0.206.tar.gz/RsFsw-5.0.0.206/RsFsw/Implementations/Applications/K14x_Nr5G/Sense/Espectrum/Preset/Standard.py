from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Standard:
	"""Standard commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standard", core, parent)

	def set(self, standard: enums.SelectNone, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:PRESet[:STANdard] \n
		Snippet: driver.applications.k14Xnr5G.sense.espectrum.preset.standard.set(standard = enums.SelectNone.NONE, subBlock = repcap.SubBlock.Default) \n
		This command loads an SEM settings file for combined measurements. \n
			:param standard: (enum or string) string String that contains the path to the settings file (.xml format) . NONE Removes the settings file.
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.enum_ext_scalar_to_str(standard, enums.SelectNone)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:PRESet:STANdard {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default) -> enums.SelectNone:
		"""SCPI: [SENSe]:ESPectrum<sb>:PRESet[:STANdard] \n
		Snippet: value: enums.SelectNone = driver.applications.k14Xnr5G.sense.espectrum.preset.standard.get(subBlock = repcap.SubBlock.Default) \n
		This command loads an SEM settings file for combined measurements. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: standard: (enum or string) string String that contains the path to the settings file (.xml format) . NONE Removes the settings file."""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:PRESet:STANdard?')
		return Conversions.str_to_scalar_enum_ext(response, enums.SelectNone)
