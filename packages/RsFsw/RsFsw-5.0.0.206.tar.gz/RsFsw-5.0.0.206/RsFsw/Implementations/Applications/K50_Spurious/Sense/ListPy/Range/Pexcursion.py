from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pexcursion:
	"""Pexcursion commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pexcursion", core, parent)

	def set(self, loffset: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:PEXCursion \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.pexcursion.set(loffset = 1.0, rangePy = repcap.RangePy.Default) \n
		Defines the minimum level value by which the signal must rise or fall after a detected spur so that a new spur is
		detected. \n
			:param loffset: Unit: DB
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(loffset)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:PEXCursion {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:PEXCursion \n
		Snippet: value: float = driver.applications.k50Spurious.sense.listPy.range.pexcursion.get(rangePy = repcap.RangePy.Default) \n
		Defines the minimum level value by which the signal must rise or fall after a detected spur so that a new spur is
		detected. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: loffset: Unit: DB"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:PEXCursion?')
		return Conversions.str_to_float(response)
