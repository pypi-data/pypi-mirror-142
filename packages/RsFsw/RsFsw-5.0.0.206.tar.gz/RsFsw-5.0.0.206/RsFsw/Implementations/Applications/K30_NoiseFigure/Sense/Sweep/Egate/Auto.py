from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:AUTO \n
		Snippet: driver.applications.k30NoiseFigure.sense.sweep.egate.auto.set(state = False) \n
		Determines whether the same or different triggers are used for general measurement and gating. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The gate is opened by the trigger source defined by [SENSe:]SWEep:EGATe:SOURce, but only after a trigger from the general method RsFsw.Applications.K17_Mcgd.Trigger.Sequence.Source.set occurs. ON | 1 (Default:) The trigger defined by method RsFsw.Applications.K17_Mcgd.Trigger.Sequence.Source.set is used both for the general measurement trigger and the gating trigger.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SWEep:EGATe:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWEep:EGATe:AUTO \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.sense.sweep.egate.auto.get() \n
		Determines whether the same or different triggers are used for general measurement and gating. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The gate is opened by the trigger source defined by [SENSe:]SWEep:EGATe:SOURce, but only after a trigger from the general method RsFsw.Applications.K17_Mcgd.Trigger.Sequence.Source.set occurs. ON | 1 (Default:) The trigger defined by method RsFsw.Applications.K17_Mcgd.Trigger.Sequence.Source.set is used both for the general measurement trigger and the gating trigger."""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:AUTO?')
		return Conversions.str_to_bool(response)
