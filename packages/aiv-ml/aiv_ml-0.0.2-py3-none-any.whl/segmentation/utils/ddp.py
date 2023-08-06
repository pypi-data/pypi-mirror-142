
'''
setting parameters for Pytorch Distributed Process
'''
import os
import os.path as osp
import torch 
from utils.logger import get_root_logger
def setup_for_distributed(is_master):
    """
    This function disables printing when not in master process
    """
    import builtins as __builtin__

    builtin_print = __builtin__.print

    def print(*args, **kwargs):
        force = kwargs.pop("force", False)
        if is_master or force:
            builtin_print(*args, **kwargs)

    __builtin__.print = print

def init_distributed_mode(args):
    logger = get_root_logger(name='DDP', log_file=osp.join(args.log_path, 'ddp.log'))

    if "RANK" in os.environ and "WORLD_SIZE" in os.environ:
        args.rank = int(os.environ["RANK"])
        args.world_size = int(os.environ["WORLD_SIZE"])
        args.gpu = int(os.environ["LOCAL_RANK"])

        logger.info("RANK: {}".format(args.rank))
        logger.info("WORLD_SIZE: {}".format(args.world_size))
        logger.info("LOCAL_RANK: {}".format(args.gpu))
        logger.info("> Above information is from environment.")
    elif "SLURM_PROCID" in os.environ:
        args.rank = int(os.environ["SLURM_PROCID"])
        args.gpu = args.rank % torch.cuda.device_count()

        logger.info("SLURM_PROCID: {}".format(args.rank))
        logger.info("RANK % NUM_OF_GPUS: {}".format(args.gpu))
        logger.info("> Above information is from environment.")
    elif hasattr(args, "rank"):
        logger.info("Not using distributed mode")
        args.distributed = False
        return
    else:
        logger.info("Not using distributed mode")
        args.distributed = False
        return

    args.distributed = True

    torch.cuda.set_device(args.gpu)
    args.dist_backend = "gloo" #"nccl"
    logger.info(f"distributed init (rank {args.rank}): {args.dist_url}")
    torch.distributed.init_process_group(
        backend=args.dist_backend, init_method=args.dist_url, world_size=args.world_size, rank=args.rank
    )
    logger.info("INITIALIZED DISTRIBUTED PROCESS GROUP: torch.distributed.init_process_group")

    setup_for_distributed(args.rank == 0)

