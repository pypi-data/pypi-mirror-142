from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, factory: enums.Factory) -> None:
		"""SCPI: [SENSe]:DDEMod:FACTory[:VALue] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.factory.value.set(factory = enums.Factory.ALL) \n
		This command restores the factory settings of standards or patterns for the VSA application. \n
			:param factory: ALL | STANdard | PATTern ALL Restores both standards and patterns.
		"""
		param = Conversions.enum_scalar_to_str(factory, enums.Factory)
		self._core.io.write(f'SENSe:DDEMod:FACTory:VALue {param}')
