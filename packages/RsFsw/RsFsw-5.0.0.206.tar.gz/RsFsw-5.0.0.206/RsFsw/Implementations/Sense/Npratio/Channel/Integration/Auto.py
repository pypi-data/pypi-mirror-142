from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:NPRatio:CHANnel:INTegration:AUTO \n
		Snippet: driver.sense.npratio.channel.integration.auto.set(state = False) \n
		Determines which bandwidth is used for total power density calculation. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The integration bandwidth and its position is defined manually using [SENSe:]NPRatio:CHANnel:INTegration:BWIDth and [SENSe:]NPRatio:CHANnel:INTegration:FREQuency:OFFSet. The entire specified bandwidth is used, including any defined notches. ON | 1 The integration bandwidth is defined automatically as the channel bandwidth, without the notches, centered around the center frequency (see [SENSe:]NPRatio:CHANnel:BWIDth) .
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:NPRatio:CHANnel:INTegration:AUTO {param}')
