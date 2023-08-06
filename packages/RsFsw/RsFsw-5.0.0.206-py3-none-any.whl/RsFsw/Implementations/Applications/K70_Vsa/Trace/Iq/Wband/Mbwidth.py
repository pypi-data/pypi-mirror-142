from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mbwidth:
	"""Mbwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mbwidth", core, parent)

	def set(self, max_bandwidth: float) -> None:
		"""SCPI: TRACe:IQ:WBANd:MBWidth \n
		Snippet: driver.applications.k70Vsa.trace.iq.wband.mbwidth.set(max_bandwidth = 1.0) \n
		Defines the maximum analysis bandwidth. Any value can be specified; the next higher fixed bandwidth is used. Defining a
		value other than 'MAX' is useful if you want to specify the sample rate directly and at the same time, ensure a minimum
		bandwidth is available. (See 'Sample rate and maximum usable I/Q bandwidth for RF input') . \n
			:param max_bandwidth: 80 MHz Restricts the analysis bandwidth to a maximum of 80 MHz. The bandwidth extension options greater than 160 MHz are disabled. method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.State.set is set to OFF. 160 MHz Restricts the analysis bandwidth to a maximum of 160 MHz. The bandwidth extension option R&S FSW-B320 is deactivated. (Not available or required if other bandwidth extension options larger than 320 MHz are installed.) method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.State.set is set to ON. 1200 MHz | 500 MHz | 320 MHz | MAX All installed bandwidth extension options are activated. The currently available maximum bandwidth is allowed. (See 'Sample rate and maximum usable I/Q bandwidth for RF input') . method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.State.set is set to ON. Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(max_bandwidth)
		self._core.io.write(f'TRACe:IQ:WBANd:MBWidth {param}')

	def get(self) -> float:
		"""SCPI: TRACe:IQ:WBANd:MBWidth \n
		Snippet: value: float = driver.applications.k70Vsa.trace.iq.wband.mbwidth.get() \n
		Defines the maximum analysis bandwidth. Any value can be specified; the next higher fixed bandwidth is used. Defining a
		value other than 'MAX' is useful if you want to specify the sample rate directly and at the same time, ensure a minimum
		bandwidth is available. (See 'Sample rate and maximum usable I/Q bandwidth for RF input') . \n
			:return: max_bandwidth: No help available"""
		response = self._core.io.query_str(f'TRACe:IQ:WBANd:MBWidth?')
		return Conversions.str_to_float(response)
