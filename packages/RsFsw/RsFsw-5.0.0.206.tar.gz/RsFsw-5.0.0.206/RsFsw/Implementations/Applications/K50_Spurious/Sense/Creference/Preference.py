from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preference:
	"""Preference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preference", core, parent)

	def set(self, limits: enums.ReferenceMode) -> None:
		"""SCPI: [SENSe]:CREFerence:PREFerence \n
		Snippet: driver.applications.k50Spurious.sense.creference.preference.set(limits = enums.ReferenceMode.ABSolute) \n
		No command help available \n
			:param limits: ABSolute | RELative
		"""
		param = Conversions.enum_scalar_to_str(limits, enums.ReferenceMode)
		self._core.io.write(f'SENSe:CREFerence:PREFerence {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ReferenceMode:
		"""SCPI: [SENSe]:CREFerence:PREFerence \n
		Snippet: value: enums.ReferenceMode = driver.applications.k50Spurious.sense.creference.preference.get() \n
		No command help available \n
			:return: limits: ABSolute | RELative"""
		response = self._core.io.query_str(f'SENSe:CREFerence:PREFerence?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceMode)
