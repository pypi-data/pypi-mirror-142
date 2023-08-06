from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenter:
	"""Scenter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scenter", core, parent)

	def set(self, frequency: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:SCENter \n
		Snippet: driver.sense.espectrum.scenter.set(frequency = 1.0, subBlock = repcap.SubBlock.Default) \n
		This command defines the center frequency of the selected sub block in a Multi-SEM measurement. \n
			:param frequency: Frequency within the currently defined global span (see [SENSe:]FREQuency:SPAN and [SENSe:]FREQuency:CENTer) . Range: 1 to 3, Unit: Hz
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:SCENter {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:SCENter \n
		Snippet: value: float = driver.sense.espectrum.scenter.get(subBlock = repcap.SubBlock.Default) \n
		This command defines the center frequency of the selected sub block in a Multi-SEM measurement. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: frequency: Frequency within the currently defined global span (see [SENSe:]FREQuency:SPAN and [SENSe:]FREQuency:CENTer) . Range: 1 to 3, Unit: Hz"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:SCENter?')
		return Conversions.str_to_float(response)
