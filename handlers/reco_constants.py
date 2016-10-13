class manufacturer:
	def __init__(self):
		self.name = ''
		self.keywords = []

dw_manufacturer = manufacturer()
dw_manufacturer.name = 'Dresser Wayne'
dw_manufacturer.keywords = ['dresser', 'wayne', 'Ovation', 'Helix', 'Vista', 'CNG', 'HS', 'Reliance', 'Global', 'Centure', 'Select']

gvr_manufacturer = manufacturer()
gvr_manufacturer.name = 'Gilbarco Veeder-Root'
gvr_manufacturer.keywords = ['Gilbarco', 'veeder', 'root', 'Encore']

t_manufacturer = manufacturer()
t_manufacturer.name = 'Tokheim'
t_manufacturer.keywords = ['Tokheim', 'quantium', 'adblue', 'lpg', '310', '510', '410', 'UHS', '210', '110', 'dialog']

b_manufacturer = manufacturer()
b_manufacturer.name = 'bennett'
b_manufacturer.keywords = ['bennett', 'pacific']

manufacturers = [dw_manufacturer, gvr_manufacturer, t_manufacturer, b_manufacturer]

class sub_equip:
	def __init__(self):
		self.name = ''
		self.keywords = []
		self.manufacturers = []

dispensing_se = sub_equip()
dispensing_se.name = 'Dispensing'
dispensing_se.keywords = ['hydraulics', 'fuel filters', 'breakaways', 'hoses', 'retractors', 'nozzles', 'fuel', 'filter']
dispensing_se.manufacturers = ["Dresser Wayne", 'Gilbarco', 'Schlumberger', 'Tokheim', 'Bennett', 'Veeder Root', 'CIM-TEK', 'PetroClear', 'SPATCO DEF', 'FE Petro', 'Esco', 'OPW', 'Catlow', 'Husky', 'Flex-ing', 'Goodyear']

pos_se = sub_equip()
pos_se.name = 'POS'
pos_se.keywords = ['circuit boards', 'keypads', 'kits', 'printers', 'card readers', 'lcd', 'circuit', 'board', 'keypad', 'kit', 'printer', 'card', 'reader']
pos_se.manufacturers = ['Esco', 'Dresser Wayne', 'Gilbarco', 'Schlumberger', 'Tokheim', 'Bennett', 'Veeder Root', 'Southwest', 'Bennett', 'Centurion', 'Citizen', 'DH Print', 'Eaton', 'EBW', 'Emco', 'Epson', 'Esco', 'Gasboy', 'Incon', 'Omntec', 'Petro Vend', 'Red Jacket', 'Schlumberger', 'Star', 'TMS', 'Tuthill', 'Verifone', 'Wayne']

print_se = sub_equip()
print_se.name = 'Printing'
print_se.keywords = ['paper', 'ribbons', 'ribbon']
print_se.manufacturers = []

controller_se = sub_equip()
controller_se.name = 'Controller'
controller_se.keywords = ['controller']
controller_se.manufacturers = []

outershell_se = sub_equip()
outershell_se.name = 'Outershell'
outershell_se.keywords = ['outer shell', 'decal', 'overlay', 'outer', 'shell']
outershell_se.manufacturers = ['Esco', 'Dresser Wayne', 'Gilbarco', 'Schlumberger', 'Tokheim', 'Bennett', 'Veeder Root', 'Southwest']

sub_equips = [dispensing_se, pos_se, print_se, controller_se, outershell_se]