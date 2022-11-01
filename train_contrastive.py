
import os
import yaml

import contrastive


def main():

    with open("params_contrastive.yml", 'r') as f:
        params = yaml.safe_load(f)

    # Remove SLURM_JOBID to prevent ignite assume we are using SLURM to run multiple tasks.
    os.environ.pop("SLURM_JOBID", None)

    contrastive.train_contrastive(0, params)


if __name__ == "__main__":
    main()
