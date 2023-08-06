from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rterminator:
	"""Rterminator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rterminator", core, parent)

	def set(self, terminator: enums.GpibTerminator) -> None:
		"""SCPI: SYSTem:COMMunicate:GPIB[:SELF]:RTERminator \n
		Snippet: driver.system.communicate.gpib.self.rterminator.set(terminator = enums.GpibTerminator.EOI) \n
		This command selects the GPIB receive terminator. Output of binary data from the instrument to the control computer does
		not require such a terminator change. \n
			:param terminator: LFEOI | EOI LFEOI According to the standard, the terminator in ASCII is LF and/or EOI. EOI For binary data transfers (e.g. trace data) from the control computer to the instrument, the binary code used for LF might be included in the binary data block, and therefore should not be interpreted as a terminator in this particular case. This can be avoided by using only the receive terminator EOI.
		"""
		param = Conversions.enum_scalar_to_str(terminator, enums.GpibTerminator)
		self._core.io.write(f'SYSTem:COMMunicate:GPIB:SELF:RTERminator {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GpibTerminator:
		"""SCPI: SYSTem:COMMunicate:GPIB[:SELF]:RTERminator \n
		Snippet: value: enums.GpibTerminator = driver.system.communicate.gpib.self.rterminator.get() \n
		This command selects the GPIB receive terminator. Output of binary data from the instrument to the control computer does
		not require such a terminator change. \n
			:return: terminator: LFEOI | EOI LFEOI According to the standard, the terminator in ASCII is LF and/or EOI. EOI For binary data transfers (e.g. trace data) from the control computer to the instrument, the binary code used for LF might be included in the binary data block, and therefore should not be interpreted as a terminator in this particular case. This can be avoided by using only the receive terminator EOI."""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:GPIB:SELF:RTERminator?')
		return Conversions.str_to_scalar_enum(response, enums.GpibTerminator)
