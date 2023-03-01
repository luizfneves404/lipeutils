def main():
    import importlib

    import argparse

    from .Util import Util

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

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    for util in util_list:
        module = importlib.import_module(f".{util}", "lipeutils")
        Util(
            module.command_name, module.command_func, module.util_args
        ).add_to_subparsers(subparsers)

    # parse args
    args = parser.parse_args()
    # get only the values, not the keys, from the args
    values = list(vars(args).values())
    # remove the last value, because it is the func
    values.pop(-1)
    # pass in the values as arguments to the func, which is the calc_and_print of the module
    args.func(*values)


if __name__ == "__main__":
    main()
