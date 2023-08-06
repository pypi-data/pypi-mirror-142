from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	@property
	def next(self):
		"""next commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_next'):
			from .Next import Next
			self._next = Next(self._core, self._cmd_group)
		return self._next

	def set(self, filename: str) -> None:
		"""SCPI: MMEMory:STORe:STATe \n
		Snippet: driver.massMemory.store.state.set(filename = '1') \n
		This command saves the current instrument configuration in a *.dfl file. Secure User Mode In secure user mode, settings
		that are stored on the instrument are stored to volatile memory, which is restricted to 256 MB. Thus, a 'memory limit
		reached' error can occur although the hard disk indicates that storage space is still available.
		To store data permanently, select an external storage location such as a USB memory device. For details, see 'Protecting
		data using the secure user mode'. \n
			:param filename: String containing the path and name of the target file. The file extension is .dfl.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write_with_opc(f'MMEMory:STORe:STATe 1, {param}')

	def clone(self) -> 'State':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = State(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
