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

	def set(self, once: enums.EventOnce) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:REFerence:AUTO \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.reference.auto.set(once = enums.EventOnce.ONCE) \n
		No command help available \n
			:param once: No help available
		"""
		param = Conversions.enum_scalar_to_str(once, enums.EventOnce)
		self._core.io.write(f'SENSe:POWer:ACHannel:REFerence:AUTO {param}')
