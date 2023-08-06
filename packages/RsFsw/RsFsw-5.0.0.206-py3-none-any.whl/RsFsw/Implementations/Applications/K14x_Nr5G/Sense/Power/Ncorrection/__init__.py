from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ncorrection:
	"""Ncorrection commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ncorrection", core, parent)

	@property
	def calibration(self):
		"""calibration commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_calibration'):
			from .Calibration import Calibration
			self._calibration = Calibration(self._core, self._cmd_group)
		return self._calibration

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:POWer:NCORrection \n
		Snippet: driver.applications.k14Xnr5G.sense.power.ncorrection.set(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:NCORrection {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:NCORrection \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.power.ncorrection.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:NCORrection?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Ncorrection':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ncorrection(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
