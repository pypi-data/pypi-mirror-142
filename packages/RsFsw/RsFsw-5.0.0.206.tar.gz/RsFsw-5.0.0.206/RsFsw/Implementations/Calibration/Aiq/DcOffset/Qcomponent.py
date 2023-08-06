from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qcomponent:
	"""Qcomponent commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qcomponent", core, parent)

	def set(self, offset: float) -> None:
		"""SCPI: CALibration:AIQ:DCOFfset:Q \n
		Snippet: driver.calibration.aiq.dcOffset.qcomponent.set(offset = 1.0) \n
		This command defines a DC offset of the Q input from the Analog Baseband interface (R&S FSW-B71) . \n
			:param offset: numeric value DC offset Unit: V
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CALibration:AIQ:DCOFfset:Q {param}')

	def get(self) -> float:
		"""SCPI: CALibration:AIQ:DCOFfset:Q \n
		Snippet: value: float = driver.calibration.aiq.dcOffset.qcomponent.get() \n
		This command defines a DC offset of the Q input from the Analog Baseband interface (R&S FSW-B71) . \n
			:return: offset: numeric value DC offset Unit: V"""
		response = self._core.io.query_str(f'CALibration:AIQ:DCOFfset:Q?')
		return Conversions.str_to_float(response)
