from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eval:
	"""Eval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eval", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: TRACe:IQ:EVAL \n
		Snippet: driver.trace.iq.eval.set(state = False) \n
		This command turns I/Q data analysis on and off. Before you can use this command, you have to turn on the I/Q data
		acquisition using INST:CRE:NEW IQ or method RsFsw.Instrument.Create.Replace.set, or using the TRACe:IQ[:STATe] command to
		replace the current channel while retaining the settings. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TRACe:IQ:EVAL {param}')

	def get(self) -> bool:
		"""SCPI: TRACe:IQ:EVAL \n
		Snippet: value: bool = driver.trace.iq.eval.get() \n
		This command turns I/Q data analysis on and off. Before you can use this command, you have to turn on the I/Q data
		acquisition using INST:CRE:NEW IQ or method RsFsw.Instrument.Create.Replace.set, or using the TRACe:IQ[:STATe] command to
		replace the current channel while retaining the settings. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'TRACe:IQ:EVAL?')
		return Conversions.str_to_bool(response)
