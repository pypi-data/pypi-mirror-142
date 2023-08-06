from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rpower:
	"""Rpower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rpower", core, parent)

	def set(self, mode: enums.PvtRefPower) -> None:
		"""SCPI: CONFigure:BURSt:PVT:RPOWer \n
		Snippet: driver.applications.k91Wlan.configure.burst.pvt.rpower.set(mode = enums.PvtRefPower.MAXimum) \n
		This remote control command configures the use of either mean or maximum PPDU power as a reference power for the 802.11b,
		g (DSSS) PVT measurement. \n
			:param mode: MEAN | MAXimum
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PvtRefPower)
		self._core.io.write(f'CONFigure:BURSt:PVT:RPOWer {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PvtRefPower:
		"""SCPI: CONFigure:BURSt:PVT:RPOWer \n
		Snippet: value: enums.PvtRefPower = driver.applications.k91Wlan.configure.burst.pvt.rpower.get() \n
		This remote control command configures the use of either mean or maximum PPDU power as a reference power for the 802.11b,
		g (DSSS) PVT measurement. \n
			:return: mode: MEAN | MAXimum"""
		response = self._core.io.query_str(f'CONFigure:BURSt:PVT:RPOWer?')
		return Conversions.str_to_scalar_enum(response, enums.PvtRefPower)
