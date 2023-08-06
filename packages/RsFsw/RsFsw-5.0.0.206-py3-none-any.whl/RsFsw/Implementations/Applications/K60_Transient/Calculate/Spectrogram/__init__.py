from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spectrogram:
	"""Spectrogram commands group definition. 9 total commands, 4 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrogram", core, parent)

	@property
	def frame(self):
		"""frame commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import Frame
			self._frame = Frame(self._core, self._cmd_group)
		return self._frame

	@property
	def hdepth(self):
		"""hdepth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hdepth'):
			from .Hdepth import Hdepth
			self._hdepth = Hdepth(self._core, self._cmd_group)
		return self._hdepth

	@property
	def tstamp(self):
		"""tstamp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tstamp'):
			from .Tstamp import Tstamp
			self._tstamp = Tstamp(self._core, self._cmd_group)
		return self._tstamp

	@property
	def tresolution(self):
		"""tresolution commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tresolution'):
			from .Tresolution import Tresolution
			self._tresolution = Tresolution(self._core, self._cmd_group)
		return self._tresolution

	def clear(self, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:SPECtrogram:CLEar \n
		Snippet: driver.applications.k60Transient.calculate.spectrogram.clear(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:SPECtrogram:CLEar')

	def clear_with_opc(self, window=repcap.Window.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		"""SCPI: CALCulate<n>:SPECtrogram:CLEar \n
		Snippet: driver.applications.k60Transient.calculate.spectrogram.clear_with_opc(window = repcap.Window.Default) \n
		No command help available \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:SPECtrogram:CLEar', opc_timeout_ms)

	def clear_all(self, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:SPECtrogram:CLEar:ALL \n
		Snippet: driver.applications.k60Transient.calculate.spectrogram.clear_all(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:SPECtrogram:CLEar:ALL')

	def clear_all_with_opc(self, window=repcap.Window.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		"""SCPI: CALCulate<n>:SPECtrogram:CLEar:ALL \n
		Snippet: driver.applications.k60Transient.calculate.spectrogram.clear_all_with_opc(window = repcap.Window.Default) \n
		No command help available \n
		Same as clear_all, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:SPECtrogram:CLEar:ALL', opc_timeout_ms)

	def clone(self) -> 'Spectrogram':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Spectrogram(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
