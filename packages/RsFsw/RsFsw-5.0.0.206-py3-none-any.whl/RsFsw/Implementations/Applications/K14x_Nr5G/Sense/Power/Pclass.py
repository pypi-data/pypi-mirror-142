from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pclass:
	"""Pclass commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pclass", core, parent)

	def set(self, power_class: enums.PowerClass) -> None:
		"""SCPI: [SENSe]:POWer:PCLass \n
		Snippet: driver.applications.k14Xnr5G.sense.power.pclass.set(power_class = enums.PowerClass.PC1) \n
		This command selects the power class of a UE for ACLR measurements. \n
			:param power_class: PC2 | PC3
		"""
		param = Conversions.enum_scalar_to_str(power_class, enums.PowerClass)
		self._core.io.write(f'SENSe:POWer:PCLass {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PowerClass:
		"""SCPI: [SENSe]:POWer:PCLass \n
		Snippet: value: enums.PowerClass = driver.applications.k14Xnr5G.sense.power.pclass.get() \n
		This command selects the power class of a UE for ACLR measurements. \n
			:return: power_class: PC2 | PC3"""
		response = self._core.io.query_str(f'SENSe:POWer:PCLass?')
		return Conversions.str_to_scalar_enum(response, enums.PowerClass)
