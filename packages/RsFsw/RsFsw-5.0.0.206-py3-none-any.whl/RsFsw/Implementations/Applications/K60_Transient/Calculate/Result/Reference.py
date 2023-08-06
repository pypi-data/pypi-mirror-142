from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	def set(self, reference: enums.ResultReference, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:RESult:REFerence \n
		Snippet: driver.applications.k60Transient.calculate.result.reference.set(reference = enums.ResultReference.CENTer, window = repcap.Window.Default) \n
		Defines the reference point for positioning the result range. \n
			:param reference: RISE | CENTer | FALL RISE The result range is defined in reference to the rising edge. CENTer The result range is defined in reference to the center of the hop/chirp top. FALL The result range is defined in reference to the falling edge.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.ResultReference)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:RESult:REFerence {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.ResultReference:
		"""SCPI: CALCulate<n>:RESult:REFerence \n
		Snippet: value: enums.ResultReference = driver.applications.k60Transient.calculate.result.reference.get(window = repcap.Window.Default) \n
		Defines the reference point for positioning the result range. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: reference: RISE | CENTer | FALL RISE The result range is defined in reference to the rising edge. CENTer The result range is defined in reference to the center of the hop/chirp top. FALL The result range is defined in reference to the falling edge."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:RESult:REFerence?')
		return Conversions.str_to_scalar_enum(response, enums.ResultReference)
