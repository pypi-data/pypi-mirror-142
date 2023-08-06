from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS:PATTern:AUTO \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.kdata.prbs.pattern.auto.set(state = False) \n
		If enabled, the R&S FSW VSA application assumes the pattern is part of the PRBS sequence. If disabled, configure the
		setting using the [SENSe:]DDEMod:KDATa:PRBS:PATTern[:STATe] command. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:KDATa:PRBS:PATTern:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS:PATTern:AUTO \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.kdata.prbs.pattern.auto.get() \n
		If enabled, the R&S FSW VSA application assumes the pattern is part of the PRBS sequence. If disabled, configure the
		setting using the [SENSe:]DDEMod:KDATa:PRBS:PATTern[:STATe] command. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:DDEMod:KDATa:PRBS:PATTern:AUTO?')
		return Conversions.str_to_bool(response)
