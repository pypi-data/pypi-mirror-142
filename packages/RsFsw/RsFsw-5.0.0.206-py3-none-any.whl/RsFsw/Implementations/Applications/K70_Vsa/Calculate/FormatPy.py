from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, format_py: enums.TraceFormat, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:FORMat \n
		Snippet: driver.applications.k70Vsa.calculate.formatPy.set(format_py = enums.TraceFormat.BERate, window = repcap.Window.Default) \n
		This command defines the result type of the traces. Which parameters are available depends on the setting for the data
		source (see method RsFsw.Layout.Add.Window.get_ and Table 'Available result types depending on data source') . Whether
		the result type shows absolute or relative values is defined using the DISP:WIND:TRAC:Y:MODE command (see method RsFsw.
		Display.Window.Subwindow.Trace.Y.Scale.Mode.set) . \n
			:param format_py: MAGNitude | PHASe | UPHase | RIMag | FREQuency | COMP | CONS | IEYE | QEYE | FEYE | CONF | COVF | RCONstellation | RSUMmary | BERate | GDELay | MOVerview | BIN | OCT | DEC | HEX | NONE MAGNitude Magnitude Absolute MOVerview Magnitude Overview Absolute (entire capture buffer) PHASe Phase Wrap UPHase Phase Unwrap RIMag Real/Imag (I/Q) FREQuency Frequency Absolute COMP Vector I/Q CONS Constellation I/Q IEYE Eye Diagram Real (I) QEYE Eye Diagram Imag (Q) FEYE Eye Diagram Frequency CONF Constellation Frequency COVF Vector Frequency RCONstellation Constellation I/Q (Rotated) RSUMmary Result summary BERate Bit error rate GDELay Frequency Response Group Delay BIN Symbol table in binary format OCT Symbol table in octal format DEC Symbol table in decimal format HEX Symbol table in hexadecimal format
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.TraceFormat)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.TraceFormat:
		"""SCPI: CALCulate<n>:FORMat \n
		Snippet: value: enums.TraceFormat = driver.applications.k70Vsa.calculate.formatPy.get(window = repcap.Window.Default) \n
		This command defines the result type of the traces. Which parameters are available depends on the setting for the data
		source (see method RsFsw.Layout.Add.Window.get_ and Table 'Available result types depending on data source') . Whether
		the result type shows absolute or relative values is defined using the DISP:WIND:TRAC:Y:MODE command (see method RsFsw.
		Display.Window.Subwindow.Trace.Y.Scale.Mode.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: format_py: MAGNitude | PHASe | UPHase | RIMag | FREQuency | COMP | CONS | IEYE | QEYE | FEYE | CONF | COVF | RCONstellation | RSUMmary | BERate | GDELay | MOVerview | BIN | OCT | DEC | HEX | NONE MAGNitude Magnitude Absolute MOVerview Magnitude Overview Absolute (entire capture buffer) PHASe Phase Wrap UPHase Phase Unwrap RIMag Real/Imag (I/Q) FREQuency Frequency Absolute COMP Vector I/Q CONS Constellation I/Q IEYE Eye Diagram Real (I) QEYE Eye Diagram Imag (Q) FEYE Eye Diagram Frequency CONF Constellation Frequency COVF Vector Frequency RCONstellation Constellation I/Q (Rotated) RSUMmary Result summary BERate Bit error rate GDELay Frequency Response Group Delay BIN Symbol table in binary format OCT Symbol table in octal format DEC Symbol table in decimal format HEX Symbol table in hexadecimal format"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.TraceFormat)
