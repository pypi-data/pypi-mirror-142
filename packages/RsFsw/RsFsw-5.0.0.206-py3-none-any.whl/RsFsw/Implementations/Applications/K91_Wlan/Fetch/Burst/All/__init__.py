from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	@property
	def formatted(self):
		"""formatted commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatted'):
			from .Formatted import Formatted
			self._formatted = Formatted(self._core, self._cmd_group)
		return self._formatted

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:ALL \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.all.get() \n
		Note that this command is maintained for compatibility reasons only. Use the method RsFsw.Applications.K91_Wlan.Fetch.
		Burst.All.Formatted.get_ command for new remote control programs. This command returns all results from the default WLAN
		measurement (Modulation Accuracy, Flatness and Tolerance) . The results are output as a list of result strings separated
		by commas in ASCII format. The results are output in the following order: \n
			:return: result: list preamble power, payload power, min rms power, average rms power, max rms power, peak power, min crest factor,average crest factor,max crest factor, min frequency error,average frequency error, max frequency error, min symbol error, average symbol error, max symbol error, min IQ offset, average IQ offset, maximum IQ offset, min gain imbalance, average gain imbalance, max gain imbalance, min quadrature offset, average quadrature offset, max quadrature offset, min EVM all bursts, average EVM all bursts, max EVM all bursts, min EVM data carriers, average EVM data carriers , max EVM data carriers min EVM pilots, average EVM pilots , max EVM pilots min IQ skew, average IQ skew, max IQ skew"""
		response = self._core.io.query_str(f'FETCh:BURSt:ALL?')
		return trim_str_response(response)

	def clone(self) -> 'All':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = All(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
