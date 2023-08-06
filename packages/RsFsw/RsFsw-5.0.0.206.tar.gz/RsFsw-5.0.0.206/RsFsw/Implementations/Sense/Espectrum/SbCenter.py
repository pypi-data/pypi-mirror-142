from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SbCenter:
	"""SbCenter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sbCenter", core, parent)

	def set(self, frequency: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:SBCenter \n
		Snippet: driver.sense.espectrum.sbCenter.set(frequency = 1.0, subBlock = repcap.SubBlock.Default) \n
		This command defines the number of sub blocks in the SEM measurement. Note that this command is maintained for
		compatibility reasons only. For newer remote control programs use the [SENSe:]ESPectrum<sb>:SCOunt command. \n
			:param frequency: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:SBCenter {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:SBCenter \n
		Snippet: value: float = driver.sense.espectrum.sbCenter.get(subBlock = repcap.SubBlock.Default) \n
		This command defines the number of sub blocks in the SEM measurement. Note that this command is maintained for
		compatibility reasons only. For newer remote control programs use the [SENSe:]ESPectrum<sb>:SCOunt command. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: frequency: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:SBCenter?')
		return Conversions.str_to_float(response)
