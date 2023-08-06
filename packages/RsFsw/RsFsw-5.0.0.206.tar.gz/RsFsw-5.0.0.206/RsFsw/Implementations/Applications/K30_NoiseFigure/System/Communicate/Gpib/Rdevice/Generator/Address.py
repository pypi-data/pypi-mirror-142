from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("address", core, parent)

	def set(self, number: int) -> None:
		"""SCPI: SYSTem:COMMunicate:GPIB:RDEVice:GENerator:ADDRess \n
		Snippet: driver.applications.k30NoiseFigure.system.communicate.gpib.rdevice.generator.address.set(number = 1) \n
		Changes the IEC/IEEE-bus address of the external generator. This command is only valid if External Generator Control (R&S
		FSW-B10) is installed. \n
			:param number: Range: 0 to 30
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'SYSTem:COMMunicate:GPIB:RDEVice:GENerator:ADDRess {param}')

	def get(self) -> int:
		"""SCPI: SYSTem:COMMunicate:GPIB:RDEVice:GENerator:ADDRess \n
		Snippet: value: int = driver.applications.k30NoiseFigure.system.communicate.gpib.rdevice.generator.address.get() \n
		Changes the IEC/IEEE-bus address of the external generator. This command is only valid if External Generator Control (R&S
		FSW-B10) is installed. \n
			:return: number: Range: 0 to 30"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:GPIB:RDEVice:GENerator:ADDRess?')
		return Conversions.str_to_int(response)
