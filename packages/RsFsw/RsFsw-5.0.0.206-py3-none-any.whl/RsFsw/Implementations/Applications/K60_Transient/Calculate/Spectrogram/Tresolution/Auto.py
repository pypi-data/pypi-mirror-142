from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, reference: enums.AutoManualMode, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:SPECtrogram:TRESolution:AUTO \n
		Snippet: driver.applications.k60Transient.calculate.spectrogram.tresolution.auto.set(reference = enums.AutoManualMode.AUTO, window = repcap.Window.Default) \n
		No command help available \n
			:param reference: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.AutoManualMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:SPECtrogram:TRESolution:AUTO {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.AutoManualMode:
		"""SCPI: CALCulate<n>:SPECtrogram:TRESolution:AUTO \n
		Snippet: value: enums.AutoManualMode = driver.applications.k60Transient.calculate.spectrogram.tresolution.auto.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: reference: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:SPECtrogram:TRESolution:AUTO?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
