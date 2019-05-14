import sys

import psutil as ps

cpu = ('idle', 'user', 'guest', 'iowait', 'steal', 'system')
virtual_memory = ('total', 'used', 'free', 'shared')
swap_memory = ('total', 'used', 'free')


def get_cpu():
    print("CPU:")
    for item in cpu:
        print(f"system.cpu.{item}: {getattr(ps.cpu_times_percent(), item)}")


def get_memory():
    print("Memory:")
    for item in virtual_memory:
        print(f"virtual {item}: {getattr(ps.virtual_memory(), item)}")
    for item in swap_memory:
        print(f'swap {item}: {getattr(ps.swap_memory(), item)}')


def run_script():
    command = sys.argv[1::]

    if len(command) == 1:
        command = command[0]

        if command == 'cpu':
            get_cpu()
        elif command == 'mem':
            get_memory()
        else:
            sys.exit(f'Argument "{command}" is not supported. Try "cpu" or "mem" instead.')
    elif len(command) == 0:
        sys.exit('Too few arguments. Try "cpu" or "mem".')
    else:
        sys.exit('Too many arguments provided. Try "cpu" or "mem" instead.')


if __name__ == '__main__':
    run_script()
