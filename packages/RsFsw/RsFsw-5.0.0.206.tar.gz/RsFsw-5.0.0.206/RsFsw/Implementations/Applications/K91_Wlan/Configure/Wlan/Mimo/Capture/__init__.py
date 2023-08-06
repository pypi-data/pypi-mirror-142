from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Capture:
	"""Capture commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("capture", core, parent)

	@property
	def buffer(self):
		"""buffer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_buffer'):
			from .Buffer import Buffer
			self._buffer = Buffer(self._core, self._cmd_group)
		return self._buffer

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	def set(self, signal_path: enums.SignalPath) -> None:
		"""SCPI: CONFigure:WLAN:MIMO:CAPTure \n
		Snippet: driver.applications.k91Wlan.configure.wlan.mimo.capture.set(signal_path = enums.SignalPath.RX1) \n
		Specifies the signal path to be captured in MIMO sequential manual measurements. Subsequently, use the method RsFsw.
		Applications.K10x_Lte.Initiate.Immediate.set command to start capturing data. \n
			:param signal_path: RX1 | RX2 | RX3 | RX4 | RX5 | RX6 | RX7 | RX8 For details see 'Manual Sequential MIMO Data Capture'.
		"""
		param = Conversions.enum_scalar_to_str(signal_path, enums.SignalPath)
		self._core.io.write(f'CONFigure:WLAN:MIMO:CAPTure {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SignalPath:
		"""SCPI: CONFigure:WLAN:MIMO:CAPTure \n
		Snippet: value: enums.SignalPath = driver.applications.k91Wlan.configure.wlan.mimo.capture.get() \n
		Specifies the signal path to be captured in MIMO sequential manual measurements. Subsequently, use the method RsFsw.
		Applications.K10x_Lte.Initiate.Immediate.set command to start capturing data. \n
			:return: signal_path: RX1 | RX2 | RX3 | RX4 | RX5 | RX6 | RX7 | RX8 For details see 'Manual Sequential MIMO Data Capture'."""
		response = self._core.io.query_str(f'CONFigure:WLAN:MIMO:CAPTure?')
		return Conversions.str_to_scalar_enum(response, enums.SignalPath)

	def clone(self) -> 'Capture':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Capture(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
