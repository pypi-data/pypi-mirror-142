from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stream:
	"""Stream commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stream", core, parent)

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	def set(self, channel: str) -> None:
		"""SCPI: MMEMory:LOAD:IQ:STReam \n
		Snippet: driver.applications.k70Vsa.massMemory.load.iq.stream.set(channel = '1') \n
		Only available for files that contain more than one data stream from multiple channels: selects the data stream to be
		used as input for the currently selected channel. Automatic mode (method RsFsw.MassMemory.Load.Iq.Stream.Auto.set) is set
		to OFF. \n
			:param channel: String containing the channel name.
		"""
		param = Conversions.value_to_quoted_str(channel)
		self._core.io.write(f'MMEMory:LOAD:IQ:STReam {param}')

	def get(self) -> str:
		"""SCPI: MMEMory:LOAD:IQ:STReam \n
		Snippet: value: str = driver.applications.k70Vsa.massMemory.load.iq.stream.get() \n
		Only available for files that contain more than one data stream from multiple channels: selects the data stream to be
		used as input for the currently selected channel. Automatic mode (method RsFsw.MassMemory.Load.Iq.Stream.Auto.set) is set
		to OFF. \n
			:return: channel: String containing the channel name."""
		response = self._core.io.query_str(f'MMEMory:LOAD:IQ:STReam?')
		return trim_str_response(response)

	def clone(self) -> 'Stream':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Stream(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
