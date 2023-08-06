from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def set(self, maximum: float) -> None:
		"""SCPI: [SENSe]:DETect:BURSt:LENGth:MAXimum \n
		Snippet: driver.applications.k149Uwb.sense.detect.burst.length.maximum.set(maximum = 1.0) \n
		Defines the maximum burst length. \n
			:param maximum: numeric value
		"""
		param = Conversions.decimal_value_to_str(maximum)
		self._core.io.write(f'SENSe:DETect:BURSt:LENGth:MAXimum {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DETect:BURSt:LENGth:MAXimum \n
		Snippet: value: float = driver.applications.k149Uwb.sense.detect.burst.length.maximum.get() \n
		Defines the maximum burst length. \n
			:return: maximum: numeric value"""
		response = self._core.io.query_str(f'SENSe:DETect:BURSt:LENGth:MAXimum?')
		return Conversions.str_to_float(response)
