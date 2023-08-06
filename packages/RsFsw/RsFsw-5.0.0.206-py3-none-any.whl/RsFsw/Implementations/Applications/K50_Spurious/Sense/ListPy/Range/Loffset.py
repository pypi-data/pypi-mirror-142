from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Loffset:
	"""Loffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loffset", core, parent)

	def set(self, loffset: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:LOFFset \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.loffset.set(loffset = 1.0, rangePy = repcap.RangePy.Default) \n
		Defines a limit line as an offset to the detection threshold for each range. \n
			:param loffset: Range: 0 to 20, Unit: DB
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(loffset)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:LOFFset {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:LOFFset \n
		Snippet: value: float = driver.applications.k50Spurious.sense.listPy.range.loffset.get(rangePy = repcap.RangePy.Default) \n
		Defines a limit line as an offset to the detection threshold for each range. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: loffset: Range: 0 to 20, Unit: DB"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:LOFFset?')
		return Conversions.str_to_float(response)
