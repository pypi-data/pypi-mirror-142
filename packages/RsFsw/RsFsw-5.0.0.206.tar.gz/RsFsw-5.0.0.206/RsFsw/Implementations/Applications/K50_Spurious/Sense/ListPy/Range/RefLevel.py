from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefLevel:
	"""RefLevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refLevel", core, parent)

	def set(self, ref_level: int, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:RLEVel \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.refLevel.set(ref_level = 1, rangePy = repcap.RangePy.Default) \n
		No command help available \n
			:param ref_level: Range: -130 dBm to 30 dBm (–10 dBm + RF attenuation – RF preamplifier gain) , Unit: DBM
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(ref_level)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:RLEVel {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> int:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:RLEVel \n
		Snippet: value: int = driver.applications.k50Spurious.sense.listPy.range.refLevel.get(rangePy = repcap.RangePy.Default) \n
		No command help available \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: ref_level: Range: -130 dBm to 30 dBm (–10 dBm + RF attenuation – RF preamplifier gain) , Unit: DBM"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:RLEVel?')
		return Conversions.str_to_int(response)
