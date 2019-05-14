import psutil as ps
import sys

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


def cli():
    command = sys.argv[1::]

    if command == 'cpu':
        get_cpu()
    elif command == 'mem':
        get_memory()
    elif len(command) == 0:
        sys.exit('Need 1 argument: "cpu" or "mem"')
    elif len(command) > 1:
        sys.exit('Too many arguments provided. Need only 1: "cpu" or "mem"')
    else:
        sys.exit('Wrong argument provided: only "cpu" or "mem" supported')


if __name__ == '__main__':
    cli()
