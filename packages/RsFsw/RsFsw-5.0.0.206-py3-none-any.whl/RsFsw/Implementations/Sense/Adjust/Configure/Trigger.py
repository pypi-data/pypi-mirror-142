from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:ADJust:CONFigure:TRIGger \n
		Snippet: driver.sense.adjust.configure.trigger.set(state = False) \n
		Defines the behavior of the measurement when adjusting a setting automatically (using SENS:ADJ:LEV ON, for example) . See
		'Adjusting settings automatically during triggered measurements'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:ADJust:CONFigure:TRIGger {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:ADJust:CONFigure:TRIGger \n
		Snippet: value: bool = driver.sense.adjust.configure.trigger.get() \n
		Defines the behavior of the measurement when adjusting a setting automatically (using SENS:ADJ:LEV ON, for example) . See
		'Adjusting settings automatically during triggered measurements'. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:ADJust:CONFigure:TRIGger?')
		return Conversions.str_to_bool(response)
