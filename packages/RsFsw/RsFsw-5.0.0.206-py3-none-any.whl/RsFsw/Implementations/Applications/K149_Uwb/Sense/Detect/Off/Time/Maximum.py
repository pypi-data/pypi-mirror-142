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
		"""SCPI: [SENSe]:DETect:OFF:TIME:MAXimum \n
		Snippet: driver.applications.k149Uwb.sense.detect.off.time.maximum.set(maximum = 1.0) \n
		Defines the maximum allowed off time within a burst. \n
			:param maximum: numeric value
		"""
		param = Conversions.decimal_value_to_str(maximum)
		self._core.io.write(f'SENSe:DETect:OFF:TIME:MAXimum {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DETect:OFF:TIME:MAXimum \n
		Snippet: value: float = driver.applications.k149Uwb.sense.detect.off.time.maximum.get() \n
		Defines the maximum allowed off time within a burst. \n
			:return: maximum: numeric value"""
		response = self._core.io.query_str(f'SENSe:DETect:OFF:TIME:MAXimum?')
		return Conversions.str_to_float(response)
