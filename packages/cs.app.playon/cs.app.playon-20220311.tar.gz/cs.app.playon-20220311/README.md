PlayOn facilities, primarily access to the download API.
Includes a nice command line tool.

*Latest release 20220311*:
Bugfix criteria for refreshing the PlayOn state.

## Function `main(argv=None)`

Playon command line mode;
see the `PlayOnCommand` class below.

## Class `PlayOnAPI(cs.resources.MultiOpenMixin, cs.context.ContextManagerMixin)`

Access to the PlayOn API.

*Method `PlayOnAPI.__getitem__(self, download_id: int)`*:
Return the recording `TagSet` associated with the recording `download_id`.

*Method `PlayOnAPI.account(self, *a, **kw)`*:
Return account information.

*Property `PlayOnAPI.auth_token`*:
An auth token obtained from the login state.

*Method `PlayOnAPI.cdsurl_data(self, suburl, _method='GET', headers=None, **kw)`*:
Wrapper for `suburl_data` using `CDS_BASE` as the base URL.

*Method `PlayOnAPI.download(self, *a, **kw)`*:
Download the file with `download_id` to `filename_basis`.
Return the `TagSet` for the recording.

The default `filename` is the basename of the filename
from the download.
If the filename is supplied with a trailing dot (`'.'`)
then the file extension will be taken from the filename
of the download URL.

*Method `PlayOnAPI.from_playon_date(date_s)`*:
The PlayOn API seems to use UTC date strings.

*Property `PlayOnAPI.jwt`*:
The JWT token.

*Property `PlayOnAPI.login_state`*:
The login state, a `dict`. Performs a login if necessary.

*Method `PlayOnAPI.queue(self, *a, **kw)`*:
Return the `TagSet` instances for the queued recordings.

*Method `PlayOnAPI.recordings(self, *a, **kw)`*:
Return the `TagSet` instances for the available recordings.

*Method `PlayOnAPI.service(self, service_id)`*:
Return the service `SQLTags` instance for `service_id`.

*Method `PlayOnAPI.services(self, *a, **kw)`*:
Fetch the list of services.

*Method `PlayOnAPI.startup_shutdown(self)`*:
Start up: open and init the `SQLTags`, open the `FSTags`.

*Method `PlayOnAPI.suburl_data(self, suburl, _base_url=None, _method='GET', headers=None, raw=False, **kw)`*:
Call `suburl` and return the `'data'` component on success.

Parameters:
* `suburl`: the API subURL designating the endpoint.
* `_method`: optional HTTP method, default `'GET'`.
* `headers`: hreaders to accompany the request;
  default `{'Authorization':self.jwt}`.
Other keyword arguments are passed to the `requests` method
used to perform the HTTP call.

*Method `PlayOnAPI.suburl_request(base_url, method, suburl)`*:
Return a curried `requests` method
to fetch `API_BASE/suburl`.

## Class `PlayOnCommand(cs.cmdutils.BaseCommand)`

Playon command line implementation.

Command line usage:

    Usage: playon subcommand [args...]

        Environment:
          PLAYON_USER               PlayOn login name, default from $EMAIL.
          PLAYON_PASSWORD           PlayOn password.
                                    This is obtained from .netrc if omitted.
          PLAYON_FILENAME_FORMAT  Format string for downloaded filenames.
                                    Default: {playon.Series}--{playon.Name}--{resolution}--{playon.ProviderID}--playon--{playon.ID}
          PLAYON_TAGS_DBURL         Location of state tags database.
                                    Default: ~/var/playon.sqlite

        Recording specification:
          an int        The specific recording id.
          all           All known recordings.
          downloaded    Recordings already downloaded.
          expired       Recording which are no longer available.
          pending       Recordings not already downloaded.
          /regexp       Recordings whose Series or Name match the regexp,
                        case insensitive.

      Subcommands:
        account
          Report account state.
        dl [-j jobs] [-n] [recordings...]
          Download the specified recordings, default "pending".
          -j jobs   Run this many downloads in parallel.
                    The default is 2.
          -n        No download. List the specified recordings.
        help [-l] [subcommand-names...]
          Print the full help for the named subcommands,
          or for all subcommands if no names are specified.
          -l  Long help even if no subcommand-names provided.
        ls [-l] [recordings...]
          List available downloads.
          -l        Long listing: list tags below each entry.
          -o format Format string for each entry.
          Default format: {playon.ID} {playon.HumanSize} {resolution} {playon.Series} {playon.Name} {playon.ProviderID} {status:upper}
        q [-l] [recordings...]
          List queued recordings.
          -l        Long listing: list tags below each entry.
          -o format Format string for each entry.
          Default format: {playon.ID} {playon.Series} {playon.Name} {playon.ProviderID}
        queue [-l] [recordings...]
          List queued recordings.
          -l        Long listing: list tags below each entry.
          -o format Format string for each entry.
          Default format: {playon.ID} {playon.Series} {playon.Name} {playon.ProviderID}
        refresh [queue] [recordings]
          Update the db state from the PlayOn service.
        service [service_id]
          List services.

*Method `PlayOnCommand.cmd_account(self, argv)`*:
Usage: {cmd}
Report account state.

*Method `PlayOnCommand.cmd_dl(self, argv)`*:
Usage: {cmd} [-j jobs] [-n] [recordings...]
Download the specified recordings, default "pending".
-j jobs   Run this many downloads in parallel.
          The default is {DEFAULT_DL_PARALLELISM}.
-n        No download. List the specified recordings.

*Method `PlayOnCommand.cmd_ls(self, argv)`*:
Usage: {cmd} [-l] [recordings...]
List available downloads.
-l        Long listing: list tags below each entry.
-o format Format string for each entry.
Default format: {LS_FORMAT}

*Method `PlayOnCommand.cmd_q(self, argv)`*:
Usage: {cmd} [-l] [recordings...]
List queued recordings.
-l        Long listing: list tags below each entry.
-o format Format string for each entry.
Default format: {QUEUE_FORMAT}

*Method `PlayOnCommand.cmd_queue(self, argv)`*:
Usage: {cmd} [-l] [recordings...]
List queued recordings.
-l        Long listing: list tags below each entry.
-o format Format string for each entry.
Default format: {QUEUE_FORMAT}

*Method `PlayOnCommand.cmd_refresh(self, argv)`*:
Usage: {cmd} [queue] [recordings]
Update the db state from the PlayOn service.

*Method `PlayOnCommand.cmd_service(self, argv, locale='en_US')`*:
Usage: {cmd} [service_id]
List services.

*Method `PlayOnCommand.run_context(self)`*:
Prepare the `PlayOnAPI` around each command invocation.

## Class `PlayOnSQLTags(cs.sqltags.SQLTags, cs.tagset.BaseTagSets, cs.resources.MultiOpenMixin, cs.context.ContextManagerMixin, collections.abc.MutableMapping, collections.abc.Mapping, collections.abc.Collection, collections.abc.Sized, collections.abc.Iterable, collections.abc.Container)`

`SQLTags` subclass with PlayOn related methods.

*Method `PlayOnSQLTags.__iter__(self)`*:
Yield recording `TagSet`s, those named `"recording.*"`.

Note that this includes both recorded and queued items.

*Method `PlayOnSQLTags.infer_db_url(envvar=None, default_path=None)`*:
Infer the database URL.

Parameters:
* `envvar`: environment variable to specify a default,
  default from `DBURL_ENVVAR` (`PLAYON_TAGS_DBURL`).

*Method `PlayOnSQLTags.recording_ids_from_str(self, *a, **kw)`*:
Convert a string to a list of recording ids.

*Method `PlayOnSQLTags.recordings(self)`*:
Yield recording `TagSet`s, those named `"recording.*"`.

Note that this includes both recorded and queued items.

## Class `Recording(cs.sqltags.SQLTagSet, cs.obj.SingletonMixin, cs.tagset.TagSet, builtins.dict, cs.dateutils.UNIXTimeMixin, cs.lex.FormatableMixin, cs.lex.FormatableFormatter, string.Formatter, cs.mappings.AttrableMappingMixin)`

An `SQLTagSet` with knowledge about PlayOn recordings.

*Method `Recording.is_available(self)`*:
Is a recording available for download?

*Method `Recording.is_downloaded(self)`*:
Test whether this recording has been downloaded
based on the presence of a `download_path` `Tag`.

*Method `Recording.is_expired(self)`*:
Test whether this recording is expired,
which implies that it is no longer available for download.

*Method `Recording.is_pending(self)`*:
A pending download: available and not already downloaded.

*Method `Recording.is_queued(self)`*:
Is a recording still in the queue?

*Method `Recording.is_stale(self, max_age=None)`*:
Test whether this entry is stale
i.e. the time since `self.last_updated` exceeds `max_age` seconds
(default from `self.STALE_AGE`).
Note that expired recordings are never stale
because they can no longer be queried from the API.

*Method `Recording.ls(self, ls_format=None, long_mode=False, print_func=None)`*:
List a recording.

*Method `Recording.nice_name(self)`*:
A nice name for the recording: the PlayOn series and name,
omitting the series if `None`.

*Method `Recording.recording_id(self)`*:
The recording id or `None`.

*Method `Recording.resolution(self)`*:
The recording resolution derived from the quality
via the `Recording.RECORDING_QUALITY` mapping.

*Method `Recording.status(self)`*:
Return a short status string.

# Release Log



*Release 20220311*:
Bugfix criteria for refreshing the PlayOn state.

*Release 20211212*:
Initial release.
