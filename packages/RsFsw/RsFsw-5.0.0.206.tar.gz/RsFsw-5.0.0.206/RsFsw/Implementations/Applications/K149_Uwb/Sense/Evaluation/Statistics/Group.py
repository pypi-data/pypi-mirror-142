from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Group:
	"""Group commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("group", core, parent)

	def set(self, group: int) -> None:
		"""SCPI: [SENSe]:EVALuation:STATistics:GROup \n
		Snippet: driver.applications.k149Uwb.sense.evaluation.statistics.group.set(group = 1) \n
		Sets the statistics group to be analyzed. \n
			:param group: No help available
		"""
		param = Conversions.decimal_value_to_str(group)
		self._core.io.write(f'SENSe:EVALuation:STATistics:GROup {param}')

	def get(self) -> int:
		"""SCPI: [SENSe]:EVALuation:STATistics:GROup \n
		Snippet: value: int = driver.applications.k149Uwb.sense.evaluation.statistics.group.get() \n
		Sets the statistics group to be analyzed. \n
			:return: group: No help available"""
		response = self._core.io.query_str(f'SENSe:EVALuation:STATistics:GROup?')
		return Conversions.str_to_int(response)
