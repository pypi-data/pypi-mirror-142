from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Category:
	"""Category commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("category", core, parent)

	@property
	def b(self):
		"""b commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_b'):
			from .B import B
			self._b = B(self._core, self._cmd_group)
		return self._b

	def set(self, category: enums.PowerCategory) -> None:
		"""SCPI: [SENSe]:POWer:CATegory \n
		Snippet: driver.applications.k14Xnr5G.sense.power.category.set(category = enums.PowerCategory.A) \n
		This command selects the base station category- \n
			:param category: A Category A base station. B Category B base station. LARE Large area base station. MED Medium area base station.
		"""
		param = Conversions.enum_scalar_to_str(category, enums.PowerCategory)
		self._core.io.write(f'SENSe:POWer:CATegory {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PowerCategory:
		"""SCPI: [SENSe]:POWer:CATegory \n
		Snippet: value: enums.PowerCategory = driver.applications.k14Xnr5G.sense.power.category.get() \n
		This command selects the base station category- \n
			:return: category: A Category A base station. B Category B base station. LARE Large area base station. MED Medium area base station."""
		response = self._core.io.query_str(f'SENSe:POWer:CATegory?')
		return Conversions.str_to_scalar_enum(response, enums.PowerCategory)

	def clone(self) -> 'Category':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Category(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
