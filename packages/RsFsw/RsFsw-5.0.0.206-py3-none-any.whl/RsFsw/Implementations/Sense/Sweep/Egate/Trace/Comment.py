from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Comment:
	"""Comment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("comment", core, parent)

	def set(self, comment: str, trace=repcap.Trace.Default) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:TRACe<t>:COMMent \n
		Snippet: driver.sense.sweep.egate.trace.comment.set(comment = '1', trace = repcap.Trace.Default) \n
		This command defines a comment for the gate of a particular trace. \n
			:param comment: String containing the comment.
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.value_to_quoted_str(comment)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'SENSe:SWEep:EGATe:TRACe{trace_cmd_val}:COMMent {param}')

	def get(self, trace=repcap.Trace.Default) -> str:
		"""SCPI: [SENSe]:SWEep:EGATe:TRACe<t>:COMMent \n
		Snippet: value: str = driver.sense.sweep.egate.trace.comment.get(trace = repcap.Trace.Default) \n
		This command defines a comment for the gate of a particular trace. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: comment: String containing the comment."""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:TRACe{trace_cmd_val}:COMMent?')
		return trim_str_response(response)
