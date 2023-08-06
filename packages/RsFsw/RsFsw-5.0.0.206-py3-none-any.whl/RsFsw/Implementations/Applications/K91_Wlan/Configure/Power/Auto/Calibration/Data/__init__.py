from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_path'):
			from .Path import Path
			self._path = Path(self._core, self._cmd_group)
		return self._path

	def set(self, data: str) -> None:
		"""SCPI: CONFigure:POWer:AUTO:CALibration:DATA \n
		Snippet: driver.applications.k91Wlan.configure.power.auto.calibration.data.set(data = '1') \n
		No command help available \n
			:param data: No help available
		"""
		param = Conversions.value_to_quoted_str(data)
		self._core.io.write(f'CONFigure:POWer:AUTO:CALibration:DATA {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:POWer:AUTO:CALibration:DATA \n
		Snippet: value: str = driver.applications.k91Wlan.configure.power.auto.calibration.data.get() \n
		No command help available \n
			:return: data: No help available"""
		response = self._core.io.query_str(f'CONFigure:POWer:AUTO:CALibration:DATA?')
		return trim_str_response(response)

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
