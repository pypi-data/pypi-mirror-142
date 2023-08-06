from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:EPRate:AUTO \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.epRate.auto.set(state = False) \n
		Defines how many sample points are used at each symbol to calculate modulation accuracy results automatically. If enabled,
		the VSA application uses the following settings, depending on the modulation type:
			Table Header: Modulation / Est. Points \n
			- PSK, QAM / 1
			- Offset QPSK / 2
			- FSK, MSK / Sample rate (see [SENSe:]DDEMod:PRATe) \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:EPRate:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:EPRate:AUTO \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.epRate.auto.get() \n
		Defines how many sample points are used at each symbol to calculate modulation accuracy results automatically. If enabled,
		the VSA application uses the following settings, depending on the modulation type:
			Table Header: Modulation / Est. Points \n
			- PSK, QAM / 1
			- Offset QPSK / 2
			- FSK, MSK / Sample rate (see [SENSe:]DDEMod:PRATe) \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:EPRate:AUTO?')
		return Conversions.str_to_bool(response)
