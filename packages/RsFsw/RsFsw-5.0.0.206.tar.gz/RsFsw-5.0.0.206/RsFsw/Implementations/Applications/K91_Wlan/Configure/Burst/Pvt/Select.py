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

	def set(self, mode: enums.PvTmode) -> None:
		"""SCPI: CONFigure:BURSt:PVT:SELect \n
		Snippet: driver.applications.k91Wlan.configure.burst.pvt.select.set(mode = enums.PvTmode.EDGE) \n
		This remote command determines how to interpret the Power vs Time measurement results. \n
			:param mode: EDGE | FULL | RISE | FALL EDGE Displays rising and falling edges only FALL Displays falling edge only FULL Displays the full PPDU RISE Displays the rising edge only
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PvTmode)
		self._core.io.write(f'CONFigure:BURSt:PVT:SELect {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PvTmode:
		"""SCPI: CONFigure:BURSt:PVT:SELect \n
		Snippet: value: enums.PvTmode = driver.applications.k91Wlan.configure.burst.pvt.select.get() \n
		This remote command determines how to interpret the Power vs Time measurement results. \n
			:return: mode: EDGE | FULL | RISE | FALL EDGE Displays rising and falling edges only FALL Displays falling edge only FULL Displays the full PPDU RISE Displays the rising edge only"""
		response = self._core.io.query_str(f'CONFigure:BURSt:PVT:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.PvTmode)
