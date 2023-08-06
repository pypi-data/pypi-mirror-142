from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, prbs_type: float) -> None:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS[:TYPE] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.kdata.prbs.typePy.set(prbs_type = 1.0) \n
		Defines the type of the used PRBS model. The type of the model defines the degree, complexity and number of terms in the
		polynomial model. If the PRBS data is generated in accordance with the ITU-T standard, no further settings are required.
		This function requires the R&S FSW-K70P option. For details, see 'Known data from PRBS generators'. \n
			:param prbs_type: 7 | 9 | 11 | 15 | 16 | 20 | 21 | 23 | 31
		"""
		param = Conversions.decimal_value_to_str(prbs_type)
		self._core.io.write(f'SENSe:DDEMod:KDATa:PRBS:TYPE {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS[:TYPE] \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.kdata.prbs.typePy.get() \n
		Defines the type of the used PRBS model. The type of the model defines the degree, complexity and number of terms in the
		polynomial model. If the PRBS data is generated in accordance with the ITU-T standard, no further settings are required.
		This function requires the R&S FSW-K70P option. For details, see 'Known data from PRBS generators'. \n
			:return: prbs_type: 7 | 9 | 11 | 15 | 16 | 20 | 21 | 23 | 31"""
		response = self._core.io.query_str(f'SENSe:DDEMod:KDATa:PRBS:TYPE?')
		return Conversions.str_to_float(response)
