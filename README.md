# agusmart
./odoo-bin --addons-path=addons,custom --xmlrpc-port=8080 --db_port 5432 -d agusmart --limit-memory-hard 0 --limit-time-real=10000 -u agusmart -i base 

# dormitory_control
./odoo-bin --addons-path=addons,custom --xmlrpc-port=8069 --db_port 5432 -d dormitorydb --limit-memory-hard 0 --limit-time-real=10000 -u dormitory_control -i base 
