from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pinterval:
	"""Pinterval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pinterval", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: CONFigure:SETTings:NR5G:PINTerval \n
		Snippet: driver.applications.k14Xnr5G.configure.settings.nr5G.pinterval.set(time = 1.0) \n
		This command defines the polling interval for periodic synchronization between analyzer and generator.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) .
			- Periodic synchronization is on (method RsFsw.Applications.K14x_Nr5G.Configure.Settings.Nr5G.Sync.set) . \n
			:param time: Unit: s
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'CONFigure:SETTings:NR5G:PINTerval {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:SETTings:NR5G:PINTerval \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.settings.nr5G.pinterval.get() \n
		This command defines the polling interval for periodic synchronization between analyzer and generator.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) .
			- Periodic synchronization is on (method RsFsw.Applications.K14x_Nr5G.Configure.Settings.Nr5G.Sync.set) . \n
			:return: time: Unit: s"""
		response = self._core.io.query_str(f'CONFigure:SETTings:NR5G:PINTerval?')
		return Conversions.str_to_float(response)
