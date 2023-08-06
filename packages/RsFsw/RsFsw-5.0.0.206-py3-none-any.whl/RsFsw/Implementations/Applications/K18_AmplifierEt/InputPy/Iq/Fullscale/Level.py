from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, peak_voltage: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:FULLscale:LEVel \n
		Snippet: driver.applications.k18AmplifierEt.inputPy.iq.fullscale.level.set(peak_voltage = 1.0, inputIx = repcap.InputIx.Default) \n
		This command defines the peak voltage at the Baseband Input connector if the full scale level is set to manual mode (see
		method RsFsw.Applications.K10x_Lte.InputPy.Iq.Fullscale.Auto.set) . \n
			:param peak_voltage: 0.25 V | 0.5 V | 1 V | 2 V Peak voltage level at the connector. For probes, the possible full scale values are adapted according to the probe's attenuation and maximum allowed power. Unit: V
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(peak_voltage)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:FULLscale:LEVel {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<ip>:IQ:FULLscale:LEVel \n
		Snippet: value: float = driver.applications.k18AmplifierEt.inputPy.iq.fullscale.level.get(inputIx = repcap.InputIx.Default) \n
		This command defines the peak voltage at the Baseband Input connector if the full scale level is set to manual mode (see
		method RsFsw.Applications.K10x_Lte.InputPy.Iq.Fullscale.Auto.set) . \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: peak_voltage: 0.25 V | 0.5 V | 1 V | 2 V Peak voltage level at the connector. For probes, the possible full scale values are adapted according to the probe's attenuation and maximum allowed power. Unit: V"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:FULLscale:LEVel?')
		return Conversions.str_to_float(response)
