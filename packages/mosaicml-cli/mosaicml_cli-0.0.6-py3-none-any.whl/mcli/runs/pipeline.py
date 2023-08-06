""" Run Pipeline for singular runs """
import logging
import uuid
from dataclasses import asdict
from typing import Any, Dict, Optional

from mcli.models.run import PartialRunModel, RunModel
from mcli.submit.kubernetes.mcli_job import MCLIJob
from mcli.submit.kubernetes.runners import Runner
from mcli.utils.utils_config import format_jinja

log = logging.getLogger(__name__)


def create_partial_run_models(
    file: Optional[str] = None,
    name: Optional[str] = None,
    instance: Optional[str] = None,
    image: Optional[str] = None,
    git_repo: Optional[str] = None,
    git_branch: Optional[str] = None,
    model: Optional[str] = None,
    command: Optional[str] = None,
    parameters: Optional[Dict[str, Any]] = None,
) -> PartialRunModel:
    args_dict = {
        'name': name,
        'instance': instance,
        'image': image,
        'git_repo': git_repo,
        'git_branch': git_branch,
        'model': model,
        'command': command,
        'parameters': parameters,
    }

    # TODO: load the current project config and use relevant fields from it as the base PartialRunModel here
    # TODO: if forking from a previous run, load the RunModel here and append it to partial_run_models

    prm = PartialRunModel.empty()

    if file is not None:
        log.info(f'Loading config from file {file}')
        file_model = PartialRunModel.from_file(file)
        prm = prm.merge(file_model)

    args_prm = PartialRunModel.from_dict(args_dict)
    prm = prm.merge(args_prm)
    return prm


def mcli_job_from_run_model(run_model: RunModel) -> MCLIJob:
    formatted_command = format_jinja(run_model.command, asdict(run_model))

    return MCLIJob(
        name=f'{run_model.name}-{str(uuid.uuid4())[0:8]}',
        container_image=run_model.image,
        command=[formatted_command],
        parameters=run_model.parameters,
    )


def submit_mcli_job(mcli_job: MCLIJob, run_model: RunModel):
    runner = Runner()
    runner.submit(mcli_job, run_model.instance)
