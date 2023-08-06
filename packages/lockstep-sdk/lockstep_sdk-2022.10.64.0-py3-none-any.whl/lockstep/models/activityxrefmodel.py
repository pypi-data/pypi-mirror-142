#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class ActivityXRefModel:
    """
    Represents links between an Activity and another record.
    """

    activityXRefId: str = None
    activityId: str = None
    groupKey: str = None
    tableKey: str = None
    objectKey: str = None

