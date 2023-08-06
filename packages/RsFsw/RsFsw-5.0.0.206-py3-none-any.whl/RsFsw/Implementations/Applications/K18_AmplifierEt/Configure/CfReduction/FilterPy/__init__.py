from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	def set(self, filter_mode: enums.Complexity) -> None:
		"""SCPI: CONFigure:CFReduction:FILTer \n
		Snippet: driver.applications.k18AmplifierEt.configure.cfReduction.filterPy.set(filter_mode = enums.Complexity.ENHanced) \n
		Selects simple or enhanced filter mode for crest factor reduction. \n
			:param filter_mode: SIMPle | ENHanced
		"""
		param = Conversions.enum_scalar_to_str(filter_mode, enums.Complexity)
		self._core.io.write(f'CONFigure:CFReduction:FILTer {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Complexity:
		"""SCPI: CONFigure:CFReduction:FILTer \n
		Snippet: value: enums.Complexity = driver.applications.k18AmplifierEt.configure.cfReduction.filterPy.get() \n
		Selects simple or enhanced filter mode for crest factor reduction. \n
			:return: filter_mode: SIMPle | ENHanced"""
		response = self._core.io.query_str(f'CONFigure:CFReduction:FILTer?')
		return Conversions.str_to_scalar_enum(response, enums.Complexity)

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
