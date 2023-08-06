from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, data_type: enums.IqType, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:TYPE \n
		Snippet: driver.inputPy.iq.typePy.set(data_type = enums.IqType.Ipart=I, inputIx = repcap.InputIx.Default) \n
		This command defines the format of the input signal. \n
			:param data_type: IQ | I | Q IQ The input signal is filtered and resampled to the sample rate of the application. Two input channels are required for each input signal, one for the in-phase component, and one for the quadrature component. I The in-phase component of the input signal is filtered and resampled to the sample rate of the application. If the center frequency is not 0, the in-phase component of the input signal is down-converted first (Low IF I) . Q The quadrature component of the input signal is filtered and resampled to the sample rate of the application. If the center frequency is not 0, the quadrature component of the input signal is down-converted first (Low IF Q) .
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(data_type, enums.IqType)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.IqType:
		"""SCPI: INPut<ip>:IQ:TYPE \n
		Snippet: value: enums.IqType = driver.inputPy.iq.typePy.get(inputIx = repcap.InputIx.Default) \n
		This command defines the format of the input signal. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: data_type: IQ | I | Q IQ The input signal is filtered and resampled to the sample rate of the application. Two input channels are required for each input signal, one for the in-phase component, and one for the quadrature component. I The in-phase component of the input signal is filtered and resampled to the sample rate of the application. If the center frequency is not 0, the in-phase component of the input signal is down-converted first (Low IF I) . Q The quadrature component of the input signal is filtered and resampled to the sample rate of the application. If the center frequency is not 0, the quadrature component of the input signal is down-converted first (Low IF Q) ."""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.IqType)
