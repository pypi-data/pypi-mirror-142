from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rtype:
	"""Rtype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rtype", core, parent)

	def set(self, type_py: enums.EspectrumRtype, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RTYPe \n
		Snippet: driver.sense.espectrum.rtype.set(type_py = enums.EspectrumRtype.CPOWer, subBlock = repcap.SubBlock.Default) \n
		This command defines the type of the power reference. \n
			:param type_py: PEAK | CPOWer PEAK Measures the highest peak within the reference range. CPOWer Measures the channel power within the reference range (integral bandwidth method) .
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.EspectrumRtype)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default) -> enums.EspectrumRtype:
		"""SCPI: [SENSe]:ESPectrum<sb>:RTYPe \n
		Snippet: value: enums.EspectrumRtype = driver.sense.espectrum.rtype.get(subBlock = repcap.SubBlock.Default) \n
		This command defines the type of the power reference. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: type_py: PEAK | CPOWer PEAK Measures the highest peak within the reference range. CPOWer Measures the channel power within the reference range (integral bandwidth method) ."""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.EspectrumRtype)
