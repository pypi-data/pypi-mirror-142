from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, guard_time: enums.GuardTime) -> None:
		"""SCPI: CONFigure:WLAN:GTIMe:SELect \n
		Snippet: driver.applications.k91Wlan.configure.wlan.gtime.select.set(guard_time = enums.GuardTime.NORMal) \n
		This remote control command specifies the guard time the PPDUs in the IEEE 802.11n or ac input signal should have. If the
		guard time is specified to be detected from the input signal using the method RsFsw.Applications.K91_Wlan.Configure.Wlan.
		Gtime.Auto.set command then this command is query only and allows the detected guard time to be obtained. \n
			:param guard_time: SHORt | NORMal SHORt Only the PPDUs with short guard interval are analyzed. NORMal Only the PPDUs with long guard interval are analyzed. ('Long' in manual operation)
		"""
		param = Conversions.enum_scalar_to_str(guard_time, enums.GuardTime)
		self._core.io.write(f'CONFigure:WLAN:GTIMe:SELect {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GuardTime:
		"""SCPI: CONFigure:WLAN:GTIMe:SELect \n
		Snippet: value: enums.GuardTime = driver.applications.k91Wlan.configure.wlan.gtime.select.get() \n
		This remote control command specifies the guard time the PPDUs in the IEEE 802.11n or ac input signal should have. If the
		guard time is specified to be detected from the input signal using the method RsFsw.Applications.K91_Wlan.Configure.Wlan.
		Gtime.Auto.set command then this command is query only and allows the detected guard time to be obtained. \n
			:return: guard_time: SHORt | NORMal SHORt Only the PPDUs with short guard interval are analyzed. NORMal Only the PPDUs with long guard interval are analyzed. ('Long' in manual operation)"""
		response = self._core.io.query_str(f'CONFigure:WLAN:GTIMe:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.GuardTime)
