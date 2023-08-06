from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McOffset:
	"""McOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcOffset", core, parent)

	def set(self, max_clock_offset: float) -> None:
		"""SCPI: [SENSe]:CESTimation:MCOFfset \n
		Snippet: driver.applications.k17Mcgd.sense.cestimation.mcOffset.set(max_clock_offset = 1.0) \n
		Defines the maximum clock offset the frequency estimation algorithm of the R&S FSW MCGD application is able to handle.
		Larger values for this parameter result in slower measurement speed. This parameter is automatically calculated using the
		other three 'Doppler Shift Compensation' parameter settings. For the calculation, speed of light in medium vacuum (cvac)
		is used. \n
			:param max_clock_offset: numeric value
		"""
		param = Conversions.decimal_value_to_str(max_clock_offset)
		self._core.io.write(f'SENSe:CESTimation:MCOFfset {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CESTimation:MCOFfset \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.cestimation.mcOffset.get() \n
		Defines the maximum clock offset the frequency estimation algorithm of the R&S FSW MCGD application is able to handle.
		Larger values for this parameter result in slower measurement speed. This parameter is automatically calculated using the
		other three 'Doppler Shift Compensation' parameter settings. For the calculation, speed of light in medium vacuum (cvac)
		is used. \n
			:return: max_clock_offset: numeric value"""
		response = self._core.io.query_str(f'SENSe:CESTimation:MCOFfset?')
		return Conversions.str_to_float(response)
