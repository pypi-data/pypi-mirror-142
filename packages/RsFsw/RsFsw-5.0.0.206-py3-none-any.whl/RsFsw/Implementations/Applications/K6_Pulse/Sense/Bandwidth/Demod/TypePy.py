from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, filter_type: enums.FilterTypeA) -> None:
		"""SCPI: [SENSe]:BWIDth:DEMod:TYPE \n
		Snippet: driver.applications.k6Pulse.sense.bandwidth.demod.typePy.set(filter_type = enums.FilterTypeA.FLAT) \n
		This command defines the type of demodulation filter to be used. For information on supported filter bandwidths see the
		data sheet. \n
			:param filter_type: FLAT | GAUSs FLAT Standard flat demodulation filter GAUSs Gaussian filter for optimized settling behavior For Gaussian filters with a large 3dB bandwidth ( 40 MHz, only available with the bandwidth extension option) the actual filter shape deviates strongly from the ideal Gauss filter outside a range of approximately ±80 MHz. For this range the flat filter is more accurate. For details see 'Effects of large gauss filters'.
		"""
		param = Conversions.enum_scalar_to_str(filter_type, enums.FilterTypeA)
		self._core.io.write(f'SENSe:BWIDth:DEMod:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FilterTypeA:
		"""SCPI: [SENSe]:BWIDth:DEMod:TYPE \n
		Snippet: value: enums.FilterTypeA = driver.applications.k6Pulse.sense.bandwidth.demod.typePy.get() \n
		This command defines the type of demodulation filter to be used. For information on supported filter bandwidths see the
		data sheet. \n
			:return: filter_type: FLAT | GAUSs FLAT Standard flat demodulation filter GAUSs Gaussian filter for optimized settling behavior For Gaussian filters with a large 3dB bandwidth ( 40 MHz, only available with the bandwidth extension option) the actual filter shape deviates strongly from the ideal Gauss filter outside a range of approximately ±80 MHz. For this range the flat filter is more accurate. For details see 'Effects of large gauss filters'."""
		response = self._core.io.query_str(f'SENSe:BWIDth:DEMod:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FilterTypeA)
