from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, off_level: float, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure:WLAN:ANTMatrix:RLEVel<ant>:OFFSet \n
		Snippet: driver.applications.k91Wlan.configure.wlan.antMatrix.refLevel.offset.set(off_level = 1.0, antenna = repcap.Antenna.Default) \n
		This remote control command determines whether the reference value offset for the specified antenna if the primary and
		secondary devices in a simultaneous MIMO setup are not coupled (seemethod RsFsw.Applications.K91_Wlan.Configure.Wlan.
		AntMatrix.Source.RefLevel.Offset.set ) . \n
			:param off_level: level offset in dB Unit: DB
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RefLevel')
		"""
		param = Conversions.decimal_value_to_str(off_level)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:WLAN:ANTMatrix:RLEVel{antenna_cmd_val}:OFFSet {param}')

	def get(self, antenna=repcap.Antenna.Default) -> float:
		"""SCPI: CONFigure:WLAN:ANTMatrix:RLEVel<ant>:OFFSet \n
		Snippet: value: float = driver.applications.k91Wlan.configure.wlan.antMatrix.refLevel.offset.get(antenna = repcap.Antenna.Default) \n
		This remote control command determines whether the reference value offset for the specified antenna if the primary and
		secondary devices in a simultaneous MIMO setup are not coupled (seemethod RsFsw.Applications.K91_Wlan.Configure.Wlan.
		AntMatrix.Source.RefLevel.Offset.set ) . \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RefLevel')
			:return: off_level: level offset in dB Unit: DB"""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'CONFigure:WLAN:ANTMatrix:RLEVel{antenna_cmd_val}:OFFSet?')
		return Conversions.str_to_float(response)
