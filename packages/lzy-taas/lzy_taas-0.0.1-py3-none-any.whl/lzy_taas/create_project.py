from uuid import uuid4
from datasphere_python import DataSphereApiClient
from .config import Config
import logging


def create_blank_project(client: DataSphereApiClient, subnet_id: str):
    logger = logging.getLogger()

    if len(subnet_id) == 0:
        subnet_id = None

    project_name = "nirvana-" + str(uuid4())
    logger.info(f'Going to create project with name {project_name}')

    code, _ = client.create_project_from_checkpoint(
        project_name,
        Config.SERVICE_ACCOUNT_ID,
        Config.TEMPLATE_PROJECT_CHECKPOINT_ID,
        subnet_id=subnet_id
    )

    if code != 0:
        raise RuntimeError("Unable to create project, code: " + str(code))

    logger.info(f'Successfully created project {project_name}')

    logger.info(f"Retrieve project_id for project {project_name}")
    project_id = client.get_project_id(project_name)
    project_id_last_part = project_id.split("/")[-1]
    logger.info(f"Identifier of created project: {project_id}")

    return project_id, project_id_last_part


def download_file_to_project(
        client: DataSphereApiClient,
        notebook_meta: dict,
        project_id_last_part: str,
        source_code_archive_name: str):
    download_sources_cell_id = f"{notebook_meta['notebookId']}/cell/{Config.DOWNLOAD_FROM_S3_CELL_ID}"
    s3_data_path = f'{project_id_last_part}/{source_code_archive_name}'
    _ = client.execute(project_id_last_part, {"key": s3_data_path}, [], sync=True, cell_id=download_sources_cell_id)


def unpack_file_in_project(client: DataSphereApiClient,
                           notebook_meta: dict,
                           project_id_last_part: str,
                           source_code_archive_name: str):
    unpack_sources_cell_id = f"{notebook_meta['notebookId']}/cell/{Config.UNPACK_TAR_ARCHIVE_CELL_ID}"
    _ = client.execute(project_id_last_part, {"filename": source_code_archive_name}, [], sync=True,
                       cell_id=unpack_sources_cell_id)
