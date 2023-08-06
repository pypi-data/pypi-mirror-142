from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evaluate:
	"""Evaluate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evaluate", core, parent)

	def set(self, dsp: enums.EvaluateDsp, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:EVALuate \n
		Snippet: driver.applications.k60Transient.display.window.evaluate.set(dsp = enums.EvaluateDsp.CHIRp, window = repcap.Window.Default) \n
		Determines the evaluation basis for the specified result display. Which evaluation basis is available for which result
		display is indicated in Table 'Available evaluation methods and evaluation basis'. \n
			:param dsp: FULL | REGion | HOP | CHIRp FULL the full capture buffer REGion the selected analysis region (see 'Selecting the analysis region') HOP an individual selected hop (see method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Selected.set) CHIRp an individual selected chirp (see method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.Selected.set)
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.enum_scalar_to_str(dsp, enums.EvaluateDsp)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:EVALuate {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.EvaluateDsp:
		"""SCPI: DISPlay[:WINDow<n>]:EVALuate \n
		Snippet: value: enums.EvaluateDsp = driver.applications.k60Transient.display.window.evaluate.get(window = repcap.Window.Default) \n
		Determines the evaluation basis for the specified result display. Which evaluation basis is available for which result
		display is indicated in Table 'Available evaluation methods and evaluation basis'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: dsp: FULL | REGion | HOP | CHIRp FULL the full capture buffer REGion the selected analysis region (see 'Selecting the analysis region') HOP an individual selected hop (see method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Selected.set) CHIRp an individual selected chirp (see method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.Selected.set)"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:EVALuate?')
		return Conversions.str_to_scalar_enum(response, enums.EvaluateDsp)
