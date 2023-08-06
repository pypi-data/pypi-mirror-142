from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS:FEEDback[:STATe] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.kdata.prbs.feedback.state.set(state = False) \n
		Determines how the feedback bit is calculated. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The xor connected bit from the specified feedback positions is fed into the last shift register. ON | 1 The xor connected bit from the specified feedback positions is inverted before it is fed into the last shift register.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:KDATa:PRBS:FEEDback:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS:FEEDback[:STATe] \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.kdata.prbs.feedback.state.get() \n
		Determines how the feedback bit is calculated. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The xor connected bit from the specified feedback positions is fed into the last shift register. ON | 1 The xor connected bit from the specified feedback positions is inverted before it is fed into the last shift register."""
		response = self._core.io.query_str(f'SENSe:DDEMod:KDATa:PRBS:FEEDback:STATe?')
		return Conversions.str_to_bool(response)
