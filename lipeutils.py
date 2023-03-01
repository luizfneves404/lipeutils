import argparse
from Util import Util

util_list = [
    "calc_anti",
    "calc_centavos_crescentes",
    "calc_dias_vida",
    "calc_imc",
    "calc_juros_compostos",
    "calc_juros_simples",
    "calc_lucro",
    "conversor_m_p",
    "loterias",
    "mega_sena",
    "simp_fracoes",
    "test_primos",
]

# importing the modules using util_list
for util in util_list:
    exec(f"import {util}")

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# getting the references to the modules from the util_list
module_list = [globals()[util] for util in util_list]

for module in module_list:
    # creating util and adding it to subparsers
    Util(module.command_name, module.command_func, module.util_args).add_to_subparsers(
        subparsers
    )


# parse args
args = parser.parse_args()
# get only the values, not the keys, from the args
values = list(vars(args).values())
# remove the last value, because it is the func
values.pop(-1)
# pass in the values as arguments to the func, which is the calc_and_print of the module
args.func(*values)
