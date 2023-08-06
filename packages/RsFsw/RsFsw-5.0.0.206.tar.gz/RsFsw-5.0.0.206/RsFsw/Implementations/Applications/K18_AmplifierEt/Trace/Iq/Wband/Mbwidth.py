from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mbwidth:
	"""Mbwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mbwidth", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: TRACe:IQ:WBANd:MBWidth \n
		Snippet: driver.applications.k18AmplifierEt.trace.iq.wband.mbwidth.set(bandwidth = 1.0) \n
		This command selects the largest possible bandwidth that can be applied for the wideband signal path. The wideband signal
		path is available with the corresponding bandwidth extensions available for the R&S FSW. The command is available when
		you turn on method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.State.set. \n
			:param bandwidth: 80MHZ Restricts the bandwidth to 80 MHz. (The wideband signal path is not used in that case. method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.State.set is turned off.) 160MHZ | 320MHZ | 500MHZ Restricts the bandwidth to the corresponding value, even if you have installed a higher bandwidth extension. Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'TRACe:IQ:WBANd:MBWidth {param}')

	def get(self) -> float:
		"""SCPI: TRACe:IQ:WBANd:MBWidth \n
		Snippet: value: float = driver.applications.k18AmplifierEt.trace.iq.wband.mbwidth.get() \n
		This command selects the largest possible bandwidth that can be applied for the wideband signal path. The wideband signal
		path is available with the corresponding bandwidth extensions available for the R&S FSW. The command is available when
		you turn on method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.State.set. \n
			:return: bandwidth: 80MHZ Restricts the bandwidth to 80 MHz. (The wideband signal path is not used in that case. method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.State.set is turned off.) 160MHZ | 320MHZ | 500MHZ Restricts the bandwidth to the corresponding value, even if you have installed a higher bandwidth extension. Unit: Hz"""
		response = self._core.io.query_str(f'TRACe:IQ:WBANd:MBWidth?')
		return Conversions.str_to_float(response)
