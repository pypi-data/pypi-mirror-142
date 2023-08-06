from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sfunction:
	"""Sfunction commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfunction", core, parent)

	@property
	def lastResult(self):
		"""lastResult commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lastResult'):
			from .LastResult import LastResult
			self._lastResult = LastResult(self._core, self._cmd_group)
		return self._lastResult

	@property
	def results(self):
		"""results commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_results'):
			from .Results import Results
			self._results = Results(self._core, self._cmd_group)
		return self._results

	def set(self, service_function: str) -> None:
		"""SCPI: DIAGnostic:SERVice:SFUNction \n
		Snippet: driver.diagnostic.service.sfunction.set(service_function = '1') \n
		This command starts a service function. The service functions are available after you have entered the level 1 or level 2
		system password. \n
			:param service_function: String containing the ID of the service function. The ID of the service function is made up out of five numbers, separated by a point. • function group number • board number • function number • parameter 1 (see the Service Manual) • parameter 2 (see the Service Manual)
		"""
		param = Conversions.value_to_quoted_str(service_function)
		self._core.io.write(f'DIAGnostic:SERVice:SFUNction {param}')

	def get(self, service_function: str) -> str:
		"""SCPI: DIAGnostic:SERVice:SFUNction \n
		Snippet: value: str = driver.diagnostic.service.sfunction.get(service_function = '1') \n
		This command starts a service function. The service functions are available after you have entered the level 1 or level 2
		system password. \n
			:param service_function: String containing the ID of the service function. The ID of the service function is made up out of five numbers, separated by a point. • function group number • board number • function number • parameter 1 (see the Service Manual) • parameter 2 (see the Service Manual)
			:return: result: No help available"""
		param = Conversions.value_to_quoted_str(service_function)
		response = self._core.io.query_str(f'DIAGnostic:SERVice:SFUNction? {param}')
		return trim_str_response(response)

	def clone(self) -> 'Sfunction':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sfunction(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
