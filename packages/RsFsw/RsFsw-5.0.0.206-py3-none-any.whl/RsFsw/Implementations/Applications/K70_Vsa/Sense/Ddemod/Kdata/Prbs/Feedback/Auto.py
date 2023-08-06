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
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS:FEEDback:AUTO \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.kdata.prbs.feedback.auto.set(state = False) \n
		Determines how the feedback value is calculated. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The setting defined by [SENSe:]DDEMod:KDATa:PRBS:FEEDback[:STATe] is used for all PRBS types. ON | 1 The feedback value is negated or not, depending on the standard for the used PRBS type.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:KDATa:PRBS:FEEDback:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS:FEEDback:AUTO \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.kdata.prbs.feedback.auto.get() \n
		Determines how the feedback value is calculated. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The setting defined by [SENSe:]DDEMod:KDATa:PRBS:FEEDback[:STATe] is used for all PRBS types. ON | 1 The feedback value is negated or not, depending on the standard for the used PRBS type."""
		response = self._core.io.query_str(f'SENSe:DDEMod:KDATa:PRBS:FEEDback:AUTO?')
		return Conversions.str_to_bool(response)
