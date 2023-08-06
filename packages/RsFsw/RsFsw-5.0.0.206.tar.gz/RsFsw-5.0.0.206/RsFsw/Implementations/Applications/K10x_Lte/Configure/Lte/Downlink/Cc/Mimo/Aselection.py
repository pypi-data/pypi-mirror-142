from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aselection:
	"""Aselection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aselection", core, parent)

	def set(self, antenna: enums.AntennaC, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:MIMO:ASELection \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.mimo.aselection.set(antenna = enums.AntennaC.ALL, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the antenna for measurements with MIMO setups. For time alignment error measurements, the command
		selects the reference antenna. \n
			:param antenna: ANT1 | ANT2 | ANT3 | ANT4 Select a single antenna to be analyzed ALL Select all antennas to be analyzed AUT1 | AUT2 | AUT4 Automatically selects the antenna(s) to be analyzed. AUT1 tests a single antenna, AUT2 tests two antennas, AUT4 tests four antennas. Available if the number of input channels is taken 'From Antenna Selection'. AUTO Automatically selects the antenna(s) to be analyzed.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(antenna, enums.AntennaC)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:MIMO:ASELection {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.AntennaC:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:MIMO:ASELection \n
		Snippet: value: enums.AntennaC = driver.applications.k10Xlte.configure.lte.downlink.cc.mimo.aselection.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the antenna for measurements with MIMO setups. For time alignment error measurements, the command
		selects the reference antenna. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: antenna: ANT1 | ANT2 | ANT3 | ANT4 Select a single antenna to be analyzed ALL Select all antennas to be analyzed AUT1 | AUT2 | AUT4 Automatically selects the antenna(s) to be analyzed. AUT1 tests a single antenna, AUT2 tests two antennas, AUT4 tests four antennas. Available if the number of input channels is taken 'From Antenna Selection'. AUTO Automatically selects the antenna(s) to be analyzed."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:MIMO:ASELection?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaC)
