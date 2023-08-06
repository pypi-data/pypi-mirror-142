from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coupling:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)

	def set(self, coupling: enums.CouplingTypeB, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:OSC:COUPling \n
		Snippet: driver.inputPy.iq.osc.coupling.set(coupling = enums.CouplingTypeB.AC, inputIx = repcap.InputIx.Default) \n
		Determines the coupling of the oscilloscope to the R&S FSW. \n
			:param coupling: DC | DCLimit | AC DC DC coupling shows all parts of an input signal. DC 50 Ω coupling is the default for 50Ω input impedance to connect, for example, active probes. DCLimit DC coupling with 1 M Ω input impedance to connect standard passive probes. AC AC coupling is useful if the DC component of a signal is of no interest. AC coupling blocks the DC component of the signal so that the waveform is centered on zero volts.
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(coupling, enums.CouplingTypeB)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:OSC:COUPling {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.CouplingTypeB:
		"""SCPI: INPut<ip>:IQ:OSC:COUPling \n
		Snippet: value: enums.CouplingTypeB = driver.inputPy.iq.osc.coupling.get(inputIx = repcap.InputIx.Default) \n
		Determines the coupling of the oscilloscope to the R&S FSW. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: coupling: DC | DCLimit | AC DC DC coupling shows all parts of an input signal. DC 50 Ω coupling is the default for 50Ω input impedance to connect, for example, active probes. DCLimit DC coupling with 1 M Ω input impedance to connect standard passive probes. AC AC coupling is useful if the DC component of a signal is of no interest. AC coupling blocks the DC component of the signal so that the waveform is centered on zero volts."""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:OSC:COUPling?')
		return Conversions.str_to_scalar_enum(response, enums.CouplingTypeB)
