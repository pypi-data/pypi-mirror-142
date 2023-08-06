from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Harmonics:
	"""Harmonics commands group definition. 6 total commands, 5 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("harmonics", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def bandwidth(self):
		"""bandwidth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def nharmonics(self):
		"""nharmonics commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nharmonics'):
			from .Nharmonics import Nharmonics
			self._nharmonics = Nharmonics(self._core, self._cmd_group)
		return self._nharmonics

	@property
	def distortion(self):
		"""distortion commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_distortion'):
			from .Distortion import Distortion
			self._distortion = Distortion(self._core, self._cmd_group)
		return self._distortion

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	def preset(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:HARMonics:PRESet \n
		Snippet: driver.calculate.marker.function.harmonics.preset(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command initiates a measurement to determine the ideal configuration for the harmonic distortion measurement.
		The method depends on the span.
			INTRO_CMD_HELP: Note the following prerequisites for the selected transducer: \n
			- Frequency domain (span > 0) Frequency and level of the first harmonic are determined and used for the measurement list.
			- Time domain (span = 0) The level of the first harmonic is determined. The frequency remains unchanged. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:HARMonics:PRESet')

	def preset_with_opc(self, window=repcap.Window.Default, marker=repcap.Marker.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:HARMonics:PRESet \n
		Snippet: driver.calculate.marker.function.harmonics.preset_with_opc(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command initiates a measurement to determine the ideal configuration for the harmonic distortion measurement.
		The method depends on the span.
			INTRO_CMD_HELP: Note the following prerequisites for the selected transducer: \n
			- Frequency domain (span > 0) Frequency and level of the first harmonic are determined and used for the measurement list.
			- Time domain (span = 0) The level of the first harmonic is determined. The frequency remains unchanged. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:HARMonics:PRESet', opc_timeout_ms)

	def clone(self) -> 'Harmonics':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Harmonics(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
