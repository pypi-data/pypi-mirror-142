import copy
import logging
import os
import urllib.request
from uuid import uuid4
from datasphere_python import DataSphereApiClient
from .config import Config
from .upload_to_s3 import S3Loader


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


def prepare_metadata(client: DataSphereApiClient, notebook_meta: dict, project_id: str):
    if "/" in project_id:
        project_id = project_id.split("/")[-1]

    if notebook_meta is None:
        notebook_meta = client.get_notebook_metadata(project_id, Config.UTILS_NOTEBOOK_NAME)

    return project_id, notebook_meta


def upload_file_to_project_s3(source_code_path, s3_access_key, s3_secret_key, project_id_last_part):
    helper = S3Loader(s3_access_key, s3_secret_key, Config.NIRVANA_PROJECTS_BUCKET_NAME)
    helper.upload_file(source_code_path, project_id_last_part)


def download_file_to_project(client: DataSphereApiClient,
                             notebook_meta: dict,
                             project_id: str,
                             s3_path: str):
    project_id, notebook_meta = prepare_metadata(client, notebook_meta, project_id)
    download_sources_cell_id = f"{notebook_meta['notebookId']}/cell/{Config.DOWNLOAD_FROM_S3_CELL_ID}"
    _ = client.execute(project_id, {"key": s3_path}, [], sync=True, cell_id=download_sources_cell_id)


def unpack_archive_in_project(client: DataSphereApiClient,
                              notebook_meta: dict,
                              project_id: str,
                              archive_name: str):
    project_id, notebook_meta = prepare_metadata(client, notebook_meta, project_id)
    unpack_sources_cell_id = f"{notebook_meta['notebookId']}/cell/{Config.UNPACK_TAR_ARCHIVE_CELL_ID}"
    _ = client.execute(project_id, {"filename": archive_name}, [], sync=True, cell_id=unpack_sources_cell_id)


def upload_nirvana_library(client: DataSphereApiClient,
                           notebook_meta: dict,
                           project_id: str):
    project_id, notebook_meta = prepare_metadata(client, notebook_meta, project_id)
    download_file_to_project(client, notebook_meta, project_id, Config.NIRVANA_LIBRARY_ARCHIVE_NAME)
    unpack_archive_in_project(client, notebook_meta, project_id, Config.NIRVANA_LIBRARY_ARCHIVE_NAME)


def download_nirvana_inputs(nirvana_job: dict, dirname: str):
    if dirname is not None and not os.path.exists(dirname):
        os.mkdir(dirname)

    for input_name, input_metadata in nirvana_job['inputItems'].items():
        response = urllib.request.urlopen(input_metadata[0]['downloadURL'].replace("https", "http"))
        file_path = input_name
        if dirname is not None:
            file_path = f'{dirname}/{input_name}'

        with open(file_path, "wb") as f:
            f.write(response.read())


def upload_nirvana_inputs_to_project_s3(nirvana_job: dict,
                                        dirname: str,
                                        project_id: str,
                                        s3_access_key: str,
                                        s3_secret_key: str):
    uploader = S3Loader(s3_access_key, s3_secret_key, Config.NIRVANA_PROJECTS_BUCKET_NAME)
    for input_name, input_metadata in nirvana_job['inputItems'].items():
        file_path = input_name
        if dirname is not None:
            file_path = f'{dirname}/{input_name}'

        uploader.upload_file(file_path, project_id)


def download_nirvana_inputs_to_project(client: DataSphereApiClient,
                                       notebook_meta: dict,
                                       project_id: str,
                                       nirvana_job: dict):
    project_id, notebook_meta = prepare_metadata(client, notebook_meta, project_id)

    for input_name, input_metadata in nirvana_job['inputItems'].items():
        download_file_to_project(client, notebook_meta, project_id, f'{project_id}/{input_name}')


def patch_nirvana_io(nirvana_job):
    nirvana_job_patched = copy.deepcopy(nirvana_job)

    for input_name, input_metadata in nirvana_job['inputItems'].items():
        nirvana_job_patched['inputs'][input_name] = [f"home/jupyter/work/resources/{input_name}"]

    for output_name, output_metadata in nirvana_job['outputItems'].items():
        nirvana_job_patched['outputs'][output_name] = [f"home/jupyter/work/resources/{output_name}"]

    return nirvana_job_patched

