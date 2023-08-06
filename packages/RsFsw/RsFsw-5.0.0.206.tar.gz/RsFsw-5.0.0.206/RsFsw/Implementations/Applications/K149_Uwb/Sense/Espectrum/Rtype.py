from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rtype:
	"""Rtype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rtype", core, parent)

	def set(self, mode: enums.EspectrumRtype, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RTYPe \n
		Snippet: driver.applications.k149Uwb.sense.espectrum.rtype.set(mode = enums.EspectrumRtype.CPOWer, subBlock = repcap.SubBlock.Default) \n
		No command help available \n
			:param mode: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EspectrumRtype)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default) -> enums.EspectrumRtype:
		"""SCPI: [SENSe]:ESPectrum<sb>:RTYPe \n
		Snippet: value: enums.EspectrumRtype = driver.applications.k149Uwb.sense.espectrum.rtype.get(subBlock = repcap.SubBlock.Default) \n
		No command help available \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: mode: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.EspectrumRtype)
