from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nfft:
	"""Nfft commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nfft", core, parent)

	def set(self, loffset: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:NFFT \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.nfft.set(loffset = 1.0, rangePy = repcap.RangePy.Default) \n
		Defines the number of FFT averages to be performed for each range or segment. \n
			:param loffset: integer Range: 1 to 20, Unit: DB
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(loffset)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:NFFT {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:NFFT \n
		Snippet: value: float = driver.applications.k50Spurious.sense.listPy.range.nfft.get(rangePy = repcap.RangePy.Default) \n
		Defines the number of FFT averages to be performed for each range or segment. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: loffset: integer Range: 1 to 20, Unit: DB"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:NFFT?')
		return Conversions.str_to_float(response)
