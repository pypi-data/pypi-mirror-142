from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 22 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	@property
	def range(self):
		"""range commands group. 13 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import Range
			self._range = Range(self._core, self._cmd_group)
		return self._range

	def save(self, filename: str) -> None:
		"""SCPI: [SENSe]:LIST:SAVE \n
		Snippet: driver.applications.k50Spurious.sense.listPy.save(filename = '1') \n
		Saves the current range setup to a user-defined comma-separated (.csv) file for later use. The values are stored in the
		following order for each range: <No>,<Start>,<Stop>,<TNRStart>,<TNRStop>,<LimitOffset>,<PeakExcursion>,<SNR>,<AutoRBW>,
		<RBW>,<MaxFinalRBW>,<Detector>,<DetLength>,<Reserved>,<RefLevel>,<RFAttenuation>,<Preamp> \n
			:param filename: String containing the path and name of the file.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:LIST:SAVE {param}')

	def load(self, filename: str) -> None:
		"""SCPI: [SENSe]:LIST:LOAD \n
		Snippet: driver.applications.k50Spurious.sense.listPy.load(filename = '1') \n
		Loads a stored range setup from a .csv file. The current settings in the table are overwritten by the settings in the
		file! \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:LIST:LOAD {param}')

	def clear(self) -> None:
		"""SCPI: [SENSe]:LIST:CLEar \n
		Snippet: driver.applications.k50Spurious.sense.listPy.clear() \n
		Removes all but the first range from the wide search settings table. \n
		"""
		self._core.io.write(f'SENSe:LIST:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:LIST:CLEar \n
		Snippet: driver.applications.k50Spurious.sense.listPy.clear_with_opc() \n
		Removes all but the first range from the wide search settings table. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:LIST:CLEar', opc_timeout_ms)

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
