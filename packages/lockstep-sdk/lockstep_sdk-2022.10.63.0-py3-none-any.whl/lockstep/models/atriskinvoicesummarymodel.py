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
class AtRiskInvoiceSummaryModel:
    """
    Contains summarized data for an invoice
    """

    reportDate: str = None
    groupKey: str = None
    customerId: str = None
    invoiceId: str = None
    invoiceNumber: str = None
    invoiceDate: str = None
    customerName: str = None
    status: str = None
    paymentDueDate: str = None
    invoiceAmount: float = None
    outstandingBalance: float = None
    invoiceTypeCode: str = None
    newestActivity: str = None
    daysPastDue: int = None
    paymentNumbers: list[str] = None
    paymentIds: list[str] = None

