from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Buffer:
	"""Buffer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("buffer", core, parent)

	def set(self, signal_path: enums.SignalPath) -> None:
		"""SCPI: CONFigure:WLAN:MIMO:CAPTure:BUFFer \n
		Snippet: driver.applications.k91Wlan.configure.wlan.mimo.capture.buffer.set(signal_path = enums.SignalPath.RX1) \n
		Specifies the signal path to be captured in MIMO sequential manual measurements and immediately starts capturing data. \n
			:param signal_path: RX1 | RX2 | RX3 | RX4 | RX5 | RX6 | RX7 | RX8 For details see 'Manual Sequential MIMO Data Capture'.
		"""
		param = Conversions.enum_scalar_to_str(signal_path, enums.SignalPath)
		self._core.io.write(f'CONFigure:WLAN:MIMO:CAPTure:BUFFer {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SignalPath:
		"""SCPI: CONFigure:WLAN:MIMO:CAPTure:BUFFer \n
		Snippet: value: enums.SignalPath = driver.applications.k91Wlan.configure.wlan.mimo.capture.buffer.get() \n
		Specifies the signal path to be captured in MIMO sequential manual measurements and immediately starts capturing data. \n
			:return: signal_path: RX1 | RX2 | RX3 | RX4 | RX5 | RX6 | RX7 | RX8 For details see 'Manual Sequential MIMO Data Capture'."""
		response = self._core.io.query_str(f'CONFigure:WLAN:MIMO:CAPTure:BUFFer?')
		return Conversions.str_to_scalar_enum(response, enums.SignalPath)
