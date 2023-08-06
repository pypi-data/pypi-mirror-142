from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, auto: enums.EventOnce) -> None:
		"""SCPI: CONFigure:POWer:AUTO \n
		Snippet: driver.applications.k9X11Ad.configure.power.auto.set(auto = enums.EventOnce.ONCE) \n
		This command is used to switch on or off automatic power level detection. Note that this command is maintained for
		compatibility reasons only. Use [SENSe:]ADJust:LEVel for new remote control programs. \n
			:param auto: ON Automatic power level detection is performed at the start of each measurement sweep, and the reference level is adapted accordingly. OFF The reference level must be defined manually (see method RsFsw.Applications.K60_Transient.Display.Window.Trace.Y.Scale.RefLevel.set) ONCE Automatic power level detection is performed once at the start of the next measurement sweep, and the reference level is adapted accordingly.
		"""
		param = Conversions.enum_scalar_to_str(auto, enums.EventOnce)
		self._core.io.write(f'CONFigure:POWer:AUTO {param}')
