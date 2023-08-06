from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, trace_mode: List[enums.TraceModeA]) -> None:
		"""SCPI: [SENSe]:ADEMod:FM[:TDOMain][:TYPE] \n
		Snippet: driver.sense.ademod.fm.tdomain.typePy.set(trace_mode = [TraceModeA.AVERage, TraceModeA.WRITe]) \n
		This command selects the trace modes of the evaluated signal to be measured simultaneously. For each of the six available
		traces a mode can be defined. For details on trace modes see 'Trace Mode'. The trace modes are configured identically for
		all windows with a specific evaluation. The following table indicates which command syntax refers to which evaluation
		method.
			Table Header: Command syntax / Evaluation method \n
			- AM[:ABSolute][:TDOMain] / RF time domain
			- AM:RELative[:TDOMain] / AM time domain
			- AM:RELative:AFSPectrum / AM spectrum (relative)
			- FM[:TDOMain] / FM time domain
			- FM:AFSPectrum / FM spectrum
			- PM[:TDOMain] / PM time domain
			- PM:AFSPectrum / PM spectrum
			- SPECtrum / RF spectrum
		Note: The trace modes for each trace and each window can also be configured individually using the method RsFsw.Display.
		Window.Trace.Mode.set command, see method RsFsw.Display.Window.Trace.Mode.set. \n
			:param trace_mode: WRITe | AVERage | MAXHold | MINHold | VIEW | OFF WRITe Overwrite mode: the trace is overwritten by each sweep. This is the default setting. AVERage The average is formed over several sweeps. The 'Sweep/Average Count' determines the number of averaging procedures. MAXHold The maximum value is determined over several sweeps and displayed. The R&S FSW saves the sweep result in the trace memory only if the new value is greater than the previous one. MINHold The minimum value is determined from several measurements and displayed. The R&S FSW saves the sweep result in the trace memory only if the new value is lower than the previous one. VIEW The current contents of the trace memory are frozen and displayed. OFF Hides the selected trace.
		"""
		param = Conversions.enum_list_to_str(trace_mode, enums.TraceModeA)
		self._core.io.write(f'SENSe:ADEMod:FM:TDOMain:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> List[enums.TraceModeA]:
		"""SCPI: [SENSe]:ADEMod:FM[:TDOMain][:TYPE] \n
		Snippet: value: List[enums.TraceModeA] = driver.sense.ademod.fm.tdomain.typePy.get() \n
		This command selects the trace modes of the evaluated signal to be measured simultaneously. For each of the six available
		traces a mode can be defined. For details on trace modes see 'Trace Mode'. The trace modes are configured identically for
		all windows with a specific evaluation. The following table indicates which command syntax refers to which evaluation
		method.
			Table Header: Command syntax / Evaluation method \n
			- AM[:ABSolute][:TDOMain] / RF time domain
			- AM:RELative[:TDOMain] / AM time domain
			- AM:RELative:AFSPectrum / AM spectrum (relative)
			- FM[:TDOMain] / FM time domain
			- FM:AFSPectrum / FM spectrum
			- PM[:TDOMain] / PM time domain
			- PM:AFSPectrum / PM spectrum
			- SPECtrum / RF spectrum
		Note: The trace modes for each trace and each window can also be configured individually using the method RsFsw.Display.
		Window.Trace.Mode.set command, see method RsFsw.Display.Window.Trace.Mode.set. \n
			:return: trace_mode: WRITe | AVERage | MAXHold | MINHold | VIEW | OFF WRITe Overwrite mode: the trace is overwritten by each sweep. This is the default setting. AVERage The average is formed over several sweeps. The 'Sweep/Average Count' determines the number of averaging procedures. MAXHold The maximum value is determined over several sweeps and displayed. The R&S FSW saves the sweep result in the trace memory only if the new value is greater than the previous one. MINHold The minimum value is determined from several measurements and displayed. The R&S FSW saves the sweep result in the trace memory only if the new value is lower than the previous one. VIEW The current contents of the trace memory are frozen and displayed. OFF Hides the selected trace."""
		response = self._core.io.query_str(f'SENSe:ADEMod:FM:TDOMain:TYPE?')
		return Conversions.str_to_list_enum(response, enums.TraceModeA)
