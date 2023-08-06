from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Definition:
	"""Definition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("definition", core, parent)

	def set(self, result_type: enums.AmPmDef, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:AMPM:DEFinition \n
		Snippet: driver.applications.k18AmplifierEt.calculate.amPm.definition.set(result_type = enums.AmPmDef.MREF, window = repcap.Window.Default) \n
		This command selects the way the AM/PM results are calculated. \n
			:param result_type: MREF Subtracts the reference trace from the measurement trace. This is the inverse of the default REAFMeas method. REFMeas Subtracts the measurement trace from the reference trace.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(result_type, enums.AmPmDef)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:AMPM:DEFinition {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.AmPmDef:
		"""SCPI: CALCulate<n>:AMPM:DEFinition \n
		Snippet: value: enums.AmPmDef = driver.applications.k18AmplifierEt.calculate.amPm.definition.get(window = repcap.Window.Default) \n
		This command selects the way the AM/PM results are calculated. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: result_type: MREF Subtracts the reference trace from the measurement trace. This is the inverse of the default REAFMeas method. REFMeas Subtracts the measurement trace from the reference trace."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:AMPM:DEFinition?')
		return Conversions.str_to_scalar_enum(response, enums.AmPmDef)
