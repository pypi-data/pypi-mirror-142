from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, reference: enums.EventOnce) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:REFerence:AUTO \n
		Snippet: driver.applications.k91Wlan.sense.power.achannel.reference.auto.set(reference = enums.EventOnce.ONCE) \n
		No command help available \n
			:param reference: No help available
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.EventOnce)
		self._core.io.write(f'SENSe:POWer:ACHannel:REFerence:AUTO {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.EventOnce:
		"""SCPI: [SENSe]:POWer:ACHannel:REFerence:AUTO \n
		Snippet: value: enums.EventOnce = driver.applications.k91Wlan.sense.power.achannel.reference.auto.get() \n
		No command help available \n
			:return: reference: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:REFerence:AUTO?')
		return Conversions.str_to_scalar_enum(response, enums.EventOnce)
