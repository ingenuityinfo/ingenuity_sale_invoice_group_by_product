========================
Ingenuity Sale Order Invoiced Grouped By Product
========================

This Module will provide feature when invoicing a Sales Order or multiple at once, the invoice lines will be grouped based on product.
So if Sale Order SO001 contains Product-1 and Product-2, and Sale Order SO002 contains Product-1 and Product-3, the invoice generated when invoicing these two Sale Order at once will contain only 3 lines. System will combine the repeated Product in one single and sum it's Qty.
- one with Product-1 and the sum of quantities from SO001 and SO002
- one with Product 2
- one with Product 3

Important, this module will generate invoice lines with only Products, no notes and sections.


Odoo Version
=============
Odoo 15 Community Edition


Release Notes
=============

[15.0.0.0] :  Add Module


Installation
============

To install this module, you need to: 'Sale' and 'Account'

Download the module and add it to your Odoo addons folder. Afterward, log on to
your Odoo server and go to the Apps menu. Trigger the debug mode and update the
list by clicking on the "Update Apps List" link. Now install the module by
clicking on the install button.

Upgrade
=======

To upgrade this module, you need to:

Download the module and add it to your Odoo addons folder. Restart the server
and log on to your Odoo server. Select the Apps menu and upgrade the module by
clicking on the upgrade button.


Configuration
=============

There is Nothing to Configure


Credits
=======

Contributors
------------

* Ingenuity Info <contact@ingenuityinfo.in>


Author & Maintainer
-------------------

This module is maintained by the Ingenuity Info
