from .core import CouchDBDecorators, CouchError


class Server():
  __ALLOWED_KEYS__ALL_DBS__GET = {'descending': bool, 'limit': int, 'skip': int,
                                  'startkey': [], 'start_key': [], 'endkey': [], 'end_key': []}
  __ALLOWED_KEYS__DBS_INFO__POST = {'keys': []}
  __ALLOWED_KEYS__CLUSTER_SETUP__GET = {'ensure_dbs_exist': []}
  __ALLOWED_KEYS__CLUSTER_SETUP__POST = {'action': str, 'bind_address': str,
                                         'host': str, 'port': int,
                                         'node_code': int, 'remote_node': str,
                                         'username': str, 'password': str,
                                         'remote_current_user': str, 'remote_current_password': str,
                                         'ensure_dbs_exist': [], }

  __ALLOWED_KEYS__DB_UPDATES__GET = {'feed': str, 'timeout': int, 'heartbeat': int, 'since': str}

  __ALLOWED_KEYS__REPLICATE__POST = {'cancel': bool, 'continuous': bool,
                                     'create_target': bool, 'doc_ids': [],
                                     'filter': str, 'proxy': str,
                                     'source': {}, 'target': {}}

  __ALLOWED_KEYS__SCHEDULER_JOBS__GET = {'limit': int, 'skip': int}
  __ALLOWED_KEYS__SCHEDULER_DOCS__GET = {'limit': int, 'skip': int}
  __ALLOWED_KEYS__UUIDS__GET = {'count': int}

  def __init__(self, **kwargs):
    self.session = kwargs.get('session', None)

    self._predefined_segments = {'node_name': '_local'}

  def _set_simple_attribute_as_list(self, attribute, value):
    setattr(self, attribute, () if isinstance(value, CouchError) else value)
    return getattr(self, attribute)

  @CouchDBDecorators.endpoint('/')
  def get_info(self, couch_data):
    return couch_data

  @CouchDBDecorators.endpoint('/_up')
  def get_server_status(self, couch_data):
    return couch_data

  @CouchDBDecorators.endpoint('/_active_tasks')
  def get_active_tasks(self, couch_data):
    return couch_data

  @CouchDBDecorators.endpoint('/_all_dbs', filter_format=__ALLOWED_KEYS__ALL_DBS__GET)
  def get_database_names(self, couch_data):
    return couch_data

  @CouchDBDecorators.endpoint('/_dbs_info', method='post', filter_format=__ALLOWED_KEYS__DBS_INFO__POST)
  def get_databases(self, couch_data):
    return couch_data

  @CouchDBDecorators.endpoint('/_cluster_setup', filter_format=__ALLOWED_KEYS__CLUSTER_SETUP__GET)
  def get_cluster_setup(self, couch_data):
    return couch_data

  @CouchDBDecorators.endpoint('/_cluster_setup', method='post', filter_format=__ALLOWED_KEYS__CLUSTER_SETUP__POST)
  def configure_cluster_setup(self, couch_data):
    return couch_data

  @CouchDBDecorators.endpoint('/_db_updates', method='post', filter_format=__ALLOWED_KEYS__DB_UPDATES__GET)
  def get_database_updates(self, couch_data):
    return couch_data

  @CouchDBDecorators.endpoint('/_membership')
  def get_membership(self, couch_data):
    return couch_data

  @CouchDBDecorators.endpoint('/_replicate', method='post', filter_format=__ALLOWED_KEYS__REPLICATE__POST)
  def replicate(self, couch_data):
    return couch_data

  @CouchDBDecorators.endpoint('/_scheduler/jobs', filter_format=__ALLOWED_KEYS__SCHEDULER_JOBS__GET)
  def get_replication_updates(self, couch_data):
    """
    Retrieves the status of replication jobs that are currently active.
    """
    return couch_data

  @CouchDBDecorators.endpoint('/_scheduler/docs', filter_format=__ALLOWED_KEYS__SCHEDULER_DOCS__GET)
  def get_replication_docs(self, couch_data):
    """
    All Replication documents
    """
    return couch_data

  @CouchDBDecorators.endpoint('/_scheduler/docs/:db:', filter_format=__ALLOWED_KEYS__SCHEDULER_DOCS__GET)
  def get_replicator_docs(self, couch_data):
    """
    Replication documents for a specific replicator database
    """
    return couch_data

  @CouchDBDecorators.endpoint('/_scheduler/docs/:db:/:docid:')
  def get_replicator_doc(self, couch_data):
    """
    Retrives a single replication document for the specified replicator database
    """
    return couch_data

  @CouchDBDecorators.endpoint('/_node/:node_name:/_stats')
  def get_node_server_stats(self, couch_data):
    """
    Get statistics for the running server with name :node_name:
    """
    return couch_data

  @CouchDBDecorators.endpoint('/_node/:node_name:/_stats/:stat:')
  def get_node_server_stat(self, couch_data):
    """
    Get a section or subsection of the statistics for the running server with name :node_name:
    """
    return couch_data

  @CouchDBDecorators.endpoint('/_node/:node_name:/_system')
  def get_node_system_stats(self, couch_data):
    """
    Get system statistics for the running server with name :node_name:
    """
    return couch_data

  @CouchDBDecorators.endpoint('/_node/:node_name:/_restart', method='post')
  def restart_node(self, couch_data):
    """
    Restart the specified node
    """
    return couch_data

  @CouchDBDecorators.endpoint('/_node/:node_name:/_config')
  def get_server_config(self, couch_data):
    """
    Gets the entire server configuration of the specified node.
    """
    return couch_data

  @CouchDBDecorators.endpoint('/_node/:node_name:/_config/:key:')
  def get_config(self, couch_data):
    """
    Gets the server configuration section or key defined by :key: of the specified node.
    """
    return couch_data

  # TODO: implement put in endpoint decorator
  @CouchDBDecorators.endpoint('/_node/:node_name:/_config/:key:', method='put')
  def set_config(self, couch_data):
    """
    Create or update the server configuration key defined by :key: of the specified node.
    """
    return couch_data

  @CouchDBDecorators.endpoint('/_node/:node_name:/_config/:key:', method='delete')
  def delete_config(self, couch_data):
    """
    Delete the server configuration key defined by :key: of the specified node.
    """
    return couch_data

  @CouchDBDecorators.endpoint('/_uuids', filter_format=__ALLOWED_KEYS__UUIDS__GET)
  def generate_uuids(self, couch_data):
    """
    Retrieves new UUIDS from the CouchDB server

    :param int count Number of uuids to generate (Default: 1).
    """
    if isinstance(couch_data, CouchError):
      return couch_data

    if len(couch_data.get('uuids')) == 1:
      return couch_data.get('uuids')[0]

    return couch_data.get('uuids')

  @CouchDBDecorators.endpoint('/_node/:node_name:/_system')
  def get_uptime(self, couch_data):
    """
    Get the up time, in seconds, for the specified node.

    :returns CouchError if an error occured accessing the couch api
    :returns int Number of seconds that the server has been running, or -1 if the uptime key is missing.

    Usage: couchdb_instance.get_uptime(node_name='_local')
    """
    return couch_data if isinstance(couch_data, CouchError) else couch_data.get('uptime', -1)