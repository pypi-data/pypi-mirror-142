from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, single_value: enums.SingleValue, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:ITEM[:LINE][:VALue] \n
		Snippet: driver.applications.k70Vsa.display.window.item.line.value.set(single_value = enums.SingleValue.ALL, window = repcap.Window.Default) \n
		This commands switches between the whole Result Summary and the diagram showing only a single value, e.g. the EVM RMS
		value as a bargraph. The same parameters are available as those for which modulation accuracy limits can be defined (see
		'Limit Value') . \n
			:param single_value: ALL | EVMR | EVMP | PERM | PEP | MERM | MEP | CFER | RHO | IQOF | FERM | FEP | FDER ALL Complete Result Summary EVMR RMS EVM EVMP Peak EVM PERM RMS Phase error PEP Peak phase error MERM RMS Magnitude error MEP Peak magnitude error CFER Carrier frequency error RHO RHO IQOF I/Q offset FERM RMS frequency error FEP Peak frequency error FDER FSK deviation error
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.enum_scalar_to_str(single_value, enums.SingleValue)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:ITEM:LINE:VALue {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.SingleValue:
		"""SCPI: DISPlay[:WINDow<n>]:ITEM[:LINE][:VALue] \n
		Snippet: value: enums.SingleValue = driver.applications.k70Vsa.display.window.item.line.value.get(window = repcap.Window.Default) \n
		This commands switches between the whole Result Summary and the diagram showing only a single value, e.g. the EVM RMS
		value as a bargraph. The same parameters are available as those for which modulation accuracy limits can be defined (see
		'Limit Value') . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: single_value: ALL | EVMR | EVMP | PERM | PEP | MERM | MEP | CFER | RHO | IQOF | FERM | FEP | FDER ALL Complete Result Summary EVMR RMS EVM EVMP Peak EVM PERM RMS Phase error PEP Peak phase error MERM RMS Magnitude error MEP Peak magnitude error CFER Carrier frequency error RHO RHO IQOF I/Q offset FERM RMS frequency error FEP Peak frequency error FDER FSK deviation error"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:ITEM:LINE:VALue?')
		return Conversions.str_to_scalar_enum(response, enums.SingleValue)
