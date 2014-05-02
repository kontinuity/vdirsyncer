# -*- coding: utf-8 -*-
'''
    vdirsyncer.exceptions
    ~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2014 Markus Unterwaditzer
    :license: MIT, see LICENSE for more details.
'''


class Error(Exception):
    '''Baseclass for all errors.'''


class PreconditionFailed(Error):
    '''
      - The item doesn't exist although it should
      - The item exists although it shouldn't
      - The etags don't match.

    Due to CalDAV we can't actually say which error it is.
    This error may indicate race conditions.
    '''


class NotFoundError(PreconditionFailed):
    '''Item not found'''


class AlreadyExistingError(PreconditionFailed):
    '''Item already exists'''


class WrongEtagError(PreconditionFailed):
    '''Wrong etag'''


class StorageError(Error):
    '''Internal or initialization errors with storage.'''


class SyncError(Error):
    '''Errors related to synchronization.'''


class SyncConflict(SyncError):
    '''
    Two items changed since the last sync, they now have different contents and
    no conflict resolution method was given.
    '''


class StorageEmpty(SyncError):
    '''
    One storage unexpectedly got completely empty between two synchronizations.
    The first argument is the empty storage.
    '''

    @property
    def empty_storage(self):
        return self.args[0]
