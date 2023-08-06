from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Title:
	"""Title commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("title", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, arg_0: str) -> None:
		"""SCPI: HCOPy:TREPort:TITLe \n
		Snippet: driver.hardCopy.treport.title.set(arg_0 = '1') \n
		This command defines the title for the test report as shown on its title page. \n
			:param arg_0: String containing the title.
		"""
		param = Conversions.value_to_quoted_str(arg_0)
		self._core.io.write(f'HCOPy:TREPort:TITLe {param}')

	def get(self) -> str:
		"""SCPI: HCOPy:TREPort:TITLe \n
		Snippet: value: str = driver.hardCopy.treport.title.get() \n
		This command defines the title for the test report as shown on its title page. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'HCOPy:TREPort:TITLe?')
		return trim_str_response(response)

	def clone(self) -> 'Title':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Title(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
