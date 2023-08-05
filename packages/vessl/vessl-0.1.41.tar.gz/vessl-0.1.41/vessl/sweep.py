from typing import Any, Dict, List, Tuple

from openapi_client import ResponseSweepExperimentInfo
from openapi_client.models import (
    InfluxdbSweepLog,
    OrmEarlyStoppingSetting,
    OrmEarlyStoppingSpec,
    OrmHyperparameter,
    OrmParameter,
    OrmRange,
    OrmSweepObjective,
    OrmSweepSearchSpace,
    ResponseSweepInfo,
    ResponseSweepListResponse,
    SweepCreateAPIInput,
)
from vessl import vessl_api
from vessl.kernel_cluster import read_cluster
from vessl.kernel_resource_spec import (
    _configure_custom_kernel_resource_spec,
    read_kernel_resource_spec,
)
from vessl.organization import _get_organization_name
from vessl.project import _get_project_name
from vessl.util.constant import MOUNT_PATH_OUTPUT, SWEEP_OBJECTIVE_TYPE_MAXIMIZE
from vessl.util.exception import InvalidTypeError
from vessl.volume import _configure_volume_mount_requests


def read_sweep(sweep_name: str, **kwargs) -> ResponseSweepInfo:
    """Read sweep

    Keyword args:
        organization_name (str): override default organization
        project_name (str): override default project
    """
    return vessl_api.sweep_read_api(
        organization_name=_get_organization_name(**kwargs),
        project_name=_get_project_name(**kwargs),
        sweep=sweep_name,
    )


def list_sweeps(**kwargs) -> List[ResponseSweepListResponse]:
    """List sweeps

    Keyword args:
        organization_name (str): override default organization
        project_name (str): override default project
    """
    return vessl_api.sweep_list_api(
        organization_name=_get_organization_name(**kwargs),
        project_name=_get_project_name(**kwargs),
    ).results


def create_sweep(
    objective: OrmSweepObjective,
    max_experiment_count: int,
    parallel_experiment_count: int,
    max_failed_experiment_count: int,
    algorithm: str,
    parameters: List[OrmParameter],
    cluster_name: str,
    start_command: str,
    kernel_resource_spec_name: str = None,
    processor_type: str = None,
    cpu_limit: float = None,
    memory_limit: float = None,
    gpu_type: str = None,
    gpu_limit: int = None,
    kernel_image_url: str = None,
    *,
    early_stopping_name: str = None,
    early_stopping_settings: List[Tuple[str, str]] = None,
    message: str = None,
    hyperparameters: List[Tuple[str, str]] = None,
    dataset_mounts: List[str] = None,
    git_ref_mounts: List[str] = None,
    git_diff_mount: str = None,
    archive_file_mount: str = None,
    root_volume_size: str = None,
    working_dir: str = None,
    output_dir: str = MOUNT_PATH_OUTPUT,
    **kwargs,
) -> ResponseSweepInfo:
    """Create sweep

    Args:
        parameters (List[Dict[str, Any]]):
            Element keys are 'name' (str), 'type' (str), and 'range' (dict).
            'range' keys are 'list' (list), 'min' (str), 'max' (str),
            and 'step' (str).

    Keyword args:
        organization_name (str): override default organization
        project_name (str): override default project
        use_git_diff (bool): run experiment with uncommitted changes
        use_git_diff_untracked (bool): run with untracked changed (only valid if `use_git_diff` is set)
    """
    cluster = read_cluster(cluster_name)

    kernel_resource_spec = kernel_resource_spec_id = None
    if cluster.is_savvihub_managed:  # TODO: rename to vessl
        kernel_resource_spec_id = read_kernel_resource_spec(
            cluster.id,
            kernel_resource_spec_name,
        ).id
    else:
        kernel_resource_spec = _configure_custom_kernel_resource_spec(
            processor_type,
            cpu_limit,
            memory_limit,
            gpu_type,
            gpu_limit,
        )

    early_stopping_spec = OrmEarlyStoppingSpec(
        algorithm_name=early_stopping_name,
        algorithm_settings=[
            OrmEarlyStoppingSetting(name=k, value=str(v))
            for k, v in (early_stopping_settings or [])
        ],
    )

    volume_mount_requests = _configure_volume_mount_requests(
        dataset_mounts=dataset_mounts,
        git_ref_mounts=git_ref_mounts,
        git_diff_mount=git_diff_mount,
        archive_file_mount=archive_file_mount,
        root_volume_size=root_volume_size,
        working_dir=working_dir,
        output_dir=output_dir,
        **kwargs,
    )

    return vessl_api.sweep_create_api(
        organization_name=_get_organization_name(**kwargs),
        project_name=_get_project_name(**kwargs),
        sweep_create_api_input=SweepCreateAPIInput(
            objective=objective,
            max_experiment_count=max_experiment_count,
            parallel_experiment_count=parallel_experiment_count,
            max_failed_experiment_count=max_failed_experiment_count,
            algorithm=algorithm,
            search_space=OrmSweepSearchSpace(
                parameters=parameters,
            ),
            cluster_id=cluster.id,
            hyperparameters=[
                OrmHyperparameter(key, str(value))
                for key, value in map(
                    lambda hyperparameter: hyperparameter.split("="),
                    (hyperparameters or []),
                )
            ],
            image_url=kernel_image_url,
            early_stopping_spec=early_stopping_spec,
            message=message,
            resource_spec=kernel_resource_spec,
            resource_spec_id=kernel_resource_spec_id,
            start_command=start_command,
            volumes=volume_mount_requests,
        ),
    )


def terminate_sweep(sweep_name: str, **kwargs) -> ResponseSweepInfo:
    """Terminate sweep

    Keyword args:
        organization_name (str): override default organization
        project_name (str): override default project
    """
    return vessl_api.sweep_terminate_api(
        organization_name=_get_organization_name(**kwargs),
        project_name=_get_project_name(**kwargs),
        sweep=sweep_name,
    )


def list_sweep_logs(
    sweep_name: str, tail: int = 200, **kwargs
) -> List[InfluxdbSweepLog]:
    """List sweep logs

    Args:
        tail (int): number of lines to display from the end. Display all if -1.

    Keyword args:
        organization_name (str): override default organization
        project_name (str): override default project
    """

    if tail == -1:
        tail = None

    return vessl_api.sweep_logs_api(
        organization_name=_get_organization_name(**kwargs),
        project_name=_get_project_name(**kwargs),
        sweep=sweep_name,
        limit=tail,
    ).logs


def get_best_sweep_experiment(sweep_name: str, **kwargs) -> ResponseSweepExperimentInfo:
    """Read sweep and return the best experiment info

    Keyword args:
        organization_name (str): override default organization
        project_name (str): override default project
    """

    sweep_read_response = vessl_api.sweep_read_api(
        organization_name=_get_organization_name(**kwargs),
        project_name=_get_project_name(**kwargs),
        sweep=sweep_name,
    )
    if type(sweep_read_response) != ResponseSweepInfo:
        return sweep_read_response

    def best_experiments(
        items: [ResponseSweepExperimentInfo], maximize: bool
    ) -> ResponseSweepExperimentInfo:
        return sorted(
            items, key=lambda x: x.objective_metric_value, reverse=maximize
        ).pop()

    if sweep_read_response.experiment_summary.total > 0:
        filtered_experiment_summary = []
        for experiment in sweep_read_response.experiment_summary.sweep_experiment_infos:
            if not experiment.objective_metric_value:
                continue
            elif not isinstance(experiment.objective_metric_value, (int, float)):
                raise InvalidTypeError(
                    f"The type of experiment objective metric value is not integer or float: "
                    f"{type(experiment.objective_metric_value)}"
                )
            filtered_experiment_summary.append(experiment)

        if sweep_read_response.objective.type == SWEEP_OBJECTIVE_TYPE_MAXIMIZE:
            return best_experiments(filtered_experiment_summary, True)
        else:
            return best_experiments(filtered_experiment_summary, False)

    return ResponseSweepExperimentInfo()
