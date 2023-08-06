from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mpower:
	"""Mpower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mpower", core, parent)

	def set(self, power: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:MPOWer \n
		Snippet: driver.sense.espectrum.msr.mpower.set(power = 1.0, subBlock = repcap.SubBlock.Default) \n
		Defines the maximum output power of the base station. This setting is only available for base stations with a medium
		range base station class (see [SENSe:]ESPectrum<sb>:MSR:CLASs) . \n
			:param power: Range: 0 dBm to 100 dBm, Unit: dBm
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.decimal_value_to_str(power)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:MPOWer {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:MPOWer \n
		Snippet: value: float = driver.sense.espectrum.msr.mpower.get(subBlock = repcap.SubBlock.Default) \n
		Defines the maximum output power of the base station. This setting is only available for base stations with a medium
		range base station class (see [SENSe:]ESPectrum<sb>:MSR:CLASs) . \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: power: Range: 0 dBm to 100 dBm, Unit: dBm"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:MPOWer?')
		return Conversions.str_to_float(response)
