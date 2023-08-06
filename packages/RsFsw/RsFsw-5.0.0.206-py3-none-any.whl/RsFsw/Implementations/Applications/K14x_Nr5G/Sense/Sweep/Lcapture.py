from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lcapture:
	"""Lcapture commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lcapture", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:SWEep:LCAPture \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.lcapture.set(state = False) \n
		This command turns the long capture on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Number of component carriers must be '1' (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.NoCc.set) .
			- Turn off segmented capture ([SENSe:]SWEep:SCAPture:STATe) .
			- Multi frame configuration is not supported. Every frame must have the same configuration.
			INTRO_CMD_HELP: Effects of this command \n
			- Frame count functions become unavailable: [SENSe:]NR5G:FRAMe:COUNt [SENSe:]NR5G:FRAMe:COUNt:AUTO
			- [SENSe:]NR5G:FRAMe:COUNt:STATe \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SWEep:LCAPture {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWEep:LCAPture \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.sweep.lcapture.get() \n
		This command turns the long capture on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Number of component carriers must be '1' (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.NoCc.set) .
			- Turn off segmented capture ([SENSe:]SWEep:SCAPture:STATe) .
			- Multi frame configuration is not supported. Every frame must have the same configuration.
			INTRO_CMD_HELP: Effects of this command \n
			- Frame count functions become unavailable: [SENSe:]NR5G:FRAMe:COUNt [SENSe:]NR5G:FRAMe:COUNt:AUTO
			- [SENSe:]NR5G:FRAMe:COUNt:STATe \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:SWEep:LCAPture?')
		return Conversions.str_to_bool(response)
