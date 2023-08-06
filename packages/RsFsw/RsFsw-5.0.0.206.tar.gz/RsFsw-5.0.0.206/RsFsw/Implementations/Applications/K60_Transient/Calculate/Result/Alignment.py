from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alignment:
	"""Alignment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alignment", core, parent)

	def set(self, reference: enums.AdjustAlignment, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:RESult:ALIGnment \n
		Snippet: driver.applications.k60Transient.calculate.result.alignment.set(reference = enums.AdjustAlignment.CENTer, window = repcap.Window.Default) \n
		Defines the alignment of the result range in relation to the selected reference point (see method RsFsw.Applications.
		K60_Transient.Calculate.Result.Reference.set) . \n
			:param reference: LEFT | CENTer | RIGHt LEFT The result range starts at the hop/chirp center or selected edge. CENTer The result range is centered around the hop/chirp center or selected edge. RIGHt The result range ends at the hop/chirp center or selected edge.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.AdjustAlignment)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:RESult:ALIGnment {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.AdjustAlignment:
		"""SCPI: CALCulate<n>:RESult:ALIGnment \n
		Snippet: value: enums.AdjustAlignment = driver.applications.k60Transient.calculate.result.alignment.get(window = repcap.Window.Default) \n
		Defines the alignment of the result range in relation to the selected reference point (see method RsFsw.Applications.
		K60_Transient.Calculate.Result.Reference.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: reference: LEFT | CENTer | RIGHt LEFT The result range starts at the hop/chirp center or selected edge. CENTer The result range is centered around the hop/chirp center or selected edge. RIGHt The result range ends at the hop/chirp center or selected edge."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:RESult:ALIGnment?')
		return Conversions.str_to_scalar_enum(response, enums.AdjustAlignment)
