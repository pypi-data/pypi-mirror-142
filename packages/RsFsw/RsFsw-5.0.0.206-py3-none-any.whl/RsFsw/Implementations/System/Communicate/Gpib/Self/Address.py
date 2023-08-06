from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("address", core, parent)

	def set(self, address: float) -> None:
		"""SCPI: SYSTem:COMMunicate:GPIB[:SELF]:ADDRess \n
		Snippet: driver.system.communicate.gpib.self.address.set(address = 1.0) \n
		This command sets the GPIB address of the R&S FSW. \n
			:param address: Range: 0 to 30
		"""
		param = Conversions.decimal_value_to_str(address)
		self._core.io.write(f'SYSTem:COMMunicate:GPIB:SELF:ADDRess {param}')

	def get(self) -> float:
		"""SCPI: SYSTem:COMMunicate:GPIB[:SELF]:ADDRess \n
		Snippet: value: float = driver.system.communicate.gpib.self.address.get() \n
		This command sets the GPIB address of the R&S FSW. \n
			:return: address: Range: 0 to 30"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:GPIB:SELF:ADDRess?')
		return Conversions.str_to_float(response)
