from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Continuous:
	"""Continuous commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("continuous", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:ADJust:SCALe[:Y]:AUTO[:CONTinuous] \n
		Snippet: driver.sense.adjust.scale.y.auto.continuous.set(state = False) \n
		Activates automatic scaling of the y-axis in all diagrams according to the current measurement results.
		Currently auto-scaling is only available for AF measurements. RF power and RF spectrum measurements are not affected by
		the auto-scaling. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:ADJust:SCALe:Y:AUTO:CONTinuous {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:ADJust:SCALe[:Y]:AUTO[:CONTinuous] \n
		Snippet: value: bool = driver.sense.adjust.scale.y.auto.continuous.get() \n
		Activates automatic scaling of the y-axis in all diagrams according to the current measurement results.
		Currently auto-scaling is only available for AF measurements. RF power and RF spectrum measurements are not affected by
		the auto-scaling. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:ADJust:SCALe:Y:AUTO:CONTinuous?')
		return Conversions.str_to_bool(response)
