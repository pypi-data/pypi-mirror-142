from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: TRIGger[:SEQuence]:LEVel:POWer:AUTO \n
		Snippet: driver.applications.k91Wlan.trigger.sequence.level.power.auto.set(state = False) \n
		By default, the optimum trigger level for power triggers is automatically measured and determined at the start of each
		sweep (for Modulation Accuracy, Flatness, Tolerance... measurements) . This function is only considered for TRIG:SEQ:SOUR
		IFP and TRIG:SEQ:SOUR RFP, see method RsFsw.Applications.K17_Mcgd.Trigger.Sequence.Source.set In order to define the
		trigger level manually, switch this function off and define the level using method RsFsw.Applications.K17_Mcgd.Trigger.
		Sequence.Level.IfPower.set or method RsFsw.Applications.K17_Mcgd.Trigger.Sequence.Level.RfPower.set. \n
			:param state: OFF | 0 Switches the auto level detection function off ON | 1 Switches the auto level detection function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TRIGger:SEQuence:LEVel:POWer:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: TRIGger[:SEQuence]:LEVel:POWer:AUTO \n
		Snippet: value: bool = driver.applications.k91Wlan.trigger.sequence.level.power.auto.get() \n
		By default, the optimum trigger level for power triggers is automatically measured and determined at the start of each
		sweep (for Modulation Accuracy, Flatness, Tolerance... measurements) . This function is only considered for TRIG:SEQ:SOUR
		IFP and TRIG:SEQ:SOUR RFP, see method RsFsw.Applications.K17_Mcgd.Trigger.Sequence.Source.set In order to define the
		trigger level manually, switch this function off and define the level using method RsFsw.Applications.K17_Mcgd.Trigger.
		Sequence.Level.IfPower.set or method RsFsw.Applications.K17_Mcgd.Trigger.Sequence.Level.RfPower.set. \n
			:return: state: OFF | 0 Switches the auto level detection function off ON | 1 Switches the auto level detection function on"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:LEVel:POWer:AUTO?')
		return Conversions.str_to_bool(response)
