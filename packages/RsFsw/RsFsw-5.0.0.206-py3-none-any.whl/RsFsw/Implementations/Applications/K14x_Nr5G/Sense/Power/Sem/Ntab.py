from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ntab:
	"""Ntab commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ntab", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: [SENSe]:POWer:SEM:NTAB \n
		Snippet: driver.applications.k14Xnr5G.sense.power.sem.ntab.set(value = 1.0) \n
		This command defines the parameter NTABconnectors that defines the position of the spectrum emission mask for 1-H base
		stations.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a 1-H base station (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Bstation.set) . \n
			:param value: No help available
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'SENSe:POWer:SEM:NTAB {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:SEM:NTAB \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.power.sem.ntab.get() \n
		This command defines the parameter NTABconnectors that defines the position of the spectrum emission mask for 1-H base
		stations.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a 1-H base station (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Bstation.set) . \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:SEM:NTAB?')
		return Conversions.str_to_float(response)
