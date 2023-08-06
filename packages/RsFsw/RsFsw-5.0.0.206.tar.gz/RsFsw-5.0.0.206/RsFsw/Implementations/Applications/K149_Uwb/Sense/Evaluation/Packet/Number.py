from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Number:
	"""Number commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("number", core, parent)

	def set(self, packet: float) -> None:
		"""SCPI: [SENSe]:EVALuation:PACKet:NUMBer \n
		Snippet: driver.applications.k149Uwb.sense.evaluation.packet.number.set(packet = 1.0) \n
		Sets the number of the packet within its class, referring to packets in the current capture buffer. \n
			:param packet: numeric value
		"""
		param = Conversions.decimal_value_to_str(packet)
		self._core.io.write(f'SENSe:EVALuation:PACKet:NUMBer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:EVALuation:PACKet:NUMBer \n
		Snippet: value: float = driver.applications.k149Uwb.sense.evaluation.packet.number.get() \n
		Sets the number of the packet within its class, referring to packets in the current capture buffer. \n
			:return: packet: numeric value"""
		response = self._core.io.query_str(f'SENSe:EVALuation:PACKet:NUMBer?')
		return Conversions.str_to_float(response)
