from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Loffset:
	"""Loffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loffset", core, parent)

	def set(self, peak_exc: float) -> None:
		"""SCPI: [SENSe]:DIRected:LOFFset \n
		Snippet: driver.applications.k50Spurious.sense.directed.loffset.set(peak_exc = 1.0) \n
		Defines a limit line as an offset to the detection threshold for each range. \n
			:param peak_exc: Range: 0 to 200, Unit: DB
		"""
		param = Conversions.decimal_value_to_str(peak_exc)
		self._core.io.write(f'SENSe:DIRected:LOFFset {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DIRected:LOFFset \n
		Snippet: value: float = driver.applications.k50Spurious.sense.directed.loffset.get() \n
		Defines a limit line as an offset to the detection threshold for each range. \n
			:return: peak_exc: Range: 0 to 200, Unit: DB"""
		response = self._core.io.query_str(f'SENSe:DIRected:LOFFset?')
		return Conversions.str_to_float(response)
