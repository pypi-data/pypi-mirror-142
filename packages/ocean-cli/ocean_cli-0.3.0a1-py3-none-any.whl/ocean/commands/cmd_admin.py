from typing_extensions import Required
import click
import inquirer
from dateutil.parser import parse

from ocean import api, code, utils
from ocean.commands import cmd_get
from ocean.main import pass_env
from ocean.utils import sprint, PrintType


@click.group()
def cli():
    pass


####################
# Create
####################
@cli.group(cls=utils.AliasedGroup)
def create():
    pass


@create.command()
@pass_env
def machine_type(ctx):
    name = click.prompt("Machine-Type Name")

    mt_list = cmd_get._machine_type(ctx)
    while name in mt_list.items:
        sprint(f"Machine-Type `{name}` already exit.\n", PrintType.FAILED)
        name = click.prompt("Machine-Type Name")

    cpus = click.prompt("CPU cores", type=int)
    memory = click.prompt("Memory (Gi)", type=int)
    gpu_types = get_gpu_types(ctx)
    gpu_types.add(None)
    gpu_type = inquirer.list_input(
        "MachineType",
        choices=gpu_types,
    )
    gpus = click.prompt("GPUs", type=int)

    api.post(
        ctx,
        code.API_MACHINETYPE,
        {
            "name": name,
            "cpus": cpus,
            "memory": memory,
            "gpus": gpus,
            "gpuType": gpu_type,
        },
    )

    sprint(f"Machine-Type `{name}` successfully created.", PrintType.SUCCESS)


####################
# Delete
####################
@cli.group(cls=utils.AliasedGroup)
def delete():
    pass


@delete.command()
@click.option("--name", "-n", required=True, help="name of machine-type")
@pass_env
def machine_type(ctx, name):
    mt_id = api.get_machine_type_id_from_name(ctx, name)

    api.delete(ctx, code.API_MACHINETYPE + f"/{mt_id}")

    sprint(f"Machine-Type `{name}` successfully deleted.", PrintType.SUCCESS)


####################
# Request
####################
@cli.command()
@click.option("--all", "-A", is_flag=True, help="Show all requests")
@pass_env
def request(ctx, all):
    res = api.get(ctx, code.API_REQUEST)
    body = utils.dict_to_namespace(res.json())

    content = utils.dict_to_namespace(
        {
            "fstring": "{:4} {:8} {:10} {:25} {:5} {:20} {:30} {:30}",
            "header": [
                "ID",
                "STATUS",
                "USER",
                "Date",
                "QUOTA",
                "MACHINE-TYPE",
                "REASON",
                "REJECTED_REASON",
            ],
            "items": [],
        }
    )

    def shot_date(date):
        return parse(date).date()

    for req in body:
        if req.status == "pending" or all:
            content.items.append(
                [
                    req.id,
                    req.status,
                    req.user.username,
                    f"{shot_date(req.createdAt)} ~ {shot_date(req.endDate)}",
                    str(req.quota),
                    f"{req.machineType.name:12}",
                    # f"{req.machineType.name:12} (CPU {req.machineType.cpus:2.0f}, MEM {req.machineType.memory:3.0f} Gi, GPU {req.machineType.gpus:1} x {req.machineType.gpuType})",
                    req.reason,
                    req.rejectedReason,
                ]
            )

    if len(content.items) <= 0:
        sprint("No request.", PrintType.SUCCESS)
        return

    sprint("   " + content.fstring.format(*content.header))
    requests = [
        (content.fstring.format(*item), idx) for idx, item in enumerate(content.items)
    ]
    request = inquirer.list_input("", choices=requests)

    status = inquirer.list_input(
        "Select status",
        choices=["approved", "rejected"],
    )

    rejected_reason = None
    if status == "rejected":
        rejected_reason = inquirer.text("Rejected reason")

    sprint("=" * 50)
    sprint("USER:   " + content.items[request][2])
    sprint("QUOTA:  " + content.items[request][5] + " x " + content.items[request][4])
    sprint("DATE:   " + content.items[request][3])
    sprint("REASON: " + content.items[request][6])
    sprint(" -" * 25)
    sprint("STATUS: " + content.items[request][1] + " >> " + status)
    if status == "rejected":
        sprint("REJECTED REASON: " + rejected_reason)
    sprint("=" * 50)

    confirm = inquirer.confirm("Is Correct?")

    if confirm:
        res = api.patch(
            ctx,
            code.API_REQUEST + f"/{content.items[request][0]}",
            {"status": status, "rejectedReason": rejected_reason},
        )

    sprint("Request successfully updated", PrintType.SUCCESS)

    # res = api.get(ctx, "/api/manages/node")
    # body = utils.dict_to_namespace(res.json())

    # alloc = {"cpu": 0, "memory": 0, "gpu": {}}
    # usage = {"cpu": 0, "memory": 0, "gpu": {}}
    # for node in body.nodeInfos:
    #     alloc["cpu"] += node.allocatable.cpu
    #     alloc["memory"] += node.allocatable.memory
    #     if node.allocatable.gpuType in alloc["gpu"].keys():
    #         alloc["gpu"][node.allocatable.gpuType] += node.allocatable.gpu
    #     else:
    #         alloc["gpu"][node.allocatable.gpuType] = node.allocatable.gpu

    #     usage["cpu"] += node.usage.cpu
    #     usage["memory"] += node.usage.memory
    #     if node.usage.gpuType in usage["gpu"].keys():
    #         usage["gpu"][node.usage.gpuType] += node.usage.gpu
    #     else:
    #         usage["gpu"][node.usage.gpuType] = node.usage.gpu
    # print(alloc, usage)
    # return content


####################
# Utils
####################
def get_gpu_types(ctx):
    res = api.get(ctx, "/api/manages/node")
    body = utils.dict_to_namespace(res.json())

    types = set()
    for node in body.nodeInfos:
        types.add(node.allocatable.gpuType)

    types.remove("Cannot Detect Gpu Type.")
    return types
